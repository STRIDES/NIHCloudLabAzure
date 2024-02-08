### Create an Azure search inded from a csv file
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



  
