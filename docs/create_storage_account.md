# How to create a storage account and move data in and out

## 1. Create a storage account

First, go to `portal.azure.com`, then search for `storage account`. 

<img src="/docs/images/1_click_storage.png" width="550" height="450">

Next, click **Create**.

<img src="/docs/images/2_click_create.png" width="550" height="350">

Select your [Subscription](https://learn.microsoft.com/en-us/training/modules/create-an-azure-account/4-multiple-subscriptions).

If you do not yet have a resource group, create a new one. 

<img src="/docs/images/3_resource_group.png" width="550" height="450">

Now name your storage account (needs to be globally unique), select your region (should be East), performance should usually be standard, and then for redundancy leave the default, but feel free to review the options Microsoft provides [here](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy).
Feel free to review the rest of the options starting with `Next: Advanced`, but in most cases the defaults will be fine. Click **Review**.

<img src="/docs/images/4_name_resource_group.png" width="550" height="450">

Click **Create**

<img src="/docs/images/5_click_create.png" width="550" height="600">

## 2. Create a container

Within a Storage Account, data lives within containers, which you can kind of think of as folders. In one sense then, the Storage Account is like an external hard drive, and then containers are the folders on the drive.
To create a container, first click **containers** on the left menu bar. 

<img src="/docs/images/6_click_containers.png" width="550" height="600">

Now click the **+Container** icon, name your container (leave it private), and then click **Create**.

<img src="/docs/images/7_create_new_container.png" width="550" height="350">

## 3. Create SAS Token

SAS stands for shared access signatures, which allow you to access private containers from outside the azure environment. 

From within the container, click **Shared access tokens** on the left hand menu. 

<img src="/docs/images/8_SAS.png" width="550" height="450">

We recommend on this page you select **Account key** for the first option, but the rest are up to you depending what you are trying to do. View more info on SAS keys at this [Microsoft page](https://learn.microsoft.com/en-us/rest/api/storageservices/delegate-access-with-shared-access-signature). Make sure you grant sufficient permissions! The default is only 'READ' but you will need at least 'LIST' and probably a few others.

Once you click generate, copy the **Blob SAS URL**. We will need this for file copy paths.

Now we have a secure path to copy data in and out of the container. The format Microsoft uses is as follows: 

`https://<source-storage-account-name>.blob.core.windows.net/<container-name>/<blob-path>?<SAS-token>`

## 4. Copy data in and out

Usually you want to move data with Microsoft's command line tool called [azcopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10).

It should be installed on an Azure VM, but if you are moving from a Linux cluster or your laptop, install using conda/mamba using `mamba install -c conda-forge azcopy`. You can also download the executable [here](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10#download-azcopy).

Now, you can run use azcopy to move data as desired. See [these docs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits) for more details.

One example would be: 

`azcopy copy test.txt "https://<source-storage-account-name>.blob.core.windows.net/<container-name>/test.txt?<SAS-token>"`

You may or may not need the double quotes around the URL, on a Mac you will need the double quotes. 






