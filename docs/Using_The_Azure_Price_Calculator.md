# Azure Pricing Calculator
The Azure Price Calculator is an important tool to use as you are beginning to determine what resources you will need in Azure. When used correctly it will show you the potential hourly and monthly costs of each resource. It is important that you understand that both the type of resource and the amount of time it is being used effects the total cost for using that resource. So try to use the lowest cost resource for your projects to prevent cost overuns. Reading through these instructions before using the Calculator will help you better understand the options available to you.   
 [Azure Price Calculator](https://azure.microsoft.com/en-us/pricing/calculator/?OCID=AIDcmm5edswduu_SEM_0578e77bc86314f796a884a07b206fd0:G:s&ef_id=0578e77bc86314f796a884a07b206fd0:G:s&msclkid=0578e77bc86314f796a884a07b206fd0).
 
# Guide to using the Azure Pricing Calculator and calculating costs
### Main Page
1. The picture below shows the main/signin page for the calculator, which displays the four tabs across the top.
![Image of calculator](/docs/images/1_calculator.png)
The four tabs across the top are: a Products tab, an Example Scenarios tab, a saved Estimates tab, and finally an FAQ tab to help answer any questions you might have. 

### Calculating costs 
Before we review the use of the tabs, we need to get a basic understanding of how the calculations work.  
Below are screen shots of the claculations for a simple Virtual Machine (VM).The first one shows the total monthly cost for the VM at $14.60 for 730 hours of operation. (That is the average total amount of hours in a month.)

![Screenshot of calculator with VMS](/docs/images/2_virtualmachinecalculator.png)

Now lets take that same VM and only run it during working hours, eight hours a day for twenty days. you see that by shutting down the VM after hours and when not in use will generate significant savings. In this case the cost drops to $3.20 for the same resource for the month.

![Screenshot of calculator with VMS 3](/docs/images/3_calc_vmparttime.png)

With a small resource, as in the example above, we see little effect on our monthly budget. But what about if we used something larger? The screen shot below shows the largest of the A series VMs, an A7, and the cost for 730 hours is $876.00. (That's $376.00 over the Cloud Lab subscription's monthly budget of $500.00.)

![Screenshot of calculator with VMS 4](/docs/images/4_vm_large_caluclator.png)

As in the example above, even if we reduce the number of hours for the month to just the work hours the cost is still significant. In this case the cost is $192.00. That is almost two fifths of the $500.00 monthly budget just for one resource.

![Screenshot of calculator with VMS 5](/docs/images/5_calc.png)

Note: Once you configure a cost estimate for a product you can then add additional products to help determine the overall cost for a project. This will be shown and explained further under the Examples Tab decription.  
*******

## The Products Tab 
If you select the Products Tab, you will be presented with a list of twenty types of products that users can run calculations. Below I have included descriptions of the ones that will most likely be useful for people using the Azure Cloud Lab. You will notice that some resources will show up under multiple tabs. Additionally, to keep this tutorial short we did not cover Products that most likely will not be used in the Cloud Lab.

### Popular
When you select the Popular tab you are presented with tiles showing the most popular products that are requested.

![Screenshot of Popular Products](/docs/images/6_popular_products.png)

### Compute
The Compute tab displays tiles of computational products.

![Screenshot of Compute Products](/docs/images/7_compute_products.png)

### Networking
Products are available but probably not used in Azure Cloud lab.

### Storage
The Storage tab displays tiles of the various data storage options  

![Screenshot of Storage Products](/docs/images/8_storage_products.png)

### Web
Products are available but probably not used in Azure Cloud lab.

### Mobile
Products are available but probably not used in Azure Cloud lab.

### Containers
The Containers tab displays tiles showing the options for Azure based containers.

![Screenshot of Container Products](/docs/images/9_container_products.png)

### Databases
The Databases tab displays tiles listing your Azure database options.

![Screenshot of Database Products](/docs/images/10_db_products.png)

### Analytics
This tab displays the available Azure based analytic tools.

![Screenshot of Analytics Products](/docs/images/(11_analytics_products.png)

### AI + machine learning
The AI + machine learning tab displays tiles of of available products related to the title.

![Screenshot of AIML Products](/docs/images/12_AI_products.png)

### Internet of Things
The IOT tab displays products related to IOT operations plus some analytics and machine learning products.

![Screenshot of AIML Products](/docs/images/13_IOT_products.png)

### Integration
This tab displays tiles of products relating to integrating with operations outside of the Azure Cloud. 

![Screenshot of Integration Products](/docs/images/14_integration_products.png)

### Identity
Products are available but probably not used in Azure Cloud lab.

### Security
Products are available but probably not used in Azure Cloud lab.

### Developer tools
Products are available but probably not used in Azure Cloud lab.

### Management and governing
Products are available but probably not used in Azure Cloud lab. 

### Media
Products are available but probably not used in Azure Cloud lab.

### Migration
Products are available but probably not used in Azure Cloud lab.

### Mixed reality
Products are available but probably not used in Azure Cloud lab.

### Hybrid + multicloud
Products aavailable but probably not used in Azure Cloud lab.

## The Examples Tab

The Examples tab is exactly what it describes. It shows you six examples of figuring the total cost of various products that you would need for your projects. 
If we choose Real-time analysis we are presented with a project drawing with a listing of the products that will be used. 

![Screenshot of RealTimeAnaltyics](/docs/images/15_RT_Analytics.png)

If you click the Add to Estimate button you will then see a breakdown of each item's cost. Please note the number of instances and the default number of hours used to generate the estimate.   

![Screenshot of RealTimeAnaltyics](/docs/images/16_get_estimate.png)

Now, if we do the same steps with the example above as we did under calculating costs by removing items and reducing hours. We can then bring the costs down to something that is under the Cloud Lab monthly budget. 

![Screenshot of RealTimeAnaltyics](/docs/images/17_revise_estimate.png)

## Saved Estimates Tab
Just what it implies. You will find any previously saved estimates under this tab.

## FAQs
Pricing Calculator Frequently asked Questions.

