# Set up Snowflake
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

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

Set up Snowflake

You need your Snowflake administrator to run these commands   -  you may not have access yourself.



## Create user and role in Snowflakeâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Create a role and user in Snowflake using the following commands:



### Create roleâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Create a role in Snowflake using the following commands:

CREATEORREPLACEROLE atlan_user_role;GRANTOPERATE,USAGEONWAREHOUSE"<warehouse-name>"TOROLE atlan_user_role;

CREATEORREPLACEROLE atlan_user_role;GRANTOPERATE,USAGEONWAREHOUSE"<warehouse-name>"TOROLE atlan_user_role;

Replace<warehouse-name>with the default warehouse to use whenrunning the Snowflake crawler.

<warehouse-name>

Atlan requires the following privileges to:

OPERATEenables Atlan to start the virtual warehouse to fetch metadata if the warehouse has stopped.

OPERATE

USAGEenables Atlan to show or list metadata from Snowflake. This in turn enables theSnowflake crawlerto run theSHOWquery.

USAGE

SHOW



### Create a userâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Create a separate user to integrate into Atlan, using one of the following 3 options:



#### With a public key in Snowflakeâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

SeeSnowflake's official guide for details on generating an RSA key-pair. To create a user with a key-pair, replace the value forrsa_public_keywith the public key and run the following:

rsa_public_key

CREATEUSERatlan_user rsa_public_key='MIIBIjANBgkqh...'default_role=atlan_user_role default_warehouse='<warehouse-name>'display_name='Atlan'TYPE='SERVICE'

CREATEUSERatlan_user rsa_public_key='MIIBIjANBgkqh...'default_role=atlan_user_role default_warehouse='<warehouse-name>'display_name='Atlan'TYPE='SERVICE'

Learn more about theSERVICEtype property inSnowflake documentation.

SERVICE

Atlan only supports encrypted private keys with a non-empty passphrase   -  generally recommended as more secure. An empty passphrase results in workflow failures. To generate an encrypted private key, omit the-nocryptoption. Refer toSnowflake documentationto learn more.

-nocrypt



#### With a password in Snowflakeâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Snowflake recommends transitioning away from basic authentication using username and password. Change to key-pair authentication for enhanced security. For any existing Snowflake workflows, you canmodify the crawler configurationto update the authentication method.

To create a user with a password, replace<password>and run the following:

<password>

CREATEUSERatlan_user password='<password>'default_role=atlan_user_role default_warehouse='<warehouse-name>'display_name='Atlan'TYPE='LEGACY_SERVICE'

CREATEUSERatlan_user password='<password>'default_role=atlan_user_role default_warehouse='<warehouse-name>'display_name='Atlan'TYPE='LEGACY_SERVICE'

Learn more about theLEGACY_SERVICEtype property inSnowflake documentation.

LEGACY_SERVICE



#### Managed through your identity provider (IdP)Private previewâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

This method is currently only available if Okta is your IdP (Snowflake supports)authenticating natively through Okta:

Create a user in your identity provider (IdP) anduse federated authentication in Snowflake.

The password for this user must be maintained solely in the IdP and multi-factor authentication (MFA) must be disabled.



### Grant role to userâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

To grant theatlan_user_roleto the new user:

atlan_user_role

GRANTROLE atlan_user_roleTOUSERatlan_user;

GRANTROLE atlan_user_roleTOUSERatlan_user;



### Configure OAuth (client credentials flow) with Microsoft Entra IDâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

To configure OAuth authentication using Microsoft Entra ID (formerly Azure AD) with the client credentials flow:

FollowSnowflake's documentationto:Register a new application in Microsoft Entra IDCollect theclient ID,tenant ID, andclient secretAdd the required API permissions

FollowSnowflake's documentationto:

Register a new application in Microsoft Entra ID

Collect theclient ID,tenant ID, andclient secret

client ID

tenant ID

client secret

Add the required API permissions

In Snowflake, create a security integration using the following:CREATESECURITY INTEGRATION external_oauth_azure_adTYPE=external_oauthENABLED=trueEXTERNAL_OAUTH_TYPE=azureEXTERNAL_OAUTH_ISSUER='\<AZURE_AD_ISSUER\>'EXTERNAL_OAUTH_JWS_KEYS_URL='\<AZURE_AD_JWS_KEY_ENDPOINT\>'EXTERNAL_OAUTH_AUDIENCE_LIST=('\<SNOWFLAKE_APPLICATION_ID_URI\>')EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM='sub'EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE='login_name';Replace the placeholders with actual values from your Azure AD app:<AZURE_AD_ISSUER>â Your tenant's OAuth 2.0 issuer URL<AZURE_AD_JWS_KEY_ENDPOINT>â Azure JWKs URI<SNOWFLAKE_APPLICATION_ID_URI>â Application ID URI of the Azure app

In Snowflake, create a security integration using the following:

CREATESECURITY INTEGRATION external_oauth_azure_adTYPE=external_oauthENABLED=trueEXTERNAL_OAUTH_TYPE=azureEXTERNAL_OAUTH_ISSUER='\<AZURE_AD_ISSUER\>'EXTERNAL_OAUTH_JWS_KEYS_URL='\<AZURE_AD_JWS_KEY_ENDPOINT\>'EXTERNAL_OAUTH_AUDIENCE_LIST=('\<SNOWFLAKE_APPLICATION_ID_URI\>')EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM='sub'EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE='login_name';

CREATESECURITY INTEGRATION external_oauth_azure_adTYPE=external_oauthENABLED=trueEXTERNAL_OAUTH_TYPE=azureEXTERNAL_OAUTH_ISSUER='\<AZURE_AD_ISSUER\>'EXTERNAL_OAUTH_JWS_KEYS_URL='\<AZURE_AD_JWS_KEY_ENDPOINT\>'EXTERNAL_OAUTH_AUDIENCE_LIST=('\<SNOWFLAKE_APPLICATION_ID_URI\>')EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM='sub'EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE='login_name';

Replace the placeholders with actual values from your Azure AD app:

<AZURE_AD_ISSUER>â Your tenant's OAuth 2.0 issuer URL

<AZURE_AD_ISSUER>

<AZURE_AD_JWS_KEY_ENDPOINT>â Azure JWKs URI

<AZURE_AD_JWS_KEY_ENDPOINT>

<SNOWFLAKE_APPLICATION_ID_URI>â Application ID URI of the Azure app

<SNOWFLAKE_APPLICATION_ID_URI>

Create a Snowflake user with a login name that exactly matches the Azure AD client object ID:CREATEUSERoauth_svc_userWITHLOGIN_NAME='\<AZURE_AD_CLIENT_OBJECT_ID\>'-- Use Azure client OBJECT IDDEFAULT_ROLE=\<ROLE\>DEFAULT_WAREHOUSE=\<WAREHOUSE\>;

Create a Snowflake user with a login name that exactly matches the Azure AD client object ID:

CREATEUSERoauth_svc_userWITHLOGIN_NAME='\<AZURE_AD_CLIENT_OBJECT_ID\>'-- Use Azure client OBJECT IDDEFAULT_ROLE=\<ROLE\>DEFAULT_WAREHOUSE=\<WAREHOUSE\>;

CREATEUSERoauth_svc_userWITHLOGIN_NAME='\<AZURE_AD_CLIENT_OBJECT_ID\>'-- Use Azure client OBJECT IDDEFAULT_ROLE=\<ROLE\>DEFAULT_WAREHOUSE=\<WAREHOUSE\>;

Grant the configured role to this user:GRANTROLE \<ROLE\>TOUSERoauth_svc_user;

Grant the configured role to this user:

GRANTROLE \<ROLE\>TOUSERoauth_svc_user;

GRANTROLE \<ROLE\>TOUSERoauth_svc_user;



## Choose metadata fetching methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Atlan supports two methods for fetching metadata from Snowflake   -  account usage and information schema. You should choose one of these two methods to set up Snowflake:

SNOWFLAKE

SNOWFLAKE

ACCOUNT_USAGE

INFORMATION_SCHEMA

ACCOUNT_USAGE

INFORMATION_SCHEMA

ACCOUNT_USAGE

ACCOUNT_USAGE

ACCOUNT_USAGE

ACCOUNT_USAGE

ACCOUNT_USAGE

ACCOUNT_USAGE



## Grant permissions for account usage methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

If you want to set warehouse timeouts when using this method, set a large value initially for the workflow to succeed. Once the workflow has succeeded, adjust the value to be twice the extraction time.

This method uses the views inSNOWFLAKE.ACCOUNT_USAGE(or a copied version of this schema) to fetch the metadata from Snowflake into Atlan. You can be more granular with permissions using this method, but there arelimitations with this approach.

SNOWFLAKE.ACCOUNT_USAGE



### To crawl assets, generate lineage, and import tagsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

If you also want to be able to preview and query the data, you can use the preview and query existing assets permissions instead.

Snowflakestores all tag objectsin theACCOUNT_USAGEschema. If you're using theaccount usage methodto crawl metadata in Atlan or you haveconfigured the Snowflake miner, you need to grant the same permissions toimport tagsas required for crawling Snowflake assets. Note that object tagging in Snowflake currently requiresEnterprise Edition or higher.

ACCOUNT_USAGE

To use the defaultSNOWFLAKEdatabase andACCOUNT_USAGEschema and also mine Snowflake's query history (for lineage), grant these permissions:

SNOWFLAKE

ACCOUNT_USAGE

USEROLE ACCOUNTADMIN;GRANTIMPORTEDPRIVILEGESONDATABASESNOWFLAKETOROLE atlan_user_role;

USEROLE ACCOUNTADMIN;GRANTIMPORTEDPRIVILEGESONDATABASESNOWFLAKETOROLE atlan_user_role;

TheACCOUNTADMINrole is required to grant privileges on theSNOWFLAKEdatabase due to the following reasons:By default, only theACCOUNTADMINrole can access theSNOWFLAKEdatabase.To enable other roles to access the database and schemas and query the views, a user with theACCOUNTADMINrole needs to grantIMPORTED PRIVILEGESon theSNOWFLAKEdatabase to the desired roles.

TheACCOUNTADMINrole is required to grant privileges on theSNOWFLAKEdatabase due to the following reasons:

ACCOUNTADMIN

SNOWFLAKE

By default, only theACCOUNTADMINrole can access theSNOWFLAKEdatabase.

ACCOUNTADMIN

SNOWFLAKE

To enable other roles to access the database and schemas and query the views, a user with theACCOUNTADMINrole needs to grantIMPORTED PRIVILEGESon theSNOWFLAKEdatabase to the desired roles.

ACCOUNTADMIN

IMPORTED PRIVILEGES

SNOWFLAKE

To use a copied or cloned version of this default schema, where you can also remove any sensitive data for security purposes, grant these permissions:

To use a copied or cloned version of this default schema, where you can also remove any sensitive data for security purposes, grant these permissions:

GRANTUSAGEONDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTUSAGEONSCHEMA"<copied-schema>"INDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<copied-database>"TOROLE atlan_user_role;

GRANTUSAGEONDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTUSAGEONSCHEMA"<copied-schema>"INDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<copied-database>"TOROLE atlan_user_role;

Replace<copied-database>with the copied Snowflake database name.

<copied-database>

Replace<copied-schema>with the copied SnowflakeACCOUNT_USAGEschema name.

<copied-schema>

ACCOUNT_USAGE

The grants for the copied version can't be used on the originalSNOWFLAKEdatabase. This is because Snowflake produces an error that granular grants can't be given to imported databases.

SNOWFLAKE

When using a cloned or copied version, verify that the table or view definition remains unchanged as in yourSNOWFLAKEdatabase. If the format is different. For example, a column is missing and it no longer qualifies as a clone.

SNOWFLAKE



### To crawl streamsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

To crawl streams, provide the following permissions:

To crawl current streams:

GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONALLTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLSTREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;

GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONALLTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLSTREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;

Replace<database-name>with the Snowflake database name.

Replace<database-name>with the Snowflake database name.

<database-name>

To crawl future streams:

To crawl future streams:

GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;

GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;

Replace<database-name>with the Snowflake database name.

<database-name>



### (Optional) To preview and query existing assetsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

To query and preview data within assets that already exist in Snowflake, add these permissions:

GRANTUSAGEONDATABASE"<database-name>"TOROLE atlan_user_role;GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLEXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLVIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLMATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLSTREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONPIPE"<pipe-name>"TOROLE atlan_user_role;

GRANTUSAGEONDATABASE"<database-name>"TOROLE atlan_user_role;GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLEXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLVIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLMATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLSTREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONPIPE"<pipe-name>"TOROLE atlan_user_role;

Replace<database-name>with the database you want to be able to preview and query in Atlan. (Repeat the statements for every database you wish to preview and query in Atlan.)

<database-name>



### (Optional) To preview and query future assetsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

To query and preview data within assets that may be created in the future in Snowflake, add these permissions. Again, if you want to also be able to preview and query the data for future assets, you can add the preview and query future assets permissions instead.

GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE EXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE MATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONFUTURE PIPESINDATABASE"<database-name>"TOROLE atlan_user_role;

GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE EXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE MATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONFUTURE PIPESINDATABASE"<database-name>"TOROLE atlan_user_role;

Replace<database-name>with the database you want to be able to preview and query in Atlan. (Repeat the statements for every database you want to preview and query in Atlan.)

<database-name>

Verify that all the assets you'd like to crawl are present in these grants bychecking the grantson the user role defined for the crawler.



## Grant permissions for information schema methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

This method uses views in theINFORMATION_SCHEMAschema in Snowflake databases to fetch metadata. You still need to grant specific permissions to enable Atlan to crawl metadata, preview data, and query data with this method.

INFORMATION_SCHEMA



### To crawl existing assetsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Grant these permissions to crawl assets that already exist in Snowflake. If you also want to be able to preview and query the data, you can use the preview and query existing assets permissions instead.

Grant permissions to crawl existing assets:

GRANTUSAGEONDATABASE"<database-name>"TOROLE atlan_user_role;GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONALLTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONALLEXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONALLMATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLSTREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONPIPE"<pipe-name>"TOROLE atlan_user_role;

GRANTUSAGEONDATABASE"<database-name>"TOROLE atlan_user_role;GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONALLTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONALLEXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONALLMATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLSTREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONPIPE"<pipe-name>"TOROLE atlan_user_role;

Replace<database-name>with the database you want to be available in Atlan. (Repeat the statements for every database you wish to integrate into Atlan.)

<database-name>

Grant permissions to crawl functions:

GRANTUSAGEONALLFUNCTIONSINDATABASE"<database-name>"TOROLE atlan_user_role;

GRANTUSAGEONALLFUNCTIONSINDATABASE"<database-name>"TOROLE atlan_user_role;

Replace<database-name>with the database you want to be available in Atlan. (Repeat the statements for every database you wish to integrate into Atlan.)

<database-name>

For secure user-defined functions (UDFs), grantOWNERSHIPpermissions to retrieve metadata:

GRANTOWNERSHIPONFUNCTION<schema_name>.<udf_name>TOROLE<role_name>;

GRANTOWNERSHIPONFUNCTION<schema_name>.<udf_name>TOROLE<role_name>;

Replace the placeholders with the appropriate values:

<schema_name>: The name of the schema that contains the user-defined function (UDF).

<schema_name>

<udf_name>: The name of the secure UDF that requires ownership permissions.

<udf_name>

<role_name>: The role that gets assigned ownership of the secure UDF.

<role_name>

The statements given on this page apply to all schemas, tables, and views in a database in Snowflake. If you want to limit access to only certain objects, you can instead specify the exact objects individually as well.



### To crawl future assetsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

To crawl assets that may be created in the future in Snowflake, add these permissions. Again, if you want to also be able to preview and query the data for future assets, you can add the preview and query future assets permissions instead.

To grant permissions at a database level:

GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE EXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE MATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONFUTURE PIPESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTUSAGEONFUTURE FUNCTIONSINDATABASE"<database-name>"TOROLE atlan_user_role;

GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE EXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE MATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONFUTURE PIPESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTUSAGEONFUTURE FUNCTIONSINDATABASE"<database-name>"TOROLE atlan_user_role;

Replace<database-name>with the database you want to crawl in Atlan. (Repeat the statements for every database you want to integrate into Atlan.)

<database-name>

For any future grants defined at a schema level to a different role, the schema-level grants take precedence over the database-level grants and any future grants defined at a database level to the Atlan role get ignored. To learn more, refer toSnowflake documentation.

To grant permissions at a schema level:

GRANTREFERENCESONFUTURETABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE EXTERNALTABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE VIEWSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE MATERIALIZED VIEWSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTMONITORONFUTURE PIPESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;

GRANTREFERENCESONFUTURETABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE EXTERNALTABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE VIEWSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE MATERIALIZED VIEWSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTMONITORONFUTURE PIPESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;

Replace<database-name>with the database and<schema-name>with the schema you want to crawl in Atlan. (Repeat the statements for every database and schema you want to integrate into Atlan.)

<database-name>

<schema-name>



### To mine query history for lineageâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

To also mine Snowflake's query history (for lineage), add these permissions. You can use either option:

To mine query history direct from Snowflake's internal tables:

USEROLE ACCOUNTADMIN;GRANTIMPORTEDPRIVILEGESONDATABASEsnowflakeTOROLE atlan_user_role;

USEROLE ACCOUNTADMIN;GRANTIMPORTEDPRIVILEGESONDATABASEsnowflakeTOROLE atlan_user_role;

To mine query history from a cloned or copied set of tables, where you can also remove any sensitive data:

GRANTUSAGEONDATABASE"<cloned-database>"TOROLE atlan_user_role;GRANTUSAGEONSCHEMA"<cloned-database>"."<cloned-account-usage-schema>"TOROLE atlan_user_role;GRANTSELECTONALLTABLESINSCHEMA"<cloned-database>"."<cloned-account-usage-schema>"TOROLE atlan_user_role;GRANTSELECTONALLVIEWSINSCHEMA"<cloned-database>"."<cloned-account-usage-schema>"TOROLE atlan_user_role;

GRANTUSAGEONDATABASE"<cloned-database>"TOROLE atlan_user_role;GRANTUSAGEONSCHEMA"<cloned-database>"."<cloned-account-usage-schema>"TOROLE atlan_user_role;GRANTSELECTONALLTABLESINSCHEMA"<cloned-database>"."<cloned-account-usage-schema>"TOROLE atlan_user_role;GRANTSELECTONALLVIEWSINSCHEMA"<cloned-database>"."<cloned-account-usage-schema>"TOROLE atlan_user_role;

Replace<cloned-database>with the name of the cloned database, and<cloned-account-usage-schema>with the name of the cloned schema containing account usage details.

<cloned-database>

<cloned-account-usage-schema>

When using a cloned or copied version, verify that the table or view definition remains unchanged as in yourSNOWFLAKEdatabase. If the format is different. For example, a column is missing and it no longer qualifies as a clone.

SNOWFLAKE



### (Optional) To preview and query existing assetsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

To query and preview data within assets that already exist in Snowflake, add these permissions:

GRANTUSAGEONDATABASE"<database-name>"TOROLE atlan_user_role;GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLEXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLVIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLMATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLSTREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONPIPE"<pipe-name>"TOROLE atlan_user_role;

GRANTUSAGEONDATABASE"<database-name>"TOROLE atlan_user_role;GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLEXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLVIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLMATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONALLSTREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONPIPE"<pipe-name>"TOROLE atlan_user_role;

Replace<database-name>with the database you want to be able to preview and query in Atlan. (Repeat the statements for every database you wish to preview and query in Atlan.)

<database-name>



### (Optional) To preview and query future assetsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

To query and preview data within assets that may be created in the future in Snowflake, add these permissions. Again, if you want to also be able to preview and query the data for future assets, you can add the preview and query future assets permissions instead.

GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE EXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE MATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONFUTURE PIPESINDATABASE"<database-name>"TOROLE atlan_user_role;

GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE EXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE MATERIALIZED VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTMONITORONFUTURE PIPESINDATABASE"<database-name>"TOROLE atlan_user_role;

Replace<database-name>with the database you want to be able to preview and query in Atlan. (Repeat the statements for every database you want to preview and query in Atlan.)

<database-name>

For any future grants defined at a schema level to a different role, the schema-level grants take precedence over the database-level grants and any future grants defined at a database level to the Atlan role get ignored. To learn more, refer toSnowflake documentation.

To grant permissions at a schema level:

GRANTSELECTONFUTURETABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE EXTERNALTABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE VIEWSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE MATERIALIZED VIEWSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTMONITORONFUTURE PIPESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;

GRANTSELECTONFUTURETABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE EXTERNALTABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE VIEWSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE MATERIALIZED VIEWSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTSELECTONFUTURE STREAMSINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;GRANTMONITORONFUTURE PIPESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;

Replace<database-name>with the database and<schema-name>with the schema you want to be able to preview and query in Atlan. (Repeat the statements for every database and schema you want to preview and query in Atlan.)

<database-name>

<schema-name>

Verify that all the assets you'd like to crawl are present in these grants bychecking the grantson the user role defined for the crawler.



### (Optional) To import Snowflake tagsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Snowflakestores all tag objectsin theACCOUNT_USAGEschema. Note that object tagging in Snowflake currently requiresEnterprise Edition or higher.

ACCOUNT_USAGE

Toimport tags from Snowflake, grant these permissions:

To use the defaultSNOWFLAKEdatabase andACCOUNT_USAGEschema and also mine Snowflake's query history (for lineage), grant these permissions:

SNOWFLAKE

ACCOUNT_USAGE

USEROLE ACCOUNTADMIN;GRANTIMPORTEDPRIVILEGESONDATABASESNOWFLAKETOROLE atlan_user_role;

USEROLE ACCOUNTADMIN;GRANTIMPORTEDPRIVILEGESONDATABASESNOWFLAKETOROLE atlan_user_role;

TheACCOUNTADMINrole is required to grant privileges on theSNOWFLAKEdatabase due to the following reasons:By default, only theACCOUNTADMINrole can access theSNOWFLAKEdatabase.To enable other roles to access the database and schemas and query the views, a user with theACCOUNTADMINrole needs to grantIMPORTED PRIVILEGESon theSNOWFLAKEdatabase to the desired roles.

TheACCOUNTADMINrole is required to grant privileges on theSNOWFLAKEdatabase due to the following reasons:

ACCOUNTADMIN

SNOWFLAKE

By default, only theACCOUNTADMINrole can access theSNOWFLAKEdatabase.

ACCOUNTADMIN

SNOWFLAKE

To enable other roles to access the database and schemas and query the views, a user with theACCOUNTADMINrole needs to grantIMPORTED PRIVILEGESon theSNOWFLAKEdatabase to the desired roles.

ACCOUNTADMIN

IMPORTED PRIVILEGES

SNOWFLAKE

To use a copied or cloned version of this default schema, where you can also remove any sensitive data for security purposes, grant these permissions:

To use a copied or cloned version of this default schema, where you can also remove any sensitive data for security purposes, grant these permissions:

GRANTUSAGEONDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTUSAGEONSCHEMA"<copied-schema>"INDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<copied-database>"TOROLE atlan_user_role;

GRANTUSAGEONDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTUSAGEONSCHEMA"<copied-schema>"INDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<copied-database>"TOROLE atlan_user_role;

Replace<copied-database>with the copied Snowflake database name.

<copied-database>

Replace<copied-schema>with the copied SnowflakeACCOUNT_USAGEschema name.

<copied-schema>

ACCOUNT_USAGE

The grants for the copied version can't be used on the originalSNOWFLAKEdatabase. This is because Snowflake produces an error that granular grants can't be given to imported databases.

SNOWFLAKE



### (Optional) To push updated tags to Snowflakeâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Topush tags updated for assets in Atlan to Snowflake, grant these permissions:

GRANTAPPLYTAGONACCOUNTTOROLE<role-name>;

GRANTAPPLYTAGONACCOUNTTOROLE<role-name>;

You can learn more about tag privileges fromSnowflake documentation.



### (Optional) To crawl dynamic tablesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Atlan currently supports fetching metadata for dynamic tables using theMONITORprivilege. Refer toSnowflake documentationto learn more.

MONITOR

To crawl existing dynamic tables from Snowflake:

Grant permissions at a database level:

GRANTMONITORONALLDYNAMICTABLESINDATABASE"<DATABASE_NAME>"TOROLE atlan_user_role;

GRANTMONITORONALLDYNAMICTABLESINDATABASE"<DATABASE_NAME>"TOROLE atlan_user_role;

Grant permissions at a schema level:

GRANTMONITORONALLDYNAMICTABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;

GRANTMONITORONALLDYNAMICTABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;

To crawl future dynamic tables from Snowflake:

Grant permissions at a database level:

GRANTMONITORONFUTURE DYNAMICTABLESINDATABASE"<DATABASE_NAME>"TOROLE atlan_user_role;

GRANTMONITORONFUTURE DYNAMICTABLESINDATABASE"<DATABASE_NAME>"TOROLE atlan_user_role;

Grant permissions at a schema level:

GRANTMONITORONFUTURE DYNAMICTABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;

GRANTMONITORONFUTURE DYNAMICTABLESINSCHEMA"<database-name>.<schema-name>"TOROLE atlan_user_role;

Replace<database-name>with the database and<schema-name>with the schema you want to crawl in Atlan. (Repeat the statements for every database and schema you want to integrate into Atlan.)

<database-name>

<schema-name>



### (Optional) To crawl Iceberg tablesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Atlan currently supports fetching metadata forIceberg tablesonly for the information schema extraction method.

To crawl Iceberg tables from Snowflake, grant the following permissions:

To crawl existing Iceberg tables in Snowflake:

GRANTREFERENCESONALLICEBERGTABLESINDATABASE<database-name>TOROLE atlan_user_role;

GRANTREFERENCESONALLICEBERGTABLESINDATABASE<database-name>TOROLE atlan_user_role;

To crawl future Iceberg tables in Snowflake:

GRANTREFERENCESONFUTURE ICEBERGTABLESINDATABASE<database-name>TOROLE atlan_user_role;

GRANTREFERENCESONFUTURE ICEBERGTABLESINDATABASE<database-name>TOROLE atlan_user_role;

To crawl Iceberg catalog metadata for Iceberg tables in Snowflake:

GRANTUSAGEONINTEGRATION<integration-name>TOROLE atlan_user_role;

GRANTUSAGEONINTEGRATION<integration-name>TOROLE atlan_user_role;

You must first grant permissions to crawl existing Iceberg tables for this permission to work on catalogs. You must also grant permissions to all the catalogs you want to crawl in Atlan individually.



### (Optional) To crawl Snowflake stagesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

Atlan supports crawling metadata for Snowflake stages using the USAGE and READ privileges. For more information, see the Snowflake documentation for INFORMATION_SCHEMA.STAGES.

To crawl stages from Snowflake:

GrantUSAGEandREADprivileges on all existing stages at the database level:

USAGE

READ

GRANTUSAGEONALLSTAGESINDATABASE<database_name>TOROLE atlan_user_role;GRANTREADONALLSTAGESINDATABASE<database_name>TOROLE atlan_user_role;

GRANTUSAGEONALLSTAGESINDATABASE<database_name>TOROLE atlan_user_role;GRANTREADONALLSTAGESINDATABASE<database_name>TOROLE atlan_user_role;

Replace<database_name>with the name of your Snowflake database

Replace<database_name>with the name of your Snowflake database

<database_name>

Replace<atlan_user_role>with the role you've granted Atlan to use for crawling.

Replace<atlan_user_role>with the role you've granted Atlan to use for crawling.

<atlan_user_role>

GrantUSAGEandREADprivileges on all future stages at the database level:

GrantUSAGEandREADprivileges on all future stages at the database level:

USAGE

READ

GRANTUSAGEONFUTURE STAGESINDATABASE<database_name>TOROLE atlan_user_role;GRANTREADONFUTURE STAGESINDATABASE<database_name>TOROLE atlan_user_role;

GRANTUSAGEONFUTURE STAGESINDATABASE<database_name>TOROLE atlan_user_role;GRANTREADONFUTURE STAGESINDATABASE<database_name>TOROLE atlan_user_role;

Replace<database_name>with the name of your Snowflake database

<database_name>

Replace<atlan_user_role>with the role you've granted Atlan to use for crawling.

<atlan_user_role>



## Allowlist the Atlan IPâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/set-up-snowflake#allowlist-the-atlan-ip)

If you are using the IP allowlist in your Snowflake instance, you must add the Atlan IP to the allowlist. Please raise a support ticket from within Atlan, orsubmit a request.

(If you aren't using the IP allowlist in your Snowflake instance, you can skip this step.)

connectors

data

crawl

Create user and role in Snowflake

Choose metadata fetching method

Grant permissions for account usage method

Grant permissions for information schema method

Allowlist the Atlan IP
