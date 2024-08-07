# Guide to Azure Billing and Cost Management

Understanding how to manage your costs can be difficult in the cloud. For one thing, you have to keep track of how much you have spent with the obvious services, like Virtual Machines, Azure Machine Learning and Azure Storage Accounts. On the other hand, how can you figure out how much you are being charged for your network (Virtual Networks)? 
Further, some Cloud Lab users are interested in understanding how to forecast cloud costs for a larger project. For example, if you want to understand the cost of calling somatic variants on 100 samples, but in Cloud Lab you plan to benchmark using five samples. How would you go about doing that? 
This guide aims to answer these questions. 

- [Resource Tagging](#resource-tagging)
- [Managing Subscription Costs](#managing-subscription-costs)
- [Billing](#billing)

## Resource Tagging<a name="RT"></a>

One of the first steps to understanding costs is resource naming and tagging. Billing reports will be aggregated across time and services, and it can be hard to figure out how much did that variant calling pipeline cost to run? 
Tagging allows you attach metadata to resources that you can later filter for in Billing reports. Azure has a Resource Naming and Tagging decision guide [here](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/resource-tagging/?toc=%2Fazure%2Fazure-resource-manager%2Fmanagement%2Ftoc.json).

You can add a tag to pretty much any resource but let's look at a few examples. These examples show use of the [Azure Portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json#portal) to manage tags. Corresponding examples can be found here for [PowerShell](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json#powershell) and [Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json#azure-cli).

*******
### Viewing Tags
1. To view the tags for a resource or a resource group, look for existing tags in the overview. If you have not previously applied tags, the list is empty.

   ![View Tags](/docs/images/view-tags.png)

### Add a Tag
1. To add a tag, select Click here to add tags.
2. Provide a name and value.

   ![Add Tag](/docs/images/add-tag.png)

3. Continue adding tags as needed. When done, select Save.

   ![Save Tags](/docs/images/save-tags.png)

4. The tags are now displayed in the overview.

   ![View New Tags](/docs/images/view-new-tags.png)

### Delete a Tag
1. To delete a tag, select the trash icon. Then, select Save.

   ![Delete Tag](/docs/images/delete-tag.png)

### Bulk Assign Tags to Multiple Resources
1. From any list of resources, select the checkbox for the resources you want to assign the tag. Then, select Assign tags.

   ![Select Resources](/docs/images/select-multiple-resources.png)

2. Add names and values. When done, select Save.
   ![Select Assign](/docs/images/select-assign.png)

### Viewing all Resources with a Tag
1. On the Azure portal menu, search for tags. Select it from the available options.

   ![Find Tags General](/docs/images/find-tags-general.png)

2. Select the tag for viewing resources.

   ![Select Tag](/docs/images/select-tag.png)
   
4. All resources with that tag are displayed.

   ![View Resources by Tag](/docs/images/view-resources-by-tag.png)

##  Managing Subscription Costs<a name="MSC"></a>

The left panel on the subscription home screen lists your options for managing costs within your subscription. Overview gives you a snapshot of your current and predicted future spending rates.  

   ![Billing Dashboard](/docs/images/1_billing_dashboard_image.png)

Under **Cost Management** there are three tools to help you manage costs, Cost analysis, Cost alerts, and Budgets. Additionally there is one tool called Advisor recommendations to help you configure your Subscription, and resources, in the most cost effective manners. 

Clicking on **Cost Analysis** displays a screen similar to Overview but with a breakdown on the costs. In the screen shot below the costs are broken down by Service, Location, and Resource Group. 

   ![Cost Analysis](/docs/images/2_cost_analysis.png)

Click on **Cost Alert** on the left panel. Here you are able to configure alerts for budgets and create cost anomaly alerts to automatically get notified if an anomaly is detected. Such as a resource running up costs to quickly. Click on **Learn more** to get detailed descriptions and instructions.

   ![Image of Billing v1](/docs/images/3_cost_analysis.png)

Click on **Budgets** on the left panel. This is where you will set the spending limits for your organization and send notifications out when certain limits of the budget are reached. You can click on the **Visit the budget documentation** for a short tutorial on creating and managing budgets.

   ![Image of Billing 2](/docs/images/4_budget.png)

There is one final tool under Cost Management. As stated before this tool can help you manage your budget and keep your costs inline.

Click on **Advisor Recommendations** This will take you to a screen where you can see what steps you can take to help minimize costs to help meet any budget constraints. Click on **See list of cost recommendations** to get indepth information on ways to configure your resources in a cost effective manner.   

   ![Image of Billing 3](/docs/images/5_advisor.png)

## Billing<a name="BG"></a>

Further down on the left panel is another subtitle called "Billing". Under this subtitle Click on **Billing Profile Invoices** to view both current and past invoices. You can click on the link **Learn more about billing profiles** to get more information on billing account. 

   ![Image of Billing 4](/docs/images/6_amount_due.png)

