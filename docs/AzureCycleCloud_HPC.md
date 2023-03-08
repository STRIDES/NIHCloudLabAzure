# Deploying and using Azure CycleCloud

Azure CycleCloud is Microsoft's solution for cloud-based HPC. As such, you can spin up a cluster with a variety of clusters already configured, including SLURM, Grid Engine and others. Further, Azure CycleCloud deploys autoscaling plugins meaning that users do not need to implement complex autoscaling functions and routines themselves, but rather interface only with the job scheduler in a way they are familiar with.

## Deploy Azure CycleCloud from Azure Marketplace and Add a Subscription to the CycleCloud instance

Navigate to the Azure [portal](portal.azure.com) and type in **marketplace** in the search bar on top of screen.

<img src="/docs/images/Marketplace_Azure.png" width="600">

Once in the Azure Marketplace, in the Marketplace search bar, search for **Azure CycleCloud** as shown here.

<img src="/docs/images/AzureCycleCloud.png" width="600">

Click **Azure CycleCloud**, then select the version you want, then click **Create**.

Fill out the appropriate information for the Virtual Machine to run and then click **Review + Create**.

Once the Azure CycleCloud virtual machine is deployed, navigate to the resource in the portal and look for the IP address.

<img src="/docs/images/Azure_cycleCloud2.png" width="600">

Enter the IP address of you Azure CycleCloud instance in a browser, if this is the first time opening up Azure CycleCloud a pop up should display to associate your subscription and virtual machine with Azure Cycle Cloud as shown here. 

<img src="/docs/images/Add_subscription_CycleCloud.png" width="600">

Fill out the necessary information required; you may need to configure a custom role for Azure CycleCloud to find your subscription.

## Create Cluster from Azure CycleCloud UI

Once logged into the CycleCloud VM click the plus sign on the bottom left corner and the following options should appear:

<img src="/docs/images/CycleCloud_UI.png" width="600">

Select a scheduler and file system if necessary.

Give your cluster a name, and provide the correct parameters in the required settings section.

Once Cluster is created navigate back to the main page and start your cluster if it is not up already, see example:

<img src="/docs/images/CycleCloudTest.png" width="600">

Click **start**, once cluster is up you can SSH into the scheduler node, see example below: 

<img src="/docs/images/SSH_example.png" width="600">

Click connect and screen should prompt you with a command to ssh into scheduler node:

<img src="/docs/images/SSH_2.png" width="600">
