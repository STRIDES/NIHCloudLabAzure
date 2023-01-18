

>This repository falls under the NIH STRIDES Initiative. STRIDES aims to harness the power of the cloud to accelerate biomedical discoveries. To learn more, visit https://cloud.nih.gov. 

# NIH Cloud Lab for Azure
---------------------------------

The sheer quantity of resources available to learn Azure can quickly become overwhelming. NIH Cloud Lab’s goal is to make cloud easy and accessible for you, so that you can spend less time on administrative tasks and focus more on your research.

Use this repository to learn about how to use Azure by exploring the linked resources and walking through the tutorials. If you are a beginner, we suggest you begin with this jumpstart section. If you already have foundational knowledge of Azure and cloud, feel free to skip ahead to the [tutorials](/tutorials/) section for in-depth examples of how to run specific workflows such as genomic variant calling and medical image analysis.

## Overview of Page Contents

+ [Getting Started](#GS)
+ [Overview](#OV)
+ [Command Line Tools](#CLI)
+ [Azure Marketplace](#MARK)
+ [Ingest and Store Data](#STO)
+ [Virtual Machines](#VM)
+ [Disk Images](#IM)
+ [Azure Machine learning](#SAG)
+ [Creating a Conda Environment](#CO)
+ [Managing Containers and Code Repositories](#DOCK)
+ [Clusters](#CLU)
+ [Billing and Benchmarking](#BB)
+ [Cost Optimization](#COST)
+ [Getting Support](#SUP)
+ [Additional Training](#TR)

## **Getting Started** <a name="GS"></a>
You can learn a lot of what is possible on Azure in the Azure Getting Started [Tutorials Page](https://azure.microsoft.com/en-us/get-started/) and we recommend you go there and explore some of the tutorials on offer. Nonetheless, it can be hard to know where to start if you are new to the cloud. To help you, we thought through some of the most common tasks you will encounter doing cloud-enabled research, and gathered tutorials and guides specific to those topics. We hope the following materials are helpful as you explore cloud-based research. 

## **Overview** <a name="OV"></a>
There are three primary ways you can run analyses using Azure: using **Virtual Machines**, **Jupyter Notebook instances**, and **Serverless services**. We give a breif overview of each of these here and go into more detail in the sections below. [Virtual Machines](https://azure.microsoft.com/en-us/products/virtual-machines/) are like desktop computers, but you access them through the cloud console and you get to pick the operating system and the specs such as CPU and memory. In Azure, these virtual machines are also called Virtual Machines or VMs for short. Jupyter Notebook instances are virtual machines with a preconfigured Jupyter Lab. On Azure these are run through [Azure Machine Learning](https://azure.microsoft.com/en-us/products/machine-learning/#product-overview), which is also Azure's ML/AI platform. You decide what kind of virtual machine you want to 'spin up' and then you can run Juptyer notebooks on that virtual machine. Finally, Serverless services are services that allow you to run things, an analysis, an app, a website, and not have to deal with your own servers (VMs). There are still servers running somewhere, you just don't have to manage them. All you have to do is call a command that runs your analysis in the background, and copies the output files to a storage bucket. 

## **Command Line Tools** <a name="CLI"></a>
Most tasks in Azure can be done without the command line, but the command line tools will generally make your life easier in the long run. Command line interface (CLI) tools are those that you use directly in a terminal/shell as opposed to clicking within the Azure portals graphical user interface (GUI). The primary tool you will need is the Azure CLI, which will allow you to interact with Virtual Machines (VMs) or Storage Accounts (see below) from your local terminal. Instructions for the CLI can be found [here](https://learn.microsoft.com/en-us/cli/azure/). If you are unable to install locally, you can use all the CLI commands from within VM and Machine Learning instances, or from the [Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview).

To install and configure Azure CLI, redirect to [Get started with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli), which provides detailed instructions on installation as well as documentation on common Azure ClI commands. Microsoft Azure also has a cloud native service called [Microsoft Genomics](https://www.microsoft.com/en-us/genomics/) which offers cloud implementation of the Burrows-Wheeler Aligner (BWA) and the Genome Analysis Toolkit (GATK) for secondary analysis. The service is ISO-certified and compliant with HIPAA regulations, and offers price predictability for your genome sequencing needs. Find documentatation on how to use Microsoft Genomics [here](https://learn.microsoft.com/en-us/azure/genomics/overview-what-is-genomics)

## **Azure Marketplace** <a name="MARK"></a>
The [Microsoft Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/) is an online store in Azure that contains thousands of IT software applications and services by industry leading companies to fit your business needs. [Azure CycleCloud](https://learn.microsoft.com/en-us/azure/cyclecloud/?view=cyclecloud-8) is a service designed to provide organizations secure and flexible cloud HPV and Big Compute environments

## **Ingest and Store Data using Azure Storage Accounts** <a name="STO"></a>
Microsofts object storage solution for the cloud is Azure Blob. Blob is the equivalent to Amazon's S3 block storage service, and is optimized for storing massive amounts of unstructured data. Azure also offers many different storage services listed [here](https://azure.microsoft.com/en-us/products/category/storage/). To get started you must create a [Storage Account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal)


## **Virtual Machines** <a name="VM"></a>
Virtual machines (VMs) on Azure can be accessed via SSH or from the Azure portal. More information on Vms can be found [here](https://azure.microsoft.com/en-us/products/virtual-machines/#overview) as well as [guide](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/ssh-from-windows) on how to use SSH keys with windows in Azure. To view the different types of VMs availabe in Azure check out the [Virtual Machine Series](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/) 


## **Disk Images** <a name="IM"></a>
Part of the power of virtual machines is that they offer a blank slate for you to configure as desired. [Azure VM Image Builder](https://azure.microsoft.com/en-us/products/image-builder/#overview) simplifies the image building process allowing for custom built images to be saved.

## **Launch a Machine Learning Workspace** <a name="SAG"></a>
[Azure Machine Learning studio](https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning) is one of the preferred tools whne using Azure Machine learning. ML studion allows for you to run your own code in managed jupyter notebooks. Foll the [Quickstart](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-run-notebooks) page to begin running Jupyter Notebooks in studio.


## **Creating a Conda Environment** <a name="CO"></a>
Virtual environments allow you to manage package versions without having package conflicts. For example, if you needed Python 3 for one analysis, but Python 2.7 for another, you could create separate environments to use the two versions of Python. One of the most popular package managers used for creating virtual environments is the [conda package manager](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html#:~:text=A%20conda%20environment%20is%20a,NumPy%201.6%20for%20legacy%20testing). 


## **Managing Containers with Azure Container Registry** <a name="DOCK"></a>
You can host containers within Azure Container Registry. We outline how to build a container, push to Azure Container Registry, and pull to a compute environment in our [docs](/docs/ecr.md).


## **Clusters** <a name="CLU"></a>
One great thing about the cloud is its ability to scale with demand. When you submit a job to a traditional cluster, you specify up front how many CPUs and memory you want to give to your job, and you may over or under utilize these resources. With managed resources like serverless and clusters you can leverage a feature called autoscaling, where the compute resources will scale up or down with the demand. This is more efficient and keeps costs down when demand is low, but prevents latency when demand is high (think about workshop participants all submitting jobs at the same time to a cluster). For most users of Cloud Lab, the best way to leverage scaling is to use Azure Batch, but in some cases, maybe for a whole lab group or large project, it may make sense to spin up a [Kubernetes cluster](https://azure.microsoft.com/en-us/products/kubernetes-service/). Azure Cycle cloud has [tutorials](https://learn.microsoft.com/en-us/azure/cyclecloud/tutorials/tutorial?view=cyclecloud-8) on cluster creation 

## **Billing and Benchmarking** <a name="BB"></a>
Many Cloud Lab users are interested in understanding how to estimate the price of a large scale project using a reduced sample size. Generally, you should be able to benchmark with a few representative samples to get an idea of time and cost required for a larger scale project. Follow our [Cost Management Guide](/docs/billing_and_cost_management.md) to see how to tag specific resources for workflow benchmarking. 

In terms of cost, the best way to estimate costs is to use the Azure pricing calculator [here](https://azure.microsoft.com/en-us/pricing/calculator/) for an initial figure, which is a pricing tool that forcasts costs based on products and useage. Then, you can run some benchmarks and double check that everything is acting as you expect..

## **Cost Optimization** <a name="COST"></a>
Azure related cost management guide

## **Getting Support** <a name="SUP"></a>
 As part of your participation in Cloud Lab you will be added to the Cloud Lab Teams channel where you can chat with other Cloud Lab users, and gain support from the Cloud Lab team. For NIH Intramural users, you can submit a support ticket to Service Now.

## **Additional Training** <a name="TR"></a>
This repo only scratches the surface of what can be done in the cloud. If you are interested in additional cloud training opportunities please visit the [STRIDES Training page](https://cloud.nih.gov/training/). For more information on the STRIDES Initiative at the NIH, visit [our website](https://cloud.nih.gov) or contact the NIH STRIDES team at STRIDES@nih.gov for more information.

