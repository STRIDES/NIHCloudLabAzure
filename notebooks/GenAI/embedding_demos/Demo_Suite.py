import streamlit as st  
from styling import global_page_style
  
def main():  
    # Set page configuration  
    # st.set_page_config(page_title="Azure OpenAI RAG Demo Suite", layout="wide")  
  
    # Title and subtitle  
        # Create columns for logo and title  

    st.markdown(  
    f'<div style="text-align: center;"><img src="{"https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg"  }" width="{60}"></div>',  
    unsafe_allow_html=True  
                )  
    st.title("Azure OpenAI RAG Demo Suite")  
    st.markdown("### Demo Overviews")  
    st.write("""  
    Welcome to the Azure OpenAI RAG Demo Suite. On the left side-panel, you will find various demonstrations that showcase the capabilities of Azure OpenAI with a Streamlit frontend. Each demonstration is described in detail below, highlighting their unique features and functionalities.  
    """)  
  
    # Horizontal divider  
    st.markdown("---")  
  
    # Chat with Your Data section  
    st.markdown("### Generate & Search with Azure OpenAI & Azure AI Search (AI Search Query)")  
    st.write("""  
This demo provides an interactive platform for users to manage documents stored in their Azure Blob Container. 
This is accomplished by indexing the documents in Azure AI Search and employing a combination of semantic and vector search techniques. 
In this demo, we concentrate on real documents that are housed in an Azure Blob Container. 
These documents undergo a process of chunking, after which embeddings from these chunks are stored in Azure AI Search, serving as our vector database.  
    """)  
    st.write("""  
    - **Semantic Search**: Understands the meaning and context of your queries to deliver more relevant results.  
    - **Vector Search**: Utilizes numerical representations of text to find similar content based on cosine similarity.  
    """)  
    # Ensure the user has uploaded documents to an Azure Storage Account Blob container. 
    st.write("""  
**Important**: Ensure that you have already created an Azure Storage Account and [uploaded documents](https://github.com/STRIDES/NIHCloudLabAzure/tree/main/notebooks/GenAI/search_documents) to a Blob container. If you haven't completed this step yet, please follow one of the options below:
1. [Create and upload documents via Azure CLI or PowerShell with an ARM template](https://github.com/STRIDES/NIHCloudLabAzure/blob/main/notebooks/GenAI/azure_infra_setup/README.md)
2. [Manually upload documents via Azure Portal](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal)  
    """)  
        
    # Horizontal divider  
    st.markdown("---")  
  
    # Generate & Search with Azure OpenAI Embeddings section  
    st.markdown("### Generate & Search with Azure OpenAI Embeddings (AOAI Embeddings)")  
    st.write("""  
This demo empowers users to generate embeddings from a pre-chunked CSV file and execute content searches using vector search. 
Our sole focus in this instance is on producing document embeddings with Azure OpenAI and storing them in a local .csv file. 
This exercise aids in understanding the functionality of the Azure OpenAI service, specifically its embedding generation process.  
This demo is primarily designed as a learning tool, serving as an introduction to working with embeddings in Azure OpenAI. 
As such, there is no prerequisite to chunk documents or store them in a vector database.  
    """)  
    st.write("""  
    - **Vectorize**: Creates embeddings based on the "microsoft-earnings.csv" file provided in this directory. The embeddings are generated from the "text" column. The CSV file is pre-chunked, meaning the text has already been split and prepared for embedding generation. A new CSV file will be created to store all generated embeddings, forming your vector store.  
    - **Retrieve**: Generates embeddings based on user queries. The query embedding is then used to search for the most similar document within the vector store using cosine similarity.  
    """)  
    st.write("""  
    Example questions a user can ask about the microsoft-earnings.csv:  
    - What was said about the budget?  
    - How many people utilize GitHub to build software?  
    - How many points did Microsoft Cloud gross margin percentage increase by?  
    - What are the expectations for the Q2 cash flow?  
    """)  

  
if __name__ == '__main__': 
    global_page_style() 
    main()  