# How to create a storage account and move data in and out

## 1. Create a storage account

First, go to `portal.azure.com`, then search for `storage account`. 

<img src="/docs/images/1_click_storage.png" width="550" height="450">

Next, click **Create**.

<img src="/docs/images/2_click_create.png" width="550" height="450">

Select your [Subscription](https://learn.microsoft.com/en-us/training/modules/create-an-azure-account/4-multiple-subscriptions).

If you do not yet have a resource group, create a new one. 

<img src="/docs/images/3_resource_group.png" width="550" height="450">

Now name your storage account (needs to be globally unique), select your region (should be East), performance should usually be standard, and then for redundancy leave the default, but feel free to review the options Microsoft provides [here](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy).
Feel free to review the rest of the options starting with `Next: Advanced`, but in most cases the defaults will be fine. Click **Review**.

<img src="/docs/images/4_name_resource_group.png" width="550" height="450">

Click **Create**

<img src="/docs/images/5_click_create.png" width="550" height="450">

## Create a container

Within a Storage Account, data lives within containers, which you can kind of think of as folders. In one sense then, the Storage Account is like an external hard drive, and then containers are the folders on the drive.
To create a container, first click **containers** on the left menu bar. 

<img src="/docs/images/6_click_containers.png" width="550" height="450">
