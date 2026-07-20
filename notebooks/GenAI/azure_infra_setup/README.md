---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.3
kernelspec:
  name: python3
  display_name: Python 3 (ipykernel)
  language: python
---

# **Setting Up Azure Environment for Azure GenAI Cloud Lab**
****

+++

##### **Skill Level: Beginner**

+++

This guide will help you set up your Azure environment to complete the activities in the [GenAI](https://github.com/STRIDES/NIHCloudLabAzure/tree/main/notebooks/GenAI) directory of the NIH Cloud Lab. The purpose of this guide is to walk you through a deployment of the resources needed to carry out these activities.

+++

### Prerequisites
*****

+++

- An active Azure subscription

+++

### Resources and Pricing
*****

+++

Provided is a list of resources that will be deployed along with the estimated cost breakdown for each resource. Please find the resources that will be deployed below.

+++

#### Resources deployed

+++

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

+++

#### Get Started
****

+++

### Azure OpenAI
****

+++

Navigate to Azure OpenAI. The easiest way is to search at the top of the page.

+++

![Step1.jpg](/images/Step1.jpg)

+++

Click **Create** and then select **Foundry (Recommended)**

+++

![Step2.jpg](/images/Step2.jpg)

+++

In a **Create a Foundry resource window**, you should be able to see your Azure Subscription and click **Create new** for resource group

+++

![Step3.jpg](/images/Step3.jpg)

+++

Select Region **East US 2**, create Name for your foundry resource, click **Review + create** and click **Create**

+++

![Step4.jpg](/images/Step4.jpg)

+++

You would see a message that **Deployment is in progress**

+++

There should be a messsage that **Your deployment is complete** then select **Go to resource**

+++

![Step5.jpg](/images/Step5.jpg)

+++

In your resource window, select **Go to Foundry portal** 

+++

![Step6.jpg](/images/Step6.jpg)

+++

![Step7.jpg](/images/Step7.jpg)

+++

Select **View Deployments**. 

```{code-cell} ipython3
Select **Deploy a base model**
```

![Step8.jpg](/images/Step8.jpg)

+++

![Step9.jpg](/images/Step9.jpg)

+++

In search bar type a gpt model that you would like to deploy. Click on selected model, select **Deploy** and then select **Default settings**

+++

![Step10.jpg](/images/Step10.jpg)

+++

![Step11.jpg](/images/Step11.jpg)

+++

Similar way, in search bar type a embedding model that you would like to deply. Click on selected model, select **Deploy** and then select **Default settings**

+++

Azure infrastructre setup is done

```{code-cell} ipython3

```
