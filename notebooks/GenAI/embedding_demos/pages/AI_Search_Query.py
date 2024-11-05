from openai import AzureOpenAI  
import os
import streamlit as st
from dotenv import load_dotenv
from styling import global_page_style

# load in .env variables 
load_dotenv()

# Configure Azure OpenAI params, using an Azure OpenAI account with a deployment of an embedding model
azure_endpoint: str = os.getenv('AZURE_OPENAI_BASE')
azure_openai_api_key: str = os.getenv('AZURE_OPENAI_KEY')
azure_openai_api_version: str = os.getenv('AZURE_OPENAI_VERSION')
azure_ada_deployment: str = os.getenv('AZURE_EMBEDDINGS_DEPLOYMENT')
azure_gpt_deployment: str = os.getenv('AZURE_GPT_DEPLOYMENT')

# Configure Azure AI Search params
search_endpoint: str = os.getenv('AZURE_SEARCH_ENDPOINT')
search_key: str = os.getenv('AZURE_SEARCH_ADMIN_KEY')

def chat_on_your_data(query, search_index, messages):
    messages.append({"role": "user", "content":query})  
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
                {"role": "system", "content": "You are an AI assistant that helps people find information. \
                Ensure the Markdown responses are correctly formatted before responding."},  
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
                        "endpoint": f"{search_endpoint}",  
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
                            "key": f"{search_key}"  
                        },  
                        "embedding_dependency": {  
                            "type": "deployment_name",  
                            "deployment_name": azure_ada_deployment 
                        }  
                    }  
                }]  
            }  
        )  
        print(completion)
        response_data = completion.to_dict()  
        ai_response = response_data['choices'][0]['message']['content'] 
        messages.append({"role": "assistant", "content":ai_response})  
        with st.chat_message("assistant"):  
            st.markdown(ai_response) 

def main():
    st.markdown(  
    f'<div style="text-align: center;"><img src="{"https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg"  }" width="{60}"></div>',  
    unsafe_allow_html=True  
                )  
    st.title("Demo - Azure OpenAI & AI Search")
    # image = Image.open('image_logo2.png')
    # st.image(image, caption = '')
    st.write('This demo showcases an innovative way for users to engage with data housed in their Azure AI Search Index by leveraging both \
             semantic and vector search techniques. Semantic search enhances the querying process by comprehending the meaning and context of \
             user queries, thereby providing more pertinent results. Vector search, on the other hand, employs numerical representations of \
             text to identify similar content using cosine similarity. ***For users to effectively utilize this demo, it is essential that they \
             have previously created their Azure AI Search Index, following the necessary steps to upload and query their data as outlined [here](https://github.com/STRIDES/NIHCloudLabAzure/blob/main/notebooks/GenAI/Azure_Open_AI_README.md).***')
    if 'messages' not in st.session_state:  
        st.session_state.messages = []  
    index_name = st.text_input(label="Azure AI Search index name:", value="")
    st.write('-'*50)
    if index_name:
        query = st.chat_input('Input search query here...')
        for message in st.session_state.messages:  
            with st.chat_message(message["role"]):  
                st.markdown(message['content'])  
        if query:
            chat_on_your_data(query, index_name, st.session_state.messages)


if __name__ == '__main__':
    global_page_style()
    main()