import os  
import io  
import pdfplumber  
import streamlit as st  
from azure.storage.blob import BlobServiceClient  
from azure.core.credentials import AzureKeyCredential  
from azure.identity import DefaultAzureCredential  
from azure.search.documents import SearchClient  
from azure.search.documents.indexes import SearchIndexClient  
from azure.search.documents.indexes.models import (  
    SimpleField,  
    SearchFieldDataType,  
    VectorSearch,  
    SearchIndex,  
    SearchableField,  
    SearchField,  
    VectorSearchProfile,  
    HnswAlgorithmConfiguration  
)  
from dotenv import load_dotenv  
from openai import AzureOpenAI  
import tiktoken  
from styling import global_page_style  
import re
  
# Load environment variables  
load_dotenv()  
  
# Configure Azure AI Search parameters  
search_endpoint = os.getenv('AZURE_SEARCH_ENDPOINT')  
search_key = os.getenv('AZURE_SEARCH_ADMIN_KEY')  
  
def chat_on_your_data(query, search_index, messages):  
    """  
    Perform retrieval queries over documents from the Azure AI Search Index.  
    """  
    # Configure Azure OpenAI parameters  
    azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')  
    azure_openai_api_key = os.getenv('AZURE_OPENAI_KEY')  
    azure_openai_api_version = os.getenv('AZURE_OPENAI_VERSION')  
    azure_ada_deployment = os.getenv('AZURE_EMBEDDINGS_DEPLOYMENT')  
    azure_gpt_deployment = os.getenv('AZURE_GPT_DEPLOYMENT')  

    messages.append({"role": "user", "content": query})  
      
    with st.chat_message("user"):  
        st.markdown(query)  
      
    with st.spinner('Processing...'):  
        client = AzureOpenAI(  
            azure_endpoint=azure_endpoint,  
            api_key=azure_openai_api_key,  
            api_version=azure_openai_api_version,  
        )  
        completion = client.chat.completions.create(  
            model=azure_gpt_deployment,  
            messages=[  
                {"role": "system", "content": "You are an AI assistant that helps people find information. Ensure the Markdown responses are correctly formatted before responding."},  
                {"role": "user", "content": query}  
            ],  
            max_tokens=800,  
            temperature=0.7,  
            top_p=0.95,  
            frequency_penalty=0,  
            presence_penalty=0,  
            stop=None,  
            stream=False,  
            extra_body={  
                "data_sources": [{  
                    "type": "azure_search",  
                    "parameters": {  
                        "endpoint": search_endpoint,  
                        "index_name": search_index,  
                        "semantic_configuration": "default",  
                        "query_type": "vector_simple_hybrid",  
                        "fields_mapping": {},  
                        "in_scope": True,  
                        "role_information": "You are an AI assistant that helps people find information.",  
                        "filter": None,  
                        "strictness": 3,  
                        "top_n_documents": 5,  
                        "authentication": {  
                            "type": "api_key",  
                            "key": search_key  
                        },  
                        "embedding_dependency": {  
                            "type": "deployment_name",  
                            "deployment_name": azure_ada_deployment  
                        }  
                    }  
                }]  
            }  
        )  
          
        response_data = completion.to_dict() 
        ai_response = response_data['choices'][0]['message']['content']  
        ai_response_cleaned = re.sub(r'\s+\.$', '.', re.sub(r'\[doc\d+\]', '', ai_response)) 
        citation = response_data["choices"][0]["message"]["context"]["citations"][0]["url"]  
        ai_response_final = f"{ai_response_cleaned}\n\nCitation(s):\n{citation}"
        messages.append({"role": "assistant", "content": ai_response_final})  
        with st.chat_message("assistant"):  
            st.markdown(ai_response_final)  
  
def setup_azure_openai(log_text):  
    """  
    Sets up Azure OpenAI.  
    """  
    log_text.write("Setting up Azure OpenAI...")  
    azure_openai = AzureOpenAI(  
        api_key=os.getenv("Azure_OPENAI_KEY"),  
        api_version=os.getenv('AZURE_OPENAI_VERSION'),  
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')  
    )  
    log_text.write("Azure OpenAI setup complete.")  
    return azure_openai  
  
def connect_to_blob_storage(log_text):  
    """  
    Connects to Azure Blob Storage.  
    """  
    log_text.write("Connecting to Blob Storage...")  
    blob_service_client = BlobServiceClient.from_connection_string(os.getenv("BLOB_CONNECTION_STRING"))  
    container_client = blob_service_client.get_container_client(os.getenv("BLOB_CONTAINER_NAME"))  
    log_text.write("Connected to Blob Storage.")  
    return container_client  
  
def split_text_with_metadata(text, metadata, max_length=800, overlap=75, encoding_name='cl100k_base'):  
    """  
    Splits the text into chunks with metadata.  
    """  
    tokenizer = tiktoken.get_encoding(encoding_name)  
    tokens = tokenizer.encode(text)  
    chunks = []  
    start = 0  
    end = max_length  
      
    while start < len(tokens):  
        chunk = tokens[start:end]  
        chunk_text = tokenizer.decode(chunk)  
        chunk_metadata = metadata.copy()  
        chunk_metadata.update({  
            'start_token': start,  
            'end_token': end,  
            'chunk_length': len(chunk),  
            'chunk_text_preview': chunk_text[:50] + '...'  
        })  
        chunks.append({  
            'text': chunk_text,  
            'metadata': chunk_metadata  
        })  
        start = end - overlap  
        end = start + max_length  
      
    return chunks  
  
def load_blob_content(blob_client):  
    """  
    Loads and returns the content of the PDF blob.  
    """  
    blob_name = blob_client.blob_name  
    if not blob_name.lower().endswith('.pdf'):  
        raise ValueError(f"Blob {blob_name} is not a PDF file.")  
      
    blob_data = blob_client.download_blob().readall()  
    pdf_stream = io.BytesIO(blob_data)  
    document_text = ""  
      
    with pdfplumber.open(pdf_stream) as pdf:  
        for page in pdf.pages:  
            document_text += page.extract_text() + "\n"  
      
    return document_text  
  
def vectorize(log_text):  
    """  
    Main function that orchestrates the vector workflow.  
    """  
    azure_openai = setup_azure_openai(log_text)  
    container_client = connect_to_blob_storage(log_text)  
      
    # Read and chunk documents with metadata  
    log_text.write("Listing blobs in container...")  
    blob_list = container_client.list_blobs()  
    documents = []  
    for blob in blob_list:  
        if not blob.name.lower().endswith('.pdf'):  
            log_text.write(f"Skipping non-PDF blob: {blob.name}")  
            continue  
          
        log_text.write(f"Processing blob: {blob.name}")  
        blob_client = container_client.get_blob_client(blob)  
        try:  
            document = load_blob_content(blob_client)  
            document_link = f'https://{os.getenv("BLOB_ACCOUNT_NAME")}.blob.core.windows.net/{os.getenv("BLOB_CONTAINER_NAME")}/{blob.name}'
            metadata = {"blob_name": blob.name, 
                        "document_link": document_link}  
            chunks = split_text_with_metadata(document, metadata)  
            documents.extend(chunks)  
        except Exception as e:  
            log_text.write(f"Failed to process blob {blob.name}: {e}")  
      
    log_text.write("Blobs processed and documents chunked.")  
      
    # Generate embeddings  
    log_text.write("Generating embeddings...")  
    embeddings = []  
    tokenizer = tiktoken.get_encoding("cl100k_base")  
    max_tokens = 8192  
    for i, doc in enumerate(documents):  
        log_text.write(f"Processing chunk {i + 1}/{len(documents)}")  
        log_text.write(f"Chunk text: {doc['text']}\n")  
        tokens = tokenizer.encode(doc["text"])  
        if len(tokens) > max_tokens:  
            log_text.write(f"Skipping document chunk {i + 1} with {len(tokens)} tokens, exceeding max limit of {max_tokens}.")  
            continue  
        response = azure_openai.embeddings.create(input=doc["text"], model=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT"))  
        embeddings.append({  
            "embedding": response.data[0].embedding,  
            "metadata": doc["metadata"]  
        })  
        log_text.write(f"Embeddings: {response.data[0].embedding}")  
      
    log_text.write("Embeddings generation complete.")  
      
    # Create Search Index  
    log_text.write("Creating search index...")  
    credential = AzureKeyCredential(os.getenv("AZURE_SEARCH_ADMIN_KEY"))  
    search_index_client = SearchIndexClient(endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"), credential=credential)  
    fields = [  
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),  
        SearchableField(name="content", type=SearchFieldDataType.String),  
        SearchableField(name="blob_name", type=SearchFieldDataType.String),  
        SearchableField(name="document_link", type=SearchFieldDataType.String),
        SearchField(  
            name="embedding",  
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),  
            searchable=True,  
            vector_search_dimensions=1536,  
            vector_search_profile_name="myHnswProfile"  
        )  
    ]  
    vector_search = VectorSearch(  
        algorithms=[  
            HnswAlgorithmConfiguration(name="myHnsw")  
        ],  
        profiles=[  
            VectorSearchProfile(  
                name="myHnswProfile",  
                algorithm_configuration_name="myHnsw"  
            )  
        ]  
    )  
    index = SearchIndex(name="documents-index", fields=fields, vector_search=vector_search)  
    search_index_client.create_index(index)  
    log_text.write("Search index created.")  
      
    # Upload chunks and embeddings to Azure AI Search  
    log_text.write("Uploading documents to search index...")  
    search_client = SearchClient(endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"), index_name="documents-index", credential=credential)  
    documents_to_upload = []  
      
    for i, doc in enumerate(embeddings):  
        documents_to_upload.append({  
            "id": str(i),  
            "content": documents[i]["text"],  
            "embedding": doc["embedding"],  
            "blob_name": doc["metadata"]["blob_name"],
            "document_link": doc["metadata"]["document_link"] 
        })  
    search_client.upload_documents(documents=documents_to_upload)  
    log_text.success("Documents uploaded to search index.")  
  
def main():  
    """  
    Main program execution function.  
    """  
    st.markdown(  
        f'<div style="text-align: center;"><img src="{"https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" }" width="{60}"></div>',  
        unsafe_allow_html=True  
    )  
    st.title("Demo - Azure OpenAI & AI Search")  
      
    task = st.sidebar.radio(  
        'Choose a function below:',  
        ['Vectorize', 'Retrieve']  
    )  
      
    # Task for retrieving documents from Azure AI Search in Streamlit UI  
    if task == 'Retrieve':  
        st.write('This demo allows users to chat over the data in the Azure AI Search Index by \
                 leveraging both semantic and vector search techniques alongside the GPT model. Semantic search enhances the querying process by comprehending \
                 the meaning and context of user queries, thereby providing more pertinent results. Vector search, on the other hand, employs \
                 numerical representations of text to identify similar content using cosine similarity. ***For users to effectively \
                 utilize this demo, it is essential that they have previously created their Azure AI Search Index, by executing the \
                 "vectorize" task.***')  
          
        if 'messages' not in st.session_state:  
            st.session_state.messages = []  
          
        index_name = os.getenv('AZURE_SEARCH_INDEX')  
          
        st.write('-'*50)  
        query = st.chat_input('Input search query here...')  
        for message in st.session_state.messages:  
            with st.chat_message(message["role"]):  
                st.markdown(message['content'])  
        if query:  
            chat_on_your_data(query, index_name, st.session_state.messages)  
      
    # Task for embedding documents from Azure Blob to Azure AI Search index in Streamlit UI  
    elif task == 'Vectorize':  
        st.write('This demo processes PDF files from Azure Blob Storage, generates embeddings, and uploads them to Azure AI Search for indexing. \
                 **Please complete this process before performing retrieval.** \
                 For users to effectively utilize this demo, it is essential that they upload PDF files from the \
                 [/search_documents](https://github.com/STRIDES/NIHCloudLabAzure/tree/main/notebooks/GenAI/search_documents) directory to Azure Blob container.')  
        if st.button("Start Process"):  
            log_text = st.empty()  
            vectorize(log_text)  
  
if __name__ == '__main__':  
    global_page_style()  
    main()  