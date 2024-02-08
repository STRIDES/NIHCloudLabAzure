### Create an Azure search inded from a csv file
:sparkles: Here we outline how to create an Azure search index from a CSV file summarizing funded award data exported from Reporter.nih.gov

### 1) Generate input CSV
:ear: If you already have your csv ready, skip to (2).

Our input data comes from the csv export option for [Reporter.nih.gov](https://reporter.nih.gov/). Navigate to reporter.nih.gov and select `Advanced Search`. Input your search parameters. In this case we filtered for awards made by NIGMS in FY 23. In the top right, select `Export`.

Select your export columns and make sure you export as a csv. In the example input data file we only selected 'Title', 'Project_ID', and 'Total_Cost', although a few other columns were also exported.

  ![Export from Reporter](/docs/images/1_export_from_reporter.png)

  
