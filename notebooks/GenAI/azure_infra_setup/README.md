
# **Setting Up Azure Environment for Azure GenAI Cloud Lab**
****


##### **Skill Level: Beginner**


This guide will help you set up your Azure environment to complete the activities in the [GenAI](https://github.com/STRIDES/NIHCloudLabAzure/tree/main/notebooks/GenAI) directory of the NIH Cloud Lab. The purpose of this guide is to walk you through a deployment of the resources needed to carry out these activities.


### Prerequisites
*****


- An active Azure subscription


### Resources and Pricing
*****


Provided is a list of resources that will be deployed along with the estimated cost breakdown for each resource. Please find the resources that will be deployed below.


#### Resources deployed


1. ##### **Azure Storage Account**
   -  **Resource Type:** Storage Account (Standard_LRS)
   -  **Purpose:** This resource is used to store and manage files.
   -  **Estimated Cost:** $0.018 per GB / $18.40 per 1000 GB per month
2. ##### **Azure OpenAI**
   - **Resource Type:** Cognitive Services (Standard)
   - **Purpose:** This resource provides access to OpenAI models, including GPT and embeddings for AI processing.
   - **Models Deployed.**
     - **Model:** gpt-5.4-nano
       - **Version:** 2024-07-18
       - **Cost per 1M Tokens:** $0.15 input / $0.60 output  
     - **Model:** text-embedding-3-small  
       - **Version:** 1  
       - **Cost per 1K Tokens:** $0.00002  
   - **Estimated Cost:** Varies based on model usage and API calls. Please refer to [Azure OpenAI Service Pricing](https://azure.microsoft.com/en-us/pricing/details/azure-openai/?msockid=3df6a53ac4916aa73e41b1e3c5c36bd4) for more details.

Please refer to the [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/) for a more detailed and personalized estimate based on your specific usage patterns and region.


#### Get Started
****

### Azure OpenAI
****


Navigate to Azure OpenAI. The easiest way is to search at the top of the page.


![AZ_OpenAI_setup_1.jpg](/docs/images/AZ_OpenAI_setup_1.jpg)


Click **Create** and then select **Foundry (Recommended)**


![AZ_OpenAI_setup_2.jpg](/docs/images/AZ_OpenAI_setup_2.jpg)


In a **Create a Foundry resource window**, you should be able to see your Azure Subscription and click **Create new** for resource group


![AZ_OpenAI_setup_3.jpg](/docs/images/AZ_OpenAI_setup_3.jpg)


Select Region **East US 2**, create Name for your foundry resource, click **Review + create** and click **Create**


![AZ_OpenAI_setup_4.jpg](/docs/images/AZ_OpenAI_setup_4.jpg)

![AZ_OpenAI_setup_5.jpg](/docs/images/AZ_OpenAI_setup_5.jpg)  

You would see a message that **Deployment is in progress**

![AZ_OpenAI_setup_6.jpg](/docs/images/AZ_OpenAI_setup_6.jpg)  


There should be a messsage that **Your deployment is complete**. Select **Go to resource**

![AZ_OpenAI_setup_7.jpg](/docs/images/AZ_OpenAI_setup_7.jpg)  


In your resource window, select **Go to Foundry portal** 

![AZ_OpenAI_setup_8.jpg](/docs/images/AZ_OpenAI_setup_8.jpg)


Select **View Deployments**. 

![AZ_OpenAI_setup_9.jpg](/docs/images/AZ_OpenAI_setup_9.jpg)

Select **Deploy a base model**

![AZ_OpenAI_setup_10.jpg](/docs/images/AZ_OpenAI_setup_10.jpg)


In search bar type a gpt model that you would like to deploy. Click on selected model, select **Deploy** and then select **Default settings**


![AZ_OpenAI_setup_11.jpg](/docs/images/AZ_OpenAI_setup_11.jpg)  


![AZ_OpenAI_setup_12.jpg](/docs/images/AZ_OpenAI_setup_12.jpg)  

Similar way, in search bar type a embedding model that you would like to deply. Click on selected model, select **Deploy** and then select **Default settings**

![AZ_OpenAI_setup_13.jpg](/docs/images/AZ_OpenAI_setup_13.jpg)  

Azure infrastructre setup is done


