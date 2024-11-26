# Setting Up Azure Environment for Azure GenAI Cloud Lab  
  
Welcome! This guide will help you set up your Azure environment to complete the activities in the [Azure GenAI](../) directory of the NIH Cloud Lab. We will walk you through the steps required to configure PowerShell, deploy necessary resources using an ARM template, upload local files to Azure Storage Account, and acquire keys and secrets for `.env` variables.  
  
## Prerequisites  

- An active Azure subscription  
- PowerShell installed on your machine (option 1)
- Azure CLI installed (option 2)
  
## Steps  
  
### 1. Setting Up the Azure Module in PowerShell  
  
First, you need to install the Azure module in PowerShell to connect to your Azure account.  
  
```powershell  
# Install the Az module (if using PowerShell)
Install-Module -Name Az -AllowClobber -Force  
  
# Import the Az module (if using Azure CLI)
Import-Module Az  
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
az login  
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
```bash
# Variables  
resourceGroupName="nihcloudlabrg"   
location="eastus2"   
templateFilePath="Path To ./arm_resources.json"  
storageAccountName="cloudlabstgacct"  
containerName="cloudlabdocuments"  
localFilePath="Path To ../search_documents"   
searchServiceName="cloudlabsearch" 
openAIResourceName="cloudlabaoai"  
```

### 4. Creating an Empty Resource Group
 
Create an empty resource group where the ARM template will deploy the necessary resources.

**Using PowerShell**
```powershell
# Create a resource group  
New-AzResourceGroup -Name $resourceGroupName -Location $location  
```
**Using Azure CLI**
```bash
# Create a resource group  
az group create --name $resourceGroupName --location $location  
```

### 5. Deploying the ARM Template

Deploy the [ARM template](/notebooks/GenAI/azure_infra_setup/arm_resources.json) to create the Azure Storage Account, Azure AI Search, and Azure OpenAI resources.

***Using PowerShell***
```powershell
# Deploy the ARM template  
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -TemplateFile $templateFilePath  
```
***Using Azure CLI***
```bash
# Deploy the ARM template  
az deployment group create --resource-group $resourceGroupName --template-file $templateFilePath 
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
```bash
# Get storage account key  
storageAccountKey=$(az storage account keys list --resource-group $resourceGroupName --account-name $storageAccountName --query "[0].value" --output tsv)  
  
# Upload all files in the directory  
for file in localFilePath/*; do  
    az storage blob upload --account-name $storageAccountName --account-key $storageAccountKey --container-name $containerName --file file --name (basename file)  
done  
```

### 7. Retrieving API Keys
 
Retrieve the API keys for each service created by the ARM template deployment. These secrets are confidential and should be handled appropriately. Once the output is received, the values will be added to your `.env` file, which should be created in the ./notebooks/GenAI directory. Note that this `.env` file is already added to the `.gitignore`.

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
```bash
# Get the storage account key  
storageAccountKey=(az storage account keys list --resource-group $resourceGroupName --account-name $storageAccountName --query '[0].value' --output tsv)  
echo $storageAccountKey
# Construct the Blob connection string  
connectionString="DefaultEndpointsProtocol=https;AccountName=$storageAccountName;AccountKey=$storageAccountKey;EndpointSuffix=core.windows.net"
echo $connectionString
```

You now have the secrets to set the following .env variables in your local file. Copy the values to your `.env`:
- ***BLOB_CONTAINER_NAME*** = Use the value of `$containerName` or `containerName`. 
- ***BLOB_CONNECTION_STRING*** = Use the value of `$connectionString ` or `connectionString`.  
- ***BLOB_ACCOUNT_NAME*** = Use the value of `$storageAccountName` or `storageAccountName`. 

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
```bash
# Acquire the AI Search Admin Key
searchServiceKey = az search admin-key show --resource-group resourceGroupName --service-name $searchServiceName --query primaryKey -o tsv
echo $searchServiceKey
# Construct the AI Search endpoint 
searchServiceEndpoint="https://$searchServiceName.search.windows.net"
echo $searchServiceEndpoint
```

You now have the secrets to set the following .env variables in your local file. Copy the values to your `.env`:
- ***AZURE_SEARCH_ENDPOINT*** =  Use the value of `$searchServiceEndpoint` or `searchServiceEndpoint`.
- ***AZURE_SEARCH_ADMIN_KEY*** = Use the value of `$searchServiceKey` or `searchServiceKey`.

**Azure OpenAI**

***Using PowerShell***
```powershell
# Get the Azure OpenAI key 1
$openAIKey = az cognitiveservices account keys list --resource-group $resourceGroupName --name $openAIResourceName --query "key1" --output tsv
Write-Output $openAIKey
# Construct the Azure OpenAI endpoint
$openAIEndpoint = "https://$openAIResourceName.openai.azure.com/"
Write-Output $openAIEndpoint
```
***Using Azure CLI***
```bash
# Get the Azure OpenAI key  
openAIKey=$(az cognitiveservices account keys list --resource-group $resourceGroupName --name $openAIResourceName  --query "key1" --output tsv)  
echo $openAIKey
# Construct the Azure OpenAI endpoint
openAIEndpoint = "https://$openAIResourceName.openai.azure.com/"
echo $openAIEndpoint
```

You now have the secrets to set the following .env variables in your local file. Copy the values to your `.env`:
- ***AZURE_OPENAI_ENDPOINT*** = Use the value of `$openAIEndpoint` or `openAIEndpoint`.
- ***AZURE_OPENAI_KEY*** = Use the value of `$openAIKey` or `openAIKey`.
- ***AZURE_GPT_DEPLOYMENT*** = Use the value of `gpt-4o-mini`.
- ***AZURE_EMBEDDINGS_DEPLOYMENT*** = Use the value of `text-embedding-3-small`.

**Note**: To find the ***API version (Azure_OPENAI_VERSION)*** for your resource in the Azure OpenAI playground, follow these steps:
1. **Navigate to Deployments**: In the left side panel of the Azure OpenAI playground, click on “Deployments.”
2. **Select the Model Deployment**: Click on the specific model deployment you are working with.
3. **Locate the Endpoint Section**: In the endpoint section, you will see the Target URI.
4. **Find the API Version**: Look for the part of the URL that includes `api-version=2024-08-01-preview`. This will be your API version.

Your final local `.env` file should look something like this:
```sh
AZURE_OPENAI_VERSION = "Your Azure OpenAI API version"  
AZURE_OPENAI_ENDPOINT = "Your Azure OpenAI API endpoint"
AZURE_OPENAI_KEY = "Your Azure OpenAI API key"
AZURE_GPT_DEPLOYMENT = "Your Azure OpenAI deployed GPT model name"
AZURE_EMBEDDINGS_DEPLOYMENT = "Your Azure OpenAI deployed ADA model name"
AZURE_SEARCH_ENDPOINT = "Your Azure AI Search API endpoint"
AZURE_SEARCH_ADMIN_KEY = "Your Azure AI Search API key"
BLOB_CONTAINER_NAME = "Your Azure Blob Container name hosting files from /search_documents"
BLOB_CONNECTION_STRING = "Your Azure Blob connection string"
```
## Conclusion

Congratulations on completing the Azure setup! During this process, we established a new resource group dedicated to the NIH Cloud Lab environment and configured three Azure resources in your tenant using an ARM template file. The resources include:

- An Azure Storage Account with a deployed Blob container and files uploaded from `../search_documents`
- Azure AI Search
- Azure OpenAI with deployed `gpt-4o-mini` and `text-embedding-3-small` models

Additionally, we configured `.env` variables in your local `.env` file, which is added to `.gitignore` by default.

You are now ready to proceed with the GenAI activities in the NIH Cloud Lab.