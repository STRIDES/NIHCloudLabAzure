# Microsoft Azure Tutorial Resources

---------------------------------
## Overview of Page Contents

+ [Artificial Intelligence](#ai)
+ [Clinical Informatics](#ci)
+ [Medical Imaging](#mi)
+ [Genomics on Azure](#bio)
+ [GWAS](#gwas)
+ [BLAST](#blast)
+ [VCF Query](#vcf)
+ [RNAseq](#rna)
+ [scRNAseq](#sc)
+ [Long Read Sequencing Analysis](#long)
+ [Open Data](#open)

## **Artificial Intelligence** <a name="ai"></a>
Machine learning is a subfield of artificial intelligence that focuses on the development of algorithms and models that enable computers to learn from and make predictions or decisions based on data, without being explicitly programmed. Artificial intelligence and machine learning algorithms are being applied to a variety of biomedical research questions, ranging from image classification to genomic variant calling. Azure offers AI services through the Azure AI Studio, as well as Azure Machine Learning.

See our suite of tutorials to learn more about [Gen AI on Azure](/tutorials/notebooks/GenAI/) that go over several Azure products such as [Azure AI Studio](/tutorials/notebooks/GenAI/Azure_AI_Studio_README.md), [Azure OpenAI](/tutorials/notebooks/GenAI/Azure_Open_AI_README.md) and [Azure AI Search](/tutorials/notebooks/GenAI/notebooks/Azure_Pubmed_chatbot.ipynb) and other tools like [Langchain](/tutorials/notebooks/GenAI/notebooks/AzureOpenAI-langchain.ipynb) to deploy, train, prompt, and implement techniques like [Retrieval-Augmented Generation (RAG)](/tutorials/notebooks/GenAI/notebooks/Azure_Pubmed_chatbot.ipynb) to GenAI models.

 ## **Clinical Informatics with FHIR** <a name="ci"></a>
 Azure Health Data Services is a set of services that enables you to store, process, and analyze medical data in Azure. These services are designed to help organizations quickly connect disparate health data sources and formats, such as structured, imaging, and device data, and normalize it to be persisted in the cloud. At its core, Azure Health Data Services possesses the ability to transform and ingest data into FHIR (Fast Healthcare Interoperability Resources) format. This allows you to transform health data from legacy formats, such as HL7v2 or CDA, or from high-frequency IoT data in device proprietary formats to FHIR. This makes it easier to connect data stored in Azure Health Data Services with services across the Azure ecosystem, like Azure Synapse Analytics, and Azure Machine Learning (Azure ML).

Azure Health Data Services includes support for multiple health data standards for the exchange of structured data, and the ability to deploy multiple instances of different service types (FHIR, DICOM, and MedTech) that seamlessly work with one another. Services deployed within a workspace also share a compliance boundary and common configuration settings. The product scales automatically to meet the varying demands of your workloads, so you spend less time managing infrastructure and more time generating insights from health data. 

Copying healthcare data stored in Azure FHIR Server to Synapse Analytics allows researchers to leverage a cloud-scale data warehousing and analytics tool to extract insights from their data as well as build scalable research pipelines. 
For information on how to perform this export and downstream analytics, please visit [this repository](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/healthcare-apis/fhir/copy-to-synapse.md). 

You can also see hands-on examples of using [FHIR on Azure](https://github.com/microsoft/genomicsnotebook/tree/main/fhirgenomics), but note that you will need to supply your own VCF files as these are not provided with the tutorial content.

## **Medical Imaging Analysis** <a name="mi"></a>
Medical imaging analysis requires the analysis of large image files and often requires elastic storage and accelerated computing. Microsoft Azure offers cloud-based medical imaging analysis capabilities through its Azure Healthcare APIs and Azure Medical Imaging solutions. Azure's DICOM Service allows for the secure storage, management, and processing of medical images in the cloud, using industry standard DICOM (Digital Imaging and Communications in Medicine) format. The DICOM Service provides features like high availability, disaster recovery, and scalable storage options, making it an ideal solution for pipelines that need to store, manage, and analyze large amounts of medical imaging data. In addition, the server integrates with other Azure services like Azure ML, facilitating the use of advanced machine learning algorithms for image analysis tasks such as object detection, segmentation, and classification. Read about how to deploy the service [here](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/deploy-dicom-services-in-azure).

Microsoft has several medical imaging notebooks that showcase different medical imaging use-cases on Azure Machine Learning. These notebooks demonstrate various data science techniques such as manual model development with PyTorch, automated machine learning, and MLOPS-based examples for automating the machine learning lifecycle in medical use cases, including retraining.
These notebooks are available [here](https://github.com/Azure/medical-imaging). Make sure you select a kernel that includes Pytorch else the install of dependencies can be challenging. Note also that you need to use a GPU VM for most of the notebook cells, but you can create several compute environments and switch between them as needed. Be sure to shut them off when you are finished.

For Cloud Lab users interested in multi-modal clinical informatics, DICOMcast provides the ability to synchronize data from a DICOM service to a FHIR service, allowing users to integrate clinical and imaging data. DICOMcast expands the use cases for health data by supporting both a streamlined view of longitudinal patient data and the ability to effectively create cohorts for medical studies, analytics, and machine learning. For more information on how to utilize DICOMcast please visit Microsoft’s [documentation](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/dicom-cast-overview) or the open-source [GitHub repository](https://github.com/microsoft/dicom-server/blob/main/docs/quickstarts/deploy-dicom-cast.md).

For users hoping to train deep learning models on imaging data, InnerEye-DeepLearning (IE-DL) is a toolbox that Microsoft developed for easily training deep learning models on 3D medical images. Simple to run both locally and in the cloud with Azure Machine Learning, it allows users to train and run inference on the following:
•	Segmentation models
•	Classification and regression models
•	Any PyTorch Lightning model, via a bring-your-own-model setup
This project exists in a separate [GitHub repository](https://github.com/microsoft/InnerEye-DeepLearning).

## **Microsoft Genomics** <a name="bio"></a>
Microsoft has several genomics-related offerings that will be useful to many Cloud Lab users. For a broad overview, visit the [Microsoft Genomics Community site](https://microsoft.github.io/Genomics-Community/index.html). You can also get an overview of different execution options from [this blog](https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/genomic-workflow-managers-on-microsoft-azure/ba-p/3747052), and a detailed analysis for Nextflow with AWS Batch at [this blog](https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/rna-sequencing-analysis-on-azure-using-nextflow-configuration/ba-p/3738854). We highlight a few key services here: 
+ [Genomics Notebooks](https://github.com/microsoft/genomicsnotebook): These example notebooks highlight many common use cases in genomics research. The Bioconductor/Rstudio notebook will not work in Cloud Lab. To run Rstudio, look at [Posit Workbench from the Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/rstudio-5237862.rstudioserverprostandard). 
+ [Cromwell on Azure](https://github.com/microsoft/CromwellOnAzure): Documentation on how to spin up the resources needed to run Cromwell on Azure. Note that this service will not work within Cloud Lab because you need high-level permissions, but we list it here for demonstration purposes.
+ [Microsoft Genomics](https://learn.microsoft.com/en-us/azure/genomics/quickstart-run-genomics-workflow-portal): Run BWA and GATK using this managed service. Note that it uses Python 2.7 and thus is not compatible with AzureML (which uses Python 3), but you can run it from any other shell environment.
+ [Nextflow on Azure](https://microsoft.github.io/Genomics-Community/mydoc_nextflow.html): Run Nextflow workflows using Azure Batch. 
+ [NVIDIA Parabricks for Secondary Genomics Analysis on Azure](https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/benchmarking-the-nvidia-clara-parabricks-for-secondary-genomics/ba-p/3722434). Follow this guide to run Parabricks on a VM by pulling the Docker container directly from NVIDIA.

## **Genome Wide Association Studies** <a name="gwas"></a>
Genome-wide association studies (GWAS) are large-scale investigations that analyze the genomes of many individuals to identify common genetic variants associated with traits, diseases, or other phenotypes.
- This [NIH CFDE written tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud
) walks you through running a simple GWAS on AWS, thus we converted it to Azure in [this notebook](/tutorials/notebooks/GWAS). Note that the CFDE page has a few other bioinformatics related tutorials like BLAST and Illumina read simulation. 
- This blog post [illustrates some of the costs associated](https://techcommunity.microsoft.com/t5/azure-high-performance-computing/azure-to-accelerate-genome-wide-analysis-study/ba-p/2644120) with running GWAS on Azure

## **NCBI BLAST+** <a name="blast"></a>
NCBI BLAST (Basic Local Alignment Search Tool) is a widely used bioinformatics program provided by the National Center for Biotechnology Information (NCBI) that compares nucleotide or protein sequences against a large database to identify similar sequences and infer evolutionary relationships, functional annotations, and structural information.
- [This Microsoft Blog](https://techcommunity.microsoft.com/t5/azure-high-performance-computing/running-ncbi-blast-on-azure-performance-scalability-and-best/ba-p/2410483) explains how to optimize BLAST analyses on Azure VMs. Feel free to install BLAST+ on a VM or an AzureML notebook and run queries there.

## **Query a VCF file in Azure Synapse** <a name="vcf"></a>
- You can use SQL to rapidly query a VCF file in Azure Synapse. The requires converting the file from VCF to Parquet format, a common format for databases. Read more about how to do this in Azure on [this Microsoft blog](https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/genomic-data-in-parquet-format-on-azure/ba-p/3150554). Although the notebooks for this tutorial are bundled with the other genomics notebooks, to get them to work you will need to use Azure Databricks or Synapse Analytics, not AzureML. 

## **RNAseq** <a name="rna"></a>
RNA-seq analysis is a high-throughput sequencing method that allows the measurement and characterization of gene expression levels and transcriptome dynamics. Workflows are typically run using workflow managers, and final results can often be visualized in notebooks.
- You can run this [Nextflow on Azure tutorial](https://microsoft.github.io/Genomics-Community/mydoc_nextflow.html) for RNAseq a variety of ways on Azure. Following the instructions outlined above, you could use Virtual Machines, Azure Machine Learning, or Azure Batch. 
- For a notebook version of a complete RNAseq pipeline from Fastq to Salmon quantification from the NIGMS Sandbox Program use this [notebook](/tutorials/notebooks/rnaseq-myco-tutorial-main), which we re-wrote to work on Azure.

## **Single Cell RNAseq** <a name="sc"></a>
Single-cell RNA sequencing (scRNA-seq) is a technique that enables the analysis of gene expression at the individual cell level, providing insights into cellular heterogeneity, identifying rare cell types, and revealing cellular dynamics and functional states within complex biological systems.
-  This [NVIDIA blog](https://developer.nvidia.com/blog/accelerating-single-cell-genomic-analysis-using-rapids/) details how to run an accelerated scRNAseq pipeline using RAPIDS. You can find a link to the GitHub that has lots of example notebooks [here](https://github.com/clara-parabricks/rapids-single-cell-examples). For each example use case they show some nice benchmarking data with time and cost for CPU vs. GPU machine types on AWS. You will see that most runs cost less than $1.00 with GPU machines (priced on AWS). If you want a CPU version that users Scanpy you can use this [notebook](https://github.com/clara-parabricks/rapids-single-cell-examples/blob/master/notebooks/hlca_lung_cpu_analysis.ipynb). Pay careful attention to the environment setup as there are a lot of dependencies for these notebooks. Create a conda environment in the terminal, then run the notebook. Consider using [mamba](https://github.com/mamba-org/mamba) to speed up environment creation. We created a [guide](/docs/create_conda_env.md) for conda environment set up as well.

## **Long Read Sequence Analysis** <a name="long"></a>
Long read DNA sequence analysis involves analyzing sequencing reads typically longer than 10 thousand base pairs (bp) in length, compared with short read sequencing where reads are about 150 bp in length.
Oxford Nanopore has a pretty complete offering of notebook tutorials for handling long read data to do a variety of things including variant calling, RNAseq, Sars-Cov-2 analysis and much more. Access the notebooks [here](https://labs.epi2me.io/nbindex/) and on [GitHub](https://github.com/epi2me-labs). These notebooks expect you are running locally and accessing the epi2me notebook server. To run them in Cloud Lab, skip the first cell that connects to the server and then the rest of the notebook should run correctly, with a few tweaks. Oxford Nanopore also offers a host of [Nextflow workflows](https://labs.epi2me.io/wfindex/) that will allow you to run a variety of long read pipelines. 

## **Open Data** <a name="open"></a>
These publicly available datasets can save you time on data discovery and preparation by being curated and ready to use in your workflows.
+ The [COVID-19 Data Lake](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-covid-19-data-lake) contains COVID-19 related datasets from various sources. It covers testing and patient outcome tracking data, social distancing policy, hospital capacity and mobility. 
+ In response to the COVID-19 pandemic, the Allen Institute for AI has partnered with leading research groups to prepare and distribute the [COVID-19 Open Research Dataset (CORD-19)](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-covid-19-open-research?tabs=azure-storage). This dataset is a free resource of over 47,000 scholarly articles, including over 36,000 with full text, about COVID-19 and the coronavirus family of viruses for use by the global research community. This dataset mobilizes researchers to apply recent advances in natural language processing to generate new insights in support of the fight against this infectious disease.
+ [The Genomics Data Lake](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-genomics-data-lake) provides various public datasets that you can access for free and integrate into your genomics analysis workflows and applications. The datasets include genome sequences, variant info, and subject/sample metadata in BAM, FASTA, VCF, CSV file formats: [Illumina Platinum Genomes](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-illumina-platinum-genomes), [Human Reference Genomes](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-human-reference-genomes), [ClinVar Annotations](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-clinvar-annotations), [SnpEff](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-snpeff), [Genome Aggregation Database (gnomAD)](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-gnomad), [1000 Genomes](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-1000-genomes), [OpenCravat](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-open-cravat), [ENCODE](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-encode), [GATK Resource Bundle](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-gatk-resource-bundle).
