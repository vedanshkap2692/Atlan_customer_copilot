# Infrastructure security
(source: https://docs.atlan.com/platform/references/infrastructure-security)

Get StartedWhat is Atlan?Quick Start GuidesCore ConceptsAdministrationSecurity & ComplianceInfrastructure securityHow are resources isolated?Security monitoringCompliance standards and assessmentsIncident response planReferencesFAQs

What is Atlan?

Quick Start Guides

Core Concepts

Administration

Security & ComplianceInfrastructure securityHow are resources isolated?Security monitoringCompliance standards and assessmentsIncident response plan

Infrastructure security

How are resources isolated?

Security monitoring

Compliance standards and assessments

Incident response plan

References

FAQs

Get Started

Security & Compliance

Infrastructure security

Seesecurity.atlan.comfor the latest policies and standards, reports and certifications, architecture, diagrams and more.

Atlan is deployed using Kubernetes in an Atlan-managed VPC (virtual private cloud).

Atlan also carries out:

Vulnerability management through frequent releasesÂ   -  Atlan makes weekly releases to minimize vulnerability at a product and operating system level.

Application Penetration Testing (APT)-  Atlan uses a third-party toolÂ to conduct industry standard APT. A penetration test is an authorized simulated cyber attack on a computer system, performed to evaluate the security of the system. The test is performed to identify both weaknesses (including the potential for unauthorized parties to gain access to the system's features and data) and strengths, enabling a full risk assessment to be completed.

Event logging and monitoringÂ   -  Atlan has many tools to support monitoring and event logging:Prometheus and Grafana for monitoringFluent Bit and Loki for event logging

Prometheus and Grafana for monitoring

Fluent Bit and Loki for event logging



## Network access to the control planeâ
(source: https://docs.atlan.com/platform/references/infrastructure-security)

We restrict access to the Kubernetes control plane by IP address to cluster administrators. We deny public internet access to the control plane.



## Network access to nodesâ
(source: https://docs.atlan.com/platform/references/infrastructure-security)

Nodes are configured to only accept connections (via network access control lists):

from the control plane on the specified ports

for services in Kubernetes of typeNodePortandLoadBalancer

NodePort

LoadBalancer

Each component of the Kubernetes cluster has security measures configured. These security measures are at the following levels:

Cluster security

Node security

Pod security

Container security

Network security

Code security

Secret management

Data encryption in transit

integration

connectors

security

access-control

permissions

Network access to the control plane

Network access to nodes
