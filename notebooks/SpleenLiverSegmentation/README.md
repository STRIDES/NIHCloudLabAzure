# Spleen Segmentation Example using NVIDIA Models and MONAI
_We have put together a training example that segments the Spleen in 3D CT Images._

## Introduction
Two pre-trained models from NVIDIA are used in this training, a Spleen model . 
The Spleen model is additionally retrained on the medical decathlon spleen dataset: [http://medicaldecathlon.com/](http://medicaldecathlon.com/)
Data is not necessary to be downloaded to run the notebook. The notebook downloads the data during it's run.
The notebook uses the Python package [MONAI](https://monai.io/), the Medical Open Network for Artificial Intelligence. 

- Spleen Model - [monai_spleen_ct_segmentation_V0.5.3](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_spleen_ct_segmentation)

## Outcomes
After following along with this notebook the user will be familiar with:
- Downloading public datasets using MONAI
- Using MONAI transformations for training
- Downloading a pretrained NVIDIA Clara model using MONAI
- Retrain model using MONAI
- Visualizing medical images in python/matplotlib

## Installing MONAI
Please follow the [instructions](https://monai.io/started.html#installation) on MONAI's website for up to date install.
Installing MONAI in a notebook environment can be completed with the commands:
- !python -c "import monai" || pip install -q 'monai[all]'
- !python -c "import matplotlib" || pip install -q matplotlib

## Dependencies
_It is recommended to use an NVIDIA GPU for training. If the user does not have access to a NVIDIA GPU then it is recommended to skip the training cells._

The following packages and versions were installed during the testing of this notebook:
- MONAI version: 1.3.0
- Numpy version: 1.23.5
- Pytorch version: 1.12.0
- ITK version: 5.3.0
- Nibabel version: 5.2.1
- scikit-image version: 0.21.0
- scipy version: 1.10.1
- Pillow version: 8.2.0
- Tensorboard version: 2.11.2
- gdown version: 4.7.3
- TorchVision version: 0.13.0
- tqdm version: 4.65.0
- lmdb version: 1.4.1
- psutil version: 5.9.0
- pandas version: 2.0.2
- einops version: 0.7.0
- transformers version: 4.21.3
- mlflow version: 2.11.3
- pynrrd version: 1.0.0
- clearml version: 1.14.5rc0