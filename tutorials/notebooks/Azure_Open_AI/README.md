# Azure OpenAI Tutorial
✨ The following tutorial was modified from this excellent [Microsoft workshop](https://github.com/t-cjackson/AOAI-FED-CIV-Workshop) developed by [Cameron Jackson](https://github.com/t-cjackson). ✨

Welcome to this repository, a comprehensive collection of examples that will help you chat with your data using the Azure OpenAI Playground, create highly efficient large language model prompts, and build Azure OpenAI embedding applications. This repository offers a wide range of examples that can be catered to your use cases, including:
- 2 documents for LLM interactions in the Azure OpenAI Playground. 
- 7 best practices for implementing prompt egineering in LLM applications.  
- 4 Python scripts that demonstrate how to use Azure OpenAI Embeddings to create embedding applications. 
- 42 in-depth content slides on the information covered in this workshop. Please find ```aoai_workshop_content.pdf``` in [search_documents](https://github.com/t-cjackson/Azure-OpenAI-Workshop/tree/main/search_documents) folder in this repository. 
  
The purpose of this workshop is to equip participants with the necessary skills to make the most out of the Azure OpenAI Playground, Prompt Engineering, and Azure OpenAI Embeddings in Python. You can view in-depth info on these topics in the [workshop slides](/tutorials/notebooks/Azure_Open_AI/search_documents/aoai_workshop_content.pdf).

## Overview of Page Contents
+ [Azure OpenAI Playground Prerequisites](#Azure-OpenAI-Playground-Prerequisites)
+ [Overview](#ov)
+ [Resource Groups](#rg)
+ [Command Line Tools](#cli)
+ [Azure Marketplace](#mark)
+ [Ingest and Store Data](#sto)
+ [Virtual Machines](#vm)
+ [Azure Functions](#vm)
+ [Disk Images](#disk)

## Azure OpenAI Playground Prerequisites

Navigate to Azure OpenAI. The easiest way is to search at the top of the page.

  ![search for azure openai](/docs/images/1_navigate_openai.png)

At the time of writing, Azure OpenAI is in Beta and only available to customers via an application form, if you click **Create** that is the message you will see. If you click **Create** and do not get this message, then feel free to create a new OpenAI Service. Otherwise, please email us at CloudLab@nih.gov and ask us to set this part up for you. Once you have an OpenAI Service provisioned, click to open it. 

  ![click to open azure open ai](/docs/images/2_select_openai_project.png)

Now click **Go to Azure OpenAI Studio** or **Explore** to be connected to the Azure OpenAI studio user interface. 

  ![connect to OpenAI UI](/docs/images/3_connect_open_ai.png)

Click **Chat**

  ![click chat image](/docs/images/4_click_chat.png)

Next, you need to deploy an OpenAI model.

## Deploy an OpenAI model

On the left navigation panel, click **Models**

  ![Click Models](/docs/images/10_click_models.png)

Select the (A) `gpt-35-turbo model`, click (B) **Deploy**. You can learn more about the available models by clicking (C) **Learn more about the different types of base models**.

  ![Deploy the model](/docs/images/11_deploy_model.png)

Name your deployment and then click **Create**.

  ![Name your Deployment](/docs/images/12_name_your_deployment.png)

Now if you select `Deployments` on the left panel, you should see your deployed model listed. 

  ![Check Deployments](/docs/images/13_check_deployments.png)

Run a quick test to ensure our deployment is acting as expected. Navigate to `Chat`, add an optional system message (we will cover this more later), and then type `Hello World` in the chat box. If you get a response, things are working well!

  ![test model](/docs/images/14_test_your_model.png)

Now we will look at [adding and querying over your own data](own-data) and then review [prompt engineering best practices](prompt engineering) using a general GPT model.

## Chat Playground Navigation

If you have not already (A) Navigate to the Chat Playground. Here we will walk through the various options available to you. First, you can specify a `System Message` which tells the model what context with which to respond to inquiries. To modify this, (B) select `System message`, then (B) input a [System Message](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/system-message#define-the-models-profile-capabilities-and-limitations-for-your-scenario) in the prompt box, then (D) click **Save**. 

On the next tab over, you can (A) add your own data, which we dive into in the [next section](own-data). In the middle of the page is where you actually interact with the model (B) through the chat prompts. Always (C) clear the chat after each session. 

  ![add your own data](/data/images/18_add_custom_data.png)

On the far right, you can modify which model you are deploying, which allows you to switch between different model deployments depending on the context. 

  ![modify deployment](/data/images/19_deployment.png)

Finally, you can select the `parameters` tab to modify the model parameters. Review [this presentation](/tutorials/notebooks/Azure_Open_AI/search_documents/aoai_workshop_content.pdf) to learn more about the parameters.

  ![modify parameters](/docs/images/20_parameters.png)

## Upload your own data and query over it (#own-data)

For an in-depth overview of adding your own data, check out this [Microsoft documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/use-your-data-quickstart?tabs=command-line&pivots=programming-language-studio). We give a quick start version here. 

Now, if you want to add your own data and query it, keep going here. If you want to jump ahead to prompt engineering with the general GPT model, jump down to [Prompt Engineering Best Practices](prompt_engineering).

Within this repo there is a directory called `search_documents`. This directory contains a few PDFs that we will upload and query over related to [Immune Response to Mpox in Woman Living with HIV](https://www.niaid.nih.gov/news-events/immune-response-mpox) and the [DCEG Diesel Exhaust in Minors Study](https://dceg.cancer.gov/news-events/news/2023/dems-ii).

We are going to upload these PDFs to an Azure Storage Account and then add them to our Azure OpenAI workspace. 

Follow [this guide](/docs/create_storage_account.md) to create and upload to a storage account. Use a separate browswer window so that you can easily get back to Azure OpenAI.

Once you have uploaded your PDFs, navigate back to the `Chat` section of Azure OpenAI and click **Add a data source**.

  ![Add data source image](/docs/images/5_add_data_source.png)

Select `Azure Blob Storage`, and then the correct `Storage Account` and `Container`. If this is your first time indexing documents, for `Select Azure Cognitive Search resource` click **Create a new Azure Cognitive Search resource** which will open a new window. 

  ![select data source](/docs/images/6_point_to_data.png)

If needed, create the new Azure Cognitive Search resource. Make sure you delete this when you are finished with Azure OpenAI because it will accrue charges over time. 

  ![create cog search](/docs/images/7_cog_search_resource.png)

Now select your newly made Azure Cognitive Search resource, and click **Next**. On the Data Management Page, choose **Keyword**, then click **Next**.

  ![choose keyword](/docs/images/choose_keyword.png)

On the last page, click **Save and close**. It will now take a few minutes to index your updated data.

  ![Save and close](/docs/images/9_review_and_close.png)

Once it is complete, you should see your data source listed. Note that you can select the box that says `Limit responses to your data content` depending on if you want to limit to your data or query your data plus the general model. 

Also check that the index is complete by viewing your Cognitive Search resource, and going to `Indexes`. Ensure that the number of documents listed > 0. 

  ![Cog Search](/docs/images/15_check_index.png)

Now let's run some example queries of our custom data set. Feel free to modify and experiment. After reading the prompt engineering section below, return to this section and see how you can improve these examples. If you get errors after adding your data, try to refresh the page, and if all else fails, send us an email at CloudLab@nih.gov.

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

## Prompt Engineering Best Practices (#prompt_engineering)

### Write Clear Instructions 
1. Alter the system message to reply with a document that includes a playful comment or joke in each paragraph when responding to inquiries concerning writing assistance. This format should only be used for writing-related questions.
   ```
        SYSTEM: 
        
        You are a comedian English professor at the University of Giggles.  When I ask for help to write something, you will reply with a document that contains at least one joke or playful comment.

        QUERY:

         Write a thank you note to my steel bolt vendor for getting a delivery in on time with short notice. This made it possible for my company to deliver an important order. 
    ```
    Note: Add the following to the SYSTEM message, directing the LLM to only answer questions that involve writing assistance:
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

            You will be given a paragraph delimited by XML tags. Use the following step-by-step sequence to respond to user inputs.

            Step 1) The user will provide you with a paragraph delimited by XML tags. Summarize the paragraph in one sentence with a prefix “Summary:” 
            Step 2) Translate the summary from Step 1 into Spanish, with a prefix “Translation:”

            QUERY:

            <paragraph> Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are designed to perform tasks that normally require human intelligence, such as learning, problem-solving, and decision-making. AI technology uses algorithms and statistical models to analyze data and make predictions and can be applied to a wide range of fields, including healthcare, finance, and transportation. AI is a rapidly growing field that has the potential to revolutionize many industries by increasing efficiency and productivity. However, as with any technology, there are also concerns about the ethical implications of AI, such as job displacement and privacy concerns. </paragraph>

    Note: When implementing the above example, you might encounter a problem in Step 2 of the prompt where the model translates the entire paragraph instead of the single sentence summary. This issue is likely to arise when using the gpt-35-turbo model, primarily due to its limitations in reasoning capabilities, which impact its translation proficiency. A solution to this minor glitch is the gpt-4 model, which is designed to reason more effectively than the gpt-35-turbo model.

1. Revise the model to classify the text it is given as either positive, neutral or negative. Once classified, have the LLM recognize the adjective it used to classify the text. Provide an example to the assitant for the LLM to comprehend tasks. 
   
         SYSTEM: Classify the text as either positive, neutral, or negative. Then find the adjective that allows you to classify the text. Follow the example to respond.

         USER: The movie was awesome!

         ASSISTANT: Positive. The adjective here is: awesome.

         USER: The movie was terrible.

         ASSISTANT: Negative. The adjective here is: terrible.

         USER: The movie was ok.

         ASSISTANT: Neutral. The adjective here is: ok.

         QUERY: I can’t wait to go to the beach.

### Providing Reference Text

4. Revise the system message to create four bullet points outlining the key principles of the provided text delimited by triple quotes.
To accomplish this, the following steps should be taken:
   1.	Identify the text to be analyzed, which should be delimited by triple quotes.
   2.	Analyze the text to determine the key principles.
   3.	Generate four bullet points that succinctly summarize each principle.
   4.	Display the bullet points in the system message.

            SYSTEM: 
            
            You will be given text delimited by triple quotes. Create 4 bullet points on the key principles of the text. Answer in the following format:
            -	Key principle 1
            -	Key principle 2
            -	Key principle 3
            -	Key principle 4

            QUERY: 

            “””
            Learning a new language is an excellent way to broaden your horizons and improve your cognitive abilities. Firstly, being multilingual can open new opportunities both personally and professionally, such as traveling to new countries, connecting with people from different cultures, and expanding your job prospects. Secondly, it has been shown that learning a new language can improve cognitive function, such as memory, problem-solving, and decision-making skills. Additionally, it can increase empathy and cultural understanding, as well as enhance creativity and communication skills. Finally, it can boost confidence and self-esteem, as mastering a new language is a significant achievement and can provide a sense of accomplishment. Overall, the benefits of learning a new language are numerous and can have a positive impact on many aspects of your life. 
            “””

### Split complex tasks into simpler subtasks
5. Give the system message primary and secondary categories for classifying customer service inquiries. The system should:
   - take in customer service queries
   - classify the query into primary and secondary categories
   - output the response in JSON format with the following keys: primary and secondary 

            SYSTEM: 

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

            QUERY: 
            
            I need to get my internet working again.

(5) Continued: Based on the classification of the customer query from above, provide a set of more specific set of instructions to the system message for troubleshooting in a technical support context. 

      SYSTEM:

      You will be provided with customer service inquiries that require troubleshooting in a technical support context. Help the user by:
      -	Check all router cables are connected properly. If not, reconnect them as needed.
      -	Ask the customer which router model they are using.
      -	For MTD-327J model, instruct the customer to hold the red button for 5 seconds and wait 5 minutes before testing the connection.
      -	For MTD-327S model, advise the customer to unplug and replug the device and wait for 5 minutes before testing the connection.
      -	If the issue persists, output {"IT support requested"} to connect them to IT support.
      -	If the customer's questions are unrelated to troubleshooting, ask if they would like to end the chat and classify their request accordingly.

      <insert primary/secondary classification scheme from above here>

      QUERY: 
      
      I need to get my internet working again. 

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

## Azure OpenAI Embeddings

### Installation
 
To run the Python scripts in this repository, you will need to first create a virtual environment in your workspace. Next you must have the necessary packages installed. You can complete both tasks via the following commands:

To create a virtual environment in your workspace:


1. Open the command palette: ```CTRL + SHIFT + P```
2. Search: ```Python: Create Environment```
3. Select: ```Venv```
4. Select the latest version of Python installed on your device.
5. .venv environment created  

To install the necessary packages:

```bash
pip install -r requirements.txt  
 ```

Make sure you have Python and pip installed on your machine.

### Dataset
 
A pre-chunked .csv file ```microsoft-earnings.csv``` is provided in this repository. This file will be used for embedding and search operations in the provided scripts. However, you're free to use any other .csv files of your choice.

### Usage
 
This repository contains four Python scripts: ``` workshop_embedding.py```, ```workshop_search.py```, ``` aoai_embeddings.py```, and ```acs_embeddings.py```.

To run any of these scripts, navigate to the repository root and execute one of the following commands:
```bash
python workshop_embedding.py  
python workshop_search.py  
cd embedding_demos -> streamlit run aoai_embeddings.py
cd embedding_demos -> streamlit run acs_embeddings.py
 ```

### workshop_embedding.py
 
This script demonstrates how to calculate word embeddings using Azure OpenAI.

### workshop_search.py
 
This script demonstrates how to perform a search using Azure OpenAI embeddings.

### aoai_embeddings.py
 
Located in the embeddings_demo subfolder, this script provides a complete web app demonstration of the Azure OpenAI Embeddings functionality using Streamlit. It offers an interactive GUI where users can choose to execute the functionality demonstrated in the other two scripts. It creates embeddings from a given data file and allows for search queries within the created embeddings.

Note: You should adjust the file path in lines 42, 47, and 70 in aoai_embeddings.py to fit your specific file path.

### acs_embeddings.py

Located in the embeddings_demo subfolder, this script provides a complete web app demonstration of the Azure OpenAI Embeddings functionality along with Azure Cognitive Search using Streamlit. It creates embeddings from relevant documents found in your Azure Cognitive Search index. Documents in your index only related to the query asked will be embedded and stored. The vector storage only saves embedded documents for the duration of the program's execution. Must use Azure Cognitive Search Query API Key in .env file. 

### Configuration
 
To use Azure OpenAI, you need to configure the necessary environment variables. Create a .env file in the repository root directory and set the following variables:
```dotenv
AZURE_OPENAI_VERSION = your_version  
AZURE_OPENAI_ENDPOINT = your_endpoint  
AZURE_OPENAI_KEY = your_api_key 
AZURE_COGNITIVE_SEARCH_SERVICE_NAME = your_cognitive_search_service_name 
AZURE_COGNITIVE_SEARCH_INDEX_NAME = your_cognitive_search_index_name 
AZURE_COGNITIVE_SEARCH_API_KEY = your_cognitive_search_api_query_key
```

Replace your_version, your_endpoint, and your_api_key with your actual values.

## Extra Resources 

### Azure OpenAI PLayground

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
