# Create Custom Role for Azure CycleCloud HPC

Go to this [link](https://learn.microsoft.com/en-us/azure/cyclecloud/how-to/managed-identities?view=cyclecloud-8) and copy the JSON policy and optional section and paste into notepad and save as a .JSON file

In the Azure [portal](https://portal.azure.com), open a subscription or resource group where you want the custom role to be assignable and then open Access control (IAM).

<img src="/docs/images/Custom_role1.png" width="600">

Click Add and then click Add custom role.

Give the Custom Role a name

Select "Start from JSON" option on the bottom followed by selected the blue folder and choosing the JSON file you recently created

Review + Create Role

<img src="/docs/images/Custom_role3.png" width="600">

# Assign Custom Role to VMs Managed Identity at the subscription level

Preqrequisite: Azure Cycle Cloud Virtual Machine deployed and configured(VM) and Custom role created

Navigate to the Azure CycleCloud VM 

from the left pane scroll down and click "Identity"

Click "Azure role assignments"

Click "Add role assignment(preview)" 

Select the scope to be "subscription"

Select the subscription the Azure CycleCloud instance is on 

Select the custom role you just created, example below: 

<img src="/docs/images/Custom_role2.png" width="600">
