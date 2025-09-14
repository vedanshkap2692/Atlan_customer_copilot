# Set up an Azure private network link to Databricks
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-an-azure-private-network-link-to-databricks)

DatabricksGet StartedCross-workspace SetupCrawl Databricks AssetsOn-premises SetupPrivate Network SetupSet up an AWS private network link to DatabricksSet up an Azure private network link to DatabricksLineage and UsageTag managementReferencesTroubleshooting

Get Started

Cross-workspace Setup

Crawl Databricks Assets

On-premises Setup

Private Network SetupSet up an AWS private network link to DatabricksSet up an Azure private network link to Databricks

Set up an AWS private network link to Databricks

Set up an Azure private network link to Databricks

Lineage and Usage

Tag management

References

Troubleshooting

Connect data

Data Warehouses

Databricks

Private Network Setup

Set up an Azure private network link to Databricks

Azure Private Linkcreates a secure, private connection between services running in Azure. This document describes the steps to set this up between Databricks and Atlan.

You will need Databricks support, and probably your Databricks administrator involved   -  you may not have access or the tools to run these tasks.



## Prerequisitesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-an-azure-private-network-link-to-databricks)

Your Databricks instance must be Azure-managed and created from the Azure marketplace.

For all details, seeDatabricks documentation.



## Notify Atlan supportâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-an-azure-private-network-link-to-databricks)

Provide Atlan supportwith the following information:

Resource ID of your Azure-managed Databricks instance   -  the resource ID will be in this format:/subscriptions/<subscriptionID>/resourceGroups/azure-databricks/providers/Microsoft.Databricks/workspaces/<databricks-workspace>.

/subscriptions/<subscriptionID>/resourceGroups/azure-databricks/providers/Microsoft.Databricks/workspaces/<databricks-workspace>

There are additional steps that Atlan will need to complete. Once the Atlan team has confirmed that the configuration is ready, please continue with the remaining steps.



## Approve the endpoint connection requestâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-an-azure-private-network-link-to-databricks)

To approve the endpoint connection request from Atlan:

Open your Azure-managed Databricks workspace.

In the left menu, clickNetworkingand then click thePrivate endpoint connectionstab.

From the list of endpoints, search for the endpoint connection request from Atlan. In theConnection statecolumn for the Atlan endpoint connection, click theApprovebutton to approve the request .

Once the endpoint connection from Atlan has been approved, the status of the private endpoint in Atlan will change toApproved.

Approved

When you use this endpoint in the configuration forcrawling Databricks, Atlan will connect to Databricks over Azure Private Link.

data

configuration

Prerequisites

Notify Atlan support

Approve the endpoint connection request
