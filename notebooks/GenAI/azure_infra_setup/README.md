# Setting Up Azure Environment for Azure GenAI Cloud Lab 

This guide will help you set up your Azure environment to complete the activities in the [GenAI](../) directory of the NIH Cloud Lab. 
The purpose of this guide is to walk you through an automated deployment of the resources needed to carry out these activities. 
This automated approach utilizes a pre-built [ARM template](arm_resources.json) file, which serves as an alternative approach
to manually deploying and configuring resources via the Azure portal.

## Page Contents
+ [Learning Objectives](#learning_objectives)
+ [Prerequisites](#prerequisites)
+ [Resources and Pricing](#resources_and_pricing)
+ [Get Started](#get_started)
+ [Conclusion](#conclusion)
+ [Clean Up](#clean_up)

## Learning Objectives <a name="learning_objectives"></a>

1. Configure PowerShell or Azure CLI
    - Step-by-step instructions to set up and configure PowerShell and Azure CLI for the neccessary Azure resource deployments.
2. Deploy Resources Using an ARM Template
    - Detailed guidance on deploying the necessary resources in Azure using an ARM template for the [GenAI](../) directory.
3. Upload Local Files to Azure Storage Account
    - Instructions on how to upload files from the [search_documents](../search_documents/) directory to an Azure Storage Account Blob container.
4. Acquire Keys and Secrets for .env Variables
    - Steps to obtain keys and secrets from deployed resources and use them in your .env files for the tutorials in the [GenAI](../) directory.

## Prerequisites <a name="prerequisites"></a>

- An active Azure subscription  
- PowerShell installed on your machine (option 1)
- Azure CLI installed (option 2)

### Powershell (option 1) vs. Azure CLI (option 2)

Choosing between Azure CLI and PowerShell comes down to personal preference and the working environment:

- **Cloud Environments**: For users working in the cloud, such as with Azure Machine Learning or Azure VMs, Azure CLI may be a more suitable option.
    - ***Note***: If users are utilizing any of these environments, please skip Step 1 and move directly to Step 2 using Azure CLI (option 2).
- **Local Environments**: For users working on a local machine, both Azure CLI and PowerShell are viable options. The choice depends on personal preference.
    - ***Note***: If users are utilizing Azure CLI, please skip Step 1 and move directly to Step 2. 

## Resources and Pricing <a name="resources_and_pricing"></a>
  
Provided is a list of resources that will be deployed by the provided ARM template along with the estimated cost breakdown for each resource.
***An ARM Template is a JSON file that defines the infrastructure and configuration for your Azure project***. It allows you to deploy, manage, and configure 
all the resources for your solution in a single, coordinated operation. When executing the provided ARM template, actual costs may vary depending on usage 
and the Azure pricing model for each resource. Please find the resources that will be deployed below. 
  
### Resources Deployed 
1. **Azure Storage Account**  
   - **Resource Type**: Storage Account (Standard_LRS)  
   - **Purpose**: This resource is used to store and manage files from [search_documents](../search_documents/) in a single container. 
   - **Estimated Cost**: $0.018 per GB/$18.40 per 1000 GB per month
  
2. **Azure AI Search**  
   - **Resource Type**: Cognitive Search (Basic)  
   - **Purpose**: This resource provides AI search capabilities for the GenAI tutorials, including indexing and querying.  
   - **Estimated Cost**: $0.10 per hour/$73.73 per month
  
3. **Azure OpenAI**  
   - **Resource Type**: Cognitive Services (Standard)  
   - **Purpose**: This resource provides access to OpenAI models, including GPT-4 and embeddings for AI processing.  
   - **Models Deployed**:  
     - **Model**: gpt-4o-mini  
       - **Version**: 2024-07-18  
       - **Cost per 1M Tokens**: $0.15 input/$0.60 output
     - **Model**: text-embedding-3-small  
       - **Version**: 1  
       - **Cost per 1K Tokens**: $0.00002
   - **Estimated Cost**: Varies based on model usage and API calls. Please refer to [Azure OpenAI Service Pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/?msockid=3df6a53ac4916aa73e41b1e3c5c36bd4) for more details. 
  
Please refer to the [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/) for a more detailed and personalized estimate based on your specific usage patterns and region.  
  
## Get Started <a name="get_started"></a>
  
### 1. Setting Up the Azure Module in PowerShell  
  
First, you need to install the Azure module in PowerShell to connect to your Azure account.  

```powershell
# Install the Az module (if using PowerShell)
Install-Module -Name Az -AllowClobber -Force  
```

### 2. Logging into Azure 

You can log into your Azure account either using PowerShell or Azure CLI.

**Using PowerShell**
```powershell
# Log into your Azure account 
Connect-AzAccount  
```
**Using Azure CLI**
```powershell
# Log into your Azure account 
!az login  
```

### 3. Setting Variables 

Set the following variables, which you'll need throughout the setup process.

**Using PowerShell**
```powershell
# Variables  
$resourceGroupName="nihcloudlabrg"  
$location="eastus2"  
$templateFilePath="Path To ./arm_resources.json"  
$storageAccountName="cloudlabstgacct"  
$containerName="cloudlabdocuments"  
$localFilePath="Path To ../search_documents"  
$searchServiceName="cloudlabsearch"  
$openAIResourceName="cloudlabaoai"  
```
**Using Azure CLI**
```powershell
# Variables  
resourceGroupName = 'nihcloudlabrg'   
location = 'eastus2'
templateFilePath = "arm_resources.json"  
storageAccountName = "cloudlabstgacct"  
containerName = "cloudlabdocuments"  
localFilePath = "../search_documents"   
searchServiceName = "cloudlabsearch" 
openAIResourceName = "cloudlabaoai"  
openAImodel_name = "gpt-4o-mini"
openAIEmbeddingmodel_name = "text-embedding-3-small"
```

### 4. Creating an Empty Resource Group
 
Create an empty resource group where the ARM template will deploy the necessary resources.

**Using PowerShell**
```powershell
# Create a resource group  
New-AzResourceGroup -Name $resourceGroupName -Location $location 
```
**Using Azure CLI**
```powershell
# Create a resource group  
! az group create --name {resourceGroupName} --location {location}
```

### 5. Deploying the ARM Template

Deploy the [ARM template](arm_resources.json) to create the Azure Storage Account, Azure AI Search, and Azure OpenAI resources.

***Using PowerShell***
```powershell
# Deploy the ARM template  
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -TemplateFile $templateFilePath  
```
***Using Azure CLI***
```powershell
# Deploy the ARM template  
!az deployment group create \
--resource-group {resourceGroupName} \
--template-file {templateFilePath} \
--parameters accounts_cloudlabaoai_name={openAIResourceName} \
--parameters model_name={openAImodel_name} \
--parameters embeddingModel_name={openAIEmbeddingmodel_name} \
--parameters searchServices_cloudlabsearch_name={searchServiceName} \
--parameters storageAccounts_genaicloudlab_name={storageAccountName}

```

### 6. Uploading Local Files to Azure Storage

Upload your local files to the blob container in the Azure Storage Account.

**Using PowerShell**
```powershell
# Get storage account context  
$storageContext = (Get-AzStorageAccount -ResourceGroupName $resourceGroupName -Name $storageAccountName).Context  
  
# Upload all files in the directory  
Get-ChildItem -Path $localFilePath -File | ForEach-Object {  
    Set-AzStorageBlobContent -File $_.FullName -Container $containerName -Context $storageContext  
}  
```
**Using Azure CLI**
```powershell
# Get storage account key 
storageAccountKey=!az storage account keys list --resource-group {resourceGroupName} --account-name {storageAccountName} --output tsv --query "[0].value"
```

```bash magic_args="-s \"$localFilePath\" \"$storageAccountName\" \"$storageAccountKey\" \"$containerName\""
for file in $1/*;
do
    az storage blob upload --account-name $2 --account-key $3 --container-name $4 --file "$file" --name $(basename "$file")  
done 
```

### 7. Retrieving API Keys
 
Retrieve the API keys for each service created by the ARM template deployment. These secrets are confidential and should be handled appropriately. 
Once the output is received, the values should be added to your `.env` file, which should be created in the [GenAI](../) directory. 
Note that this `.env` file is already added to the `.gitignore` file, which tells Git which files or directories to ignore in a project, 
preventing them from being tracked or included in version control. Adding `.env` to `.gitignore` is crucial because it prevents sensitive information 
like API keys and passwords from being exposed in your version control system.

**Azure Storage Account**

***Using PowerShell***
```powershell
# Get the storage account key
$storageAccountKey = (Get-AzStorageAccountKey -ResourceGroupName $resourceGroupName -Name $storageAccountName)[0].Value 
# Construct the Blob connection string  
$connectionString = "DefaultEndpointsProtocol=https;AccountName=$storageAccountName;AccountKey=$storageAccountKey;EndpointSuffix=core.windows.net"
# Output the connection string
Write-Output $connectionString
```
***Using Azure CLI***
```powershell
# Get the storage account key that was made before in step 6 
!echo "BLOB_CONTAINER_NAME={containerName}" >> .env
!echo "BLOB_ACCOUNT_NAME={storageAccountName}" >> .env
# Construct the Blob connection string  
connectionString=f"DefaultEndpointsProtocol=https;AccountName={storageAccountName};AccountKey={storageAccountKey[0]};EndpointSuffix=core.windows.net"
!echo "BLOB_CONNECTION_STRING={connectionString}" >> .env

```

Lets take a look at our .env file!

```powershell
!cat .env
```

You now have the secrets and variables set in a .env. If you run into any errors you can also copy them to your .env file using the info below:
- ***BLOB_CONTAINER_NAME*** = Use the value of `$containerName` or `containerName`.  
- ***BLOB_ACCOUNT_NAME*** = Use the value of `$storageAccountName` or `storageAccountName`. 
- ***BLOB_CONNECTION_STRING*** = Use the value of `$connectionString ` or `connectionString`. 

**Azure AI Search**

***Using PowerShell***
```powershell
# Acquire the AI Search Admin Key
$adminKeys = Get-AzSearchAdminKeyPair -ResourceGroupName $resourceGroupName -ServiceName $searchServiceName
Write-Output $adminKeys
# Construct the AI Search Admin Key
$searchServiceEndpoint="https://$searchServiceName.search.windows.net"
Write-Output $searchServiceEndpoint
```
***Using Azure CLI***
```powershell
# Acquire the AI Search Admin Key
searchServiceKey = !az search admin-key show --resource-group {resourceGroupName} --service-name {searchServiceName} --query primaryKey -o tsv
!echo "AZURE_SEARCH_API_KEY={searchServiceKey[0]}" >> .env
# Construct the AI Search endpoint 
searchServiceEndpoint=f"https://{searchServiceName}.search.windows.net"
!echo "AZURE_SEARCH_SERVICE_ENDPOINT={searchServiceEndpoint}" >> .env
```

Lets take a look at our .env file!

```powershell
!cat .env
```

<!-- #region -->
You now have the secrets and variables set in a .env. If you run into any errors you can also copy them to your .env file using the info below:
- ***AZURE_SEARCH_ADMIN_KEY*** = Use the value of `$searchServiceKey` or `searchServiceKey`.
- ***AZURE_SEARCH_ENDPOINT*** =  Use the value of `$searchServiceEndpoint` or `searchServiceEndpoint`.


**Azure OpenAI**

***Using PowerShell***
<!-- #endregion -->
```powershell
# Get the Azure OpenAI key 1
$openAIKey = az cognitiveservices account keys list --resource-group $resourceGroupName --name $openAIResourceName --query "key1" --output tsv
Write-Output $openAIKey
# Construct the Azure OpenAI endpoint
$openAIEndpoint = "https://$openAIResourceName.openai.azure.com/"
Write-Output $openAIEndpoint
```
***Using Azure CLI***
```powershell
!echo "AZURE_GPT_DEPLOYMENT={openAImodel_name}" >> .env
!echo "AZURE_EMBEDDINGS_DEPLOYMENT={openAIEmbeddingmodel_name}" >>.env

# Construct the Azure OpenAI endpoint
openAIEndpoint = f"https://{openAIResourceName}.openai.azure.com/"
!echo "AZURE_OPENAI_ENDPOINT={openAIEndpoint}" >> .env
# Get the Azure OpenAI key 
openAIKey=!az cognitiveservices account keys list --resource-group {resourceGroupName} --name {openAIResourceName}  --query "key1" --output tsv  
!echo "AZURE_OPENAI_API_KEY={openAIKey[0]}" >> .env

```

```powershell
cat .env
```

<!-- #region -->
You now have the secrets and variables set in a .env. If you run into any errors you can also copy them to your .env file using the info below:
- ***AZURE_GPT_DEPLOYMENT*** = Use the value of `gpt-4o-mini`.
- ***AZURE_EMBEDDINGS_DEPLOYMENT*** = Use the value of `text-embedding-3-small`.
- ***AZURE_OPENAI_ENDPOINT*** = Use the value of `$openAIEndpoint` or `openAIEndpoint`.
- ***AZURE_OPENAI_KEY*** = Use the value of `$openAIKey` or `openAIKey`.


**Note**: To find the ***API version (Azure_OPENAI_VERSION)*** for your resource in the Azure OpenAI playground, follow these steps:
1. **Navigate to Deployments**: In the left side panel of the Azure OpenAI playground, click on “Deployments.”
2. **Select the Model Deployment**: Click on the specific model deployment you are working with.
3. **Locate the Endpoint Section**: In the endpoint section, you will see the Target URI.
4. **Find the API Version**: Look for the part of the URL that looks similar to `api-version=2025-01-01-preview`. This will be your API version. This may differ between models

Your final local `.env` file should look something like this:
<!-- #endregion -->
```powershell
!cat .env
```

## Conclusion <a name="conclusion"></a>

Congratulations on completing the Azure setup! During this process, we established a new resource group dedicated to the NIH Cloud Lab environment and 
configured three Azure resources in your tenant using an ARM template file. The resources include:

- An Azure Storage Account with a deployed Blob container and files uploaded from `../search_documents`
- Azure AI Search
- Azure OpenAI with deployed `gpt-4o-mini` and `text-embedding-3-small` models

Additionally, we configured `.env` variables in your local `.env` file, which is added to `.gitignore` by default.

You are now ready to proceed with the GenAI tutorials!

## Clean Up <a name="clean_up"></a>
No clean up neccessary, as the created resources will be used for tutorials found in [GenAI](../) folder, specifically [embeddings demos](../embedding_demos/readme.md) and [AI Search RAG chatbot](../notebooks/AISearch_RAG_chatbot.ipynb) tutorial . 
