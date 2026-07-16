# **Setting Up Azure Environment for Azure GenAI Cloud Lab**
****
##### **Skill Level: Beginner**
This guide will help you set up your Azure environment to complete the activities in the [GenAI](https://github.com/STRIDES/NIHCloudLabAzure/tree/main/notebooks/GenAI) directory of the NIH Cloud Lab. The purpose of this guide is to walk you through a deployment of the resources needed to carry out these activities.
### Prerequisites
*****
- An active Azure subscription
- ### Resources and Pricing
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
![Step1.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_1.jpg)
Click **Create** and then select **Azure OpenAI**
![Step2.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_2.jpg)
In a **Create Azure OpenAI window**, you should be able to see your Azure Subscription and click **Create new** for resource group
![Step3.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_3.jpg)

Select Region **East US 2**, create Name for your Azure OpenAI, select Pricing tier **Standard S0** and click **Next**
In Network window select **All networks, including the internet, can access this resource.** and click Next. In **Reviwe+submit** window click **create**

![Step4.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_4.jpg)
There should be a messsage that **Your deployment is complete** then select **Go to resource**
![Step5.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_5.jpg)
In your resource window, select **Go to Foundry portal** then click **Create a project**
![Step6.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_6.jpg)
Give a **Project name**, select **Region**, you should be able to see your **Subscription**, select **Resource group** and click **Create**

![Step7.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_7.jpg)
Select **View Deployments** or **Manage Deployments**. Select **Deploy a base model**
![Step8.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_8.jpg)
![Step9.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_9.jpg)
In search bar type a gpt model that you would like to deploy. Click on selected model and then select **Deploy**

![Step10.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_10.jpg)
![Step11.jpg](https://github.com/STRIDES/NIHCloudLabAzure/tree/upadhyayk2NIH-CIT-patch-2/docs/images/AZ_OpenAI_setup_11.jpg)
Similar way, in search bar type a embedding model that you would like to deply. Click on selected model and then select **Deploy**
Azure infrastructre setup is done
