# Enable  Snowflake OAuth
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/enable-snowflake-oauth)

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

How to enable Snowflake OAuth

Atlan supportsSnowflake OAuth-based authenticationÂ forSnowflakeconnections. Once the integration has been completed, Atlan will generate a trusted secure token with Snowflake. This will allow Atlan to authenticate users with Snowflake on their behalf to:

Query data with Snowflake OAuth credentials

View sample data with Snowflake OAuth credentials



## Configure Snowflake OAuth in Atlanâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/enable-snowflake-oauth)

You will need to be aconnection adminin Atlan to complete these steps. You will also needÂ inputs and approval from yourSnowflake account administrator.

To configure Snowflake OAuth on a Snowflake connection, from Atlan:

From the left menu of any screen, clickAssets.

From theAssetspage, click theConnectorfilter, and from the dropdown, clickSnowflake.

From the pills below the search bar at the top of the screen, clickConnection.

From the list of results, select a Snowflake connection to enable Snowflake OAuth-based authentication.

From the sidebar on the right, next toConnection settings, clickEdit.

In theConnection settingsdialog:UnderAllow query, forAuthentication type, clickSnowflake OAuthto enforce Snowflake OAuth credentials forquerying data:ForAuthentication Required, clickCopy Codeto copy a security authorization code toexecute it in Snowflake.UnderÂDisplay sample data, forSource preview, clickSnowflake OAuthto enforce Snowflake OAuth credentials forviewing sample data:If Snowflake OAuth-based authentication is enabled for querying data, the same connection details will be reused for viewing sample data.If a different authentication method is enabled for querying data, clickCopy Codeto copy a security authorization code toexecute it in Snowflake.

UnderAllow query, forAuthentication type, clickSnowflake OAuthto enforce Snowflake OAuth credentials forquerying data:ForAuthentication Required, clickCopy Codeto copy a security authorization code toexecute it in Snowflake.

ForAuthentication Required, clickCopy Codeto copy a security authorization code toexecute it in Snowflake.

UnderÂDisplay sample data, forSource preview, clickSnowflake OAuthto enforce Snowflake OAuth credentials forviewing sample data:If Snowflake OAuth-based authentication is enabled for querying data, the same connection details will be reused for viewing sample data.If a different authentication method is enabled for querying data, clickCopy Codeto copy a security authorization code toexecute it in Snowflake.

If Snowflake OAuth-based authentication is enabled for querying data, the same connection details will be reused for viewing sample data.

If a different authentication method is enabled for querying data, clickCopy Codeto copy a security authorization code toexecute it in Snowflake.

(Optional) Toggle onEnable data policies created at source to apply for querying in Atlanto apply any data policies and user permissions at source to querying data and viewing sample data in Atlan. If toggled on, any existingdata policieson the connection in Atlan will be deactivated and creation of new data policies will be disabled.

At the bottom right of theConnection settingsdialog, clickUpdate.

The refresh token does not expire by default.



## Create a security integration in Snowflakeâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/enable-snowflake-oauth)

You will need yourSnowflake account administratorto run these commands. You will also need to have anexisting Snowflake connectionin Atlan.

To create a security integration in Snowflake:

Log in to your Snowflake instance.

Log in to your Snowflake instance.

From the top right of your Snowflake instance, click the+button, and then from the dropdown, clickSQL Worksheetto open a new worksheet.

From the top right of your Snowflake instance, click the+button, and then from the dropdown, clickSQL Worksheetto open a new worksheet.

In the query editor of your Snowflake SQL worksheet, paste thesecurity authorization code you copied in Atlan. See a representative example below:CREATESECURITYINTEGRATION<name>TYPE=EXTERNAL_OAUTHENABLED=TRUEEXTERNAL_OAUTH_TYPE=OKTAEXTERNAL_OAUTH_ISSUER='https://<COMPANY>.okta.com/oauth2/<ID>'EXTERNAL_OAUTH_JWS_KEYS_URL='https://<COMPANY>.okta.com/oauth2/<ID>/v1/keys'EXTERNAL_OAUTH_AUDIENCE_LIST=('<snowflake_account_url')EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM='sub'EXTERNAL_OAUTH_ANY_ROLE_MODE='ENABLE';EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE='EMAIL_ADDRESS'

In the query editor of your Snowflake SQL worksheet, paste thesecurity authorization code you copied in Atlan. See a representative example below:

CREATESECURITYINTEGRATION<name>TYPE=EXTERNAL_OAUTHENABLED=TRUEEXTERNAL_OAUTH_TYPE=OKTAEXTERNAL_OAUTH_ISSUER='https://<COMPANY>.okta.com/oauth2/<ID>'EXTERNAL_OAUTH_JWS_KEYS_URL='https://<COMPANY>.okta.com/oauth2/<ID>/v1/keys'EXTERNAL_OAUTH_AUDIENCE_LIST=('<snowflake_account_url')EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM='sub'EXTERNAL_OAUTH_ANY_ROLE_MODE='ENABLE';EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE='EMAIL_ADDRESS'

CREATESECURITYINTEGRATION<name>TYPE=EXTERNAL_OAUTHENABLED=TRUEEXTERNAL_OAUTH_TYPE=OKTAEXTERNAL_OAUTH_ISSUER='https://<COMPANY>.okta.com/oauth2/<ID>'EXTERNAL_OAUTH_JWS_KEYS_URL='https://<COMPANY>.okta.com/oauth2/<ID>/v1/keys'EXTERNAL_OAUTH_AUDIENCE_LIST=('<snowflake_account_url')EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM='sub'EXTERNAL_OAUTH_ANY_ROLE_MODE='ENABLE';EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE='EMAIL_ADDRESS'

Run the security integration in Snowflake.

Run the security integration in Snowflake.

(Optional) To allow theACCOUNTADMIN,ORGADMIN, orSECURITYADMINrole to query with Snowflake OAuth-based authentication, add and run the following command to set account-level permissions:ALTERACCOUNTSETEXTERNAL_OAUTH_ADD_PRIVILEGED_ROLES_TO_BLOCKED_LIST=FALSE;

(Optional) To allow theACCOUNTADMIN,ORGADMIN, orSECURITYADMINrole to query with Snowflake OAuth-based authentication, add and run the following command to set account-level permissions:

ACCOUNTADMIN

ORGADMIN

SECURITYADMIN

ALTERACCOUNTSETEXTERNAL_OAUTH_ADD_PRIVILEGED_ROLES_TO_BLOCKED_LIST=FALSE;

ALTERACCOUNTSETEXTERNAL_OAUTH_ADD_PRIVILEGED_ROLES_TO_BLOCKED_LIST=FALSE;

Your users will now be able torun queriesandview sample datausing their Snowflake OAuth credentials! ð

You can refer totroubleshooting connector-specific SSO authenticationto troubleshoot any errors.

connectors

data

integration

authentication

Configure Snowflake OAuth in Atlan

Create a security integration in Snowflake
