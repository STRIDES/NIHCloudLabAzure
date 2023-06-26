# Guide to implementing auto-shutdown features in virtual machines in Azure

## Automatic shutdown Azure virtual machine instance

There are 2 main ways to manage shutdowns for your Azure virtual machines.

1. [Auto-Shutdown](#auto-shutdown)
        - This is built into each virtual machine and gives you the ability to set a shutdown time, timezone, and notification options.
  
2. [Start/Stop VMs - Azure Automation](#startstop-vms---azure-automation)
        - This is a solution based on Azure Automation and gives you more flexibility.


### Auto-Shutdown:<a name="AS"></a>
1. First login to Azure Portal
2. Go to virtual machines (or if that option isn't available, use the search bar to find and open virtual machines)
3. Next select a virtual machine
4. Scroll to the Operations section and click Auto-Shutdown
5. Fill in the required details
   - **Enabled:**  Enables/disabled the auto-shutdown
   - **Scheduled shutdown:**  Text box to type the shutdown time (relative to the time zone in next selection)
   - **Time zone:**  Time zone that the Scheduled shutdown time will use
   - **Send notification before auto-shutdown?**  Option to enable/disable notifications prior to shutdown
   - **Webhook URL (optional):**  A notification will be posted to the specified webhook endpoint when the auto-shutdown is about to happen. The endpoint must support incoming TLS 1.2 connections
   - **Email address (optional):**  Provide a set of semicolon-delimited email addresses to receive alert notification emails.
6. Click the "Save" button at the top

![VM Autoshutdown](/docs/images/VirtualMachine-Properties-Autoshutdown.png)
![Autoshutdown options](/docs/images/Auto-shutdown-options.png)






