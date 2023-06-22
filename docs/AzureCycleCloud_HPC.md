# Deploying and using Azure CycleCloud

Azure CycleCloud deploys autoscaling plugins on top of the supported schedulers, so users do not need to implement complex autoscaling functions and routines themselves, but rather interface only with scheduler-level configurations that they are familiar with.

## Deploy Azure CycleCloud from Azure Marketplace and Add a Subscription to the CycleCloud instance

Navigate to the [Azure Portal](https://portal.azure.com/) and type in "marketplace" in the search bar on top of screen.

![Screenshot of the Azure Marketplace](/docs/images/Marketplace_Azure.png)

Once in the Azure Marketplace, in the Marketplace search bar , search for "Azure CycleCloud" see below.

![Screenshot of Azure CycleCloud in the Marketplace](docs/images/AzureCycleCloud.png)

Click "Azure CycleCloud" followed by selecting the version you want (we recommend the most recent) and then "Create"

Fill out the appropriate information for the virtual machine to run and then click "Review + Create". Most of the options you can leave as default, but pay attention to the size of the machine, and we recommend you use the autoshutdown feature to stop your cluster if you forget to manually shut it down. Azure CycleCloud virtual machines require a key pair to be created, there are multiple ways to create a key pair, please see [documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/) and then navigate to the dropdown on the right side of the documentation and open "Instances" and then click the "Connect to Virtual Machines" drop down to access information on how to create a key pair in Linux and Windows.

Once the Azure CycleCloud virtual machine is deployed, navigate to the resource in the portal and look for the IP address

![Screenshot of an Azure CycleCloud virtual machine](/docs/images/Azure_cycleCloud2.png)

Enter the IP address of you Azure CycleCloud instance in a browser. It may take a few minutes for the IP to populate so if it says 'Site can't be reached' just try after a few minutes. Also, on Chrome you may get 'Connection is not Private' Warning, you can click 'Advanced' then 'Proceed to IP (unsafe). 

If this is the first time opening up Azure CycleCloud a pop up should display to associate your subscription and virtual machine with Azure Cycle Cloud. See below:

![Screenshot configuring Azure CycleCloud](/docs/images/Add_Subscription_CycleCloud.png)

Fill out the neccassary information required, you will need to configure a custom role for Azure CycleCloud to find your subscription. Here is [documentation](https://github.com/STRIDES/NIHCloudLabAzure/blob/main/docs/Create_Custom_Role_AzureHPC.md) on how to create a custom role for Azure Cycle Cloud.

## Create Cluster from Azure CycleCloud UI

Once logged into the CycleCloud VM click the plus sign on the bottom left corner and the following options should appear:

![Screenshot of Azure CycleCloud new cluster wizard](/docs/images/CycleCloud_UI.png)

If necessary, select a scheduler and file system.

Give your cluster a name, and provide the correct parameters in the required settings section.

Once Cluster is created navigate back to the main page and Start your cluster if it is not up already:

![Screenshot of Azure CycleCloud cluster status](/docs/images/CycleCloudTest.png)

Once started, the cluster's scheduler node can be connected into via SSH: 

![Screenshot of Azure CycleCloud cluster scheduler node](/docs/images/SSH_example.png)

Click Connect and you should be prompted with a command to connect into the scheduler node:

![Screenshot connecting to Azure CycleCloud cluster scheduler node](/docs/images/SSH_2.png)

We recommend using the [Azure CycleCloud CLI](https://learn.microsoft.com/en-us/azure/cyclecloud/how-to/install-cyclecloud-cli?view=cyclecloud-8).
