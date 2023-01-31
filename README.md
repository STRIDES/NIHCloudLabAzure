

>This repository falls under the NIH STRIDES Initiative. STRIDES aims to harness the power of the cloud to accelerate biomedical discoveries. To learn more, visit https://cloud.nih.gov. 

# NIH Cloud Lab for Azure
---------------------------------
NIH Cloud Lab’s goal is to make Cloud easy and accessible for you, so that you can spend less time on administrative tasks and focus more on research.

Use this repository to learn about how to use Azure by exploring the linked resources and walking through the tutorials. If you are a beginner, we suggest you begin with this jumpstart section. If you already have foundational knowledge of Azure and cloud, feel free to skip ahead to the [tutorials](/tutorials/) section for in-depth examples of how to run specific workflows such as genomic variant calling and medical image analysis.

## Overview of Page Contents

+ [Getting Started](#gs)
+ [Overview](#ov)
+ [Command Line Tools](#cli)
+ [Azure Marketplace](#mark)
+ [Ingest and Store Data](#sto)
+ [Virtual Machines](#vm)
+ [Disk Images](#im)
+ [Azure Machine learning](#sag)
+ [Creating a Conda Environment](#co)
+ [Managing Containers and Code Repositories](#dock)
+ [Clusters](#clu)
+ [Billing and Benchmarking](#bb)
+ [Cost Optimization](#cost)
+ [Getting Support](#sup)
+ [Additional Training](#tr)

## **Getting Started** <a name="gs"></a>
You can learn a lot of what is possible on Azure in the Azure Getting Started [Tutorials Page](https://azure.microsoft.com/en-us/get-started/) and we recommend you go there and explore some of the tutorials on offer. Nonetheless, it can be hard to know where to start if you are new to the cloud. To help you, we thought through some of the most common tasks you will encounter doing cloud-enabled research, and gathered tutorials and guides specific to those topics. We hope the following materials are helpful as you explore cloud-based research.

** Add note somwhere about resource groups, what they are and what they are used for and how they relate to VMS and other resource creation. **

## **Overview** <a name="ov"></a>
There are three primary ways you can run analyses using Azure: using **Virtual Machines**, **Jupyter Notebook instances**, and **Serverless services**. We give a breif overview of each of these here and go into more detail in the sections below. [Virtual Machines](https://azure.microsoft.com/en-us/products/virtual-machines/) are like desktop computers, but you access them through the cloud console and you get to pick the operating system and the specifications such as CPU and memory. In Azure, these virtual machines are called VMs for short. Jupyter Notebook instances are virtual machines with a preconfigured Jupyter Lab. On Azure these are run through [Azure Machine Learning](https://azure.microsoft.com/en-us/products/machine-learning/#product-overview), which is also Azure's ML/AI platform. You decide what kind of virtual machine you want to 'spin up' and then you can run Juptyer notebooks on that virtual machine. Finally, Serverless services are services that allow you to run things, an analysis, an app, a website, and not have to deal with your own servers (VMs). There are still servers running somewhere, you just don't have to manage them. All you have to do is call a command that runs your analysis in the background, and copies the output files to a storage bucket. [Azure Batch](https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview) is a common example. 

## **Command Line Tools** <a name="cli"></a>
Most tasks in Azure can be done without the command line, but the command line tools will generally make your life easier in the long run. Command line interface (CLI) tools are those that you use directly in a terminal/shell as opposed to clicking within the Azure portals graphical user interface (GUI). The primary tool you will need is the Azure CLI, which will allow you to interact with Virtual Machines (VMs) or Storage Accounts (see below) from your local terminal. Instructions for the CLI can be found [here](https://learn.microsoft.com/en-us/cli/azure/). If you are unable to install locally, you can use all the CLI commands from within VM and Machine Learning instances, or from the [Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview).

To install and configure Azure CLI, redirect to [Get started with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli), which provides detailed instructions on installation as well as documentation on common Azure ClI commands. Microsoft Azure also has a cloud native service called [Microsoft Genomics](https://www.microsoft.com/en-us/genomics/) which offers cloud implementation of the Burrows-Wheeler Aligner (BWA) and the Genome Analysis Toolkit (GATK) for secondary analysis. The service is ISO-certified and compliant with HIPAA regulations, and offers price predictability for your genome sequencing needs. Find documentatation on how to use Microsoft Genomics [here](https://learn.microsoft.com/en-us/azure/genomics/overview-what-is-genomics)

## **Azure Marketplace** <a name="mark"></a>
The [Microsoft Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/) is an online store in Azure that contains thousands of software applications and services to fit your research needs. For example, you can find VMs configured for Microsoft Genomics or NVIDIA machine learning.

## **Ingest and Store Data using Azure Storage Accounts** <a name="sto"></a>
Microsoft's object storage solution for the cloud is called Azure Blob. Blob is the equivalent to Amazon's S3 block storage service, and is optimized for storing massive amounts of unstructured data. Azure also offers many different storage services listed [here](https://azure.microsoft.com/en-us/products/category/storage/). To get started you must create a [Storage Account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal). Accessing private data in Azure is a bit different than the other cloud providers. See [our documentation](/docs/storage_accounts.md) on how to access public and private data from a storage account. 

**Need to update this storage account doc **

## **Virtual Machines** <a name="vm"></a>
Virtual machines (VMs) on Azure can be accessed via SSH or from the Azure portal. For an overview of Azure Vms go [here](https://azure.microsoft.com/en-us/products/virtual-machines/#overview). Follow these links to see how to specifically spin up a [Windows VM](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/quick-create-portal) and [here](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal?tabs=ubuntu) on how to spin up a Linux VM. To view the different types of VMs availabe in Azure check out the [Virtual Machine Series](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/). 

** Consider removing this Disk Image, or else make sure we test it**

## **Disk Images** <a name="im"></a>
Part of the power of virtual machines is that they offer a blank slate for you to configure as desired. [Azure VM Image Builder](https://azure.microsoft.com/en-us/products/image-builder/#overview) simplifies the image building process allowing for custom built images to be saved.

## **Launch a Machine Learning Workspace** <a name="sag"></a>
[Azure Machine Learning studio](https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning) is one of the preferred tools when using Azure Machine learning. ML studio allows for you to run your own code in managed Jupyter notebooks. Follow the [Quickstart](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-run-notebooks) page to begin running Jupyter Notebooks in studio. Make sure you start by creating a [workspace and a VM](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources).

## **Creating a Conda Environment** <a name="co"></a>
Virtual environments allow you to manage package versions without having package conflicts. For example, if you needed Python 3 for one analysis, but Python 2.7 for another, you could create separate environments to use the two versions of Python. One of the most popular package managers used for creating virtual environments is the [conda package manager](), but you can also use pip to create [virtual Python environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/). 


## **Managing Containers with Azure Container Registry** <a name="dock"></a>
You can host containers within Azure Container Registry. We outline how to build a container, push to Azure Container Registry, and pull to a compute environment in our [docs](/docs/ecr.md).


## **Clusters** <a name="clu"></a>
One great thing about the cloud is its ability to scale with demand. When you submit a job to a traditional cluster, you specify up front how many CPUs and memory you want to give to your job, and you may over or under utilize these resources. With managed resources like serverless and clusters you can leverage a feature called autoscaling, where the compute resources will scale up or down with the demand. This is more efficient and keeps costs down when demand is low, but prevents latency when demand is high (think about workshop participants all submitting jobs at the same time to a cluster). For most users of Cloud Lab, the best way to leverage scaling is to use Azure Batch, but in some cases, maybe for a whole lab group or large project, it may make sense to spin up a [Kubernetes cluster](https://azure.microsoft.com/en-us/products/kubernetes-service/). Azure Cycle cloud has [tutorials](https://learn.microsoft.com/en-us/azure/cyclecloud/tutorials/tutorial?view=cyclecloud-8) on cluster creation 

## **Billing and Benchmarking** <a name="bb"></a>
Many Cloud Lab users are interested in understanding how to estimate the price of a large scale project using a reduced sample size. Generally, you should be able to benchmark with a few representative samples to get an idea of time and cost required for a larger scale project. Follow our [Cost Management Guide](/docs/billing_and_cost_management.md) to see how to tag specific resources for workflow benchmarking. 

In terms of cost, the best way to estimate costs is to use the Azure pricing calculator [here](https://azure.microsoft.com/en-us/pricing/calculator/) for an initial figure, which is a pricing tool that forcasts costs based on products and useage. Then, you can run some benchmarks and double check that everything is acting as you expect..

## **Cost Optimization** <a name="cost"></a>
Follow our [Cost Management Guide](/docs/billing_and_cost_management.md) for details on how to monitor costs, set up budget alerts, and cost-benchmark specific analyses using resource tagging. In addition, here are a few tips to help you stay on budget.

## **Getting Support** <a name="sup"></a>
As part of your participation in Cloud Lab you will be added to the Cloud Lab Teams channel where you can chat with other Cloud Lab users, and gain support from the Cloud Lab team. For NIH Intramural users, you can submit a support ticket to Service Now. For issues related to the cloud environment, feel free to request [Azure Enterprise Support](/docs/request_enterprise_support.md). For issues related to scientific use cases, such as, how can I best run an RNAseq pipeline in Azure, email us at `CloudLab@nih.gov`.

If you have a question about Quota Limits, visit our [documentation](/docs/service_quotas.md) on how to request a limit increase. 

## **Additional Training** <a name="tr"></a>
This repo only scratches the surface of what can be done in the cloud. If you are interested in additional cloud training opportunities please visit the [STRIDES Training page](https://cloud.nih.gov/training/). For more information on the STRIDES Initiative at the NIH, visit [our website](https://cloud.nih.gov) or contact the NIH STRIDES team at STRIDES@nih.gov for more information.

