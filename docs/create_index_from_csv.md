### Create an Azure search index from a csv file
:sparkles: Here we outline how to create an Azure search index from a CSV file summarizing funded award data exported from Reporter.nih.gov

### 1) Download input CSV
:ear: If you already have your csv ready, skip to section (2)

Download this public [csv file](https://www.kaggle.com/datasets/henryshan/2023-data-scientists-salary?resource=download) from kaggle to use as our input. 

  ![Kaggle-csv](/docs/images/kaggle-input.jpeg)

### 2) Import data into Azure blob storage
:ear: If you already added your data to blob storage skip to section (3)

On the home page, navigate to `Storage Accounts`.

  ![Nav Storage Account](/docs/images/2_storage_accounts.png)

[Create a new storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal) if needed. Place your storage account in US East region. 

Create a new container if needed, otherwise navigate to an existing container.

  ![Create new container](/docs/images/3_create_container.png)

Select `Upload` and then add your file by dropping or browsing. 

  ![Add your file](/docs/images/4_add_your_csv.png)

### 3) Index your CSV

Navigate to AI Search and [create a new search](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal).

  ![Create new search](/docs/images/5_create_new_db.png)

Click `Import data`.

  ![Import Data](/docs/images/6_import_data.png)

Now fill out all the necessary parameters. 
+ Data Source: Select `Azure Blob Storage`. New options will drop down.
+ Data source name: This can be anything, but go with something like `ds-salaries-data`.
+ Data to extract: Select `Content and metadata`.
+ Parsing mode: Select `Delimited text`. Check the `First Line Contains Header` box and leave `Delimiter Character` as `,`.
+ Connection string: Click `Choose an existing connection` and navigate to your storage account and container.
+ Managed identity authentication: Leave as default.
+ Container name: Should be populated when you connect via Connection String, but otherwise just enter your container name here.
+ Blob folder: *Optional*, if you have a folder within the container with the file(s) you want to index, enter that path here.
+ Description: *Optional*.
+ If you get errors when trying to go to the next screen, make sure you don't have trailing commas in your csv, and there are not spaces in the header names. If this happens, fix those errors, re-upload to blob storage, and then try again! 

  ![Connect to blog](/docs/images/import-data.jpeg)

Skip ahead to `Customize target index`. 
+ Give your index a name.
+ Make `Project_Number` your key.
+ Make sure the expected column names are present under fields. For the columns you expect to use, select `Retrievable` and `Searchable`. If you select all the columns you will just pay for indexing you are not using.

  ![Customize index](/docs/images/index-csv.jpeg)

Advance to `Create an indexer`, name your indexer, then click `Submit`. 

  ![Create indexer](/docs/images/create-indexer.jpeg)

Navigate to `Indexes` on the left panel and wait until your index shows as many documents as you have lines in your file. It will read 0 documents until it is finished indexing. The example 500 line csv takes about one minute.

And that is it! Now return to [the tutorial notebook to run queries against this csv using GPT-4]( /notebooks/GenAI/notebooks/AzureAIStudio_index_structured_with_console.ipynb).









  
