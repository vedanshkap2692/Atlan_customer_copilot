# Deployment architecture
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

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

Deployment architecture

The Atlan Secure Agent is a Kubernetes-based application that runs within a customer's environment. It acts as a gateway between the single-tenant Atlan SaaS and external systems like Snowflake, Tableau, and other data sources. This document explains the Secure Agent's deployment architecture, key components, communication flows, and security considerations.



## High-level architectureâ
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

This section describes how the Secure Agent is structured and deployed. It explains the core components that enable metadata extraction, job execution, and communication with Atlan.

Figure 1:Atlan Secure Agent deployment architecture.



## Core componentsâ
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

The Secure Agent runs as a Kubernetes-based application within a customer's private cloud or on-premises environment. It consists of several key components that work together to execute metadata extraction tasks.



### Argo Workflowsâ
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

An Argo Workflow server is deployed to coordinate all activities and launch Kubernetes workloads.

The Secure Agent uses Argo Workflows to orchestrate and manage metadata extraction jobs.

Each workflow represents a unit of work, such as extracting metadata from a source system.



### Agent orchestratorâ
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

A scheduled job that runs every five minutes to check for jobs that need to be executed.

It connects to the Atlan tenant, retrieves job details, and initiates workflows accordingly.



### Auxiliary servicesâ
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

Additional services that support agent operations:

Health monitoring servicesends periodic heartbeats to Atlan to confirm the agent is active.

Logging serviceuploads execution logs to Atlan for monitoring and debugging.



### Metadata extraction workflowsâ
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

Connector-specific jobs that extract metadata from source systems.

Workflows run in isolated containers, ensuring security and reliability.



## Data flowâ
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

The Secure Agent supports two modes of metadata transfer. Each mode determines how extracted metadata is delivered to Atlan.



### Bucket relayâ
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

Metadata extraction in bucket relay mode stores metadata in enterprise-managed cloud storage before Atlan retrieves it.

Figure 2:Data flow in bucket relay mode.

The Secure Agent extracts metadata and writes it to a storage bucket in the customerâs cloud environment (such as AWS S3, Azure Blob Storage, or Google Cloud Storage). This is managed by providing the agent write access to cloud storage.

Atlan retrieves metadata from the storage bucket and processes it further. This is managed by providing Atlan read access to list and read files in cloud storage.

This mode ensures the extracted data remains within the customerâs infrastructure until Atlan explicitly fetches it. Customers can also use this data for auditing.



### Direct ingestionâ
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

In direct ingestion mode, metadata is transferred directly from the Secure Agent to Atlan.

Figure 3:Data flow in direct ingestion mode.

The Secure Agent uses pre-signed URLs to upload metadata directly to Atlan. Some cloud storage providers that use pre-signed URLs include:

The Secure Agent uses pre-signed URLs to upload metadata directly to Atlan. Some cloud storage providers that use pre-signed URLs include:

AWS reference

AWS reference

Azure reference

Azure reference

GCP reference

GCP reference

A pre-signed URL grants temporary access to upload files without exposing long-term credentials.

A pre-signed URL grants temporary access to upload files without exposing long-term credentials.

Each URL has an expiration time, ensuring access is only available for a limited duration.

Each URL has an expiration time, ensuring access is only available for a limited duration.



## See alsoâ
(source: https://docs.atlan.com/secure-agent/references/deployment-architecture)

Secure Agent - Security: Details on security mechanisms.

integration

connectors

security

access-control

permissions

High-level architecture

Core components

Data flow

See also
