# Install on AWS EKS
(source: https://docs.atlan.com/secure-agent/how-tos/aws-eks/install-secure-agent-on-aws-eks)

Secure AgentManage AgentK3sAWS EKSInstall on AWS EKSConfigure workflow executionReferencesDeployment architectureSecurity

Manage AgentK3sAWS EKSInstall on AWS EKSConfigure workflow execution

K3s

AWS EKSInstall on AWS EKS

Install on AWS EKS

Configure workflow execution

ReferencesDeployment architectureSecurity

Deployment architecture

Security

Connect data

Secure Agent

Manage Agent

AWS EKS

Install on AWS EKS

This guide provides step-by-step instructions to install the Secure Agent on an Amazon Elastic Kubernetes Service (AWS EKS) cluster.



## System requirementsâ
(source: https://docs.atlan.com/secure-agent/how-tos/aws-eks/install-secure-agent-on-aws-eks)

To deploy the Secure Agent on AWS EKS, ensure the following system requirements are met:

Configure network access between your Secure Agent and Atlan tenant. For more information, seeWhitelisting Secure Agent.

Configure network access between your Secure Agent and Atlan tenant. For more information, seeWhitelisting Secure Agent.

You need Kubernetes version 1.19 or higher.

You need Kubernetes version 1.19 or higher.

You need to install Helm and kubectl on the machine you're using to connect to the AWS EKS cluster.

You need to install Helm and kubectl on the machine you're using to connect to the AWS EKS cluster.

You need at least 1 node for base services with a disk space of 20 GB and instance configuration as below:EnvironmentMinimum instance typeRecommended instance typeProductiont3.largeCustom based on workloadNon-productiont3.larget3.xlargeinfoðªDid you know?For optimal autoscaling, scale nodes based on the number of concurrent workflows.

You need at least 1 node for base services with a disk space of 20 GB and instance configuration as below:

ðªDid you know?For optimal autoscaling, scale nodes based on the number of concurrent workflows.



## Permissions requiredâ
(source: https://docs.atlan.com/secure-agent/how-tos/aws-eks/install-secure-agent-on-aws-eks)

Before installing the Secure Agent, make sure the following permissions are in place:



### Permissions for the Installerâ
(source: https://docs.atlan.com/secure-agent/how-tos/aws-eks/install-secure-agent-on-aws-eks)

The user, service or system account performing the installation needs access to the EKS cluster and permissions to manage Custom Resource Definitions (CRDs).

Ensure the kubeconfig is correctly configured for your target EKS cluster. If needed, use the following command to configure or update your kubeconfig file.aws eks update-kubeconfig --region ``<region>`` --name ``<cluster-name>``Replace<region>with your AWS region (for example, us-east-1) and<cluster-name>with the name of your EKS cluster.

Ensure the kubeconfig is correctly configured for your target EKS cluster. If needed, use the following command to configure or update your kubeconfig file.

aws eks update-kubeconfig --region ``<region>`` --name ``<cluster-name>``

aws eks update-kubeconfig --region ``<region>`` --name ``<cluster-name>``

Replace<region>with your AWS region (for example, us-east-1) and<cluster-name>with the name of your EKS cluster.

<region>

<cluster-name>

The installer needs permission to create, update, and delete Custom Resource Definitions (CRDs). If not using the cluster-admin role, grant the following:

The installer needs permission to create, update, and delete Custom Resource Definitions (CRDs). If not using the cluster-admin role, grant the following:

Create a file namedagent-crd-permissions.yamlon your machine.

Create a file namedagent-crd-permissions.yamlon your machine.

agent-crd-permissions.yaml

Copy the following content into the file:apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRolemetadata:# Use a descriptive namename: helm-crd-installer-rolerules:- apiGroups: ["apiextensions.k8s.io"]resources: ["customresourcedefinitions"]# Recommended verbs for Helm CRD managementverbs: ["create", "get", "list", "watch", "update", "patch", "delete"]---apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRoleBindingmetadata:# Use a descriptive namename: helm-crd-installer-bindingsubjects:# *** IMPORTANT: Modify this section based on who is running Helm ***# Choose ONE of the following options and replace placeholders.# Option 1: Bind to a specific User- kind: Username: "your-kubernetes-username" # Replace with the installing user's K8s username recognized by the clusterapiGroup: rbac.authorization.k8s.io# Option 2: Bind to a specific Group# - kind: Group#   name: "your-kubernetes-groupname" # Replace with the installing user's K8s group name#   apiGroup: rbac.authorization.k8s.io# Option 3: Bind to a Service Account (e.g., for CI/CD pipelines)# - kind: ServiceAccount#   name: "installer-sa-name" # Replace with the installer SA's name#   namespace: "installer-sa-namespace" # Replace with the installer SA's namespaceroleRef:# This refers to the ClusterRole created abovekind: ClusterRolename: helm-crd-installer-roleapiGroup: rbac.authorization.k8s.ioFollow the comments in the file to replace the placeholders. In the above file:Resource:customresourcedefinitions- needed for managing CRDs in the cluster.API Group:apiextensions.k8s.io- required to work with CRDs.Verbs: create, get, list, update, delete - necessary for installing, inspecting, updating, and cleaning up CRDs using Helm.ClusterRoleBinding: needed to assign the role to the user or group performing the installation.Once youâve updated the placeholders, use the belowkubectlcommand to apply the configuration:

Copy the following content into the file:

apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRolemetadata:# Use a descriptive namename: helm-crd-installer-rolerules:- apiGroups: ["apiextensions.k8s.io"]resources: ["customresourcedefinitions"]# Recommended verbs for Helm CRD managementverbs: ["create", "get", "list", "watch", "update", "patch", "delete"]---apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRoleBindingmetadata:# Use a descriptive namename: helm-crd-installer-bindingsubjects:# *** IMPORTANT: Modify this section based on who is running Helm ***# Choose ONE of the following options and replace placeholders.# Option 1: Bind to a specific User- kind: Username: "your-kubernetes-username" # Replace with the installing user's K8s username recognized by the clusterapiGroup: rbac.authorization.k8s.io# Option 2: Bind to a specific Group# - kind: Group#   name: "your-kubernetes-groupname" # Replace with the installing user's K8s group name#   apiGroup: rbac.authorization.k8s.io# Option 3: Bind to a Service Account (e.g., for CI/CD pipelines)# - kind: ServiceAccount#   name: "installer-sa-name" # Replace with the installer SA's name#   namespace: "installer-sa-namespace" # Replace with the installer SA's namespaceroleRef:# This refers to the ClusterRole created abovekind: ClusterRolename: helm-crd-installer-roleapiGroup: rbac.authorization.k8s.io

apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRolemetadata:# Use a descriptive namename: helm-crd-installer-rolerules:- apiGroups: ["apiextensions.k8s.io"]resources: ["customresourcedefinitions"]# Recommended verbs for Helm CRD managementverbs: ["create", "get", "list", "watch", "update", "patch", "delete"]---apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRoleBindingmetadata:# Use a descriptive namename: helm-crd-installer-bindingsubjects:# *** IMPORTANT: Modify this section based on who is running Helm ***# Choose ONE of the following options and replace placeholders.# Option 1: Bind to a specific User- kind: Username: "your-kubernetes-username" # Replace with the installing user's K8s username recognized by the clusterapiGroup: rbac.authorization.k8s.io# Option 2: Bind to a specific Group# - kind: Group#   name: "your-kubernetes-groupname" # Replace with the installing user's K8s group name#   apiGroup: rbac.authorization.k8s.io# Option 3: Bind to a Service Account (e.g., for CI/CD pipelines)# - kind: ServiceAccount#   name: "installer-sa-name" # Replace with the installer SA's name#   namespace: "installer-sa-namespace" # Replace with the installer SA's namespaceroleRef:# This refers to the ClusterRole created abovekind: ClusterRolename: helm-crd-installer-roleapiGroup: rbac.authorization.k8s.io

Follow the comments in the file to replace the placeholders. In the above file:

Resource:customresourcedefinitions- needed for managing CRDs in the cluster.

customresourcedefinitions

API Group:apiextensions.k8s.io- required to work with CRDs.

apiextensions.k8s.io

Verbs: create, get, list, update, delete - necessary for installing, inspecting, updating, and cleaning up CRDs using Helm.

ClusterRoleBinding: needed to assign the role to the user or group performing the installation.

Once youâve updated the placeholders, use the belowkubectlcommand to apply the configuration:

kubectl

Once youâve updated the placeholders, use the below kubectl command to apply the configuration:kubectl apply -f agent-crd-permissions.yaml

Once youâve updated the placeholders, use the below kubectl command to apply the configuration:

kubectl apply -f agent-crd-permissions.yaml

kubectl apply -f agent-crd-permissions.yaml



### Permissions for the Secure Agent Pod (Runtime)â
(source: https://docs.atlan.com/secure-agent/how-tos/aws-eks/install-secure-agent-on-aws-eks)

The Secure Agent runs as pods in your EKS cluster and requires permissions to interact with AWS services like S3. These permissions are granted through IAM Roles for Service Accounts (IRSA).

Create a new IAM role for the Secure Agent pod.

Create a new IAM role for the Secure Agent pod.

Configure the trust policy to enable the Secure Agentâs Kubernetes service account to assume the role. Make sure the argo-workflow service account exists in the same namespace where you plan to install the agent. For more information, see the AWS documentation onIAM roles for service accounts (IRSA).Example: Trust policy for the argo-workflow service account:"Condition": {"StringEquals": {":sub": "system:serviceaccount::argo-workflow"}}Replace<namespace>with the namespace where you plan to install agent.Create an S3 bucket (or use an existing one), and attach the following permissions to the IAM role used by the Secure Agent:s3:PutObject: Needed to write logs and artifactss3:GetObject: Needed to read logs and artifacts.s3:ListBucket: Needed by Argo artifact repository for listing objects.

Configure the trust policy to enable the Secure Agentâs Kubernetes service account to assume the role. Make sure the argo-workflow service account exists in the same namespace where you plan to install the agent. For more information, see the AWS documentation onIAM roles for service accounts (IRSA).

Example: Trust policy for the argo-workflow service account:"Condition": {"StringEquals": {":sub": "system:serviceaccount::argo-workflow"}}Replace<namespace>with the namespace where you plan to install agent.

Example: Trust policy for the argo-workflow service account:

"Condition": {"StringEquals": {":sub": "system:serviceaccount::argo-workflow"}}

"Condition": {"StringEquals": {":sub": "system:serviceaccount::argo-workflow"}}

Replace<namespace>with the namespace where you plan to install agent.

<namespace>

Create an S3 bucket (or use an existing one), and attach the following permissions to the IAM role used by the Secure Agent:s3:PutObject: Needed to write logs and artifactss3:GetObject: Needed to read logs and artifacts.s3:ListBucket: Needed by Argo artifact repository for listing objects.

Create an S3 bucket (or use an existing one), and attach the following permissions to the IAM role used by the Secure Agent:

s3:PutObject: Needed to write logs and artifacts

s3:PutObject

s3:GetObject: Needed to read logs and artifacts.

s3:GetObject

s3:ListBucket: Needed by Argo artifact repository for listing objects.

s3:ListBucket

The Helm chart automatically configures the necessary Kubernetes RBAC for Argo Workflows, which the Secure Agent uses. No additional configuration is required for the Secure Agent pod..



## Prerequisitesâ
(source: https://docs.atlan.com/secure-agent/how-tos/aws-eks/install-secure-agent-on-aws-eks)

Before proceeding, complete the following setup steps to prepare your Atlan tenant and AWS EKS cluster.



### Configure Atlan tenantâ
(source: https://docs.atlan.com/secure-agent/how-tos/aws-eks/install-secure-agent-on-aws-eks)

In your Atlan tenant:

Sign in as an Atlan admin.

Go toAdminfrom the left menu.

UnderWorkspace, clickLabs.

Navigate toWorkflow Center.

Enable theCrawl assets using Secure Agenttoggle.



### Configure Secure Agent settingsâ
(source: https://docs.atlan.com/secure-agent/how-tos/aws-eks/install-secure-agent-on-aws-eks)

Theagent_config_values.yamlfile is used to configure the Secure Agent, Argo Workflows, and storage for the AWS EKS cluster. Follow these instructions on the machine where you're performing the installation.

agent_config_values.yaml

Create a file namedagent_config_values.yamlfile.

Create a file namedagent_config_values.yamlfile.

agent_config_values.yaml

Copy the configuration below into the file:# -----------------------------------------------------------------------------------------# Agent core settings   -  Follow the comments to update:# 1. Image registry settings - To be updated only if you are using a private image registry# 2. Atlan connection settings - To be updated only if you want agent to use the S3 bucket# 3. Argo Private repository settings - To be updated only if you are using private repository for Argo workflows# 4. Kubernetes Pod Annotation settings - To be updated only if you want to customize the Kubernetes podâs metadata# 5. Argo Private repository settings - To be updated only if you are using private repository for Argo workflows# 6. S3 storage settings - To be updated with S3 bucket details.# -----------------------------------------------------------------------------------------agent:enabled: trueenableStorageProxy: falseca:crt: ""#Provide a base64-encoded string of a JSON object, e.g., {"client_id": 123, "client_secret": 1243}.#Set this only if you need to include custom headers in API calls made by the agent.restAPIHeaders: ""versions:k3s: ""k8s: ""helm: ""# 1. Image Registry Settingsimage:# Only update if you're using a private image registryregistry: "public.ecr.aws"repository: "atlanhq"# Only update if you're using custom imagesrestImageName: "rest-2"restImageTag: "1.0"# Only update if you're using custom imagesjdbcImageName: "jdbc-metadata-extractor-with-jars"jdbcImageTag: "1.0"# Only update if you're using custom imagescredentialImageName: "connector-auth"credentialImageTag: "1.0"# Only update if you're using custom imagescsaScriptsImageName: "marketplace-csa-scripts"csaScriptsImageTag: "1.0"# Marketplace scripts image details - keep these values as is unless using custom imagesmarketplaceScriptsImageName: "marketplace-scripts-agent"marketplaceScriptsImageTag: "1.0"pullPolicy: IfNotPresentpullSecrets: []  # Add pull secrets if using private registryannotations: {}labels: {}serviceAccountName: ""automountServiceAccountToken: trueresources: {}# 2. Atlan connection settings - Only update if you want to agent to use the S3 bucketatlan:argoToken: ""vaultEnvEnabled: false# Set to true only if the agent should store metadata# in your bucket instead of sending it to Atlan via presigned URL.useAgentBucket: falsemetadataBucket: ""persistentVolume:scripts:enabled: falsedata:enabled: falseminio:enabled: falseargo-workflows:images:pullPolicy: IfNotPresentpullSecrets: []crds:install: truekeep: trueannotations: {}singleNamespace: trueworkflow:serviceAccount:create: truerbac:create: truecontroller:# 3. Argo Private repository settings - Only update if you are using a private image repository for Argoimage:# update the private image repository detailsregistry: quay.iorepository: argoproj/workflow-controllertag: ""parallelism: 10resourceRateLimit:limit: 10burst: 5rbac:create: truesecretWhitelist: []accessAllSecrets: falsewriteConfigMaps: falseconfigMap:create: truename: ""namespaceParallelism: 10workflowDefaults:# 4. Kubernetes Pod Annotation settings - Only update if you want to customize the Pod metadata.## For example, the annotation might be used by external systems such as proxies, or monitoring tools, and more.spec:podMetadata:annotations:argo.workflow/agent-type: "atlan-agent-service"labels:app.kubernetes.io/name: "atlan-agent"podGC:strategy: OnPodSuccessserviceAccountName: argo-workflowautomountServiceAccountToken: truettlStrategy:secondsAfterCompletion: 84600templateDefaults:container:securityContext:allowPrivilegeEscalation: falseresources: {}env:- name: CA_CERTvalueFrom:configMapKeyRef:name: cert-configkey: ca.crtoptional: true- name: REST_API_HEADERSvalueFrom:configMapKeyRef:name: agent-registry-settingskey: restAPIHeadersoptional: trueserviceAccount:create: truename: workflow-controllerworkflowNamespaces:- defaultreplicas: 1revisionHistoryLimit: 10nodeEvents:enabled: falseserver:enabled: true# 5. Argo Private repository settings - Only update if you are using a private image repository for Argoimage:registry: quay.iorepository: argoproj/argoclitag: ""rbac:create: trueserviceAccount:create: truereplicas: 1autoscaling:enabled: falseingress:enabled: falseannotations:ingress.kubernetes.io/ssl-redirect: "false"resources: {}executor:securityContext: {}resources: {}artifactRepository:archiveLogs: trueuseStaticCredentials: false# 6. S3 bucket settings - needed by the secure agent to store logs and artifactss3:# S3 bucket name - Update with the bucket name you created in the Permissions required section.bucket: "atlan--bucket"# S3 endpointendpoint: "s3.us-east-2.amazonaws.com"# AWS region - Update with the region where you created bucket in the Permissions required section.region: "us-east-2"# Artifact path formatkeyFormat: "argo-artifacts/{{workflow.namespace}}/{{workflow.name}}/{{pod.name}}"# Whether to use insecure connectionsinsecure: false# Use AWS SDK credentials (IAM role)useSDKCreds: true

Copy the configuration below into the file:

# -----------------------------------------------------------------------------------------# Agent core settings   -  Follow the comments to update:# 1. Image registry settings - To be updated only if you are using a private image registry# 2. Atlan connection settings - To be updated only if you want agent to use the S3 bucket# 3. Argo Private repository settings - To be updated only if you are using private repository for Argo workflows# 4. Kubernetes Pod Annotation settings - To be updated only if you want to customize the Kubernetes podâs metadata# 5. Argo Private repository settings - To be updated only if you are using private repository for Argo workflows# 6. S3 storage settings - To be updated with S3 bucket details.# -----------------------------------------------------------------------------------------agent:enabled: trueenableStorageProxy: falseca:crt: ""#Provide a base64-encoded string of a JSON object, e.g., {"client_id": 123, "client_secret": 1243}.#Set this only if you need to include custom headers in API calls made by the agent.restAPIHeaders: ""versions:k3s: ""k8s: ""helm: ""# 1. Image Registry Settingsimage:# Only update if you're using a private image registryregistry: "public.ecr.aws"repository: "atlanhq"# Only update if you're using custom imagesrestImageName: "rest-2"restImageTag: "1.0"# Only update if you're using custom imagesjdbcImageName: "jdbc-metadata-extractor-with-jars"jdbcImageTag: "1.0"# Only update if you're using custom imagescredentialImageName: "connector-auth"credentialImageTag: "1.0"# Only update if you're using custom imagescsaScriptsImageName: "marketplace-csa-scripts"csaScriptsImageTag: "1.0"# Marketplace scripts image details - keep these values as is unless using custom imagesmarketplaceScriptsImageName: "marketplace-scripts-agent"marketplaceScriptsImageTag: "1.0"pullPolicy: IfNotPresentpullSecrets: []  # Add pull secrets if using private registryannotations: {}labels: {}serviceAccountName: ""automountServiceAccountToken: trueresources: {}# 2. Atlan connection settings - Only update if you want to agent to use the S3 bucketatlan:argoToken: ""vaultEnvEnabled: false# Set to true only if the agent should store metadata# in your bucket instead of sending it to Atlan via presigned URL.useAgentBucket: falsemetadataBucket: ""persistentVolume:scripts:enabled: falsedata:enabled: falseminio:enabled: falseargo-workflows:images:pullPolicy: IfNotPresentpullSecrets: []crds:install: truekeep: trueannotations: {}singleNamespace: trueworkflow:serviceAccount:create: truerbac:create: truecontroller:# 3. Argo Private repository settings - Only update if you are using a private image repository for Argoimage:# update the private image repository detailsregistry: quay.iorepository: argoproj/workflow-controllertag: ""parallelism: 10resourceRateLimit:limit: 10burst: 5rbac:create: truesecretWhitelist: []accessAllSecrets: falsewriteConfigMaps: falseconfigMap:create: truename: ""namespaceParallelism: 10workflowDefaults:# 4. Kubernetes Pod Annotation settings - Only update if you want to customize the Pod metadata.## For example, the annotation might be used by external systems such as proxies, or monitoring tools, and more.spec:podMetadata:annotations:argo.workflow/agent-type: "atlan-agent-service"labels:app.kubernetes.io/name: "atlan-agent"podGC:strategy: OnPodSuccessserviceAccountName: argo-workflowautomountServiceAccountToken: truettlStrategy:secondsAfterCompletion: 84600templateDefaults:container:securityContext:allowPrivilegeEscalation: falseresources: {}env:- name: CA_CERTvalueFrom:configMapKeyRef:name: cert-configkey: ca.crtoptional: true- name: REST_API_HEADERSvalueFrom:configMapKeyRef:name: agent-registry-settingskey: restAPIHeadersoptional: trueserviceAccount:create: truename: workflow-controllerworkflowNamespaces:- defaultreplicas: 1revisionHistoryLimit: 10nodeEvents:enabled: falseserver:enabled: true# 5. Argo Private repository settings - Only update if you are using a private image repository for Argoimage:registry: quay.iorepository: argoproj/argoclitag: ""rbac:create: trueserviceAccount:create: truereplicas: 1autoscaling:enabled: falseingress:enabled: falseannotations:ingress.kubernetes.io/ssl-redirect: "false"resources: {}executor:securityContext: {}resources: {}artifactRepository:archiveLogs: trueuseStaticCredentials: false# 6. S3 bucket settings - needed by the secure agent to store logs and artifactss3:# S3 bucket name - Update with the bucket name you created in the Permissions required section.bucket: "atlan--bucket"# S3 endpointendpoint: "s3.us-east-2.amazonaws.com"# AWS region - Update with the region where you created bucket in the Permissions required section.region: "us-east-2"# Artifact path formatkeyFormat: "argo-artifacts/{{workflow.namespace}}/{{workflow.name}}/{{pod.name}}"# Whether to use insecure connectionsinsecure: false# Use AWS SDK credentials (IAM role)useSDKCreds: true

# -----------------------------------------------------------------------------------------# Agent core settings   -  Follow the comments to update:# 1. Image registry settings - To be updated only if you are using a private image registry# 2. Atlan connection settings - To be updated only if you want agent to use the S3 bucket# 3. Argo Private repository settings - To be updated only if you are using private repository for Argo workflows# 4. Kubernetes Pod Annotation settings - To be updated only if you want to customize the Kubernetes podâs metadata# 5. Argo Private repository settings - To be updated only if you are using private repository for Argo workflows# 6. S3 storage settings - To be updated with S3 bucket details.# -----------------------------------------------------------------------------------------agent:enabled: trueenableStorageProxy: falseca:crt: ""#Provide a base64-encoded string of a JSON object, e.g., {"client_id": 123, "client_secret": 1243}.#Set this only if you need to include custom headers in API calls made by the agent.restAPIHeaders: ""versions:k3s: ""k8s: ""helm: ""# 1. Image Registry Settingsimage:# Only update if you're using a private image registryregistry: "public.ecr.aws"repository: "atlanhq"# Only update if you're using custom imagesrestImageName: "rest-2"restImageTag: "1.0"# Only update if you're using custom imagesjdbcImageName: "jdbc-metadata-extractor-with-jars"jdbcImageTag: "1.0"# Only update if you're using custom imagescredentialImageName: "connector-auth"credentialImageTag: "1.0"# Only update if you're using custom imagescsaScriptsImageName: "marketplace-csa-scripts"csaScriptsImageTag: "1.0"# Marketplace scripts image details - keep these values as is unless using custom imagesmarketplaceScriptsImageName: "marketplace-scripts-agent"marketplaceScriptsImageTag: "1.0"pullPolicy: IfNotPresentpullSecrets: []  # Add pull secrets if using private registryannotations: {}labels: {}serviceAccountName: ""automountServiceAccountToken: trueresources: {}# 2. Atlan connection settings - Only update if you want to agent to use the S3 bucketatlan:argoToken: ""vaultEnvEnabled: false# Set to true only if the agent should store metadata# in your bucket instead of sending it to Atlan via presigned URL.useAgentBucket: falsemetadataBucket: ""persistentVolume:scripts:enabled: falsedata:enabled: falseminio:enabled: falseargo-workflows:images:pullPolicy: IfNotPresentpullSecrets: []crds:install: truekeep: trueannotations: {}singleNamespace: trueworkflow:serviceAccount:create: truerbac:create: truecontroller:# 3. Argo Private repository settings - Only update if you are using a private image repository for Argoimage:# update the private image repository detailsregistry: quay.iorepository: argoproj/workflow-controllertag: ""parallelism: 10resourceRateLimit:limit: 10burst: 5rbac:create: truesecretWhitelist: []accessAllSecrets: falsewriteConfigMaps: falseconfigMap:create: truename: ""namespaceParallelism: 10workflowDefaults:# 4. Kubernetes Pod Annotation settings - Only update if you want to customize the Pod metadata.## For example, the annotation might be used by external systems such as proxies, or monitoring tools, and more.spec:podMetadata:annotations:argo.workflow/agent-type: "atlan-agent-service"labels:app.kubernetes.io/name: "atlan-agent"podGC:strategy: OnPodSuccessserviceAccountName: argo-workflowautomountServiceAccountToken: truettlStrategy:secondsAfterCompletion: 84600templateDefaults:container:securityContext:allowPrivilegeEscalation: falseresources: {}env:- name: CA_CERTvalueFrom:configMapKeyRef:name: cert-configkey: ca.crtoptional: true- name: REST_API_HEADERSvalueFrom:configMapKeyRef:name: agent-registry-settingskey: restAPIHeadersoptional: trueserviceAccount:create: truename: workflow-controllerworkflowNamespaces:- defaultreplicas: 1revisionHistoryLimit: 10nodeEvents:enabled: falseserver:enabled: true# 5. Argo Private repository settings - Only update if you are using a private image repository for Argoimage:registry: quay.iorepository: argoproj/argoclitag: ""rbac:create: trueserviceAccount:create: truereplicas: 1autoscaling:enabled: falseingress:enabled: falseannotations:ingress.kubernetes.io/ssl-redirect: "false"resources: {}executor:securityContext: {}resources: {}artifactRepository:archiveLogs: trueuseStaticCredentials: false# 6. S3 bucket settings - needed by the secure agent to store logs and artifactss3:# S3 bucket name - Update with the bucket name you created in the Permissions required section.bucket: "atlan--bucket"# S3 endpointendpoint: "s3.us-east-2.amazonaws.com"# AWS region - Update with the region where you created bucket in the Permissions required section.region: "us-east-2"# Artifact path formatkeyFormat: "argo-artifacts/{{workflow.namespace}}/{{workflow.name}}/{{pod.name}}"# Whether to use insecure connectionsinsecure: false# Use AWS SDK credentials (IAM role)useSDKCreds: true

In the configuration file, follow the comments to replace the necessary attributes. You may want to update the below configurations if:You are using a private image registry (Image registry settings)You want the agent to use an S3 bucket (Atlan connection settings)You are using a private repository for Argo workflows (Argo Private repository settings)You want to customize the Kubernetes pod's metadata (Kubernetes Pod Annotation settings)You need specific S3 storage configuration (S3 storage settings)

In the configuration file, follow the comments to replace the necessary attributes. You may want to update the below configurations if:

You are using a private image registry (Image registry settings)

You want the agent to use an S3 bucket (Atlan connection settings)

You are using a private repository for Argo workflows (Argo Private repository settings)

You want to customize the Kubernetes pod's metadata (Kubernetes Pod Annotation settings)

You need specific S3 storage configuration (S3 storage settings)



## Install using Helm chartâ
(source: https://docs.atlan.com/secure-agent/how-tos/aws-eks/install-secure-agent-on-aws-eks)

Follow these steps to install the Secure Agent and its dependencies into your AWS EKS cluster using Helm charts.

Install the Argo Custom Resource Definitions (CRDs) required by the Secure Agent. This step installs only the CRDs. The Secure Agent is installed in the subsequent step using a Helm upgrade.helm install <helm-app-name> oci://registry-1.docker.io/atlanhq/workflow-offline-agent \--version 0.1.0 \-n <namespace> \--create-namespace -f <path/to/agent_config_values.yaml> \--set agent.name="<secure-agent-name>" \--set agent.atlan.domain="<atlan-tenant-domain>" \--set agent.atlan.token="<atlan-api-token>" \--set argo-workflows.controller.workflowNamespaces={<namespace>} \--set IsUpgrade=falseReplace the placeholders:<namespace>: The Kubernetes namespace where you want to deploy the Secure Agent.<path/to/agent_config_values.yaml>: The path to the YAML config file.<secure-agent-name>: Unique name, like agent-us-east-cdw.<helm-app-name>: Unique Helm release name, like atlan-agent-v1.<atlan-tenant-domain>: Your Atlan domain, e.g., mycompany.atlan.com.<atlan-api-token>: Token used for authentication. SeeCreate a bearer token.

Install the Argo Custom Resource Definitions (CRDs) required by the Secure Agent. This step installs only the CRDs. The Secure Agent is installed in the subsequent step using a Helm upgrade.

helm install <helm-app-name> oci://registry-1.docker.io/atlanhq/workflow-offline-agent \--version 0.1.0 \-n <namespace> \--create-namespace -f <path/to/agent_config_values.yaml> \--set agent.name="<secure-agent-name>" \--set agent.atlan.domain="<atlan-tenant-domain>" \--set agent.atlan.token="<atlan-api-token>" \--set argo-workflows.controller.workflowNamespaces={<namespace>} \--set IsUpgrade=false

helm install <helm-app-name> oci://registry-1.docker.io/atlanhq/workflow-offline-agent \--version 0.1.0 \-n <namespace> \--create-namespace -f <path/to/agent_config_values.yaml> \--set agent.name="<secure-agent-name>" \--set agent.atlan.domain="<atlan-tenant-domain>" \--set agent.atlan.token="<atlan-api-token>" \--set argo-workflows.controller.workflowNamespaces={<namespace>} \--set IsUpgrade=false

Replace the placeholders:

<namespace>: The Kubernetes namespace where you want to deploy the Secure Agent.

<namespace>

<path/to/agent_config_values.yaml>: The path to the YAML config file.

<path/to/agent_config_values.yaml>

<secure-agent-name>: Unique name, like agent-us-east-cdw.

<secure-agent-name>

<helm-app-name>: Unique Helm release name, like atlan-agent-v1.

<helm-app-name>

<atlan-tenant-domain>: Your Atlan domain, e.g., mycompany.atlan.com.

<atlan-tenant-domain>

<atlan-api-token>: Token used for authentication. SeeCreate a bearer token.

<atlan-api-token>

Use the following kubectl command to associate the IAM role with the service account. This enables the Secure Agent to access the S3 bucket securely using IAM Roles for Service Accounts (IRSA). Make sure the IAM roleâs trust policy enables the argo-workflow service account to assume the role.kubectl annotate serviceaccount argo-workflow \-n  \eks.amazonaws.com/role-arn=arn:aws:iam:::role/Replace the placeholders:<namespace: The Kubernetes namespace where you want to deploy the Secure Agent.<AWS_ACCOUNT_ID>: Your AWS Account ID.<YourAgentIAMRoleName>: The IAM role name you created for the Secure Agent using IRSA.

Use the following kubectl command to associate the IAM role with the service account. This enables the Secure Agent to access the S3 bucket securely using IAM Roles for Service Accounts (IRSA). Make sure the IAM roleâs trust policy enables the argo-workflow service account to assume the role.

kubectl annotate serviceaccount argo-workflow \-n  \eks.amazonaws.com/role-arn=arn:aws:iam:::role/

kubectl annotate serviceaccount argo-workflow \-n  \eks.amazonaws.com/role-arn=arn:aws:iam:::role/

Replace the placeholders:

<namespace: The Kubernetes namespace where you want to deploy the Secure Agent.

<namespace

<AWS_ACCOUNT_ID>: Your AWS Account ID.

<AWS_ACCOUNT_ID>

<YourAgentIAMRoleName>: The IAM role name you created for the Secure Agent using IRSA.

<YourAgentIAMRoleName>

Install the Secure Agent by upgrading the Helm release. This step performs the actual Secure Agent installation after CRDs are in place.helm upgrade <helm-app-name> oci://registry-1.docker.io/atlanhq/workflow-offline-agent \--version 0.1.0 \-n <namespace> \--create-namespace -f <path/to/agent_config_values.yaml> \--set agent.name="<secure-agent-name>" \--set agent.atlan.domain="<atlan-tenant-domain>" \--set agent.atlan.token="<atlan-api-token>" \--set argo-workflows.controller.workflowNamespaces={<namespace>} \--set IsUpgrade=trueReplace the placeholders:<namespace>: The Kubernetes namespace where you want to deploy the Secure Agent.<path/to/agent_config_values.yaml>: The path to the YAML config file.<secure-agent-name>: Unique name, like agent-us-east-cdw.<helm-app-name>: Unique Helm release name, like atlan-agent-v1.<atlan-tenant-domain>: Your Atlan domain, e.g., mycompany.atlan.com.<atlan-api-token>: Token used for authentication. SeeCreate a bearer token.

Install the Secure Agent by upgrading the Helm release. This step performs the actual Secure Agent installation after CRDs are in place.

helm upgrade <helm-app-name> oci://registry-1.docker.io/atlanhq/workflow-offline-agent \--version 0.1.0 \-n <namespace> \--create-namespace -f <path/to/agent_config_values.yaml> \--set agent.name="<secure-agent-name>" \--set agent.atlan.domain="<atlan-tenant-domain>" \--set agent.atlan.token="<atlan-api-token>" \--set argo-workflows.controller.workflowNamespaces={<namespace>} \--set IsUpgrade=true

helm upgrade <helm-app-name> oci://registry-1.docker.io/atlanhq/workflow-offline-agent \--version 0.1.0 \-n <namespace> \--create-namespace -f <path/to/agent_config_values.yaml> \--set agent.name="<secure-agent-name>" \--set agent.atlan.domain="<atlan-tenant-domain>" \--set agent.atlan.token="<atlan-api-token>" \--set argo-workflows.controller.workflowNamespaces={<namespace>} \--set IsUpgrade=true

Replace the placeholders:

<namespace>: The Kubernetes namespace where you want to deploy the Secure Agent.

<namespace>

<path/to/agent_config_values.yaml>: The path to the YAML config file.

<path/to/agent_config_values.yaml>

<secure-agent-name>: Unique name, like agent-us-east-cdw.

<secure-agent-name>

<helm-app-name>: Unique Helm release name, like atlan-agent-v1.

<helm-app-name>

<atlan-tenant-domain>: Your Atlan domain, e.g., mycompany.atlan.com.

<atlan-tenant-domain>

<atlan-api-token>: Token used for authentication. SeeCreate a bearer token.

<atlan-api-token>

While the installation is in progress, you can run the following command to verify the progress:kubectl get pods -n <namespace>Replace<namespace>with the Kubernetes namespace used for deployment.

While the installation is in progress, you can run the following command to verify the progress:

kubectl get pods -n <namespace>

kubectl get pods -n <namespace>

Replace<namespace>with the Kubernetes namespace used for deployment.

<namespace>



## Verify installationâ
(source: https://docs.atlan.com/secure-agent/how-tos/aws-eks/install-secure-agent-on-aws-eks)

To confirm successful installation:

Sign in to your Atlan tenant as an admin. For example,https://<tenant>.atlan.com.

https://<tenant>.atlan.com

Navigate to theAgenttab.

Search for your Secure Agent name.

If the agent appears in the list and is markedActive, installation is complete.

security

access-control

permissions

System requirements

Permissions required

Prerequisites

Install using Helm chart

Verify installation
