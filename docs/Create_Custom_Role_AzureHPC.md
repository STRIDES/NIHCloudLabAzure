# Create Custom Role for Azure CycleCloud HPC

Go to this [link](https://learn.microsoft.com/en-us/azure/cyclecloud/how-to/managed-identities?view=cyclecloud-8) and copy the JSON policy and optional section and paste into notepad and save as a .JSON file

In the [Azure portal](https://portal.azure.com), open a subscription or resource group where you want the custom role to be assignable and then open Access control (IAM).

![Screenshot of where to find custom role](/docs/images/Custom_role1.png)

Click Add and then click Add custom role.

Give the custom role a name

Select "Start from JSON" option on the bottom followed by selected the blue folder and choosing the JSON file you recently created

Review + Create Role

![Screenshot on creating custom role](/docs/images/Custom_role3.png)

# Assign Custom Role to VMs Managed Identity at the subscription level

Preqrequisite: Azure CycleCloud virtual machine deployed and configured(VM) and Custom role created

Navigate to the Azure CycleCloud virtual machine

from the left pane scroll down and click "Identity"

Click "Azure role assignments"

Click "Add role assignment(preview)" 

Select the scope to be "subscription"

Select the subscription the Azure CycleCloud instance is on 

Select the custom role you just created, example below: 

![Screenshot on creating custom role](/docs/images/Custom_role2.png)
