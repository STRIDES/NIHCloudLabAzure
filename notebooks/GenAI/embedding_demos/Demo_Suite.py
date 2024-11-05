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
    st.markdown("### Chat with Your Data using Azure OpenAI API and AI Search Index (AI Search Query)")  
    st.write("""  
    This demo allows users to interact with data stored in their Azure AI Search Index using a combination of semantic and vector search methods.  
    """)  
    st.write("""  
    - **Semantic Search**: Understands the meaning and context of your queries to deliver more relevant results.  
    - **Vector Search**: Utilizes numerical representations of text to find similar content based on cosine similarity.  
    """)  
    # Ensure the user has created the Azure AI search index already  
    st.write("""  
    **Note**: Users must have created the Azure AI search index already as shown here: [Upload your own data and query over it](https://github.com/STRIDES/NIHCloudLabAzure/blob/main/notebooks/GenAI/Azure_Open_AI_README.md)  
    """)  
        
    # Horizontal divider  
    st.markdown("---")  
  
    # Generate & Search with Azure OpenAI Embeddings section  
    st.markdown("### Generate & Search with Azure OpenAI Embeddings (AOAI Embeddings)")  
    st.write("""  
    This demo enables users to generate embeddings from a pre-chunked CSV file and perform searches over the content using vector search.  
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