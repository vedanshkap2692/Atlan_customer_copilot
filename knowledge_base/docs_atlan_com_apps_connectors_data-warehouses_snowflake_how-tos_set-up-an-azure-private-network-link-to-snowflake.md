# Set up an Azure private network link to Snowflake
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-an-azure-private-network-link-to-snowflake)

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

Set up an Azure private network link to Snowflake

Azure Private Linkcreates a secure, private connection between services running in Azure. This document describes the steps to set this up between Snowflake and Atlan.

You will need Snowflake Support, and probably your Snowflake administrator involved   -  you may not have access or the tools to run these tasks.



## Prerequisitesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-an-azure-private-network-link-to-snowflake)

Snowflake must be set up with Business Critical Edition (or higher).

Open a ticket with Snowflake Support to enable Azure Private Link for your Snowflake account.

Snowflake support will take 1-2 days to review and enable Azure Private Link.

If you are using IP allowlist in your Snowflake instance, you must add the Atlan IP to the allowlist. Pleaseraise a support requestto do so.

(For all details, see theSnowflake documentation.)



## Fetch Private Link informationâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-an-azure-private-network-link-to-snowflake)

Log in to snowCLI using theACCOUNTADMINaccount, and run the following commands:

ACCOUNTADMIN

use role accountadmin;select system$get_privatelink_config();

use role accountadmin;select system$get_privatelink_config();

This will produce an output like the following (formatted here for readability):

{"regionless-snowsight-privatelink-url": "abc123.privatelink.snowflakecomputing.com","privatelink-account-name": "abc123.west-europe.privatelink","snowsight-privatelink-url": "abc123.west-europe.privatelink.snowflakecomputing.com","privatelink-account-url": "abc123.west-europe.privatelink.snowflakecomputing.com","privatelink-connection-ocsp-urls": "[]","privatelink-pls-id": "abc123.westeurope.azure.privatelinkservice","regionless-privatelink-account-url": "abc123.privatelink.snowflakecomputing.com","privatelink_ocsp-url": "ocsp.abc123.west-europe.privatelink.snowflakecomputing.com","privatelink-connection-urls": "[]"}

{"regionless-snowsight-privatelink-url": "abc123.privatelink.snowflakecomputing.com","privatelink-account-name": "abc123.west-europe.privatelink","snowsight-privatelink-url": "abc123.west-europe.privatelink.snowflakecomputing.com","privatelink-account-url": "abc123.west-europe.privatelink.snowflakecomputing.com","privatelink-connection-ocsp-urls": "[]","privatelink-pls-id": "abc123.westeurope.azure.privatelinkservice","regionless-privatelink-account-url": "abc123.privatelink.snowflakecomputing.com","privatelink_ocsp-url": "ocsp.abc123.west-europe.privatelink.snowflakecomputing.com","privatelink-connection-urls": "[]"}



## Share details with Atlan support teamâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-an-azure-private-network-link-to-snowflake)

Share the following values with theAtlan support team:

regionless-snowsight-privatelink-url

regionless-snowsight-privatelink-url

privatelink-account-name

privatelink-account-name

snowsight-privatelink-url

snowsight-privatelink-url

privatelink-account-url

privatelink-account-url

privatelink-connection-ocsp-urls

privatelink-connection-ocsp-urls

privatelink-pls-id

privatelink-pls-id

regionless-privatelink-account-url

regionless-privatelink-account-url

privatelink_ocsp-url

privatelink_ocsp-url

privatelink-connection-urls

privatelink-connection-urls

Atlan support will finish the configuration on the Atlan side using these values. Support will then provide you with the Snowflake private endpoint resource ID and Azure token for you to approve the request.



## Approve the endpoint connection requestâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-an-azure-private-network-link-to-snowflake)

Log in to snowCLI using theACCOUNTADMINaccount, and run the following commands:

ACCOUNTADMIN

use role accountadmin;SELECT SYSTEM$AUTHORIZE_PRIVATELINK ('/subscriptions/26d.../resourcegroups/sf-1/providers/microsoft.network/privateendpoints/test-self-service','eyJ...');

use role accountadmin;SELECT SYSTEM$AUTHORIZE_PRIVATELINK ('/subscriptions/26d.../resourcegroups/sf-1/providers/microsoft.network/privateendpoints/test-self-service','eyJ...');

Snowflake will return anAccountÂ isÂ authorizedÂ forÂ PrivateLink.message to confirm successful authorization. The status of the private endpoint in Atlan will then change toApproved.

AccountÂ isÂ authorizedÂ forÂ PrivateLink.

Approved

When you use this endpoint in the configuration forcrawlingandminingSnowflake, Atlan will connect to Snowflake over the Private Link.



## (Optional) Configure private endpoint for internal stagesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-an-azure-private-network-link-to-snowflake)

This is only required if you're using Snowflake internal stages. To enable Atlan to securely access your Snowflake internal stages, Atlan will require a private endpoint to your Azure storage account. Refer toSnowflake documentationto learn more.

To configure an Azure private endpoint to access Snowflake internal stages:

Open the Azure portal and navigate to your Azure Storage account.

On theStorage accountspage, select the storage account to connect. From the storage account menu, clickOverview. In theResource JSONform, forResource ID, click the clipboard icon to copy the value andcontact Atlan support to share the value. (Atlan support will finish the configuration on the Atlan side using theResource IDvalue and contact you to confirm endpoint creation.)

From the storage account menu, clickSecurity + networkingand then clickNetworking.

On theNetworkingpage, change to thePrivate endpoint connectionstab and then approve the endpoint connection request from Atlan.

atlan

documentation

Prerequisites

Fetch Private Link information

Share details with Atlan support team

Approve the endpoint connection request

(Optional) Configure private endpoint for internal stages
