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
### Azure OpenAI Setup Steps
****
1. Navigate to Azure OpenAI by searching at the top of the page. 
![AZ_OpenAI_setup_1.jpg](/docs/images/AZ_OpenAI_setup_1.jpg)  

2. Click **Create** and then select **Azure OpenAI**  

![AZ_OpenAI_setup_2.jpg](/docs/images/AZ_OpenAI_setup_2.jpg)  

3. In the **Create Azure OpenAI window:**
   - Select your Azure subscription
   - Click **Create new** for resource group  

![AZ_OpenAI_setup_3.jpg](/docs/images/AZ_OpenAI_setup_3.jpg)  

 - Select Region **East US 2**
 - Enter Name for your Azure OpenAI
 - Select Pricing tier **Standard S0**
 - Click **Next**
4. In the Network window:
  - Select **All networks, including the internet, can access this resource.**
  - Click Next.
5. In **Reviwe+submit** window:
  - Click **create**  

![AZ_OpenAI_setup_4.jpg](/docs/images/AZ_OpenAI_setup_4.jpg)  

6. When you see **Your deployment is complete** message:
   - Select **Go to resource**  

![AZ_OpenAI_setup_5.jpg](/docs/images/AZ_OpenAI_setup_5.jpg)  

7. In your resource window:
   - Select **Go to Foundry portal**
   - Click **Create a project**

![AZ_OpenAI_setup_6.jpg](/docs/images/AZ_OpenAI_setup_6.jpg)  

8.In the Create project window:
  - Give a **Project name**
  - Select **Region**
  - Select your **Subscription**
  - Select **Resource group**
  - Click **Create**  

![AZ_OpenAI_setup_7.jpg](/docs/images/AZ_OpenAI_setup_7.jpg)  

9. In the Deployments section:
    - Select **View Deployments** or **Manage Deployments**
    - Select **Deploy a base model**

![AZ_OpenAI_setup_8.jpg](/docs/images/AZ_OpenAI_setup_8.jpg)  

![AZ_OpenAI_setup_9.jpg](/docs/images/AZ_OpenAI_setup_9.jpg)  

10. Search for and deploy a GPT model:
    - Type a GPT model name in the search bar
    - Click on the selected model
    - Select **Deploy**

![AZ_OpenAI_setup_10.jpg](/docs/images/AZ_OpenAI_setup_10.jpg)  

![AZ_OpenAI_setup_11.jpg](/docs/images/AZ_OpenAI_setup_11.jpg)  

11. Deploy an embedding model:
    - Type an embedding model name in the search bar
    - Click on the selected model
    - Select **Deploy**

Azure infrastructre setup is complete.
