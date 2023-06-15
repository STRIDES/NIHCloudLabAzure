

>This repository falls under the NIH STRIDES Initiative. STRIDES aims to harness the power of the cloud to accelerate biomedical discoveries. To learn more, visit https://cloud.nih.gov. 

# NIH Cloud Lab for Azure
---------------------------------
NIH Cloud Lab’s goal is to make Cloud easy and accessible for you, so that you can spend less time on administrative tasks and focus more on research.

Use this repository to learn about how to use Azure by exploring the linked resources and walking through the tutorials. If you are a beginner, we suggest you begin with this jumpstart section. If you already have foundational knowledge of Azure and Cloud, feel free to skip ahead to the [tutorials](/tutorials/) section for in-depth examples of how to run specific workflows such as genomic variant calling and medical image analysis.

## Overview of Page Contents
+ [Getting Started](#gs)
+ [Overview](#ov)
+ [Resource Groups](#rg)
+ [Command Line Tools](#cli)
+ [Azure Marketplace](#mark)
+ [Ingest and Store Data](#sto)
+ [Virtual Machines](#vm)
+ [Azure Functions](#vm)
+ [Disk Images](#disk)
+ [Azure Machine Learning](#sag)
+ [Clusters](#clu)
+ [Creating a Conda Environment](#co)
+ [Azure Container Registry](#con)
+ [GitHub](#gh)
+ [Billing and Benchmarking](#bb)
+ [Cost Optimization](#cost)
+ [Getting Support](#sup)
+ [Additional Training](#tr)

## **Getting Started** <a name="gs"></a>
You can learn a lot of what is possible on Azure in the Azure Getting Started [Tutorials Page](https://azure.microsoft.com/en-us/get-started/) and we recommend you go there and explore some of the tutorials on offer. Nonetheless, it can be hard to know where to start if you are new to the cloud. To help you, we thought through some of the most common tasks you will encounter doing cloud-enabled research, and gathered tutorials and guides specific to those topics. We hope the following materials are helpful as you explore using Azure! 

## **Overview** <a name="ov"></a>
There are three primary ways you can run analyses using Azure: using **Virtual Machines**, **Jupyter Notebook instances**, and **Managed services**. We give a brief overview of each of these here and go into more detail in the sections below. [Virtual Machines](https://azure.microsoft.com/en-us/products/virtual-machines/) are like desktop computers, but you access them through the cloud console and you get to pick the operating system and the specifications such as CPU and memory. In Azure, these virtual machines are called VMs for short. Jupyter Notebook instances are virtual machines with a preconfigured Jupyter Lab. On Azure these are run through [Azure Machine Learning](https://azure.microsoft.com/en-us/products/machine-learning/#product-overview), which is also Azure's ML/AI platform. You decide what kind of virtual machine you want to 'spin up' and then you can run Juptyer notebooks on those virtual machines. Finally, Serverless services are services that allow you to run things, an analysis, an app, a website, and not have to deal with your own servers (VMs). There are still servers running somewhere, you just don't have to manage them. All you have to do is call a command that runs your analysis in the background, and copies the output files to a storage account. [Azure Batch](https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview) is a common example. 

## **Resource Groups** <a name="rg"></a>
A resource group is a container that holds related resources for an Azure solution. The resource group can include all the resources for the solution, or only those resources that you want to manage as a group. You decide how you want to allocate resources to resource groups based on what makes the most sense for your use case. Generally, add resources that share the same lifecycle to the same resource group so you can easily deploy, update, and delete them as a group. Each resource group stores metadata about the underlying resources. Therefore, when you specify a location for the resource group, you are specifying where that metadata is stored. For compliance reasons, you may need to ensure that your data is stored in a particular region.

To see more information on how to manage resource groups, visit our docs about [Managing Resource Groups](/docs/resource_groups.md).

## **Command Line Tools** <a name="cli"></a>
Most tasks in Azure can be done without the command line, but the command line tools will generally make your life easier in the long run. Command line interface (CLI) tools are those that you use directly in a terminal/shell as opposed to clicking within the Azure portal's graphical user interface (GUI). The primary tool you will need is the Azure CLI, which will allow you to interact with Virtual Machines (VMs) or Storage Accounts (see below) from your local terminal. Instructions for the CLI can be found [here](https://learn.microsoft.com/en-us/cli/azure/). If you are unable to install locally, you can use all the CLI commands from within VM and Machine Learning instances, or from the [Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview).

To install and configure Azure CLI, redirect to [Get started with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli), which provides detailed instructions on installation as well as documentation on common Azure CLI commands. Microsoft Azure also has a cloud native service called [Microsoft Genomics](https://www.microsoft.com/en-us/genomics/) which offers cloud implementation of the Burrows-Wheeler Aligner (BWA) and the Genome Analysis Toolkit (GATK) for secondary analysis. Find documentation on how to use Microsoft Genomics [here](https://learn.microsoft.com/en-us/azure/genomics/overview-what-is-genomics).

## **Azure Marketplace** <a name="mark"></a>
The [Microsoft Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/) is an online store in Azure that contains thousands of software applications and services to fit your research needs. For example, you can find VMs configured for Microsoft Genomics or NVIDIA machine learning. Within Cloud Lab, the most common use case for the Marketplace will likely be [CycleCloud](https://learn.microsoft.com/en-us/azure/cyclecloud/tutorials/tutorial?view=cyclecloud-8), which is Azure's High Performance Computing solution. If interested in CycleCloud, please contact us at `CloudLab@nih.gov` so we can help set this up in your Cloud Lab account.

## **Ingest and Store Data using Azure Storage Accounts** <a name="sto"></a>
Microsoft's object storage solution for the cloud is called Azure Blob. Blob is optimized for storing massive amounts of unstructured data. Azure also offers many other storage solutions listed [here](https://azure.microsoft.com/en-us/products/category/storage/). To get started you must create a [Storage Account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal). Users can grant limited access to Azure storage resources using [Shared Access Signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)(SAS). You can also read our guide to Storage Accounts and moving data in and out of Cloud Lab [here](/docs/create_storage_account.md). This [Microsoft guide](https://microsoft.github.io/Genomics-Community/mydoc_data_migration.html) for moving genomic data is also very helpful.

## **Virtual Machines** <a name="vm"></a>
Virtual machines (VMs) on Azure can be accessed via SSH or from the Azure portal. More information on VMs can be found [here](https://azure.microsoft.com/en-us/products/virtual-machines/#overview) as well as this [guide](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/ssh-from-windows) on how to use SSH keys with windows in Azure. To view the different types of VMs available in Azure check out the [Virtual Machine Series](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/). 

You can also spin up preconfigured VMs, such as the Azure Data Science VM, which has many data science tools preinstalled and may save you time on environment set up. Read more in [our docs](/docs/Azure_Data_Science_VMs.md).

Also, for best VM provisioning experience, please see this link for VM best practices in [our docs](/docs/Virtual-machine-best-practices.md).

## **Azure Functions** <a name="vm"></a>
Azure Functions is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. Instead of worrying about deploying and maintaining servers, the cloud infrastructure provides all the up-to-date resources needed to keep your applications running. For more information click [here](https://learn.microsoft.com/en-us/azure/azure-functions/). In general, you can consider functions for automating workflows.

## **Disk Images** <a name="disk"></a>
Part of the power of virtual machines is that they offer a blank slate for you to configure as desired. [Azure VM Image Builder](https://azure.microsoft.com/en-us/products/image-builder/#overview) simplifies the image building process allowing for custom built images to be saved. You can later redeploy these images to spin up a new machine with data or environments already installed.

## **Launch a Machine Learning Workspace (Jupyter Environment)** <a name="sag"></a>
[Azure Machine Learning studio](https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning) is Azure's ML/AI solution. ML studio allows for you to run your own code in managed Jupyter notebooks. Follow the [Quickstart](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-run-notebooks) page to begin running Jupyter Notebooks in studio. Note that you will need to start and stop your compute environment, which is run separately from the notebook. Once in the AzureML portal, go to compute, then you can select Jupyter, Notebooks, or VS Code, which means a lot of flexibility in the way you utilize the compute environment.

The Azure file share account of your Azure Machine Learning workspace is mounted as a drive on the compute instance. This drive is the default working directory for Jupyter, Jupyter Labs, RStudio, and Posit Workbench. This means that the notebooks and other files you create in Jupyter, JupyterLab, RStudio, or Posit are automatically stored on the file share and available to use in other compute instances as well.

If you are running complex ML models, look at this Microsoft [blog post](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/azureml-observability-a-scalable-and-extensible-solution-for-ml/ba-p/3474066) for an overview of Microsoft's overvability solution. The source code is [here](https://github.com/microsoft/AzureML-Observability).

## **Clusters** <a name="clu"></a>
One great thing about the cloud is its ability to scale with demand. When you submit a job to a traditional cluster, you specify up front how many CPUs and memory you want to give to your job, and you may over- or under-utilize these resources. With managed resources like serverless and clusters you can leverage a feature called autoscaling, where the compute resources will scale up or down with demand. This is more efficient and keeps costs down when demand is low, but prevents latency when demand is high (think about workshop participants all submitting jobs at the same time to a cluster). For most users of Cloud Lab, the best way to leverage scaling is to use Azure Batch, but in some cases, maybe for a whole lab group or large project, it may make sense to spin up a [Kubernetes cluster](https://azure.microsoft.com/en-us/products/kubernetes-service/). 

If you are interested in using a more traditional scheduler like SLURM or Sun Grid Engine, you can use Azure CycleCloud, which has an easy to use GUI as well as CLI options. If interested in CycleCloud, please contact us at `CloudLab@nih.gov` and we will provision a CycleCloud instance for you.

## **Creating a Conda Environment** <a name="co"></a>
Virtual environments allow you to manage package versions without having package conflicts. For example, if you needed Python 3 for one analysis, but Python 2.7 for another, you could create separate environments to use the two versions of Python. One of the most popular package managers used for creating virtual environments is the [conda package manager](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html#:~:text=A%20conda%20environment%20is%20a,NumPy%201.6%20for%20legacy%20testing). We also made a quick guide that you can reference [here](/docs/create_conda_env.md)

## **Managing Containers with Azure Container Registry** <a name="con"></a>
You can host or pull containers with Azure Container Registry. See [Microsoft's documentation](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli) on how to use this service.

## **GitHub** <a name="gh"></a>
GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere. This [tutorial](https://docs.github.com/en/get-started/quickstart/hello-world) teaches you GitHub essentials like repositories, branches, commits, and pull requests. You'll create your own Hello World repository and learn GitHub's pull request workflow, a popular way to create and review code. Since Microsoft owns GitHub, it integrates nicely with Azure.

## **Billing and Benchmarking** <a name="bb"></a>
Many Cloud Lab users are interested in understanding how to estimate the price of a large-scale project using a reduced sample size. Generally, you should be able to benchmark with a few representative samples to get an idea of time and cost required for a larger scale project. Follow our [Cost Management Guide](/docs/billing_and_cost_management.md) to see how to tag specific resources for workflow benchmarking. 

In terms of cost, the best way to estimate costs is to use the Azure pricing calculator [here](https://azure.microsoft.com/en-us/pricing/calculator/) for an initial figure, which is a pricing tool that forecasts costs based on products and usage. Then, you can run some benchmarks and double check that everything is acting as you expect. See [our docs](/docs/Using_The_Azure_Price_Calculator.md) on best practices for using this tool.

## **Cost Optimization** <a name="cost"></a>
Follow our [Cost Management Guide](/docs/billing_and_cost_management.md) for details on how to monitor costs, set up budget alerts, and cost-benchmark specific analyses using resource tagging. In addition, here are a few tips to help you stay on budget. You can also configure auto-shutdown on your VM instances following [this guide](/docs/auto-shutdown-instance.md) to prevent you from accidentally leaving instances running.

## **Getting Support** <a name="sup"></a>
As part of your participation in Cloud Lab you will be added to the Cloud Lab Teams channel where you can chat with other Cloud Lab users, and gain support from the Cloud Lab team. For NIH Intramural users, you can submit a support ticket to Service Now. For issues related to the cloud environment, feel free to request [Azure Enterprise Support](/docs/request_enterprise_support.md). For issues related to scientific use cases, such as, `how can I best run an RNAseq pipeline in Azure?`, email us at `CloudLab@nih.gov`.

## **Additional Training** <a name="tr"></a>
This repo only scratches the surface of what can be done in the cloud. If you are interested in additional cloud training opportunities, please visit the [STRIDES Training page](https://cloud.nih.gov/training/). For more information on the STRIDES Initiative at the NIH, visit [our website](https://cloud.nih.gov) or contact the NIH STRIDES team at STRIDES@nih.gov for more information.

