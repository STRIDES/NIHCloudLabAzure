# Deploying and using Azure CycleCloud

Azure CycleCloud deploys autoscaling plugins on top of the supported schedulers, so users do not need to implement complex autoscaling functions and routines themselves, but rather interface only with scheduler-level configurations that they are familiar with.

## Deploy Azure CycleCloud from Azure Marketplace and Add a Subscription to the CycleCloud instance

Navigate to the Azure [portal](https://portal.azure.com/) and type in "marketplace" in the search bar on top of screen.

<img src="/docs/images/Marketplace_Azure.png" width="600">

Once in the Azure Marketplace, in the Marketplace search bar , search for "Azure CycleCloud" see below.

<img src="/docs/images/AzureCycleCloud.png" width="600">

Click "Azure CycleCloud" followed by selecting the version you want (we recommend the most recent) and then "Create"

Fill out the appropriate information for the Virtual Machine to run and then click "Review + Create". Most of the options you can leave as default, but pay attention to the size of the machine, and we recommend you use the autoshutdown feature to stop your cluster if you forget to manually shut it down.

Once the Azure CycleCloud virtual machine is deployed, navigate to the resource in the portal and look for the IP address

<img src="/docs/images/Azure_cycleCloud2.png" width="600">

Enter the IP address of you Azure CycleCloud instance in a browser. It may take a few minutes for the IP to populate so if it says 'Site can't be reached' just try after a few minutes. Also, on Chrome you may get 'Connection is not Private' Warning, you can click 'Advanced' then 'Proceed to IP (unsafe). 

If this is the first time opening up Azure CycleCloud a pop up should display to associate your subscription and virtual machine with Azure Cycle Cloud. See below:

<img src="/docs/images/Add_Subscription_CycleCloud.png" width="600">

Fill out the neccassary information required, you will need to configure a custom role for Azure CycleCloud to find your subscription. Here is [documentation](https://github.com/STRIDES/NIHCloudLabAzure/blob/main/docs/Create_Custom_Role_AzureHPC.md) on how to create a custom role for Azure Cycle Cloud.

## Create Cluster from Azure CycleCloud UI

Once logged into the CycleCloud VM click the plus sign on the bottom left corner and the following options should appear:

<img src="/docs/images/CycleCloud_UI.png" width="600">

Select a scheduler and file system if necessary

Give your cluster a name, and provide the correct parameters in the required settings section

Once Cluster is created navigate back to the main page and start your cluster if it is not up already, see example:

<img src="/docs/images/CycleCloudTest.png" width="600">

Click start, once cluster is up you can SSH into the clusters scheduler node, see example below: 

<img src="/docs/images/SSH_example.png" width="600">

Click connect and screen should prompt you with a command to ssh into scheduler node:

<img src="/docs/images/SSH_2.png" width="600">
