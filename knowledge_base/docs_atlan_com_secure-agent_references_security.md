# Security
(source: https://docs.atlan.com/secure-agent/references/security)

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

References

Security

The Secure Agent is designed with multiple security controls to protect metadata, credentials, and communication between systems. This document outlines its security mechanisms across authentication, encryption, container security, network security, and logging and monitoring.



## Authentication and authorizationâ
(source: https://docs.atlan.com/secure-agent/references/security)

The Secure Agent implements security measures for authentication, encryption, and access control. This section details authentication mechanisms, including API key management and secret handling.



### API key managementâ
(source: https://docs.atlan.com/secure-agent/references/security)

The Secure Agent uses API keys for authentication when communicating with Atlan. These keys verify the agentâs identity and define its access scope.

Authentication:API keys authenticate the Secure Agent, allowing it to interact securely with Atlan. Each key is associated with a specific tenant and grants access based on permissions.

Storage:API keys are stored in enterprise-managed vaults, such as AWS Secrets Manager, Azure Key Vault, or Kubernetes Secrets. The Secure Agent retrieves the key dynamically during operation, eliminating manual configuration.

Expiration:API keys can have an expiration period, such as 90-180 days, or be configured based on internal security policies.

Rotation:When an API key nears expiration, a new key can be generated and stored in the secret vault. The Secure Agent automatically fetches the latest key from the vault.

Revocation:If an API key is compromised, it can be revoked. Once revoked, the Secure Agent retrieves a newly assigned key from the vault without requiring manual intervention.



### Secret managementâ
(source: https://docs.atlan.com/secure-agent/references/security)

The Secure Agent retrieves credentials securely without storing them locally.

Enterprise-managed vaults:The Secure Agent integrates with AWS Secrets Manager, Azure Key Vault, and other vaults to securely store credentials, keeping them within the organizationâs security perimeter.

Just-in-time access:Credentials, such as database secrets, are retrieved dynamically from enterprise vaults when needed and are never stored locally.

No credential transmission:Secrets are never transmitted to or stored on Atlan, ensuring complete isolation of sensitive information.



## Data security and encryptionâ
(source: https://docs.atlan.com/secure-agent/references/security)

The Secure Agent protects metadata using encryption and strict access controls.

Compliance with security standards:The Secure Agent aligns with ISO 27001 and SOC 2 security standards, ensuring strong encryption, data protection, and access control measures.

Data in transit:All communication between the Secure Agent and Atlan is encrypted using TLS 1.2 over HTTPS. For network-level protections, seeNetwork security.

Data at rest:Metadata stored in customer-managed storage or Atlanâs tenant bucket is encrypted using AES-256.

Data minimization:Only essential metadata is extracted and transmitted. Customers can configure data filters to exclude specific metadata fields from processing.

Retention control:Atlan doesn't require metadata post-ingestion, and customers can delete metadata from their storage buckets based on internal security policies.



## Container securityâ
(source: https://docs.atlan.com/secure-agent/references/security)

The Secure Agent implements security measures to protect container images, ensuring their integrity and mitigating security risks.

Container image hosting:Secure Agent container images are hosted on public repositories, such as Docker Hub and Amazon ECR. Organizations can deploy the Secure Agent from a private container registry to meet their compliance and security requirements.

Vulnerability scanning:Trivy scans container images for known vulnerabilities, outdated dependencies, misconfigurations, and exposed secrets. Scans are conducted weekly and whenever new changes are checked in.

Image signing and verification:Cosign signs container images to ensure authenticity. Image verification includes:Validating the image signature against Sigstore's transparency log.Verifying the signerâs identity through GitHub workflows.Confirming the certificate issued by GitHubâs OpenID Connect (OIDC) provider.

Validating the image signature against Sigstore's transparency log.

Verifying the signerâs identity through GitHub workflows.

Confirming the certificate issued by GitHubâs OpenID Connect (OIDC) provider.

License compliance:Trivy scans for software license compliance to ensure proper licensing for all components within the container images.



## Network securityâ
(source: https://docs.atlan.com/secure-agent/references/security)

The Secure Agent operates within a controlled network environment to facilitate secure metadata extraction and communication with Atlan.



### SSL certificatesâ
(source: https://docs.atlan.com/secure-agent/references/security)

The Secure Agent encrypts communications with Atlan, source systems, proxy servers, and secret managers.

Encryption in transit:All data communication between the Secure Agent and Atlan is encrypted using TLS 1.2 over HTTPS.

Certificate management:If trusted or well-known certificate authorities are used, no additional configuration is needed. The Default Trusted Certificate Authorities store contains certificates from the most common and trusted CAs, which the Secure Agent uses to secure connections.If internal or private certificate authorities are used, the Secure Agent trusts these custom certificate authorities through the infrastructureâs default certificate store.

If trusted or well-known certificate authorities are used, no additional configuration is needed. The Default Trusted Certificate Authorities store contains certificates from the most common and trusted CAs, which the Secure Agent uses to secure connections.

If internal or private certificate authorities are used, the Secure Agent trusts these custom certificate authorities through the infrastructureâs default certificate store.



### Whitelistingâ
(source: https://docs.atlan.com/secure-agent/references/security)

Configuring network access ensures only trusted communication between the Secure Agent and Atlan.

Domain whitelisting:The Secure Agent requires outbound access to Atlan through the domaintenant.atlan.com. Domain-based whitelisting simplifies network configurations while maintaining security.

tenant.atlan.com

DNS resolution:The Secure Agent relies on standard DNS resolution to reach Atlan domains. Network configurations must allow name resolution fortenant.atlan.com.

tenant.atlan.com

IP-based whitelisting:If domain-based whitelisting isnât feasible and specific IP ranges must be allowed, refer to thelist of required IP rangesto be whitelisted. If you need further assistance, contactAtlan Support.



## Logging and monitoringâ
(source: https://docs.atlan.com/secure-agent/references/security)

The Secure Agent captures logs for workflow execution, system orchestration, and Kubernetes operations while also providing monitoring capabilities.



### Types of logsâ
(source: https://docs.atlan.com/secure-agent/references/security)

Workflow logs:Capture job execution details, including start and completion status, connections to source systems and secret managers, metadata extraction results, and authentication status. These logs are sent to Atlan and accessible from the workflow status page.

Orchestration logs:Track the Secure Agentâs scheduled operations, including connection attempts to Atlan, retrieval of workflow requests, and workflow submission to the Argo engine. Logs also include error messages and performance metrics.

Argo logs:Provide visibility into workflow execution, including job scheduling, resource allocation, state transitions, and error handling.

Kubernetes logs:Capture system-level events, such as pod lifecycle changes, container startup and shutdown, resource allocation, network connectivity, and health checks.



### Monitoringâ
(source: https://docs.atlan.com/secure-agent/references/security)

Health checks:Secure Agent components run periodic health checks to verify connectivity, resource availability, and system integrity.

Resource utilization:CPU, memory, and storage usage are monitored to track system load and detect potential bottlenecks.

Logs can be viewed in Atlan or integrated with external monitoring systems.

data

api

authentication

Authentication and authorization

Data security and encryption

Container security

Network security

Logging and monitoring
