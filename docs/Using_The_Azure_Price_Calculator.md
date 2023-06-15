# Azure Pricing Calculator
The Azure Price Calculator is an important tool to use as you are beginning to determine what resources you will need in Azure. When used correctly it will show you the potential hourly and monthly costs of each resource. It is important that you understand that both the type of resource and the amount of time it is being used effects the total cost for using that resource. So try to use the lowest cost resource for your projects to prevent cost overuns. Reading through these instructions before using the Calculator will help you better understand the options available to you.   
 [Azure Price Calculator](https://azure.microsoft.com/en-us/pricing/calculator/?OCID=AIDcmm5edswduu_SEM_0578e77bc86314f796a884a07b206fd0:G:s&ef_id=0578e77bc86314f796a884a07b206fd0:G:s&msclkid=0578e77bc86314f796a884a07b206fd0).
 
# Guide to using the Azure Pricing Calculator and calculating costs
### Main Page
1. The picture below shows the main/signin page for the calculator, which displays the four tabs across the top.
<img width="1090" alt="PC_Mainpage" src="https://user-images.githubusercontent.com/116583981/216338154-39affe93-129e-4850-acee-0a6dbe9310ab.png">
The four tabs across the top are: a Products tab, an Example Scenarios tab, a saved Estimates tab, and finally an FAQ tab to help answer any questions you might have. 

### Calculating costs 
Before we review the use of the tabs, we need to get a basic understanding of how the calculations work.  
Below are screen shots of the claculations for a simple Virtual Machine (VM).The first one shows the total monthly cost for the VM at $14.60 for 730 hours of operation. (That is the average total amount of hours in a month.) 
<img width="600" alt="A0 1Core 730" src="https://user-images.githubusercontent.com/116583981/217034381-881b0b0b-5d53-498f-b77d-15e7f4f29b1f.png">

Now lets take that same VM and only run it during working hours, eight hours a day for twenty days. you see that by shutting down the VM after hours and when not in use will generate significant savings. In this case the cost drops to $3.20 for the same resource for the month.
<img width="600" alt="A0 1Core 160" src="https://user-images.githubusercontent.com/116583981/217039565-3d9cda15-c28c-4594-897a-16e585d05447.png">

With a small resource, as in the example above, we see little effect on our monthly budget. But what about if we used something larger? The screen shot below shows the largest of the A series VMs, an A7, and the cost for 730 hours is $876.00. (That's $376.00 over the Cloud Lab subscription's monthly budget of $500.00.)

<img width="600" alt="A7 8 Cores 730" src="https://user-images.githubusercontent.com/116583981/217044030-bad4093d-5d58-49d7-ae70-0c8c9267fb85.png">

As in the example above, even if we reduce the number of hours for the month to just the work hours the cost is still significant. In this case the cost is $192.00. That is almost two fifths of the $500.00 monthly budget just for one resource.

<img width="600" alt="A7 8Cores 160" src="https://user-images.githubusercontent.com/116583981/217047401-a27c9ae1-274a-47ce-b053-b0ee77447e37.png">

Note: Once you configure a cost estimate for a product you can then add additional products to help determine the overall cost for a project. This will be shown and explained further under the Examples Tab decription.  
*******

## The Products Tab 
If you select the Products Tab, you will be presented with a list of twenty types of products that users can run calculations. Below I have included descriptions of the ones that will most likely be useful for people using the Azure Cloud Lab. You will notice that some resources will show up under multiple tabs. Additionally, to keep this tutorial short we did not cover Products that most likely will not be used in the Cloud Lab.

### Popular
When you select the Popular tab you are presented with tiles showing the most popular products that are requested.
<img width="600" alt="Popular" src="https://user-images.githubusercontent.com/116583981/217568591-0acd4187-e060-4078-966c-98150154756c.png">

### Compute
The Compute tab displays tiles of computational products.
<img width="600" alt="Compute" src="https://user-images.githubusercontent.com/116583981/217588206-36fb013d-5ef9-4567-a03b-9a212757c831.png">

### Networking
Products are available but probably not used in Azure Cloud lab.

### Storage
The Storage tab displays tiles of the various data storage options   
<img width="600" alt="Storage" src="https://user-images.githubusercontent.com/116583981/217591511-155d39ad-b100-4b90-a515-43e40c89d519.png">

### Web
Products are available but probably not used in Azure Cloud lab.

### Mobile
Products are available but probably not used in Azure Cloud lab.

### Containers
The Containers tab displays tiles showing the options for Azure based containers.
<img width="600" alt="Containers" src="https://user-images.githubusercontent.com/116583981/217594440-36ed7c44-8bb9-4651-8efe-1877782e9f6a.png">

### Databases
The Databases tab displays tiles listing your Azure database options.
<img width="600" alt="Databases" src="https://user-images.githubusercontent.com/116583981/217598473-7ee778f2-2f71-4a9a-87cf-7466dd0723bb.png">

### Analytics
This tab displays the available Azure based analytic tools.

<img width="600" alt="Analytics" src="https://user-images.githubusercontent.com/116583981/217828471-bfb4e4cf-95da-4e00-a459-3111d6fe34f5.png">

### AI + machine learning
The AI + machine learning tab displays tiles of of available products related to the title.
<img width="600" alt="AI+ML" src="https://user-images.githubusercontent.com/116583981/217830483-3717346c-cf13-41b1-9451-20e186d44168.png">

### Internet of Things
The IOT tab displays products related to IOT operations plus some analytics and machine learning products.  
<img width="600" alt="IOT" src="https://user-images.githubusercontent.com/116583981/217859267-77f2638b-af03-4320-a853-7ce0aa1a37f5.png">

### Integration
This tab displays tiles of products relating to integrating with operations outside of the Azure Cloud.  
<img width="600" alt="Integration" src="https://user-images.githubusercontent.com/116583981/217888966-7501f7a2-aeaf-49fb-9bf6-3bffdbb5bbfb.png">

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
<img width="600" alt="RTA pic" src="https://user-images.githubusercontent.com/116583981/217897935-ea62b651-1966-4e8b-b2d1-d0ba91ffb706.png">

If you click the Add to Estimate button you will then see a breakdown of each item's cost. Please note the number of instances and the default number of hours used to generate the estimate.   
<img width="600" alt="RTA Cost" src="https://user-images.githubusercontent.com/116583981/217899456-dcd149ca-2022-4157-a9e1-4cbdc7e72f6d.png">

Now, if we do the same steps with the example above as we did under calculating costs by removing items and reducing hours. We can then bring the costs down to something that is under the Cloud Lab monthly budget. 
<img width="600" alt="RTA_EST1" src="https://user-images.githubusercontent.com/116583981/219459440-053d9a32-26e1-4309-b459-46cc29e2ab4a.png">

## Saved Estimates Tab
Just what it implies. You will find any previously saved estimates under this tab.

## FAQs
Pricing Calculator Frequently asked Questions.

