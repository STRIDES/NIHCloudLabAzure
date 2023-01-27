Instructions for deploying Kubeflow
    
    Prerequisites
        - install [kubectl](https://kubernetes.io/docs/tasks/tools/#install-kubectl-on-linux)
        - Install and configure [Azure Command Line Interface](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
            -log in with az login
        -Install Docker
            - For Windows and WSL [Guide](https://docs.docker.com/desktop/windows/wsl/)
            - For other OS [Docker Desktop](https://docs.docker.com/docker-hub/)

    

Azure Setup 
    -To log into Azure from the command line interface, run the following commands
        -az login
        -az account set --subscription <NAME OR ID OF SUBSCRIPTION>

    Create a resource group (if neccessary)
        -az group create -n <RESOURCE_GROUP_NAME> -l <LOCATION>


    Create a specifically defined cluster:
        -az aks create -g <RESOURCE_GROUP_NAME> -n <NAME> -s <AGENT_SIZE> -c <AGENT_COUNT> -l <LOCATION> --generate-ssh-keys



KubeFlow installation
    -Create user credentials. You only need to run this command once.
        -az aks get-credentials -n <NAME> -g <RESOURCE_GROUP_NAME>

    -Download the kfctl v1.2.0 release from the [Kubeflow releases page](https://github.com/kubeflow/kfctl/releases/tag/v1.2.0)

    -Unpack the tar ball
        -tar -xvf kfctl_v1.2.0_<platform>.tar.gz
        
