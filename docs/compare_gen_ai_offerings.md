## Comparison of Generative AI Offerings across Cloud Service Providers

This guide is meant to give a short overview of the interfaces, service offerings, and 'out of the box' models offered by each CSP. In most cases, fine-tuning the latest models is redundant and you will be better served by strategic prompt engineering, but, if you want to re-train/fine-tune models or create custom models, we have Cloud Lab tutorials to walk you through it and do not highlight those services here. Note that CSPs are listed alphabetically.

### Amazon Web Services
Amazon offers Gen AI services through Amazon Bedrock and the Sagemaker suite. Models can be accessed via API or deployed locally and used within your account.

Amazon offers: 
+ Access to Chat and Text Playground through Bedrock
+ Access to Sagemaker Jumpstart models (same as Bedrock Foundation Models)
+ Access to deployed models from within Sagemaker/Sagemaker Studio Notebooks

  ![AWS Bedrock](/docs/images/bedrock.png)

AWS Foundation models include: 
+ AI21 Labs Jurassic models (text)
+ Amazon Titan (embedding, text not yet available)
+ Anthropic (have to submit specific use case for approval)
+ Cohere models (text and embedding)
+ Meta Llama2 (text)
+ Stability AI (image)

  ![AWS models](/docs/images/sagemaker_models.png)
  
### Google Cloud
Google Cloud offers Generative AI services through Vertex AI.

Vertex contains the following services:
+ Generative AI Studio with Language, Vision and Speech
+ Model Garden with Foundation and Fine-tunable models
+ Ability to deploy models to an endpoint

  ![Google Cloud Studio](/docs/images/vertexai_text.png)

Google Cloud offers the following models:
+ 53 Foundation Models all of which can be deployed to an endpoint and accessed from notebook/application
+ 79 models with example notebooks
+ Six models available in Generative AI Studio: PaLM 2 for Text, Chirp for Speech, PaLM 2 for Chat, Codey for Code Generation, Codey for Code Chat, Imagen for Captioning.

  ![Vertexai models](/docs/images/vertexai_models.png)
  
### Microsoft Azure
Azure offers Gen AI services through the Azure OpenAI Service.

Azure OpenAI offers: 
+ A chat playground
+ A completions playground
+ Image generation with DALL E
+ API access to deployed models (could be from AzureML notebooks)

  ![azure openai screenshot](/docs/images/openaichatplayground.png)

Azure OpenAI allows for the deployment and use of the following models:
+ GPT-35 series chat models
+ text-embedding-ada-002 embedding model
+ GPT-4 series upon request

  ![azure models](/docs/images/azure_models.png)




