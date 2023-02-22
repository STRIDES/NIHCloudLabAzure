# Microsoft Azure Tutorial Resources

---------------------------------
## Overview of Page Contents

+ [Microsoft Genomics](#bio)
+ [Clinical Informatics](#ci)
+ [Download SRA Data](#sra)
+ [GWAS](#gwas)
+ [Medical Imaging](#mi)
+ [RNAseq](#rna)
+ [scRNAseq](#sc)
+ [Long Read Sequencing Analysis](#long)
+ [AI/ML Pipeline](#ai)
+ [Open Data](#open)

## **Microsoft Genomics** <a name="bio"></a>

https://microsoft.github.io/Genomics-Community/index.html

Cromwell on Azure https://github.com/microsoft/CromwellOnAzure
The common workflows for Cromwell can be found here https://github.com/microsoft/CromwellOnAzure#run-common-workflows

How to interact with genomics tool https://learn.microsoft.com/en-us/azure/genomics/quickstart-run-genomics-workflow-portal

**needed updates**
+ We need to add a description here about MS Genomics
+ Need to update autoshutdown docs for the disclaimer below
+ Are there service quotas in Azure Cloud Lab?  
 
 **Please note, GPU machines cost more than most CPU machines, so be sure to shut these machines down after use, or use the auto shutdown feature [lifecycle configuration](/docs/auto-shutdown-instance.md). You may also encounter service quotas to protect you from the accidental use of expensive machine types. If that happens, and you still want to use a certain instance type, follow these [instructions](/docs/service_quotas.md).**
 
 ## **Clinical Informatics with FHIR** <a name="ci"></a>
 Azure Health Data Services is a set of services that enables you to store, process, and analyze medical data in Microsoft Azure. These services are designed to help organizations quickly connect disparate health data sources and formats, such as structured, imaging, and device data, and normalize it to be persisted in the cloud. 
At its core, Azure Health Data Services possesses the ability to transform and ingest data into FHIR (Fast Healthcare Interoperability Resources) format. This allows you to transform health data from legacy formats, such as HL7v2 or CDA, or from high-frequency IoT data in device proprietary formats to FHIR. This makes it easier to connect data stored in Azure Health Data Services with services across the Azure ecosystem, like Azure Synapse Analytics, and Azure Machine Learning (Azure ML).
Azure Health Data Services includes support for multiple health data standards for the exchange of structured data, and the ability to deploy multiple instances of different service types (FHIR, DICOM, and MedTech) that seamlessly work with one another. Services deployed within a workspace also share a compliance boundary and common configuration settings. The product scales automatically to meet the varying demands of your workloads, so you spend less time managing infrastructure and more time generating insights from health data. 
Leveraging Azure Synapse Analytics to Analyze EHR Data
Copying healthcare data stored in Azure FHIR Server to Synapse Analytics allows researchers to leverage a cloud-scale data warehousing and analytics tool to extract insights from their data as well as build scalable research pipelines. 
For information on how to perform this export and downstream analytics, please visit this repository. 
![image](https://user-images.githubusercontent.com/102973993/220756340-bb6e6afc-9211-4fcd-97c9-9ac9ffc5f99f.png)


## **Download Data From the Sequence Read Archive (SRA)** <a name="sra"></a>
+ We need to update this with an updated d
Next Generation genetic sequence data is housed in the NCBI Sequence Read Archive (SRA). You can access these data using the SRA Toolkit. We walk you through this using [this notebook](/tutorials/notebooks/SRADownload), which also walks you through how to set up and search Athena tables tp generate an accession list. You can also read [this guide](https://www.ncbi.nlm.nih.gov/sra/docs/sra-aws-download/) for more information on available dataset tables.

## **Genome Wide Association Studies** <a name="gwas"></a>
+ Need to update a GWAS notebook for Azure
Genome wide association studies, or GWAS, are statistical analyses that look for associations between genomic variants and phenotypic traits.
- This [NIH CFDE written tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud
) walks you through running a simple GWAS using EC2. The tutorials asks you to select the Ohio region, make sure you change your region to N. Virginia otherwise you will have network issues. Note that the CFDE page has a few other bioinformatics related tutorials like BLAST and Illumina read simulation. We also converted the GWAS tutorial to a simplified [notebook version](/tutorials/notebooks/GWAS) if you prefer that format. See our [notebook guide](/docs/Jupyter_notebook.md) for help with that.

## **Medical Imaging Analysis** <a name="mi"></a>
+Need to add imaging analysis

https://github.com/Azure/medical-imaging

Medical imaging analysis requires the analysis of large image files and often requires elastic storage and accelerated computing.
- Most medical imaging analyses are done using notebooks, so we would recommend accessing this [Jupyter Notebook](/tutorials/notebooks/SpleenLiverSegmentation) and cloning it into SageMaker. The tutorial walks through image segmentation.
- AWS has a nice intro to Machine Learning in a SageMaker notebook that predicts breast cancer from features extracted from image data, which walks you through both image analysis and some of the ML functionality of SageMaker, the notebook is found [here](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_applying_machine_learning/breast_cancer_prediction/Breast%20Cancer%20Prediction.ipynb).
- You can also view this [AWS blog](https://aws.amazon.com/blogs/machine-learning/annotate-dicom-images-and-build-an-ml-model-using-the-monai-framework-on-amazon-sagemaker/) on how to annotate DICOM images and build a custom AI model with the data.
- You can learn to deidentify medical images following this AWS [tutorial](https://aws.amazon.com/blogs/machine-learning/de-identify-medical-images-with-the-help-of-amazon-comprehend-medical-and-amazon-rekognition/).

## **RNAseq** <a name="rna"></a>
RNAseq is a technique for quantifying gene levels of gene expression across the genome. 
**Update how to run on Azure**
- You can run this [Nextflow on Azure tutorial](https://microsoft.github.io/Genomics-Community/mydoc_nextflow.html) for RNAseq a variety of ways on Azure. Following the instructions outlined above, you could use Virtual Machines, Azure Machine Learning, or Azure Batch. for more information on Microsoft Genomics check [here](/docs/Genomics_Workflows.md).
- **Test this notebook in Azure ML**
- For a notebook version of a complete RNAseq pipeline from Fastq to Salmon quantification from the King Lab of the University of Maine INBRE use this [notebook](/tutorials/notebooks/rnaseq-myco-tutorial-main), which we re-wrote to work on AWS. You can also use any of Ben King's excellent [notebooks](https://github.com/King-Laboratory/rnaseq-myco-notebook) as well, but they are originally written for GCP.

## **Single Cell RNAseq** <a name="sc"></a>
Single Cell RNAseq (scRNAseq) analyses allow for gene expression profiling at the single cell level.
**Any Microsoft resources for scRNAseq?**
**Test these NVIDIA notebooks to see how well they work on Azure**
-  This [NVIDIA blog](https://developer.nvidia.com/blog/accelerating-single-cell-genomic-analysis-using-rapids/) details how to run an accelerated scRNAseq pipeline using RAPIDS. You can find a link to the GitHub that has lots of example notebooks [here](https://github.com/clara-parabricks/rapids-single-cell-examples). For each example use case they show some nice benchmarking data with time and cost for each machine type. You will see that most runs cost less than $1.00 with GPU machines. If you want a CPU version that users Scanpy you can use this [notebook](https://github.com/clara-parabricks/rapids-single-cell-examples/blob/master/notebooks/hlca_lung_cpu_analysis.ipynb). Pay careful attention to the environment setup as there are a lot of dependencies for these notebooks. Create a conda environment in the terminal, then run the notebook. Consider using [mamba](https://github.com/mamba-org/mamba) to speed up environment creation. We created a [guide](/docs/create_conda_env.md) for conda environment set up as well.

## **Long Read Sequence Analysis** <a name="long"></a>
Long read DNA sequence analysis involves analyzing sequencing reads typically longer than 10 thousand base pairs (bp) in length, compared with short read sequencing where reads are about 150 bp in length.
Oxford Nanopore has a pretty complete offering of notebook tutorials for handling long read data to do a variety of things including variant calling, RNAseq, Sars-Cov-2 analysis and much more. Access the notebooks [here](https://labs.epi2me.io/nbindex/).  These notebooks expect you are running locally and accessing the epi2me notebook server. To run them in Cloud Lab, skip the first cell that connects to the server and then the rest of the notebook should run correctly, with a few tweaks. If you are just looking to try out notebooks, don't start with these. If you are interested in long read sequence analysis, then some troubleshooting may be needed to adapt these to the Cloud Lab environment. You may even need to rewrite them in a fresh notebook by adapting the commands. Feel free to reach out to our support team for help.

## **AI/ML Pipelines** <a name="ai"></a>
**Need to update to azure ML language**
Artificial intelligence and machine learning algorithms are being applied to a variety of biomedical research questions, ranging from image classification to genomic variant calling. AWS is moving all AI/ML workflows to SageMaker, the Juptyer notebook platform we have used a few times already. AWS has a very general tutorial [here](https://aws.amazon.com/getting-started/hands-on/build-train-deploy-machine-learning-model-sagemaker/) on how to build out an AI pipeline on Sagememaker. You can also look at the [breast cancer tutorial](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_applying_machine_learning/breast_cancer_prediction/Breast%20Cancer%20Prediction.ipynb) from the imaging section above for a more applied example. 
You can also submit a training job to SageMaker, and have your final model uploaded to S3 using [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#train-a-model-with-pytorch), [Tensorflow](https://docs.aws.amazon.com/sagemaker/latest/dg/tf.html) or [Apache MXNet](https://docs.aws.amazon.com/sagemaker/latest/dg/mxnet.html).

## **Open Data** <a name="open"></a>
**Update to Azure Open Data Content**
AWS has a lot of public data that you can integrate into your testing or use in your own research. You can access these datasets at the [Registry of Open Data on AWS](https://registry.opendata.aws/). There you can click on any of the datasets to view the S3 path to the data, as well as publications that have used those data and tutorials if available. To demonstrate, we can click the [gnomad dataset](https://registry.opendata.aws/broad-gnomad/), then get the S3 path and view the files at the command line by pasting `https://registry.opendata.aws/broad-gnomad/`. 
