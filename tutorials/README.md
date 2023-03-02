# Microsoft Azure Tutorial Resources

---------------------------------
## Overview of Page Contents

+ [Genomics on Azure](#bio)
+ [Clinical Informatics](#ci)
+ [GWAS](#gwas)
+ [BLAST](#blast)
+ [Medical Imaging](#mi)
+ [RNAseq](#rna)
+ [scRNAseq](#sc)
+ [Long Read Sequencing Analysis](#long)
+ [AI/ML Pipeline](#ai)
+ [Open Data](#open)

## **Microsoft Genomics** <a name="bio"></a>

Microsoft has genomics-related offerings that will be useful to many Cloud Lab users. For a broad overview, visit the [Microsof Genomics Community site](https://microsoft.github.io/Genomics-Community/index.html). You can also get an overview of different execution options from [this blog](https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/genomic-workflow-managers-on-microsoft-azure/ba-p/3747052), and a detailed analysis for Nextflow with AWS Batch at [this blog](https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/rna-sequencing-analysis-on-azure-using-nextflow-configuration/ba-p/3738854). We highlight a few key services here: 
+ [Genomics Notebooks](https://github.com/microsoft/genomicsnotebook): These example notebooks highlight many common use cases in genomics research.
+ [Cromwell on Azure](https://github.com/microsoft/CromwellOnAzure): Documentation on how to spin up the resources needed to run Cromwell on Azure. 
+ [Microsoft Genomics](https://learn.microsoft.com/en-us/azure/genomics/quickstart-run-genomics-workflow-portal): Run BWA and GATK using this managed service.
+ [Nextflow on Azure](https://microsoft.github.io/Genomics-Community/mydoc_nextflow.html): Run Nextflow workflows using Azure Batch. 

 ## **Clinical Informatics with FHIR** <a name="ci"></a>
 Azure Health Data Services is a set of services that enables you to store, process, and analyze medical data in Microsoft Azure. These services are designed to help organizations quickly connect disparate health data sources and formats, such as structured, imaging, and device data, and normalize it to be persisted in the cloud. At its core, Azure Health Data Services possesses the ability to transform and ingest data into FHIR (Fast Healthcare Interoperability Resources) format. This allows you to transform health data from legacy formats, such as HL7v2 or CDA, or from high-frequency IoT data in device proprietary formats to FHIR. This makes it easier to connect data stored in Azure Health Data Services with services across the Azure ecosystem, like Azure Synapse Analytics, and Azure Machine Learning (Azure ML).

Azure Health Data Services includes support for multiple health data standards for the exchange of structured data, and the ability to deploy multiple instances of different service types (FHIR, DICOM, and MedTech) that seamlessly work with one another. Services deployed within a workspace also share a compliance boundary and common configuration settings. The product scales automatically to meet the varying demands of your workloads, so you spend less time managing infrastructure and more time generating insights from health data. 

Copying healthcare data stored in Azure FHIR Server to Synapse Analytics allows researchers to leverage a cloud-scale data warehousing and analytics tool to extract insights from their data as well as build scalable research pipelines. 
For information on how to perform this export and downstream analytics, please visit [this repository](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/healthcare-apis/fhir/copy-to-synapse.md). 

You can also see hands-on examples of using [FHIR on Azure](https://github.com/microsoft/genomicsnotebook/tree/main/fhirgenomics), but note that you will need to supply your own VCF files as these are not provided in the tutorial content. 

## **Genome Wide Association Studies** <a name="gwas"></a>
+ Need to update a GWAS notebook for Azure
Genome wide association studies, or GWAS, are statistical analyses that look for associations between genomic variants and phenotypic traits.
- This [NIH CFDE written tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud
) walks you through running a simple GWAS using EC2. The tutorials asks you to select the Ohio region, make sure you change your region to N. Virginia otherwise you will have network issues. Note that the CFDE page has a few other bioinformatics related tutorials like BLAST and Illumina read simulation. We also converted the GWAS tutorial to a simplified [notebook version](/tutorials/notebooks/GWAS) if you prefer that format. See our [notebook guide](/docs/Jupyter_notebook.md) for help with that.

## **NCBI BLAST** <a name="blast"></a>
The NCBI Basic Local Alignment Search Tool (BLAST) find regions of similarity between input sequences. 
- [This Microsoft Blog](https://techcommunity.microsoft.com/t5/azure-high-performance-computing/running-ncbi-blast-on-azure-performance-scalability-and-best/ba-p/2410483) explains how to optimize BLAST analyses on Azure virtual machines. 


## **Medical Imaging Analysis** <a name="mi"></a>
Microsoft Azure offers cloud-based medical imaging analysis capabilities through its Azure Healthcare APIs and Azure Medical Imaging solutions. Azure's DICOM Service allows for the secure storage, management, and processing of medical images in the cloud, using industry standard DICOM (Digital Imaging and Communications in Medicine) format. The DICOM Service provides features like high availability, disaster recovery, and scalable storage options, making it an ideal solution for pipelines that need to store, manage, and analyze large amounts of medical imaging data. In addition, the server integrates with other Azure services like Azure Machine Learning, facilitating the use of advanced machine learning algorithms for image analysis tasks such as object detection, segmentation, and classification. Read about how to deploy the service [here](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/deploy-dicom-services-in-azure).

Microsoft has several medical imaging notebooks that showcase different medical imaging use-cases on Azure Machine Learning. These notebooks demonstrate various data science techniques such as manual model development with PyTorch, automated machine learning, and MLOPS-based examples for automating the machine learning lifecycle in medical use cases, including retraining.
These notebooks are available [here](https://github.com/Azure/medical-imaging).

For Cloud Lab users interested in multi-modal clinical informatics, DICOMcast provides the ability to synchronize data from a DICOM service to a FHIR service, allowing users to integrate clinical and imaging data. DICOMcast expands the use cases for health data by supporting both a streamlined view of longitudinal patient data and the ability to effectively create cohorts for medical studies, analytics, and machine learning. For more information on how to utilize DICOMcast please visit Microsoft’s [documentation](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/dicom-cast-overview) or the open-source [GitHub repository](https://github.com/microsoft/dicom-server/blob/main/docs/quickstarts/deploy-dicom-cast.md).

For users hoping to train deep learning models on imaging data, InnerEye-DeepLearning (IE-DL) is a toolbox that Microsoft developed for easily training deep learning models on 3D medical images. Simple to run both locally and in the cloud with AzureML, it allows users to train and run inference on the following:
•	Segmentation models.
•	Classification and regression models.
•	Any PyTorch Lightning model, via a bring-your-own-model setup.
This project exists in a separate GitHub repository available to [here](https://github.com/microsoft/InnerEye-DeepLearning).

## **RNAseq** <a name="rna"></a>
RNAseq is a technique for quantifying gene levels of gene expression across the genome. 

- You can run this [Nextflow on Azure tutorial](https://microsoft.github.io/Genomics-Community/mydoc_nextflow.html) for RNAseq a variety of ways on Azure. Following the instructions outlined above, you could use Virtual Machines, Azure Machine Learning, or Azure Batch. 
- For a notebook version of a complete RNAseq pipeline from Fastq to Salmon quantification from the King Lab of the University of Maine INBRE use this [notebook](/tutorials/notebooks/rnaseq-myco-tutorial-main), which we re-wrote to work on Azure. You can also use any of Ben King's excellent [notebooks](https://github.com/NIGMS/RNAseqUM) as well, but they are originally written for GCP.

## **Single Cell RNAseq** <a name="sc"></a>
Single Cell RNAseq (scRNAseq) analyses allow for gene expression profiling at the single cell level.
**Any Microsoft resources for scRNAseq?**
**Test these NVIDIA notebooks to see how well they work on Azure**
-  This [NVIDIA blog](https://developer.nvidia.com/blog/accelerating-single-cell-genomic-analysis-using-rapids/) details how to run an accelerated scRNAseq pipeline using RAPIDS. You can find a link to the GitHub that has lots of example notebooks [here](https://github.com/clara-parabricks/rapids-single-cell-examples). For each example use case they show some nice benchmarking data with time and cost for each machine type. You will see that most runs cost less than $1.00 with GPU machines. If you want a CPU version that users Scanpy you can use this [notebook](https://github.com/clara-parabricks/rapids-single-cell-examples/blob/master/notebooks/hlca_lung_cpu_analysis.ipynb). Pay careful attention to the environment setup as there are a lot of dependencies for these notebooks. Create a conda environment in the terminal, then run the notebook. Consider using [mamba](https://github.com/mamba-org/mamba) to speed up environment creation. We created a [guide](/docs/create_conda_env.md) for conda environment set up as well.

## **Long Read Sequence Analysis** <a name="long"></a>
Long read DNA sequence analysis involves analyzing sequencing reads typically longer than 10 thousand base pairs (bp) in length, compared with short read sequencing where reads are about 150 bp in length.
Oxford Nanopore has a pretty complete offering of notebook tutorials for handling long read data to do a variety of things including variant calling, RNAseq, Sars-Cov-2 analysis and much more. Access the notebooks [here](https://labs.epi2me.io/nbindex/). These notebooks expect you are running locally and accessing the epi2me notebook server. To run them in Cloud Lab, skip the first cell that connects to the server and then the rest of the notebook should run correctly, with a few tweaks. If you are just looking to try out notebooks, don't start with these. If you are interested in long read sequence analysis, then some troubleshooting may be needed to adapt these to the Cloud Lab environment. You may even need to rewrite them in a fresh notebook by adapting the commands. Feel free to reach out to our support team for help.

## **AI/ML Pipelines** <a name="ai"></a>
Artificial intelligence and machine learning algorithms are being applied to a variety of biomedical research questions, ranging from image classification to genomic variant calling. [Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning) provides a cloud service for accelerating and managing the machine learning project lifecycle. You can use it to train and deploy models, and manage MLOps. 

The Federated Learning paradigm gained a lot of interest in the healthcare community, because it enables model training on all available data, without sharing data between institutions. NVIDIA Flare is a domain-agnostic, open-source and extensible SDK for federated learning. A separate [GitHub repository](https://github.com/Azure/medical-imaging/tree/main/federated-learning) describes how NVIDIA Flare can be run on Azure.


## **Open Data** <a name="open"></a>
These publicly available datasets can save you time on data discovery and preparation by being curated and ready to use in your workflows.
+ The [COVID-19 Data Lake](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-covid-19-data-lake) contains COVID-19 related datasets from various sources. It covers testing and patient outcome tracking data, social distancing policy, hospital capacity and mobility. 
+ In response to the COVID-19 pandemic, the Allen Institute for AI has partnered with leading research groups to prepare and distribute the [COVID-19 Open Research Dataset (CORD-19)](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-covid-19-open-research?tabs=azure-storage). This dataset is a free resource of over 47,000 scholarly articles, including over 36,000 with full text, about COVID-19 and the coronavirus family of viruses for use by the global research community. This dataset mobilizes researchers to apply recent advances in natural language processing to generate new insights in support of the fight against this infectious disease.
+ [The Genomics Data Lake](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-genomics-data-lake) provides various public datasets that you can access for free and integrate into your genomics analysis workflows and applications. The datasets include genome sequences, variant info, and subject/sample metadata in BAM, FASTA, VCF, CSV file formats: [Illumina Platinum Genomes](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-illumina-platinum-genomes), [Human Reference Genomes](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-human-reference-genomes), [ClinVar Annotations](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-clinvar-annotations), [SnpEff](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-snpeff), [Genome Aggregation Database (gnomAD)](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-gnomad), [1000 Genomes](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-1000-genomes), [OpenCravat](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-open-cravat), [ENCODE](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-encode), [GATK Resource Bundle](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-gatk-resource-bundle).
