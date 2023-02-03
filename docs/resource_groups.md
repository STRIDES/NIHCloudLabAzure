- [Guide to Azure Resource Groups](#guide-to-azure-resource-groups)
    - [Logical Grouping](#logical-grouping)
    - [Life cycle](#life-cycle)
    - [Authorization](#authorization)
  - [Resource Group Tutorials](#resource-group-tutorials)
    - [Create Resource Group](#create-resource-group)
    - [List Resource Groups](#list-resource-groups)
    - [Open Resource Group](#open-resource-group)
    - [Delete Resource Groups](#delete-resource-groups)
    - [Move to another resource group](#move-to-another-resource-group)

# Guide to Azure Resource Groups
Resource groups are a fundamental element of the Azure platform. A resource group is a logical container for resources deployed on Azure. These resources are anything you create in an Azure subscription like VMs, Azure Application Gateway instances, and Azure Cosmos DB instances. All resources must be in a resource group, and a resource can only be a member of a single resource group. Many resources can be moved between resource groups with some services having specific limitations or requirements to move. Resource groups can't be nested. Before any resource can be provisioned, you need a resource group for it to be placed in.

<img alt="image" src="/docs/images/ResourceGroups1.png">

### Logical Grouping
Resource groups exist to help manage and organize your Azure resources. By placing resources of similar usage, type, or location in a resource group, you can provide order and organization to resources you create in Azure. Logical grouping is the aspect that you're most interested in here, because there's disorder among our resources.

### Life cycle
If you delete a resource group, all resources contained within it are also deleted. Organizing resources by life cycle can be useful in nonproduction environments, where you might try an experiment and then dispose of it. Resource groups make it easy to remove a set of resources all at once.

### Authorization
Resource groups are also a scope for applying role-based access control (RBAC) permissions. By applying RBAC permissions to a resource group, you can ease administration and limit access to allow only what's needed.

---------------------------------

## Resource Group Tutorials
### Create Resource Group<a name="crg"></a>
1. Sign in to the Azure portal.
2. Select Resource groups

<img alt="image" src="/docs/images/manage-resource-groups-add-group.png">

3. Select Add.
4. Enter the following values:
    - Subscription: Select your Azure subscription.
    - Resource group: Enter a new resource group name.
    - Region: Select an Azure location, such as Central US.

<img alt="image" src="/docs/images/manage-resource-groups-create-group.png">

5. Select Review + Create
6. Select Create. It takes a few seconds to create a resource group.
7. Select Refresh from the top menu to refresh the resource group list, and then select the newly created resource group to open it. Or select Notification(the bell icon) from the top, and then select Go to resource group to open the newly created resource group

<img alt="image" src="/docs/images/manage-resource-groups-add-group-go-to-resource-group.png">

Direct Microsoft documentation link [here.](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#create-resource-groups).


###  List Resource Groups<a name="lrg"></a>
1. Sign in to the Azure portal.
2. To list the resource groups, select Resource groups

<img alt="image" src="/docs/images/manage manage-resource-groups-list-groups.png">

3. To customize the information displayed for the resource groups, select Edit columns.

Direct Microsoft documentation link [here.](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#list-resource-groups).

### Open Resource Group<a name="org"></a>
1. Sign in to the Azure portal.
2. Select Resource groups.
3. Select the resource group you want to open.
   
Direct Microsoft documentation link [here.](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#open-resource-groups).

###  Delete Resource Groups<a name="drg"></a>
1. Open the resource group you want to delete. See Open resource groups.
2. Select Delete resource group.
   
<img alt="image" src="/docs/images/delete-group.png">

Direct Microsoft documentation link [here.](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#delete-resource-groups).


###  Move to another resource group<a name="mtarg"></a>
1. To move resources, select the resource group that contains those resources.
2. Select the resources you want to move. To move all of the resources, select the checkbox at the top of list. Or, select resources individually.

<img alt="image" src="/docs/images/select-resources-to-move.png">

3. Select the Move button.

<img alt="image" src="/docs/images/select-move.png">

4. This button gives you three options:
    - Move to a new resource group.
    - Move to a new subscription.
    - Move to a new region. To change regions, see Move resources across regions (from resource group).
5. Select whether you're moving the resources to a new resource group or a new subscription.
6. The source resource group is automatically set. Specify the destination resource group. If you're moving to a new subscription, also specify the subscription. Select Next.

<img alt="image" src="/docs/images/select-destination-group.png">

7. The portal validates that the resources can be moved. Wait for validation to complete.

<img alt="image" src="/docs/images/validation.png">

8. When validation completes successfully, select Next.
9. Acknowledge that you need to update tools and scripts for these resources. To start moving the resources, select Move.

<img alt="image" src="/docs/images/acknowledge-change.png">

10. When the move has completed, you're notified of the result.

<img alt="image" src="/docs/images/view-notification.png">

Direct Microsoft documentation link [here.](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription).






