{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6a915517-3267-4d98-839b-dc7be4dd31f9",
   "metadata": {},
   "source": [
    "# Initiating Jupyter Notebook on Azure GenAI Cloud Lab\n",
    "****"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dcce65c8-d278-4acc-9327-f79535633831",
   "metadata": {},
   "source": [
    "##### **Skill Level: Beginner**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3453c292-f959-4d3a-be2e-c8fdf000e853",
   "metadata": {},
   "source": [
    "This guide will help you initiate jupyter notebook on Azure environment and to complete the activities in the [GenAI](https://github.com/STRIDES/NIHCloudLabAzure/tree/main/notebooks/GenAI) directory of the NIH Cloud Lab. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7fc0f399-f78f-4917-86e8-187fe23e14e6",
   "metadata": {},
   "source": [
    "### Prerequisites\n",
    "*****"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd2da3d6-862b-4618-bd90-95210b570938",
   "metadata": {},
   "source": [
    "- An active Azure subscription"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07782ce1-1d3c-4032-bf29-ca125d9dd411",
   "metadata": {},
   "source": [
    "In search bar window, type **Azure Machine Learning** and select it"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07d0ca2f-b834-4f6f-a66f-f65b96ce32f9",
   "metadata": {},
   "source": [
    "![JN_1.jpg](/docs/images/JN_1.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "598343a1-4757-4ac6-a1ff-c7db7727f065",
   "metadata": {},
   "source": [
    "In Azure Machine Learning window, select **Create** and select **New workspace**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f853f01a-e721-4c42-b8b2-baf9f9e2099a",
   "metadata": {},
   "source": [
    "![JN_2.jpg](/docs/images/JN_2.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5301f54-42c3-4033-9369-0b6a53f16089",
   "metadata": {},
   "source": [
    "In workspace window, you should be able to see your azure subscription and select resource group that you created"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d700b36f-7f66-4ce1-a096-4f147ad2e96b",
   "metadata": {},
   "source": [
    "![JN_3.jpg](/docs/images/JN_3.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2673cf68-9f72-44b9-af75-e3b0fefc307c",
   "metadata": {},
   "source": [
    "Create **Name** for workspace, select  Region **East US 2**, create **Storage account**, create **Key valut**, create **Application Insights** and click **Review+create**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "573d164f-29a9-49e3-96eb-7ab342158d0f",
   "metadata": {},
   "source": [
    "![JN_4.jpg](/docs/images/JN_4.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1882712c-2e67-4273-872a-edf78d509a39",
   "metadata": {},
   "source": [
    "In workspace window, you should see a message thar **Validation passes** and click **Create**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a165024d-fe55-4306-9ebc-6f4ebcbfbc3a",
   "metadata": {},
   "source": [
    "![JN_5.jpg](/docs/images/JN_5.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6aa933d3-8b24-4fae-bcf8-d6fc1e65dc5f",
   "metadata": {},
   "source": [
    "In workspace window, you should see a url under **Studio web URL** click it."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2974ab0e-8838-4e51-90bf-af019895602d",
   "metadata": {},
   "source": [
    "![JN_6.jpg](/docs/images/JN_6.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d4e1428-3873-49ca-a757-e01526ac99a2",
   "metadata": {},
   "source": [
    "In your create workspace window, select **+New** and then select **Compute instance**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee5cba7d-0b15-492d-9806-982307a05694",
   "metadata": {},
   "outputs": [],
   "source": [
    "![JN_7.jpg](/docs/images/JN_7.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f348b821-9e48-4e3a-bb52-d76ed597f016",
   "metadata": {},
   "source": [
    "In a compute instance window, select **Review+create**, In next windoe select **Create**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66fe8fe0-596c-4af0-9d79-552a4ded9311",
   "metadata": {},
   "source": [
    "![JN_8.jpg](/docs/images/JN_8.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "675db6e2-0f05-4050-9d91-de70a66b48be",
   "metadata": {},
   "source": [
    "![JN_9.jpg](/docs/images/JN_9.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87a751bc-2641-44b7-ba5e-d5227925994a",
   "metadata": {},
   "source": [
    "It will take few mintues to create instance. Once instance is ready, you would see window like below. In this window, select **JupyterLab**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3648bb54-dfae-47dc-9686-eea5860dbebb",
   "metadata": {},
   "source": [
    "![JN_10.jpg](/docs/images/JN_10.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bf6b8d0a-522b-484b-8ecd-af5ce2cdfb76",
   "metadata": {},
   "source": [
    "From GitHub tutorial library, download your interest of python script"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d35ed00f-1e0c-419d-9349-1c7440860eb8",
   "metadata": {},
   "source": [
    "![JN_11.jpg](/docs/images/JN_11.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e122399-ddde-4fdb-91b9-32cbe4478e72",
   "metadata": {},
   "source": [
    "Upload your downloaded python script into **JupyterLab** window and now you are ready to run python script"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "056236dc-ca84-43e3-b022-4fbeb9ffffb6",
   "metadata": {},
   "source": [
    "![JN_12.jpg](/docs/images/JN_12.jpg)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10 - SDK v2",
   "language": "python",
   "name": "python310-sdkv2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.20"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
