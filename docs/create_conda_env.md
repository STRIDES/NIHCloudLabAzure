# Creating a conda environment on a Virtual Machine 

## 1. Create a conda environment

### Install mamba
```
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
bash Mambaforge-$(uname)-$(uname -m).sh -b -p $HOME/mambaforge
```

### Export to Path
`export PATH="$HOME/mambaforge/bin:$PATH"`

From within a notebook you can add Mamba to path with 
```
import os
os.environ["PATH"] += os.pathsep + os.environ["HOME"]+"/Mambaforge/bin"
```

### Create and activate the environment
`mamba create -n vcftools -c bioconda vcftools ipykernel -y`

You can also create the environment using a yaml file like this: `mamba env create -f environment.yml`

`source activate vcftools`
