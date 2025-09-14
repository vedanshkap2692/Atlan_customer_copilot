# Crawl Snowflake
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake)

SnowflakeGet StartedCrawl Snowflake AssetsCrawl SnowflakeMine SnowflakeManage Snowflake in AtlanReferencesTroubleshootingBest Practices

Get Started

Crawl Snowflake AssetsCrawl SnowflakeMine Snowflake

Crawl Snowflake

Mine Snowflake

Manage Snowflake in Atlan

References

Troubleshooting

Best Practices

Connect data

Data Warehouses

Snowflake

Crawl Snowflake Assets

Crawl Snowflake

Once you have configured theSnowflake user permissions, you can establish a connection between Atlan and Snowflake. (If you are also usingAWS PrivateLinkorAzure Private Linkfor Snowflake, you will need to set that up first, too.)

To crawl metadata from Snowflake, review theorder of operationsand then complete the following steps.



## Select the sourceâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake)

To select Snowflake as your source:

In the top right of any screen, navigate toNewand then clickNew Workflow.

From the list of packages, selectSnowflake Assetsand click onSetup Workflow.



## Provide credentialsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake)

Choose your extraction method:

InDirectextraction, Atlan connects to your database and crawls metadata directly.

InOfflineextraction, you will need to firstextract metadata yourselfandmake it available in S3. This is currently only supported when using theinformation schema extraction method to fetch metadata with basic authentication.

InAgentextraction, Atlan's secure agent executes metadata extraction within the organization's environment.



### Direct extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake)

To enter your Snowflake credentials:

ForAccount Identifiers (Host), enter the hostname,AWS PrivateLink endpoint, orAzure Private Link endpointfor your Snowflake instance.

ForAuthentication, choose the method you configured whensetting up the Snowflake user:ForBasicauthentication, enter theUsernameandPasswordyou configured in either Snowflake or the identity provider.infoðªDid you know?Snowflake recommends transitioning away from basic authentication using username and password. Change tokey-pair authenticationfor enhanced security. For any existing Snowflake workflows, you canmodify the crawler configurationto update the authentication method.ForKeypairauthentication, enter theUsername,Encrypted Private Key, andPrivate KeyPasswordyou configured. Atlan only supports encrypted private keys with a non-empty passphrase   -  generally recommended as more secure. An empty passphrase will result in workflow failures. To generate an encrypted private key, refer toSnowflake documentation.ForOkta SSOauthentication,Â enter theUsername,ÂPassword, andAuthenticatoryou configured. TheAuthenticatorwill be theOkta URL endpoint of your Okta account, typically in the form ofhttps://<okta_account_name>.okta.com.

ForBasicauthentication, enter theUsernameandPasswordyou configured in either Snowflake or the identity provider.infoðªDid you know?Snowflake recommends transitioning away from basic authentication using username and password. Change tokey-pair authenticationfor enhanced security. For any existing Snowflake workflows, you canmodify the crawler configurationto update the authentication method.

ForBasicauthentication, enter theUsernameandPasswordyou configured in either Snowflake or the identity provider.

ðªDid you know?Snowflake recommends transitioning away from basic authentication using username and password. Change tokey-pair authenticationfor enhanced security. For any existing Snowflake workflows, you canmodify the crawler configurationto update the authentication method.

ForKeypairauthentication, enter theUsername,Encrypted Private Key, andPrivate KeyPasswordyou configured. Atlan only supports encrypted private keys with a non-empty passphrase   -  generally recommended as more secure. An empty passphrase will result in workflow failures. To generate an encrypted private key, refer toSnowflake documentation.

ForKeypairauthentication, enter theUsername,Encrypted Private Key, andPrivate KeyPasswordyou configured. Atlan only supports encrypted private keys with a non-empty passphrase   -  generally recommended as more secure. An empty passphrase will result in workflow failures. To generate an encrypted private key, refer toSnowflake documentation.

ForOkta SSOauthentication,Â enter theUsername,ÂPassword, andAuthenticatoryou configured. TheAuthenticatorwill be theOkta URL endpoint of your Okta account, typically in the form ofhttps://<okta_account_name>.okta.com.

ForOkta SSOauthentication,Â enter theUsername,ÂPassword, andAuthenticatoryou configured. TheAuthenticatorwill be theOkta URL endpoint of your Okta account, typically in the form ofhttps://<okta_account_name>.okta.com.

https://<okta_account_name>.okta.com

ForRole, select the Snowflake role through which the crawler should run.

ForWarehouse, select the Snowflake warehouse in which the crawler should run.

ClickTest Authenticationto confirm connectivity to Snowflake using these details.

Once successful, at the bottom of the screen, clickNext.



### Offline extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake)

Atlan supports theoffline extraction methodfor fetching metadata from Snowflake. This method uses Atlan's metadata-extractor tool to fetch metadata. You will need to firstextract the metadatayourself and thenmake it available in S3.

To enter your S3 details:

ForBucket name, enter the name of your S3 bucket. If you are reusing Atlan's S3 bucket, you can leave this blank.

ForÂBucket prefix, enter the S3 prefix under which all the metadata files exist. These includedatabases.json,columns-<database>.json, and so on.

databases.json

columns-<database>.json

ForBucket region, enter the name of the S3 region.

When complete, at the bottom of the screen, clickNext.



## Configure the connectionâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake)

To complete the Snowflake connection configuration:

Provide aConnection Namethat represents your source environment. For example, you might use values likeproduction,development,gold, oranalytics.

Provide aConnection Namethat represents your source environment. For example, you might use values likeproduction,development,gold, oranalytics.

production

development

gold

analytics

(Optional) To change the users able to manage this connection, change the users or groups listed underConnection Admins.dangerIf you do not specify any user or group, nobody will be able to manage the connection   -  not even admins.

(Optional) To change the users able to manage this connection, change the users or groups listed underConnection Admins.

If you do not specify any user or group, nobody will be able to manage the connection   -  not even admins.

(Optional) To prevent users from querying any Snowflake data, changeAllow SQL QuerytoNo.

(Optional) To prevent users from querying any Snowflake data, changeAllow SQL QuerytoNo.

(Optional) To prevent users from previewing any Snowflake data, changeAllow Data PreviewtoNo.

(Optional) To prevent users from previewing any Snowflake data, changeAllow Data PreviewtoNo.

At the bottom of the screen, clickNextto proceed.

At the bottom of the screen, clickNextto proceed.



### Agent extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake)

Atlan supports using a Secure Agent for fetching metadata from Snowflake. To use a Secure Agent, follow these steps:

Select theAgenttab.

Configure the Snowflake data source by adding the secret keys for your secret store. For details on the required fields, refer to theDirect extractionsection.

Complete the Secure Agent configuration by following the instructions in theHow to configure Secure Agent for workflow executionguide.

ClickNextafter completing the configuration.



## Configure the crawlerâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake)

Whenmodifyingan existing Snowflake connection, switching to a differentextraction methodwill delete and recreate all assets in the existing connection. If you'd like to change the extraction method,contact Atlan supportÂ for assistance.

Before running the Snowflake crawler, you can further configure it.

You must select theExtraction methodyou configured when youset up Snowflake:

ForInformation SchemaÂmethod, keep the default selection.

Change toAccount UsagemethodÂ and specify the following:Database Nameof the copied Snowflake databaseSchema Nameof the copiedACCOUNT_USAGEschemaIncremental extractionPublic preview- Toggle incremental extraction for faster and more efficient metadata extraction.

Database Nameof the copied Snowflake database

Schema Nameof the copiedACCOUNT_USAGEschema

ACCOUNT_USAGE

Incremental extractionPublic preview- Toggle incremental extraction for faster and more efficient metadata extraction.

You can override the defaults for any of the remaining options:

ForAsset selection, select a filtering option:To select the assets you want to include in crawling, clickInclude by hierarchyand filter for assets down to the database or schema level. (This will default to all assets, if none are specified.)To have the crawler includeDatabases,Schemas, orTables & Viewsbased on a naming convention, clickInclude by regexand specify a regular expression   -  for example, specifyingATLAN_EXAMPLE_DB.*forDatabaseswill include all the matching databases and their child assets.To select the assets you want to exclude from crawling, clickExclude by hierarchyand filter for assets down to the database or schema level. (This will default to no assets, if none are specified.)ÂTo have the crawler ignoreDatabases,Schemas, orTables & Viewsbased on a naming convention, clickExclude by regexand specify a regular expression   -  for example, specifyingATLAN_EXAMPLE_TABLES.*forTables & Viewswill exclude all the matching tables and views.Click+to add more filters. If you add multiple filters, assets will be crawled based on matchingallthe filtering conditions you have set.

ForAsset selection, select a filtering option:

To select the assets you want to include in crawling, clickInclude by hierarchyand filter for assets down to the database or schema level. (This will default to all assets, if none are specified.)

To have the crawler includeDatabases,Schemas, orTables & Viewsbased on a naming convention, clickInclude by regexand specify a regular expression   -  for example, specifyingATLAN_EXAMPLE_DB.*forDatabaseswill include all the matching databases and their child assets.

ATLAN_EXAMPLE_DB.*

To select the assets you want to exclude from crawling, clickExclude by hierarchyand filter for assets down to the database or schema level. (This will default to no assets, if none are specified.)Â

To have the crawler ignoreDatabases,Schemas, orTables & Viewsbased on a naming convention, clickExclude by regexand specify a regular expression   -  for example, specifyingATLAN_EXAMPLE_TABLES.*forTables & Viewswill exclude all the matching tables and views.

ATLAN_EXAMPLE_TABLES.*

Click+to add more filters. If you add multiple filters, assets will be crawled based on matchingallthe filtering conditions you have set.

To exclude lineage for views in Snowflake, changeView Definition LineagetoNo.

To exclude lineage for views in Snowflake, changeView Definition LineagetoNo.

Toimport tags from Snowflake to Atlan, changeImport TagstoYes. Note the following:If using theAccount Usageextraction method,grant the same permissionsas required for crawling Snowflake assets to import tags and push updated tags to Snowflake.If using theInformation Schemaextraction method, note that Snowflakestores all tag objectsin theACCOUNT_USAGEschema. You will need togrant permissions on the account usage schema instead to import tagsfrom Snowflake.dangerObject tagging in Snowflake currently requiresEnterprise Edition or higher. If your organization does not have Enterprise Edition or higher and you try to import Snowflake tags to Atlan, the Snowflake connection will fail with an error   -  unable to retrieve tags.

Toimport tags from Snowflake to Atlan, changeImport TagstoYes. Note the following:

If using theAccount Usageextraction method,grant the same permissionsas required for crawling Snowflake assets to import tags and push updated tags to Snowflake.

If using theInformation Schemaextraction method, note that Snowflakestores all tag objectsin theACCOUNT_USAGEschema. You will need togrant permissions on the account usage schema instead to import tagsfrom Snowflake.

ACCOUNT_USAGE

Object tagging in Snowflake currently requiresEnterprise Edition or higher. If your organization does not have Enterprise Edition or higher and you try to import Snowflake tags to Atlan, the Snowflake connection will fail with an error   -  unable to retrieve tags.

ForControl Config, keepDefaultfor the default configuration or clickCustomto further configure the crawler:If you have received a custom crawler configuration from Atlan support, forCustom Config, enter the value provided. You can also:Enter{"ignore-all-case": true}to enable crawling assets with case-sensitive identifiers.ForEnable Source Level Filtering, clickTrueto enable schema-level filtering at source or keepFalseto disable it.ForUse JDBC Internal Methods, clickTrueto enable JDBC internal methods for data extraction or clickFalseto disable it.ForExclude tables with empty data, change toYesto exclude any tables and corresponding columns without any data.ForExclude views, change toYesto exclude all views from crawling.

ForControl Config, keepDefaultfor the default configuration or clickCustomto further configure the crawler:

If you have received a custom crawler configuration from Atlan support, forCustom Config, enter the value provided. You can also:Enter{"ignore-all-case": true}to enable crawling assets with case-sensitive identifiers.

Enter{"ignore-all-case": true}to enable crawling assets with case-sensitive identifiers.

{"ignore-all-case": true}

ForEnable Source Level Filtering, clickTrueto enable schema-level filtering at source or keepFalseto disable it.

ForUse JDBC Internal Methods, clickTrueto enable JDBC internal methods for data extraction or clickFalseto disable it.

ForExclude tables with empty data, change toYesto exclude any tables and corresponding columns without any data.

ForExclude views, change toYesto exclude all views from crawling.

If an asset appears in both the include and exclude filters, the exclude filter takes precedence.



## Run the crawlerâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/crawl-snowflake)

To run the Snowflake crawler, after completing the steps above:

To check for anypermissions or other configuration issuesbefore running the crawler, clickPreflight checks.

You can either:To run the crawler once immediately, at the bottom of the screen, click theRunbutton.To schedule the crawler to run hourly, daily, weekly, or monthly, at the bottom of the screen, click theSchedule Runbutton.

To run the crawler once immediately, at the bottom of the screen, click theRunbutton.

To schedule the crawler to run hourly, daily, weekly, or monthly, at the bottom of the screen, click theSchedule Runbutton.

Once the crawler has completed running, you will see the assets in Atlan's asset page! ð

Note that the Atlan crawler will currently skip any unsupported data types to ensure a successful workflow run.

connectors

data

crawl

Select the source

Provide credentials

Configure the connection

Configure the crawler

Run the crawler
