# Set up an AWS private network link to Databricks
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-an-aws-private-network-link-to-databricks)

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

Set up an AWS private network link to Databricks

AWS PrivateLinkcreates a secure, private connection between services running in AWS. This document describes the steps to set this up between Databricks and Atlan.

You will need Databricks support, and probably your Databricks administrator involved   -  you may not have access or the tools to run these tasks.



## Prerequisitesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-an-aws-private-network-link-to-databricks)

Databricks must be set up on the E2 version of the platform and Enterprise pricing tier.

Your Databricks workspace must be in an AWS region that supports the E2 version of the platform, and not theus-west-1region. Your Databricks workspace must also be hosted in the same region as Atlan.

us-west-1

Your Databricks workspace must use customer-managed VPC. (Note that you cannot update an existing Databricks-managed VPC to a customer-managed VPC.)

For all details, seeDatabricks documentation.



## Notify Atlan supportâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-an-aws-private-network-link-to-databricks)

Once setup is completed,provide Atlan supportwith the following information:

The AWS region of your Databricks instance.

There are additional steps that Atlan will need to complete:

Creating a security group

Creating an endpoint

Once the Atlan team has confirmed that the configuration is ready, please continue with the remaining steps.



## Accept the endpoint connection requestâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-an-aws-private-network-link-to-databricks)

You can either:

Accept the endpoint connection request from Atlan viaAPI.

Accept the endpoint connection request from Atlan from theDatabricks console.

Once the endpoint connection is accepted, Atlan support will finish the configuration on the Atlan side.

When you use this endpoint in the configuration forcrawling Databricks, Atlan will connect to Databricks over AWS PrivateLink.

api

rest-api

graphql

Prerequisites

Notify Atlan support

Accept the endpoint connection request
