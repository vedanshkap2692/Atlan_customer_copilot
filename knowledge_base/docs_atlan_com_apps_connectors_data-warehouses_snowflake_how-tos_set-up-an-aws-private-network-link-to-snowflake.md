# Set up an AWS private network link to Snowflake
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-an-aws-private-network-link-to-snowflake)

SnowflakeGet StartedSet up SnowflakeSet up an AWS private network link to SnowflakeSet up an Azure private network link to SnowflakeHow to enable Snowflake OAuthCrawl Snowflake AssetsManage Snowflake in AtlanReferencesTroubleshootingBest Practices

Get StartedSet up SnowflakeSet up an AWS private network link to SnowflakeSet up an Azure private network link to SnowflakeHow to enable Snowflake OAuth

Set up Snowflake

Set up an AWS private network link to Snowflake

Set up an Azure private network link to Snowflake

How to enable Snowflake OAuth

Crawl Snowflake Assets

Manage Snowflake in Atlan

References

Troubleshooting

Best Practices

Connect data

Data Warehouses

Snowflake

Get Started

Set up an AWS private network link to Snowflake

AWS PrivateLinkcreates a secure, private connection between services running in AWS. This document describes the steps to set this up between Snowflake and Atlan, when you use our Single Tenant SaaS deployment.

You will need Snowflake Support, and probably your Snowflake administrator involved   -  you may not have access or the tools to run these tasks.



## Prerequisitesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-an-aws-private-network-link-to-snowflake)

Snowflake must be setup with Business Critical Edition (or higher).

Open a ticket with Snowflake Support to enable PrivateLink for your Snowflake account.

Snowflake support will take 1-2 days to review and enable PrivateLink.

If you are using IP allowlist in your Snowflake instance, you must add the Atlan IP to the allowlist. Pleaseraise a support requestto do so.

(For all details, see theSnowflake documentation.)



## Fetch PrivateLink informationâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-an-aws-private-network-link-to-snowflake)

Log in to snowCLI using theACCOUNTADMINaccount, and run the following commands:

ACCOUNTADMIN

use role accountadmin;select system$get_privatelink_config();

use role accountadmin;select system$get_privatelink_config();

This will produce output like the following (formatted here for readability):

{"privatelink-account-name":"abc123.ap-south-1.privatelink","privatelink-vpce-id":"com.amazonaws.vpce.ap-south-1.vpce-svc-257a4d536bd8e3594","privatelink-account-url":"abc123.ap-south-1.privatelink.snowflakecomputing.com","regionless-privatelink-account-url":"xyz789-abc123.privatelink.snowflakecomputing.com","privatelink_ocsp-url":"ocsp.abc123.ap-south-1.privatelink.snowflakecomputing.com","privatelink-connection-urls":"[]"}

{"privatelink-account-name":"abc123.ap-south-1.privatelink","privatelink-vpce-id":"com.amazonaws.vpce.ap-south-1.vpce-svc-257a4d536bd8e3594","privatelink-account-url":"abc123.ap-south-1.privatelink.snowflakecomputing.com","regionless-privatelink-account-url":"xyz789-abc123.privatelink.snowflakecomputing.com","privatelink_ocsp-url":"ocsp.abc123.ap-south-1.privatelink.snowflakecomputing.com","privatelink-connection-urls":"[]"}



## Share details with Atlan support teamâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-an-aws-private-network-link-to-snowflake)

Share the following values with theAtlan supportteam:

privatelink-account-name

privatelink-account-name

privatelink-vpce-id

privatelink-vpce-id

privatelink-account-url

privatelink-account-url

privatelink_ocsp-url

privatelink_ocsp-url

Atlan support will finish the configuration on the Atlan side using these values. Support will then provide the Snowflake PrivateLink endpoint back to you.

When you use this endpoint in the configuration forcrawlingandmining, Atlan will connect to Snowflake over the PrivateLink.

atlan

documentation

Prerequisites

Fetch PrivateLink information

Share details with Atlan support team
