# Azure OpenAI Demo w/ Streamlit Frontend

The Azure OpenAI Demo w/ Streamlit Frontend is designed to host various demonstrations that showcase the capabilities of Azure OpenAI with a Streamlit frontend. Demonstrations include utilizing Azure OpenAI to create/chat over data indexes in Azure AI Search, and utilizing Azure OpenAI SDK to generate embeddings for text and query those embeddings. For documentation on building Streamlit apps, please search links below:
- [Streamlit Documentation](https://docs.streamlit.io/get-started)
- [Geeksforgeeks](https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/)

## Environment Setup
To excute this demo, be sure to complete the following steps:

1. Create a virtual environment in the \GenAI directory.

    - Navigate to the /GenAI directory:
        ```sh
        cd .\notebooks\GenAI
        ```
    - Create the virtual environment:
        ```
        python -m venv venv
        ```
        - ***Note: This command will create a virtual environment named venv in \GenAI***
    - Activate the virtual environment:
        - On ***Windows***:
            ```sh
            venv\Scripts\activate
            ```
        - On ***macOS/Linux***:
            ```sh
            source venv/bin/activate
            ```

2. Install all required libraries from the provided requirements.txt file. 
    ```sh
    pip install -r requirements.txt  
    ```

3.  Create a .env file in the /GenAI directory and set the following variables:
    ```sh
    AZURE_OPENAI_VERSION = "Your Azure OpenAI API version"  
    AZURE_OPENAI_BASE = "Your Azure OpenAI API endpoint"
    AZURE_OPENAI_KEY = "Your Azure OpenAI API key"
    AZURE_GPT_DEPLOYMENT = "Your Azure OpenAI deployed GPT model name"
    AZURE_EMBEDDINGS_DEPLOYMENT = "Your Azure OpenAI deployed ADA model name"
    AZURE_SEARCH_ENDPOINT = "Your Azure AI Search API endpoint"
    AZURE_SEARCH_ADMIN_KEY = "Your Azure AI Search API key"
    AZURE_SEARCH_INDEX = "documents-index" # The index name 'documents-index' is used as default in this demo
    BLOB_CONTAINER_NAME = "Your Azure Blob Container name hosting files from /search_documents"
    BLOB_CONNECTION_STRING = "Your Azure Blob connection string"
    ```

4. Navigate to the /embeddings directory (location of the Streamlit demo)
    ```sh
    cd .\notebooks\GenAI\embedding_demos 
    ```

5. Execute the Streamlit demo
    ```sh
    streamlit run Demo_Suite.py
    ```