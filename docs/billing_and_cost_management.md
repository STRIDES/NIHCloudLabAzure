# **Content Being Updated**

# Guide to Azure Billing and Cost Management

Understanding how to manage your costs can be difficult in the cloud. For one thing, you have to keep track of how much you have spent with the obvious services, like Virtual Machines, Azure Machine Learning and Azure Storage Accounts. On the other hand, how can you figure out how much you are being charged for your network (Virtual Networks)? 
Further, some Cloud Lab users are interested in understanding how to forecast cloud costs for a larger project. For example, if you want to understand the cost of calling somatic variants on 100 samples, but in Cloud Lab you plan to benchmark using five samples. How would you go about doing that? 
This guide aims to answer these questions. 

## 1. Resource Tagging

One of the first steps to understanding costs is resource naming and tagging. Billing reports will be aggregated across time and services, and it can be hard to figure out how much did that variant calling pipeline cost to run? 
Tagging allows you attach metadata to resources that you can later filter for in Billing reports. Azure has a Resource Naming and Tagging decision guide [here](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/resource-tagging/?toc=%2Fazure%2Fazure-resource-manager%2Fmanagement%2Ftoc.json).

You can add a tag to pretty much any resource but let's look at a few examples. These examples show use of the [Azure Portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json#portal) to manage the tags.  Corresponding examples can be found here for [PowerShell](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json#powershell) and [Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json#azure-cli).

*******
### Viewing Tags
1. To view the tags for a resource or a resource group, look for existing tags in the overview. If you have not previously applied tags, the list is empty.
<img src="/docs/images/view-tags.png" width="600" height="245">

### Add a Tag
1. To add a tag, select Click here to add tags.
2. Provide a name and value.
   
    <img src="/docs/images/add-tag.png" width="700" height="341">
3. Continue adding tags as needed. When done, select Save.
    <img src="/docs/images/save-tags.png" width="700" height="404">
4. The tags are now displayed in the overview.
    <img src="/docs/images/view-new-tags.png" width="700" height="252">

### Delete a Tag
1. To delete a tag, select the trash icon. Then, select Save.
<img src="/docs/images/delete-tag.png" width="700" height="357">

### Bulk Assign Tags to Multiple Resources
1. From any list of resources, select the checkbox for the resources you want to assign the tag. Then, select Assign tags.
    <img src="/docs/images/select-multiple-resources.png" width="700" height="465">
2. Add names and values. When done, select Save.
    <img src="/docs/images/select-assign.png" width="700" height="669">


### Viewing all Resources with a Tag
1. On the Azure portal menu, search for tags. Select it from the available options.
    <img src="/docs/images/find-tags-general.png" width="600" height="216">
2. Select the tag for viewing resources.
   
    <img src="/docs/images/select-tag.png" width="200" height="291">
3. All resources with that tag are displayed.
   
    <img src="/docs/images/view-resources-by-tag.png" width="600" height="431">

## 2. Explore Billing Reports
You can find a lot of billing tools by searching for billing in the bar at the top of your console. 

**Next text to put in**

## 3. Create Budget Alerts
One way to help stay on budget is to create budget alerts. You can do this using the *Budgets* tool within *Cost Management*.

**Next text to put in**


*******
## To Be Deleted
AWS Specific Examples:

