# Configure workflow execution
(source: https://docs.atlan.com/secure-agent/how-tos/configure-secure-agent-for-workflow-execution)

Secure AgentManage AgentK3sAWS EKSConfigure workflow executionReferencesDeployment architectureSecurity

Manage AgentK3sAWS EKSConfigure workflow execution

K3s

AWS EKS

Configure workflow execution

ReferencesDeployment architectureSecurity

Deployment architecture

Security

Connect data

Secure Agent

Manage Agent

Configure workflow execution

When using Secure Agent for extraction, source system credentials (secrets) required for workflow execution are stored in a Secret Manager. This guide provides steps to set up workflows with Secure Agent and specify the secret details it uses during workflow execution.



### Before you beginâ
(source: https://docs.atlan.com/secure-agent/how-tos/configure-secure-agent-for-workflow-execution)

Before configuring Secure Agent for workflow execution, ensure you have:

A registered and active Secure Agent.

Access to one of the supported secret stores: AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, environment variable-based secret injection technique, or a custom secret store.



### Configure secrets retrieval for workflow executionâ
(source: https://docs.atlan.com/secure-agent/how-tos/configure-secure-agent-for-workflow-execution)

Follow these steps to configure Secure Agent to retrieve secrets from a secret store required for the workflow execution. This is necessary for secure data access while running your workflows.

For each field, you can enter either the name of a secret stored in your secret manager or the actual value. Use secret names when using a secret store with Secure Agent, or enter values directly if no secret is required.

AWS

Azure

GCP

Environment variables

Custom store

Secure Agent retrieves the required secrets from AWS Secrets Manager during workflow execution. Follow these steps to configure retrieval under the Secure Agent configuration section:

Secret path in Secret Manager:Provide the Amazon Resource Name (ARN) or the path of the secret that contains the sensitive configuration details required for the connector. These details may include credentials such as username, password, or other sensitive information needed by the Secure Agent to securely access data during workflow execution.

AWS region:Select the region where your AWS Secrets Manager is located.

AWS authentication method:Select how you want the Secure Agent to authenticate when executing the workflow. Choose one:IAM (Recommended): Use this method if the secure agent was configured to use the AWS IAM permissions to access secrets.IAM Assume Role: Use this method if the agent was configured to access secrets via cross-account roles.AWS Assume Role ARN: Provide the IAM Role ARN that grants the Secure Agent permission to retrieve secrets.Access Key & Secret Key: Use this method if the agent was configured to use the AWS Access Key ID and Secret Access Key via environment variables or Kubernetes secrets.

IAM (Recommended): Use this method if the secure agent was configured to use the AWS IAM permissions to access secrets.

IAM Assume Role: Use this method if the agent was configured to access secrets via cross-account roles.

AWS Assume Role ARN: Provide the IAM Role ARN that grants the Secure Agent permission to retrieve secrets.

Access Key & Secret Key: Use this method if the agent was configured to use the AWS Access Key ID and Secret Access Key via environment variables or Kubernetes secrets.

Secure Agent retrieves secrets from Azure Key Vault during workflow execution. Follow these steps to configure retrieval under the Secure Agent configuration section:

Secret path in Secret Manager:Provide the URL of the Azure Key Vault secret that contains the sensitive configuration details required for the connector. These details may include credentials such as username, password, or other sensitive information needed by the Secure Agent to securely access data during workflow execution.

Azure authentication method:Select how you want the Secure Agent to authenticate when accessing the Azure Key Vault secret. Choose one:Managed Identity (Recommended): Use this method if the agent was configured to use an Azure-managed identity assigned to the agent environment for authentication.Service Principal Authentication: Use this method if the agent was configured to authenticate via a Service Principal using Tenant ID, Client ID, and Client Secret.

Managed Identity (Recommended): Use this method if the agent was configured to use an Azure-managed identity assigned to the agent environment for authentication.

Service Principal Authentication: Use this method if the agent was configured to authenticate via a Service Principal using Tenant ID, Client ID, and Client Secret.

Azure Key Vault Name:Provide the name of your Azure Key Vault that stores your secrets.

Secure Agent retrieves secrets from GCP Secret Manager during workflow execution. The secret is uniquely identified by its name in GCP Secret Manager, without requiring additional attributes.

Secure Agent retrieves secrets from environment variables during workflow execution.

Secure Agent retrieves secrets from Custom Secret Store during workflow execution. Follow these steps to configure retrieval under the Secure Agent configuration section:

Agent Custom configuration:Secure agent needs information for connecting to the custom secret store. Add the configuration details in JSON format to specify the connection settings and the secrets to retrieve during workflow execution. For example, the JSON configuration to initiate a sample custom store may look like below:

{"store_url":"https://custom-secret-store.example.com","secret_name":"my-custom-secret"}

{"store_url":"https://custom-secret-store.example.com","secret_name":"my-custom-secret"}



### Next stepsâ
(source: https://docs.atlan.com/secure-agent/how-tos/configure-secure-agent-for-workflow-execution)

After configuring the Secure Agent, return to your connectorâs setup guide and continue the workflow setup.

integration

connectors

workflow

automation

orchestration

Before you begin

Configure secrets retrieval for workflow execution

Next steps
