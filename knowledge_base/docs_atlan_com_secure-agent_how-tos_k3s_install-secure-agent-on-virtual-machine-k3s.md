# Install on Virtual Machine (K3s)
(source: https://docs.atlan.com/secure-agent/how-tos/k3s/install-secure-agent-on-virtual-machine-k3s#troubleshooting)

Secure AgentManage AgentK3sInstall on Virtual Machine (K3s)AWS EKSConfigure workflow executionReferencesDeployment architectureSecurity

Manage AgentK3sInstall on Virtual Machine (K3s)AWS EKSConfigure workflow execution

K3sInstall on Virtual Machine (K3s)

Install on Virtual Machine (K3s)

AWS EKS

Configure workflow execution

ReferencesDeployment architectureSecurity

Deployment architecture

Security

Connect data

Secure Agent

Manage Agent

K3s

Install on Virtual Machine (K3s)

Secure Agent installation can be done by a non-root user. Root access isonlyneeded for setting up system prerequisites before installation.

This page provides instructions for installing the Secure Agent on a virtual machine (VM) by deployingK3s in a rootless execution mode.



## System requirementsâ
(source: https://docs.atlan.com/secure-agent/how-tos/k3s/install-secure-agent-on-virtual-machine-k3s#troubleshooting)

Before installing the Secure Agent, ensure that the virtual machine (VM) meets the following requirements:

At least 80GB of available disk space.

A Linux-based OS running on an amd64 (x86_64) architecture withsystemdenabled.

systemd

The Secure Agent requires the following ports for internal services. Ensure these ports are open and accessible:Kubernetes API:6443Internal K3s proxy:10443,10080MinIO storage:9000,32075MinIO console:9001,30614Traefik ingress:31037,32547

Kubernetes API:6443

6443

Internal K3s proxy:10443,10080

10443

10080

MinIO storage:9000,32075

9000

32075

MinIO console:9001,30614

9001

30614

Traefik ingress:31037,32547

31037

32547



## Prerequisitesâ
(source: https://docs.atlan.com/secure-agent/how-tos/k3s/install-secure-agent-on-virtual-machine-k3s#troubleshooting)

Before installing the Secure Agent, complete the following setup steps to prepare your Atlan tenant and virtual machine.



### Configure Atlan tenantâ
(source: https://docs.atlan.com/secure-agent/how-tos/k3s/install-secure-agent-on-virtual-machine-k3s#troubleshooting)

In Atlan, complete the following steps to configure the tenant:

Sign in to your tenant as an Atlan admin.

From the left menu of any screen, clickAdmin.

UnderWorkspaceclickLabs.

Navigate toWorkflow Center.

Enable theCrawl assets using Secure Agenttoggle.



### Configure virtual machineâ
(source: https://docs.atlan.com/secure-agent/how-tos/k3s/install-secure-agent-on-virtual-machine-k3s#troubleshooting)

On the virtual machine, complete the following steps to configure it:

Log in as a root user.

Log in as a root user.

Create the required directory to configure cgroup delegation with:sudo mkdir -p /etc/systemd/system/[email protected]

Create the required directory to configure cgroup delegation with:

sudo mkdir -p /etc/systemd/system/[email protected]

sudo mkdir -p /etc/systemd/system/[email protected]

Use the belowcatcommand to create the delegation file with required configuration:cat <<EOF | sudo tee /etc/systemd/system/[email protected]/delegate.conf[Service]Delegate=cpu cpuset io memory pidsEOF

Use the belowcatcommand to create the delegation file with required configuration:

cat

cat <<EOF | sudo tee /etc/systemd/system/[email protected]/delegate.conf[Service]Delegate=cpu cpuset io memory pidsEOF

cat <<EOF | sudo tee /etc/systemd/system/[email protected]/delegate.conf[Service]Delegate=cpu cpuset io memory pidsEOF

Use the below command to reload systemd:sudo systemctl daemon-reload && sudo reboot

Use the below command to reload systemd:

sudo systemctl daemon-reload && sudo reboot

sudo systemctl daemon-reload && sudo reboot

To keep the Secure Agent running after logout, the root user must enable service persistence for the user installing it by running the following command:sudo loginctl enable-linger ``<user_installing_secure_agent>``Replace<user_installing_secure_agent>with the actual username of the user installing the Secure Agent.

To keep the Secure Agent running after logout, the root user must enable service persistence for the user installing it by running the following command:

sudo loginctl enable-linger ``<user_installing_secure_agent>``

sudo loginctl enable-linger ``<user_installing_secure_agent>``

Replace<user_installing_secure_agent>with the actual username of the user installing the Secure Agent.

<user_installing_secure_agent>

Run the following commands to enable IP forwarding so Secure Agent can communicate with other Secure Agent instances and make network requests to the Atlan tenant.IPv4 forwarding:sudo sysctl -w net.ipv4.ip_forward=1IPv6 forwarding:sudo sysctl -w net.ipv6.conf.all.forwarding=1

Run the following commands to enable IP forwarding so Secure Agent can communicate with other Secure Agent instances and make network requests to the Atlan tenant.

IPv4 forwarding:sudo sysctl -w net.ipv4.ip_forward=1

IPv4 forwarding:

sudo sysctl -w net.ipv4.ip_forward=1

sudo sysctl -w net.ipv4.ip_forward=1

IPv6 forwarding:sudo sysctl -w net.ipv6.conf.all.forwarding=1

IPv6 forwarding:

sudo sysctl -w net.ipv6.conf.all.forwarding=1

sudo sysctl -w net.ipv6.conf.all.forwarding=1

To manage containerized workloads, install fuse-overlayfs with:sudo yum install fuse-overlayfs

To manage containerized workloads, install fuse-overlayfs with:

sudo yum install fuse-overlayfs

sudo yum install fuse-overlayfs

The VM must have access to the source systemâs secret manager to retrieve secrets. For more information, see how to provide access for some popular secret managers listed below:AWS:Configure access for AWS Secrets Manager.Azure:Configure access for Azure Key Vault.GCP:Configure access for GCP Secret Manager.

The VM must have access to the source systemâs secret manager to retrieve secrets. For more information, see how to provide access for some popular secret managers listed below:

AWS:Configure access for AWS Secrets Manager.

Azure:Configure access for Azure Key Vault.

GCP:Configure access for GCP Secret Manager.



## Permissions requiredâ
(source: https://docs.atlan.com/secure-agent/how-tos/k3s/install-secure-agent-on-virtual-machine-k3s#troubleshooting)

Before installing the Secure Agent, the user must have the following permissions:

Create and modify directories in the userâs home directory:~/.config/systemd/user,~/bin,~/.local/bin, and~/.rancher.

~/.config/systemd/user

~/bin

~/.local/bin

~/.rancher

Create and write log files.

Execute standard Linux commands:mkdir,chmod,tar, andsed.

mkdir

chmod

tar

sed



## Download Agent packagesâ
(source: https://docs.atlan.com/secure-agent/how-tos/k3s/install-secure-agent-on-virtual-machine-k3s#troubleshooting)

Follow these steps to download the necessary packages for setting up the Secure Agent.

The steps require Internet access to download files. In case the VM has no Internet connectivity, one can download them separately and copy the files to the VM.

Create a folder for deployment and navigate to it:mkdir -p atlan-secure-agent && cd atlan-secure-agent

Create a folder for deployment and navigate to it:

mkdir -p atlan-secure-agent && cd atlan-secure-agent

mkdir -p atlan-secure-agent && cd atlan-secure-agent

Run the following commands to download the required packages:Download theKubernetes install package, which contains files to run K3s on an air-gapped VM:curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/k3s_offline_package_main.tarDownload theContainer images packageif an image registry isn't available:curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/atlan_images_main.tarDownload theSecure Agent install package, which contains files for running the Secure Agent:curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/atlan_install_config_main.tar.gz

Run the following commands to download the required packages:

Download theKubernetes install package, which contains files to run K3s on an air-gapped VM:curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/k3s_offline_package_main.tar

Download theKubernetes install package, which contains files to run K3s on an air-gapped VM:

curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/k3s_offline_package_main.tar

curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/k3s_offline_package_main.tar

Download theContainer images packageif an image registry isn't available:curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/atlan_images_main.tar

Download theContainer images packageif an image registry isn't available:

curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/atlan_images_main.tar

curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/atlan_images_main.tar

Download theSecure Agent install package, which contains files for running the Secure Agent:curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/atlan_install_config_main.tar.gz

Download theSecure Agent install package, which contains files for running the Secure Agent:

curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/atlan_install_config_main.tar.gz

curl -O https://atlan-public.s3.amazonaws.com/workflow-offline-agent/container/atlan_install_config_main.tar.gz

Verify that all the files are downloaded.

Verify that all the files are downloaded.



## Install Secure Agentâ
(source: https://docs.atlan.com/secure-agent/how-tos/k3s/install-secure-agent-on-virtual-machine-k3s#troubleshooting)

Follow these steps to install and configure the Secure Agent on the virtual machine.

The installation can be performed by both root (administrative) and non-root (standard) users.

Navigate to the deployment folder (if not already):cd atlan-secure-agent

Navigate to the deployment folder (if not already):

cd atlan-secure-agent

cd atlan-secure-agent

Run the following command to extract the Secure Agent install package:tar -xvf atlan_install_config_main.tar.gz

Run the following command to extract the Secure Agent install package:

tar -xvf atlan_install_config_main.tar.gz

tar -xvf atlan_install_config_main.tar.gz

Therootless-installfolder is extracted from the Secure Agent install package. Run the following command to create an environment file using theenv.samplefile located in therootless-installfolder:cp ./rootless-install/.env.sample .env

Therootless-installfolder is extracted from the Secure Agent install package. Run the following command to create an environment file using theenv.samplefile located in therootless-installfolder:

rootless-install

env.sample

rootless-install

cp ./rootless-install/.env.sample .env

cp ./rootless-install/.env.sample .env

Open the.envfile and update these variables:VAR_ATLAN_SECURE_AGENT_NAME=prod-atlan-agent-vmVAR_ATLAN_DOMAIN=tenant.atlan.comVAR_ATLAN_TOKEN=<atlan-api-token>VAR_ATLAN_DATA_PATH=</absolute/path/to/atlan-secure-agent>

Open the.envfile and update these variables:

.env

VAR_ATLAN_SECURE_AGENT_NAME=prod-atlan-agent-vmVAR_ATLAN_DOMAIN=tenant.atlan.comVAR_ATLAN_TOKEN=<atlan-api-token>VAR_ATLAN_DATA_PATH=</absolute/path/to/atlan-secure-agent>

VAR_ATLAN_SECURE_AGENT_NAME=prod-atlan-agent-vmVAR_ATLAN_DOMAIN=tenant.atlan.comVAR_ATLAN_TOKEN=<atlan-api-token>VAR_ATLAN_DATA_PATH=</absolute/path/to/atlan-secure-agent>

Replace the environment variable values:VAR_ATLAN_SECURE_AGENT_NAME:Specify a meaningful and unique name for the Secure Agent. For example,prod-atlan-agent-vm.VAR_ATLAN_DOMAIN:Enter your Atlan tenant domain. For example,tenant.atlan.com.VAR_ATLAN_TOKEN:Provide the API key (Bearer token). For more information on generating an API key, seeCreate a bearer token.VAR_ATLAN_DATA_PATH:Specify the path where theatlan-secure-agentdirectory is located.

Replace the environment variable values:

VAR_ATLAN_SECURE_AGENT_NAME:Specify a meaningful and unique name for the Secure Agent. For example,prod-atlan-agent-vm.

VAR_ATLAN_SECURE_AGENT_NAME:

prod-atlan-agent-vm

VAR_ATLAN_DOMAIN:Enter your Atlan tenant domain. For example,tenant.atlan.com.

VAR_ATLAN_DOMAIN:

tenant.atlan.com

VAR_ATLAN_TOKEN:Provide the API key (Bearer token). For more information on generating an API key, seeCreate a bearer token.

VAR_ATLAN_TOKEN:

VAR_ATLAN_DATA_PATH:Specify the path where theatlan-secure-agentdirectory is located.

VAR_ATLAN_DATA_PATH:

atlan-secure-agent

Run the following command to grant execution permission for the setup script:chmod +x rootless-install/setup.sh

Run the following command to grant execution permission for the setup script:

chmod +x rootless-install/setup.sh

chmod +x rootless-install/setup.sh

The extractedsetup.shfile installs the Secure Agent and K3s. Run the following command to execute the installer:./rootless-install/setup.sh .env

The extractedsetup.shfile installs the Secure Agent and K3s. Run the following command to execute the installer:

setup.sh

./rootless-install/setup.sh .env

./rootless-install/setup.sh .env

While the installation is in progress, you can run the following command to verify the progress:kubectl get pods -A

While the installation is in progress, you can run the following command to verify the progress:

kubectl get pods -A

kubectl get pods -A



## Verify installationâ
(source: https://docs.atlan.com/secure-agent/how-tos/k3s/install-secure-agent-on-virtual-machine-k3s#troubleshooting)

After installing the Secure Agent, verify that it's running correctly. You can check its status through the Atlan UI or by accessing the Agent UI on K3s.

Log in as an Atlan admin or a similar role to access your tenant. For example:https://<tenant>.atlan.com.

https://<tenant>.atlan.com

Navigate to theAgenttab.

In theSecure Agentslist, use theSearch for agentsbox to enter your Secure Agent name.

If the agent appears in the list and is markedActive, installation is complete.



## Troubleshootingâ
(source: https://docs.atlan.com/secure-agent/how-tos/k3s/install-secure-agent-on-virtual-machine-k3s#troubleshooting)

If you encounter issues during installation, follow these steps:

Check the logs using the following command for detailed error messages that may indicate the root cause:tail -f logs/k3s.log

Check the logs using the following command for detailed error messages that may indicate the root cause:

tail -f logs/k3s.log

tail -f logs/k3s.log

For K3s rootless mode issues, follow theK3s official documentationfor troubleshooting rootless issues.

For K3s rootless mode issues, follow theK3s official documentationfor troubleshooting rootless issues.

If you continue to face issues, contact Atlan support bycreating a ticket.

atlan

documentation

System requirements

Prerequisites

Permissions required

Download Agent packages

Install Secure Agent

Verify installation

Troubleshooting
