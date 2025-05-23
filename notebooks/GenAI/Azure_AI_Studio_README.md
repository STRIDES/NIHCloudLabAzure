# Azure AI Studio Studio
Microsoft Azure migrated the AI front end from Azure OpenAI to Azure AI Studio.

✨ The following tutorial was modified from this excellent [Microsoft workshop](https://github.com/t-cjackson/AOAI-FED-CIV-Workshop) developed by [Cameron Jackson](https://github.com/t-cjackson). ✨

Welcome to this repository, a comprehensive collection of examples that will help you chat with your data using the Azure OpenAI Studio Playground, create highly efficient large language model prompts, and build Azure OpenAI embeddings. 
  
The purpose of this workshop is to equip participants with the necessary skills to make the most out of the Azure OpenAI Playground, Prompt Engineering, and Azure OpenAI Embeddings in Python. You can view in-depth info on these topics in the [workshop slides](/notebooks/GenAI/search_documents/aoai_workshop_content.pdf).

You can also learn a lot about the details of using Azure AI at this [site](https://azure.microsoft.com/en-us/products/ai-studio).

We recommend you 1) go through the steps in this README, 2) complete the general notebook called `notebooks/AzureOpenAI_embeddings.ipynb`, then 3) explore the other notebooks at [this directory](/notebooks/GenAI/notebooks) 

## Overview of Page Contents
+ [Azure AI Playground Prerequisites](#Azure-OpenAI-Playground-Prerequisites)
+ [Chat Playground Navigation](#Chat-Playground-Navigation)
+ [Upload your own data and query over it](#Upload-your-own-data-and-query-over-it)
+ [Prompt Engineering Best Practices](#Prompt-Engineering-Best-Practices)
+ [Azure OpenAI Embeddings](#Azure-OpenAI-Embeddings)
+ [Additional Resources](#Additional-Resources)

## Azure OpenAI Playground Prerequisites

Navigate to Azure AI Studio. The easiest way is to search at the top of the page.

  ![search for azure openai](/docs/images/1_azure_ai_studio.png)

Click new Azure AI. 

  ![click to open azure open ai](/docs/images/2_click_new_azureai.png)

Fill out the necessary information. Create a new Resource Group if needed. Click **Review and Create**.

  ![fill in the info](/docs/images/3_fill_form_azureai.png)

Once the resource deploys, click **go to resource**.

  ![go to resource](/docs/images/4_go_to_resource.png)

Now click **Go to Azure AI Studio**. You can also view your access keys at the bottom of the page.

  ![connect to OpenAI UI](/docs/images/5_launch_ai_studio.png)

Before diving into the UI, stop and watch [this 14 minute overview video](https://www.youtube.com/watch?v=Qes7p5w8Tz8) to learn how to take full advantage of the Studio. We won't cover every option in this tutorial, but feel free to explore! 

When ready, go to **Build** and then click **+ New Project**.

  ![select new project](/docs/images/6_select_new_project.png)

Fill in the info with the resource name and relevant information. Make sure you put your resource in the same resource group and region as your other Azure AI resources/environments. Then click **Create a Project**.

  ![create new project and resource](/docs/images/7_create_new_project.png)

When ready, select your project. Now go to **Build** then **Playground**. 

Next, you need to deploy model to power your chat bot.

## Deploy a model

On the left navigation panel, click **Deployments**, then click **Create** on the next screen. 

  ![Click Models](/docs/images/8_create_model.png)

Select your model of choice. Here we select gpt-4.

  ![select your model](/docs/images/9_select_model.png)

Name your deployment and then click **Deploy**.

  ![deploy your model](/docs/images/10_name_and_deploy.png)

Now under Deployments you should see your model. Feel free to deploy other models here, but be aware that you will pay for those deployed models. 

  ![model is deployed](/docs/images/11_model_is_deployed.png)

Run a quick test to ensure our deployment is acting as expected. Navigate to `Playground`, add an optional system message (we will cover this more later), and then type `Hello World` in the chat box. If you get a response, things are working well! Double check that on the far right it shows the correct deployment.

  ![test model](/docs/images/12_test_hello_world.png)

Now we will look at [adding and querying over your own data](#Upload-your-own-data-and-query-over-it) and then review [prompt engineering best practices](#prompt-engineering-best-practices) using a general GPT model.

## Chat Playground Navigation

If you have not already (A) Navigate to the Chat Playground. Here we will walk through the various options available to you. First, you can specify a `System Message` which tells the model what context with which to respond to inquiries. To modify this, (B) select `System message`, then (B) input a [System Message](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/system-message) in the prompt box, then (D) click **Apply Changes**. 

On the next tab over, you can (A) add your own data, which we dive into in the [next section](#Upload-your-own-data-and-query-over-it). In the middle of the page is where you actually interact with the model (B) through the chat prompts. Always (C) clear the chat after each session. 

On the far right under *Configuration*, you can modify which model you are deploying, which allows you to switch between different model deployments depending on the context. You can also modify the model's parameters on the same tab.

  ![modify deployment](/docs/images/19_deployment.png)

Finally, you can select the `parameters` tab to modify the model parameters. Review [this presentation](/notebooks/GenAI/search_documents/aoai_workshop_content.pdf) to learn more about the parameters.

  ![modify parameters](/docs/images/20_parameters.png)

Finally, click on **Prompt Samples** along the top and explore a few of these example prompts. 

  ![modify parameters](/docs/images/13_prompt_examples.png)


## Upload your own data and query over it

For an in-depth overview of adding your own data, check out this [Microsoft documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/use-your-data-quickstart?tabs=command-line&pivots=programming-language-studio). We give a quick start version here. 

Now, if you want to add your own data and query it, keep going here. If you want to jump ahead to prompt engineering with LLMs, jump down to [Prompt Engineering Best Practices](#prompt-engineering-best-practices).

Within this repo there is a directory called `search_documents`. This directory contains a few PDFs that we will upload and query over related to [Immune Response to Mpox in a Woman Living with HIV](https://www.niaid.nih.gov/news-events/immune-response-mpox) and the [DCEG Diesel Exhaust in Minors Study](https://dceg.cancer.gov/news-events/news/2023/dems-ii).

We are going to upload these PDFs to an Azure Storage Account and then add them to our Azure OpenAI workspace. Note that there are [upload limits](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits#quotas-and-limits-reference) on the number and size of documents you can query within Azure OpenAI, but sure to read these before getting started. For example, you can only query over a max of 30 documents and/or 1 GB of data. You can only upload the datatypes [listed below] [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data#data-formats-and-file-types), and will have the best results with markdown files.

+ `.txt`
+ `.md`
+ `.html`
+ Microsoft Word files
+ Microsoft PowerPoint files
+ PDF

Follow [this guide](/docs/create_storage_account.md) to create and upload to a storage account. Use a separate browswer window so that you can easily get back to Azure OpenAI.

Once you have uploaded your PDFs (or other datatypes if you are trying that), navigate back to the `Playground`, select `Add your data` then click **Add a data source**.

  ![Add data source image](/docs/images/14_add_your_data.png)

Select `Azure Blob Storage`, and then the correct `Storage Account` and `Container`. If this is your first time indexing documents, for `Select Azure AI Search resource` click **Create a new AI Search resource** which will open a new window. You can add vector search to your AI Search resource, but you will need to first deploy the embedding model for it to be available.

  ![select data source](/docs/images/15_point_to_data.png)

If needed, create the new Azure AI Search resource. Make sure you delete this when you are finished with Azure AI because it will accrue charges over time.

  ![create cog search](/docs/images/7_cog_search_resource.png)
 
Now select your newly made Azure AI Search (formally know as Cognitive Search) resource, and click **Next**. You can select to search with either [Vector](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) or [Hybrid](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview) search.

  ![choose keyword](/docs/images/16_hybrid_search.png)

On the last page, click **Save and close**. It will now take a few minutes to index your updated data. Read more [here](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) about how Azure AI Search is working behind the scenes. 

  ![Save and close](/docs/images/17_save_and_close.png)

Once it is complete, you should see your data source listed. 

Also check that the index is complete by viewing your AI Search resource, and going to `AI Search` on the left. 
  
  ![Cog Search](/docs/images/18_check_ai_search.png)

Now select your resource, select **indexes**, and then ensure that the number of documents listed is greater then 0. 

  ![Cog Search](/docs/images/15_check_index.png)

Now let's got back to the Playground and run some example queries of our custom data set. Feel free to modify and experiment. After reading the prompt engineering section below, return to this section and see how you can improve these examples. If you get errors after adding your data, try to refresh the page, and if all else fails, send us an email at CloudLab@nih.gov.

```
Summarize each of the documents I uploaded in a single paragraph, listing the title, the authors, followed by a five sentence summary for each. Give a new line after each summary.
```
```
What were some of the phenotypic presentations of MPOX on patients with HIV?
```
```
Are the phenotypic effects of MPOX the same for a patient with HIV and other patients?
```
```
Describe the primary findings of the Diesel Exhaust in Miners Study?
```
```
Does exposure to Diesel exhaust increase your risk for lung cancer? What about other cancers?  Keep your response to one sentence for each of these queries.    
```

  ![search custom data files](/docs/images/16_search_custom_data.png)

### Bonus, try uploading the grant data in the search_documents and run a few queries
Follow the instructions above for the two files in search_documents called `grant_data_sub1.txt` and `grant_data_sub2.txt`. These data were produced by searching [NIH Reporter](https://reporter.nih.gov/) for NCI-funded projects from fiscal year 2022-2024. The data were downloaded as a csv, converted to txt using Excel, then split in half using a very simple `head -2500 data.txt > grant_data_sub1.txt` and `tail -2499 data.txt > grant_data_sub2.txt`. The reason we split the data is that Azure has an upload limit of 16 MB and the downloaded file was over 30MB. If you are downloading your own data be mindful of these limits and split your files as necessary. 

Once the data is uploaded, try adding a system message like the following: 
```
Pretend to be a Program Officer at the National Institutes of Health in the National Cancer Institute. Your job is to review and summarize funded opportunities. Respond in a professional manner.
```
Now try some prompts like these:

```
What funding years are included in the data I provided?
```
```
Based on the Project Abstract, Project Title, and public health relevance please list the Project number of all projects related to women's health research and provide an summary of the women's health relevance for each.
```
```
Based on the Project Abstracts, what were the most commonly funded research areas in Fiscal Year 2022?
```

## Prompt Engineering Best Practices
First, review [this summary of prompt engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering) from Microsoft.

### Write Clear Instructions 

1. Alter the system message to reply with a document that includes a playful comment or joke in each paragraph when responding to inquiries concerning writing assistance. This format should only be used for writing-related questions

Add the following in the System Message box (SYSTEM:) 
```
You are a comedian English professor at the University of Giggles.  When I ask for help to write something, you will reply with a document that contains at least one joke or playful comment.
```
Add this query to the chat prompt box (QUERY:).
```
Write a thank you note to my steel bolt vendor for getting a delivery in on time with short notice. This made it possible for my company to deliver an important order.
```
Add the following to the system message, directing the LLM to only answer questions that involve writing assistance and then rerun the original query.
```
If the user query does not have "write" in it, respond I do not know truthfully. 
```
2. Modify the system message by adding the prefix "Summary:" which should summarize the paragraph given, delimited with XML tags. Following the summary, the system should translate the paragraph from English to Spanish and add the prefix "Translation:".
To accomplish these tasks, the following steps should be taken:
   1. Identify the paragraph to be summarized, which should be delimited by XML tags.
    2.	Generate a summary of the paragraph.
    3.	Add the prefix "Summary:" to the beginning of the summary.
    4.	Translate the paragraph from English to Spanish.
    5.	Add the prefix "Translation:" to the beginning of the translated paragraph.

SYSTEM: 
```
You will be given a paragraph delimited by XML tags. Use the following step-by-step sequence to respond to user inputs.

            Step 1) The user will provide you with a paragraph delimited by XML tags. Summarize the paragraph in one sentence with a prefix “Summary:” 
            Step 2) Translate the summary from Step 1 into Spanish, with a prefix “Translation:”
```
QUERY: 
```
<paragraph> Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are designed to perform tasks that normally require human intelligence, such as learning, problem-solving, and decision-making. AI technology uses algorithms and statistical models to analyze data and make predictions and can be applied to a wide range of fields, including healthcare, finance, and transportation. AI is a rapidly growing field that has the potential to revolutionize many industries by increasing efficiency and productivity. However, as with any technology, there are also concerns about the ethical implications of AI, such as job displacement and privacy concerns. </paragraph>
```

Note: When implementing the above example, you might encounter a problem in Step 2 of the prompt where the model translates the entire paragraph instead of the single sentence summary. This issue is likely to arise when using the gpt-35-turbo model, primarily due to its limitations in reasoning capabilities, which impact its translation proficiency. A solution to this minor glitch is the gpt-4 model, which is designed to reason more effectively than the gpt-35-turbo model.

1. Revise the model to classify the text it is given as either positive, neutral or negative. Once classified, have the LLM recognize the adjective it used to classify the text. Provide an example to the assitant for the LLM to comprehend tasks. 

SYSTEM
```
Classify the text as either positive, neutral, or negative. Then find the adjective that allows you to classify the text. Follow the example to respond.

         USER: The movie was awesome!

         ASSISTANT: Positive. The adjective here is: awesome.

         USER: The movie was terrible.

         ASSISTANT: Negative. The adjective here is: terrible.

         USER: The movie was ok.

         ASSISTANT: Neutral. The adjective here is: ok.

         QUERY: I can’t wait to go to the beach.
```

### Providing Reference Text

4. Revise the system message to create four bullet points outlining the key principles of the provided text delimited by triple quotes.
To accomplish this, the following steps should be taken:
   1.	Identify the text to be analyzed, which should be delimited by triple quotes.
   2.	Analyze the text to determine the key principles.
   3.	Generate four bullet points that succinctly summarize each principle.
   4.	Display the bullet points in the system message.

SYSTEM: 
```
You will be given text delimited by triple quotes. Create 4 bullet points on the key principles of the text. Answer in the following format:
            -	Key principle 1
            -	Key principle 2
            -	Key principle 3
            -	Key principle 4
```
QUERY: 
```
            “””
            Learning a new language is an excellent way to broaden your horizons and improve your cognitive abilities. Firstly, being multilingual can open new opportunities both personally and professionally, such as traveling to new countries, connecting with people from different cultures, and expanding your job prospects. Secondly, it has been shown that learning a new language can improve cognitive function, such as memory, problem-solving, and decision-making skills. Additionally, it can increase empathy and cultural understanding, as well as enhance creativity and communication skills. Finally, it can boost confidence and self-esteem, as mastering a new language is a significant achievement and can provide a sense of accomplishment. Overall, the benefits of learning a new language are numerous and can have a positive impact on many aspects of your life. 
            “””
```
### Split complex tasks into simpler subtasks

5. Give the system message primary and secondary categories for classifying customer service inquiries. The system should:
   - take in customer service queries
   - classify the query into primary and secondary categories
   - output the response in JSON format with the following keys: primary and secondary 

SYSTEM: 
```
You will be provided with customer services queries. Classify each query into a primary category and a secondary category. Provide your output in JSON format with the keys: primary and secondary
            Primary categories: Billing, Technical Support, Account Management, or General Inquiry 
            Billing secondary categories:
            -	Unsubscribe or upgrade 
            -	Add a payment method 
            -	Explanation for charge 
            -	Dispute a charge 
            Technical Support secondary categories:
            -	Troubleshooting 
            -	Device compatibility 
            -	Software updates 
            Account Management secondary categories:
            -	Password reset 
            -	Update personal information 
            -	Close account 
            -	Account security 
            General Inquiry secondary categories: 
            -	Product information 
            -	Pricing 
            -	Feedback 
            -	Speak to a human
```
QUERY: 
```
I need to get my internet working again.
```
(5) Continued: Based on the classification of the customer query from above, provide a set of more specific set of instructions to the system message for troubleshooting in a technical support context. 

SYSTEM:

```
You will be provided with customer service inquiries that require troubleshooting in a technical support context. Help the user by:
      -	Check all router cables are connected properly. If not, reconnect them as needed.
      -	Ask the customer which router model they are using.
      -	For MTD-327J model, instruct the customer to hold the red button for 5 seconds and wait 5 minutes before testing the connection.
      -	For MTD-327S model, advise the customer to unplug and replug the device and wait for 5 minutes before testing the connection.
      -	If the issue persists, output {"IT support requested"} to connect them to IT support.
      -	If the customer's questions are unrelated to troubleshooting, ask if they would like to end the chat and classify their request accordingly.

      <insert primary/secondary classification scheme from above here>
```
QUERY:     
```
I need to get my internet working again. 
```

### Give GPTs time to "think"

6. Modify the system message to determine if the student’s solution is correct or not. The model should work out its own solution before comparing it to the student’s solution. Following an in-depth comparison, a decision on whether the answer is correct or not should be made. Add the following example so the model knows how to solve the problem correctly:

SYSTEM: 

         First work out your own solution to the problem. Then compare your solution to the student's solution and evaluate if the student's solution is correct or not. Don't decide if the student's solution is correct until you have done the problem yourself.

         USER: 

         Problem Statement: I'm building a solar power installation and I need help working out the financials.  
         - Land costs $100 / square foot  
         - I can buy solar panels for $250 / square foot  
         - I negotiated a contract for maintenance that will cost me a flat $100k per year, and an additional $10 / square foot  
         What is the total cost for the first year of operations as a function of the number of square feet.  

         ASSISTANT: 

         Let x be the size of the installation in square feet.
         1. Land cost: 100x
         2. Solar panel cost: 250x
         3. Maintenance cost: 100,000 + 10x
         Total cost: 100x + 250x + 100,000 + 10x = 360x + 100,000

QUERY: 

         Problem Statement: I'm building a solar power installation and I need help working out the financials. 
         - Land costs $100 / square foot 
         - I can buy solar panels for $250 / square foot 
         - I negotiated a contract for maintenance that will cost me a flat $100k per year, and an additional $10 / square foot 
         What is the total cost for the first year of operations as a function of the number of square feet.
         Student's Solution: Let x be the size of the installation in square feet. 
         1. Land cost: 100x 
         2. Solar panel cost: 250x 
         3. Maintenance cost: 100,000 + 100x 
         Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000

### Test changes systematically

7. Modify the system to detect whether the text it was given contains the following pieces of information it has directly. The text should be delimited by triple quotes. Here are the pieces of information to look for:
    -	Neil Armstrong was the first person to walk on the moon. 
    -	The date Neil Armstrong walked on the moon was July 21, 1969. 

SYSTEM: 
            
            You will be provided with text delimited by triple quotes that is supposed to be the answer to a question. Check if the following pieces of information are directly contained in the answer:

            - Neil Armstrong was the first person to walk on the moon.
            - The date Neil Armstrong first walked on the moon was July 21, 1969.
  
            For each of these points perform the following steps but do not display the step number:

            Step 1 - Restate the point.
            Step 2 - Provide a citation from the answer which is closest to this point.
            Step 3 - Consider if someone reading the citation who doesn't know the topic could directly infer the point. Explain why or why not before making up your mind.
            Step 4 - Write "yes" if the answer to 3 was yes, otherwise write "no".
            Finally, provide a count of how many "yes" answers there are. Provide this count as {"count": <insert count here>}.

QUERY: 
            
            """Neil Armstrong is famous for being the first human to set foot on the Moon. This historic event took place on July 21, 1969, during the Apollo 11 mission."""

## Azure OpenAI API and Embeddings

### Background
Creating embeddings of search documents allows you to use vector search, which is much more powerful than basic keyword search. First, review this page on [how to create embeddings](https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-generate-embeddings), and then review [how vector search works](https://learn.microsoft.com/en-us/azure/search/vector-search-overview).

### Environment Setup
Navigate to your [Azure Machine Learning Studio environment](https://azure.microsoft.com/en-us/products/machine-learning). If you have not created your environment, [create one now](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-cloud-workstation?view=azureml-api-2). 

Navigate to `Notebooks`, then clone this Git repo into your environment and navigate to the notebook called [AzureOpenAI_embeddings.ipynb](/notebooks/GenAI/notebooks/AzureOpenAI_embeddings.ipynb). 

You will need a variety of parameters to authenticate with the API. You can find these within the Playground by clicking **View Code**. Input these parameters into the notebook cell when asked.

  ![Code View Image](/docs/images/find_endpointv2.png)

Follow along with the notebook, and when finished, feel free to explore the other notebooks which use more advanced tools like Azure AI Search and LangChain.

Finally, navigate back here to view the Additional Resources. Make sure to **Stop your Compute** when finished in Azure ML Studio.

## Additional Resources 

### Azure OpenAI PLayground

*These resources are for the older Azure OpenAI, but not all the docs have been updated to Azure AI Studio. While the front end has changed, the underlying services largely have not, so these docs should still serve you well.*

[Azure OpenAI Service models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)

[Adding data to Azure OpenAI Playground](https://learn.microsoft.com/en-us/azure/ai-services/openai/use-your-data-quickstart?tabs=command-line&pivots=programming-language-studio)

[Azure OpenAI Chat API](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#chat-completions)


### Basics of Prompt Egineering

[Prompting Techniques](https://www.promptingguide.ai/techniques)

[Prompting Best Practices](https://platform.openai.com/docs/guides/gpt-best-practices)

### Azure OpenAI Embeddings 

[Getting Started with Embeddings](https://learn.microsoft.com/en-us/azure/ai-services/openai/tutorials/embeddings?tabs=command-line)

[OpenAI Cookbook GitHub Repository](https://github.com/openai/openai-cookbook)

## License

This repository is licensed under the MIT License. See the [LICENSE](https://github.com/t-cjackson/Azure-OpenAI-Workshop/blob/main/LICENSE) file for more information.
