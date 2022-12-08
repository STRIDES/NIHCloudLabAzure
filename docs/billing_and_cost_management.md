# **Being Updated**
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
AWS Specific Examples:

## 2. Explore Billing Reports

You can find a lot of billing tools by searching for billing in the bar at the top of your console. 

<img src="/docs/images/search_billing.png" width="550" height="350">

However, the best billing tool for Cloud Lab use is the cost explorer. 

1. Go to the (A) *Console Home Page*, then to (B) *AWS Cost Management*.

<img src="/docs/images/aws_cost_management.png" width="550" height="350">

2. Click on **Cost Explorer** on the left panel

<img src="/docs/images/cost_explorer.png" width="550" height="350">

3. Click on (A) the data range, then (B) change the end date to today's date. By default it will show you billing to the end of last month so you won't see your current month charges.

<img src="/docs/images/change_end_date.png" width="550" height="350">

4. Filter for different parameters on the right. Here we can filter by *Service* to select only costs related to EC2.

<img src="/docs/images/Ec2_filter_service.png" width="550" height="250">

Now we see only costs related to EC2.

<img src="/docs/images/ec2-filtered.png" width="550" height="250">

5. Filter for the tags we added in Part 1 to benchmark a specific analysis. In this case, we are going to select **BLAST**.

<img src="/docs/images/filter_tag.png" width="550" height="325">

Now we can see the costs related to the analyses with the BLAST tag. If you don't see the tags you added before, make sure you have waited ~12 hours. AWS aggregates costs about three times per day, so those costs may have just not shown up yet. 

<img src="/docs/images/blast_costs.png" width="550" height="300">

6. Explore the other options available. You can change the plot type, change the filtering, and use several other tools within *Cost Management*. 

## 3. Create Budget Alerts

One way to help stay on budget is to create budget alerts. You can do this using the *Budgets* tool within *Cost Management*.

<img src="/docs/images/nav_budget.png" width="550" height="250">

1. Click **Create a budget**. 

<img src="/docs/images/create_budget.png" width="550" height="250">

2. Select your budget type. We recommend *Cost budget*. Click `Next`. 

<img src="/docs/images/budget_type.png" width="550" height="250">

3. On the next page, enter a Budget Name. Under budget amount, select **Annually** for *Period*. Under *Budget renewal type* select **Expiring budget**. For *Budgeting method* select **Fixed** and then type **500** for the Budget Amount.

<img src="/docs/images/configure_budget_aws.png" width="550" height="625">

4. You can leave the rest as default and then click **Next**

<img src="/docs/images/budget_scope.png" width="550" height="350">

5. Click **Add an alert threshold**

<img src="/docs/images/add_alert_threshold.png" width="550" height="450">

6. Configure your budget alerts as desired. Here we set one alert for when the budget reaches 50%, but you could set several alerts to let you know when you have reached 25%, 50%, 75% and then 95% for example. 

<img src="/docs/images/budget_alerts.png" width="550" height="350">

7. Click **Next**. On the following page, click **Create Budget**

<img src="/docs/images/submit_budget.png" width="550" height="400">
