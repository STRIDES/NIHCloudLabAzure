# Azure OpenAI Demo w/ Streamlit Frontend

The Azure OpenAI Demo w/ Streamlit Frontend is designed to host various demonstrations that showcase the capabilities of Azure OpenAI with a Streamlit frontend. Demonstrations include utilizing Azure OpenAI to create/chat over data indexes in Azure AI Search, and utilizing Azure OpenAI SDK to generate embeddings for text and query those embeddings. For documentation on building Streamlit apps, please search links below:
- [Streamlit Documentation](https://docs.streamlit.io/get-started)
- [Geeksforgeeks](https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/)

## Page Contents
+ [Learning Objectives](#learning_objectives)
+ [Prerequisites](#prerequisites)
+ [Overview of Streamlit Scripts](#overview_of_streamlit_scripts)
+ [Executing the Azure OpenAI Demo w/ Streamlit Frontend](#executing_the_azure_openai_demo)
+ [Conclusion](#conclusion) 
+ [Clean Up](#clean_up)

## Learning Objectives <a name="learning_objectives"></a>
1. **Integrate Azure OpenAI with Streamlit**:
    - Use Azure OpenAI in a Streamlit frontend. 
2. **Understand Streamlit Scripts**:
    - Learn the roles and functionalities of `Demo_Suite.py`, `AI_Search_Query.py`, and `AOAI_Embeddings.py`.
3. **Generate and Query Embeddings**:
    - Create and query text embeddings using the Azure OpenAI SDK.
4. **Use Ngrok with Azure ML**:
    - Set up Ngrok to securely run the demo on Azure ML or a VM.
5. **Setup Development Environment**:
    - Create a virtual environment, install dependencies, and configure environment variables.
    - Execute the Streamlit demo locally and in cloud environments.

## Prerequisites <a name="prerequisites"></a>
Before proceeding with this notebook, please ensure that you have the following Azure services deployed and configured. Resources can be deployed manually in Azure portal or automated by following along with the [ARM Deployment tutorial](../azure_infra_setup/README.md):  
  
1. **Azure OpenAI Service**:   
    - Ensure that you have deployed both a GPT model and an Ada model within your Azure OpenAI instance.
    - Estimated costs for this service varies based on the model usage and number of API calls.
        - ***gpt-4o-mini(2024-07-18): $0.15 input/$0.60 output per 1M tokens***
        - ***text-embedding-3-small(1): $0.00002 per 1K tokens***
2. **Azure AI Search**:   
    - Your Azure AI Search service should be a minimum of the Basic tier to ensure compatibility with Azure OpenAI.  
    - ***Estimated cost for this service is $0.10 per hour.***
3. **Azure Blob Storage Account**:   
    - You should have an Azure Blob Storage account with PDF files stored in a blob container. These files should be located in the `/search_documents` directory of the `GenAI` directory.  
    - ***Estimated cost for this service is $0.018 per GB.***

## Overview of Streamlit Scripts <a name="#overview_of_streamlit_scripts"></a>
  
### Demo_Suite.py  
  
**Purpose**:   
This script serves as the home page for the Azure OpenAI Demo site. It is the initial script that Streamlit runs to start the demo, providing users with an overview of the demo site and descriptions of each available demonstration.  
  
**Key Points**:  
- **Location**: This file is located in the root directory (/embedding_demos).  
- **Functionality**:  
  - Launches the Streamlit UI.  
  - Displays descriptive information about the demo site content.  
  - Provides links and descriptions for each demo page.  
- **Usage**: Run this script using the command `streamlit run demo_suite.py`.  
  
### AI_Search_Query.py  
  
**Purpose**:  
This script serves as the frontend for the embedding demo that utilizes Azure AI Search and Azure OpenAI SDKs to chat over documents stored in a Blob Storage account.  
  
**Key Points**:  
- **Location**: This file is located in the /pages subdirectory, identifying it as a subpage in the Streamlit interface.  
- **Functionality**:  
  - Allows users to interact with documents stored in the [/search_documents](../search_documents) directory.  
  - Consistent with the [AISearch_RAG_chatbot.ipynb](../notebooks/AISearch_RAG_chatbot.ipynb) tutorial.  
  - Provides a user interface for querying and chatting over the documents using Azure AI Search and OpenAI capabilities.  
- **Usage**: Accessible from the main page (demo_suite.py) via the left sidebar.  
  
### AOAI_Embeddings.py  
  
**Purpose**:  
This script serves as the frontend for the embedding demo that uses the Azure OpenAI SDK to generate embeddings for pre-chunked text in the [microsoft-earnings.csv](../microsoft-earnings.csv) file.  
  
**Key Points**:  
- **Location**: This file is located in the /pages subdirectory, identifying it as a subpage in the Streamlit interface.  
- **Functionality**:  
  - Demonstrates how to generate embeddings for text using the Azure OpenAI SDK.  
  - Consistent with the [AzureOpenAI_embeddings.ipynb](../notebooks/AzureOpenAI_embeddings.ipynb) tutorial.  
  - Provides a user interface for generating and viewing embeddings.  
- **Usage**: Accessible from the main page (demo_suite.py) via the left sidebar.   

## Executing the Azure OpenAI Demo w/ Streamlit Frontend <a name="executing_the_azure_openai_demo"></a>

In this phase, you will choose your preferred environment to execute the Azure OpenAI Demo with a Streamlit frontend. You can either use Azure ML or run the demo locally using VSCode. Please choose an execution environment below:
+ [Executing via Azure ML or VM](#executing_via_azure_ml_vm)
+ [Executing via VsCode](#executing_via_vscode)

### Executing via Azure ML or VM <a name="executing_via_azure_ml_vm"></a>
Streamlit's native behavior expects to run applications locally on port 8501, which isn't possible when executing this demo from Azure ML or a VM. **Ngrok** is a tool that creates a secure tunnel to expose a local server to the internet. By using Ngrok, you can securely expose the Streamlit demo app running on Azure ML or a VM to the internet, bypassing the limitation of needing to run it on the local port 8501. This ensures that you can access and interact with the Streamlit application without needing to run from your local machine.

**Phase 1 - Obtain a free Ngrok Authtoken:**
    
1. Visit the Ngrok website: https://ngrok.com.
2. Click on the "Sign Up" button at the top right corner.
3. Sign up using your email address and create a password, or use your GitHub account.
4. Check your email for a verification message from Ngrok.
5. Click the verification link in the email to activate your account.
6. Log in to your Ngrok account.
7. Once logged in, you will be taken to your dashboard.
8. In your dashboard, find and copy your authentication (Authtoken) token. This token will be used for the `ngrok_key` variable in step 2. 

**Phase 2 - Create a .env file:**
1. Open the terminal in your Azure ML Studio or Azure VM instance. 
2. Navigate to the ***/GenAI*** directory:
    ```bash
    cd ./notebooks/GenAI
    ```
3. Create a `.env` file by executing the following command:
    ```bash
    nano .env
    ``` 
4. In the text editor add the following variables:
    ```bash
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
        ngrok_key = "Your Ngrok Authtoken from STEP 1"
    ```
5. Save the `.env` file and exit the text editor:
    - Press `Ctrl + X` to exit the text editor. 
    - Press `Shift + Y` to save the changes to the file. 
    - Press `Enter` to confirm the file name to be saved (filename will be .env since we used `nano .env` command)
6. Output the `.env` variables from terminal to ensure all variables are present:
    ```bash
    cat .env
    ```
**Phase 3 - Configure the virtual environment:**
1. If not already in ***/GenAI***, navigate there by:
    ```bash
    cd ./notebooks/GenAI
    ```
2. Create a virtual environment in ***/GenAI*** by executing the following command:
    ```bash
    python3 -m venv --clear .venv
    ```
    ***Note: This command will create a virtual environment named venv in \GenAI***

3. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
4. Install all required libraries from the provided [requirements.txt](../requirements.txt) file to the virtual environment. 
    ```bash
    pip install -r requirements.txt  
    ```

**Phase 4 - Execute the Streamlit demo:**
1. Navigate to the /embeddings directory (location of the Streamlit demo):
    ```bash
    cd ./embedding_demos 
    ```
2. Execute the Streamlit demo:
    - Run the [Demo_Suite_ngrok.py](./Demo_Suite_ngrok.py) file. This file will generate the secure Ngrok tunnel to access the Streamlit app. You do not need to run the `Demo_Suite.py` file. 
        ```bash
        python Demo_Suite_ngrok.py
        ```
        ***Note: Access the Streamlit site from the provided URL in the terminal.***
        
        %Insert Image Here%



### Executing via VsCode <a name="executing_via_vscode"></a>
To excute this demo, be sure to complete the following steps:

1. Create a virtual environment in the /GenAI directory.

    - Navigate to the /GenAI directory:
        ```sh
        cd ./notebooks/GenAI
        ```
    - Create the virtual environment:
        ```
        python -m venv .venv
        ```
        - ***Note: This command will create a virtual environment named venv in /GenAI***
    - Activate the virtual environment:
        - On ***Windows***:
            ```sh
            .venv/Scripts/activate
            ```
        - On ***macOS/Linux***:
            ```sh
            source .venv/bin/activate
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

4. Navigate to the /embedding_demos directory (location of the Streamlit demo)
    ```sh
    cd ./embedding_demos 
    ```

5. Execute the Streamlit demo
    ```sh
    streamlit run Demo_Suite.py
    ```

## Conclusion <a name="conclusion"></a>
By completing the "Azure OpenAI Demo w/ Streamlit Frontend" tutorial, you have gained valuable hands-on experience in integrating Azure OpenAI services with a Streamlit frontend. You have learned how to set up and configure essential components, including Azure OpenAI, Azure AI Search, and Azure Blob Storage. Additionally, you have explored the functionalities of key scripts and understood how to generate and query embeddings for interactive applications. This tutorial also guided you through executing the demo both on Azure ML using Ngrok and locally using VSCode, ensuring you are equipped to handle different deployment scenarios. We hope this tutorial has been informative and empowers you to leverage Azure OpenAI and Streamlit for your future projects.

## Clean Up <a name="clean_up"></a>
Make sure to shut down your Azure ML compute and if desired you can delete your Azure AI Search service, Azure Blob Storage Account, and Azure OpenAI service. ***Note these services can be used in other tutorials in this notebook.***