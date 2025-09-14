# Secure Agent
(source: https://docs.atlan.com/secure-agent#see-also)

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

The Atlan Secure Agent is a lightweight, Kubernetes-based application that enables secure metadata extraction. It connects internal systems with Atlan SaaS while keeping sensitive data protected and doesnât require inbound connectivity. Running within an organizationâs controlled environment, the Secure Agent ensures compliance with security policies and automates metadata processing.

Figure 1:The Secure Agent runs in the customer environment and acts as a gateway.



## Key capabilitiesâ
(source: https://docs.atlan.com/secure-agent#see-also)

The Secure Agent is designed for secure, scalable, and efficient metadata extraction.



### Security-first architectureâ
(source: https://docs.atlan.com/secure-agent#see-also)

Runs entirely within the organization's infrastructure, preventing secrets from leaving its boundary.

Uses outbound, encrypted communication to interact with Atlan SaaS.

Supports logging and monitoring and integrates with external monitoring systems for auditing and compliance.



### Scalable metadata extractionâ
(source: https://docs.atlan.com/secure-agent#see-also)

A single deployment of the Agent can connect to multiple source systems.

Supports multiple concurrent metadata extraction jobs.

Uses Kubernetes-based workloads for efficient resource management.



### Flexible deploymentâ
(source: https://docs.atlan.com/secure-agent#see-also)

Deploys on cloud-based Kubernetes environments (such as Amazon EKS, Azure AKS, and Google GKE) or on-premises clusters.

Scales dynamically based on workload demands.



### Automated operationsâ
(source: https://docs.atlan.com/secure-agent#see-also)

Continuously monitors system health and sends heartbeats to Atlan.

Captures and uploads execution logs for troubleshooting and auditing.

Provides performance insights through metrics and alerts.



## How it worksâ
(source: https://docs.atlan.com/secure-agent#see-also)

The Secure Agent follows a job-based execution model where metadata extraction tasks are scheduled and executed within the organization's environment. The workflow typically involves:

Atlan triggers a metadata extraction job.

The Secure Agent retrieves job details and extracts metadata using source-specific connectors.

Extracted metadata is shared with Atlan either through cloud storage or direct ingestion.

Atlan workflows process the extracted metadata and publish the assets.

Logs and execution status are sent to Atlan for monitoring and auditing.



## See alsoâ
(source: https://docs.atlan.com/secure-agent#see-also)

Deployment architecture: Learn more about how the Secure Agent integrates with your environment and supports secure metadata extraction.

security

access-control

permissions

Key capabilities

How it works

See also
