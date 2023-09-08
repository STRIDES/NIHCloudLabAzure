# Azure OpenAI Fed Civ Workshop
 
Welcome to this repository, a comprehensive collection of examples that will help you chat with your data using the Azure OpenAI Playground, create highly efficient large language model prompts, and build Azure OpenAI embedding applications. This repository offers a wide range of examples that can be catered to your use cases, including:
- 2 documents for LLM interactions in the Azure OpenAI Playground. 
- 7 best practices for implementing prompt egineering in LLM applications.  
- 4 Python scripts that demonstrate how to use Azure OpenAI Embeddings to create embedding applications. 
- 42 in-depth content slides on the information covered in this workshop. Please find ```aoai_workshop_content.pdf``` in [search_documents](https://github.com/t-cjackson/Azure-OpenAI-Workshop/tree/main/search_documents) folder in this repository. 
  
The purpose of this workshop is to equip participants with the necessary skills to make the most out of the Azure OpenAI Playground, Prompt Engineering, and Azure OpenAI Embeddings in Python.

## Azure OpenAI Playground

Important steps: 

Ensure the following files are inside of a container, in the Azure storage account: 

- ```Hurricane_Irene_(2005).pdf``` 

 - ```New_York_State_Route_373.pdf```
  

If access needed to the files above, please visit the [search_documents](https://github.com/t-cjackson/Azure-OpenAI-Workshop/tree/main/search_documents) folder in this repository. 

Example queries to execute:

### ```Hurricane_Irene_(2005).pdf``` 

    1. What category hurricane was Irene?
    2. Which areas were impacted the most by hurricane Irene?
    3. Please explain the meteorological history of the hurricane.  


###  ```New_York_State_Route_373.pdf```
    1. What year was the New York State Route built?
    2. Describe the New York State Route. 
    3. Which company designed and built the New York State Route?


## Prompt Egineering Best Practices

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