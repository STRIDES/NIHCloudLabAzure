# Instructions for deploying Kubeflow
    
    Prerequisites
        - install [kubectl](https://kubernetes.io/docs/tasks/tools/#install-kubectl-on-linux)
        - Install and configure [Azure Command Line Interface](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
            -log in with az login
        -Install Docker
            - For Windows and WSL [Guide](https://docs.docker.com/desktop/windows/wsl/)
            - For other OS [Docker Desktop](https://docs.docker.com/docker-hub/)

    

# Azure Setup

To log into Azure from the command line interface, run the following commands
```
az login
az account set --subscription <NAME OR ID OF SUBSCRIPTION>
```
Create a resource group (if neccessary)
```
az group create -n <RESOURCE_GROUP_NAME> -l <LOCATION>
```

Create a specifically defined cluster:
```
az aks create -g <RESOURCE_GROUP_NAME> -n <NAME> -s <AGENT_SIZE> -c <AGENT_COUNT> -l <LOCATION> --generate-ssh-keys
```


# KubeFlow installation

Create user credentials. You only need to run this command once.
```
az aks get-credentials -n <NAME> -g <RESOURCE_GROUP_NAME>
```
Download the kfctl v1.2.0 release from the [Kubeflow releases page](https://github.com/kubeflow/kfctl/releases/tag/v1.2.0)

Unpack the tar ball.
```
tar -xvf kfctl_v1.2.0_<platform>.tar.gz
```
Run the following commands to set up and deploy Kubeflow in order. The code below includes an optional command to add the binary  kfctl to your path. If you don’t add the binary to your path, you must use the full path to the kfctl binary each time you run it.

```
export PATH=$PATH:"<path-to-kfctl>

export KF_NAME=<your choice of name for the Kubeflow deployment>

export BASE_DIR=<path to a base directory>
        
export KF_DIR=${BASE_DIR}/${KF_NAME}

export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.2-branch/kfdef/kfctl_k8s_istio.v1.2.0.yaml"

mkdir -p ${KF_DIR}
cd ${KF_DIR}
kfctl apply -V -f ${CONFIG_URI}
```

Run this command to check that the resources have been deployed correctly in namespace kubeflow:
    
```
kubectl get all -n kubeflow
```

Open the KubeFlow Dashboard , the default installation does not create an external endpoint but you can use port-forwarding to visit your cluster. Run the following command:
    
```
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
```
Next, open http://localhost:8080 in your browser.
