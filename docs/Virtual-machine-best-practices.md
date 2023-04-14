# Guide to Azure Virtual Machine Best Practices

The roles granted to Azure Cloud Lab subscribers have been reduced to protect the NIH network.  To have the best experience when provisioning Virtual Machines (VM's), follow these best practices to avoid any validation errors, and thus review and correction of VM configuration.

Best Practices for provisioning VM's include:
- [Guide to Azure Virtual Machine Best Practices](#guide-to-azure-virtual-machine-best-practices)
  - [Ensure the "Delete with VM" checkbox is checked on the Disks page](#ensure-the-delete-with-vm-checkbox-is-checked-on-the-disks-page)
  - [Virtual Network Configurations](#virtual-network-configurations)
  - [Configure your VMs to autoshutdown"](#configure-your-vms-to-autoshutdown)
  - [VM Validations](#vm-validations)

## Ensure the "Delete with VM" checkbox is checked on the Disks page<a name="disks"></a>
After using the VM, you may want to deprovision and create another or start over.  To ensure the VM and it's child resources get deleted, check the "Delete with VM" box. This ensures orphaned disks don't remain in your subscription consuming cost inadvertently.  This is available at VM provisioning time, on the Disks tab.
Conversely, if you choose to keep your disks even after VM deprovisioning, then "uncheck" the box.
<img src="/docs/images/VM-Disks.png" width="1111" height="1375">


## Virtual Network Configurations<a name="vnet"></a>
Due to controls around using the NIH Azure network, settings will be predefined for your CloudLab subscription.  
These will available at VM provisioning time, on the Networking tab.  

 - Please use the Provided Virtual Network (vNet)
 - Change "Public IP" to "None"
 - Use the provided Network Security Group (NSG)
 - Select "Delete public IP and NIC when VM is deleted"
   - After using the VM, you may want to deprovision and create another or start over.  To ensure the VM and it's child resources get deleted, check the "Delete public IP and NIC when the VM is deleted.  This is available at VM provisioning time, on the Networking tab.
<img src="/docs/images/VM-Networking.png" width="1098" height="1377">


## Configure your VMs to autoshutdown"<a name="autoshutdown"></a>
Depending on the workload, you may not want to have your VM running 24 hours a day, 7 days a week.  In this case it's a good practice to use the built in autoshutdown in Azure to power down the VM at a certain time, every day, if running.  If the VM is not running, nothing will happen.
You can find the STRIDES GitHub guide [here](/docs/auto-shutdown-instance.md).
This is available at VM provisioning time, on the Management tab.
<img src="/docs/images/VM-Autoshutdown.png" width="1048" height="1366">


## VM Validations<a name="validation"></a>
If all configurations are good, you should get a successful validation test in Green.  If there are errors that you need to correct, you will get a "Validation Failed" in red.
<img src="/docs/images/VM-ValidationPassed.png" width="1105" height="1381">


If there are errors that you need to correct, you will get a "Validation Failed" in red and you will not be able to proceed until you correct the issues.  Click on the "Click here to view details" to get additional information.
<img src="/docs/images/VM-ValidationFailed.png" width="1044" height="1366">