### Create an Azure search index from a csv file
:sparkles: Here we outline how to create an Azure search index from a CSV file summarizing funded award data exported from Reporter.nih.gov

### 1) Generate input CSV
:ear: If you already have your csv ready, skip to section (2)

Our input data comes from the csv export option for [Reporter.nih.gov](https://reporter.nih.gov/). Navigate to reporter.nih.gov and select `Advanced Search`. Input your search parameters. In this case we filtered for awards made by NIGMS in FY 23. In the top right, select `Export`.

Select your export columns and make sure you export as a csv. In the example input data file we only selected 'Title', 'Project_ID', and 'Total_Cost', although a few other columns were also exported.

  ![Export from Reporter](/docs/images/1_export_reporter_csv.png)

If using the UI to upload, you need to make two small edits to the csv that gets exported. First, remove the extra comma at the end of each line. Second, replace the spaces in column names in the header row. You can do this using something like Python, or just do a find/replace in a text editor.

### 2) Import data into Azure blob storage
:ear: If you already added your data to blob storage skip to to section (3)

On the home page, navigate to `Storage Accounts`.

  ![Nav Storage Account](/docs/images/2_storage_accounts.png)

[Create a new storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal) if needed. Place your storage account in useast region. 

Create a new container if needed, otherwise navigate to an existing container.

  ![Create new container](/docs/images/3_create_container.png)

Select `Upload` and then add your file by dropping or browsing. 

  ![Add your file](/docs/images/4_add_your_csv.png)

### 3) Index your CSV

Navigate to AI Search and [create a new search](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal).

  ![Create new search](/docs/images/5_create_new_db.png)

Click `Import data`

  ![Import Data](/docs/images/6_import_data.png)

Now fill out all the necessary parameters. 
+ Data Source: Select `Azure Blob Storage`. New options will drop down.
+ Data source name: This can be anything, but go with something like `grant-data`.
+ Data to extrac: Select `Content and metadata`.
+ Parsing mode: Select `Delimited text`. Check the `First Line Contains Header` box and leave `Delimiter Character` as `,`.
+ Connection string: Click `Choose an existing connection` and navigate to your storage account and container.
+ Managed identity authentication: Leave as default.
+ Container name: Should be populated when you connect via Connection String, but otherwise just enter your container name here.
+ Blob folder: *Optional*, if you have a folder within the container with the file(s) you want to index, enter that path here.
+ Description: *Optional*.
+ If you get errors when trying to go to the next screen, make sure you don't have trailing commas in your csv, and there are not spaces in the header names. If this happens, fix those errors, re-upload to blob storage, and then try again! 

  ![Connect to blog](/docs/images/7_connect_to_blob.png)

Skip ahead to `Customize target index`. 
+ Give your index a name.
+ Make `Project_Number` your key.
+ Make sure the expected column names are present under fields. For the columns you expect to use, select `Retrievable` and `Searchable`. If you select all the columns you will just pay for indexing you are not using.

  ![Customize index](/docs/images/8_target_index.png)

Advance to `Create an indexer`, name your indexer, then click `Submit`. 

  ![Create indexer](/docs/images/9_create_indexer.png)

Navigate to `Indexes` on the left panel and wait until your index shows as many documents as you have lines in your file. It will read 0 documents until it is finished indexing. The example 500 line csv takes about one minute.

  ![Check index](/docs/images/10_check_index.png)


And that is it! Now return to [the tutorial notebook to run queries against this csv using GPT-4]( /tutorials/notebooks/GenAI/notebooks/llm_query_csv.ipynb).









  
