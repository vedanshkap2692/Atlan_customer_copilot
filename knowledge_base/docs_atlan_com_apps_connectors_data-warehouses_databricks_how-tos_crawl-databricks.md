# Crawl Databricks
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

DatabricksGet StartedCross-workspace SetupCrawl Databricks AssetsCrawl DatabricksOn-premises SetupPrivate Network SetupLineage and UsageTag managementReferencesTroubleshooting

Get Started

Cross-workspace Setup

Crawl Databricks AssetsCrawl Databricks

Crawl Databricks

On-premises Setup

Private Network Setup

Lineage and Usage

Tag management

References

Troubleshooting

Connect data

Data Warehouses

Databricks

Crawl Databricks Assets

Crawl Databricks

Once you have configured theDatabricks access permissions, you can establish a connection between Atlan and your Databricks instance. (If you are also usingAWS PrivateLinkorAzure Private Linkfor Databricks, you will need to set that up first, too.)

To crawl metadata from your Databricks instance, review theorder of operationsand then complete the following steps.



## Select the sourceâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

To select Databricks as your source:

In the top right corner of any screen, navigate toNewand then clickNew Workflow.

In the top right corner of any screen, navigate toNewand then clickNew Workflow.

From the list of packages, selectDatabricks Assets, and clickSetup Workflow.

From the list of packages, selectDatabricks Assets, and clickSetup Workflow.



## Provide credentialsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

Choose your extraction method:

InDirectextraction, Atlan connects to your database and crawls metadata directly. Next, select an authentication method:InJDBC, you will need apersonal access token and HTTP path for authentication.InAWS Service, you will need aclient ID and client secret for AWS service principal authentication.InAzure Service, you will need atenant ID, client ID, and client secret for Azure service principal authentication.

InJDBC, you will need apersonal access token and HTTP path for authentication.

InAWS Service, you will need aclient ID and client secret for AWS service principal authentication.

InAzure Service, you will need atenant ID, client ID, and client secret for Azure service principal authentication.

InOfflineextraction, you will need to firstextract metadata yourself and make it available in S3.

InAgentextraction, Atlan's secure agent executes metadata extraction within the organization's environment.



### Direct extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)



#### JDBCâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

To enter your Databricks credentials:

ForHost, enter the hostname,AWS PrivateLink endpoint, orAzure Private Link endpointfor your Databricks instance.

ForPort, enter the port number of your Databricks instance.

ForPersonal Access Token, enter the access token you generated whensetting up access.

ForHTTP Path, enter one of the following:A path starting with/sql/1.0/warehousesto use theDatabricks SQL warehouse.A path starting withsql/protocolv1/oto use theDatabricks interactive cluster.

A path starting with/sql/1.0/warehousesto use theDatabricks SQL warehouse.

/sql/1.0/warehouses

A path starting withsql/protocolv1/oto use theDatabricks interactive cluster.

sql/protocolv1/o

ClickTest Authenticationto confirm connectivity to Databricks using these details.

Once successful, at the bottom of the screen clickNext.

Make sure your Databricks instance (SQL warehouse or interactive cluster) is up and running, otherwise theTest Authenticationstep times out.



#### AWS service principalâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

To enter your Databricks credentials:

ForHost, enter the hostname orAWS PrivateLink endpointfor your Databricks instance.

ForPort, enter the port number of your Databricks instance.

ForClient ID, enter theclient ID for your AWS service principal.

ForClient Secret, enter theclient secret for your AWS service principal.

ClickTest Authenticationto confirm connectivity to Databricks using these details.

Once successful, at the bottom of the screen clickNext.



#### Azure service principalâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

To enter your Databricks credentials:

ForHost, enter the hostname orAzure Private Link endpointfor your Databricks instance.

ForPort, enter the port number of your Databricks instance.

ForClient ID, enter theapplication (client) ID for your Azure service principal.

ForClient Secret, enter theclient secret for your Azure service principal.

ForTenant ID, enter thedirectory (tenant) ID for your Azure service principal.

ClickTest Authenticationto confirm connectivity to Databricks using these details.

Once successful, at the bottom of the screen clickNext.



### Offline extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

Atlan supports theoffline extraction methodfor fetching metadata from Databricks. This method uses Atlan's databricks-extractor tool to fetch metadata. You need to firstextract the metadatayourself and thenmake it available in S3.

To enter your S3 details:

ForBucket name, enter the name of your S3 bucket.

ForBucket prefix, enter the S3 prefix under which all the metadata files exist. These includeoutput/databricks-example/catalogs/success/result-0.json,output/databricks-example/schemas/{{catalog_name}}/success/result-0.json,output/databricks-example/tables/{{catalog_name}}/success/result-0.json, and similar files.

output/databricks-example/catalogs/success/result-0.json

output/databricks-example/schemas/{{catalog_name}}/success/result-0.json

output/databricks-example/tables/{{catalog_name}}/success/result-0.json

(Optional) ForBucket region, enter the name of the S3 region.

When complete, at the bottom of the screen, clickNext.



### Agent extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

Atlan supports using a Secure Agent for fetching metadata from Databricks. To use a Secure Agent, follow these steps:

Select theAgenttab.

Configure the Databricks data source by adding the secret keys for your secret store. For details on the required fields, refer to the Direct extraction section.

Complete the Secure Agent configuration by following the instructions in theHow to configure Secure Agent for workflow executionguide.

ClickNextafter completing the configuration.



## Configure the connectionâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

To complete the Databricks connection configuration:

Provide aConnection Namethat represents your source environment. For example, you might want to use values likeproduction,development,gold, oranalytics.

Provide aConnection Namethat represents your source environment. For example, you might want to use values likeproduction,development,gold, oranalytics.

production

development

gold

analytics

(Optional) To change the users able to manage this connection, change the users or groups listed underConnection Admins.dangerIf you don't specify any user or group, nobody can manage the connection - not even admins.

(Optional) To change the users able to manage this connection, change the users or groups listed underConnection Admins.

If you don't specify any user or group, nobody can manage the connection - not even admins.

(Optional) To prevent users from querying any Databricks data, changeEnable SQL QuerytoNo.

(Optional) To prevent users from querying any Databricks data, changeEnable SQL QuerytoNo.

(Optional) To prevent users from previewing any Databricks data, changeEnable Data PreviewtoNo.

(Optional) To prevent users from previewing any Databricks data, changeEnable Data PreviewtoNo.

(Optional) To prevent users from running large queries, changeMax Row Limitor keep the default selection.

(Optional) To prevent users from running large queries, changeMax Row Limitor keep the default selection.

At the bottom of the screen, click theNextbutton to proceed.

At the bottom of the screen, click theNextbutton to proceed.



## Configure the crawlerâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

Before running the Databricks crawler, you can further configure it.



### System tables extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

The system metadata extraction method is only available forUnity Catalog-enabled workspaces. It provides access to detailed metadata from system tables and supports all three authentication types. You can extract metadata from your Databricks workspace using this method. Follow these steps:

Set up authentication using one of the following:Personal access tokenAWS service principalAzure service principal

Set up authentication using one of the following:

Personal access token

AWS service principal

Azure service principal

The default options can work as is. You may choose to override the defaults for any of the remaining options:ForAsset selection, select a filtering option:ForSQL warehouse, click the dropdown to select the SQL warehouse you want to configure.To select the assets you want to include in crawling, clickInclude by hierarchyand filter for assets down to the database or schema level. (This defaults to all assets, if none are specified.)To have the crawler includeDatabases,Schemas, orTables & Viewsbased on a naming convention, clickInclude by regexand specify a regular expression - for example, specifyingATLAN_EXAMPLE_DB.*forDatabasesincludes all the matching databases and their child assets.To select the assets you want to exclude from crawling, clickExclude by hierarchyand filter for assets down to the database or schema level. (This defaults to no assets, if none are specified.)To have the crawler ignoreDatabases,Schemas, orTables & Viewsbased on a naming convention, clickExclude by regexand specify a regular expression - for example, specifyingATLAN_EXAMPLE_TABLES.*forTables & Viewsexcludes all the matching tables and views.Click+to add more filters. If you add multiple filters, assets are crawled based on matchingallthe filtering conditions you have set.Toimport tags from Databricks to Atlan, changeImport TagstoYes. Note that you must have aUnity Catalog-enabled workspaceto import Databricks tags in Atlan.Did you know?If an asset appears in both the include and exclude filters, the exclude filter takes precedence.

The default options can work as is. You may choose to override the defaults for any of the remaining options:

ForAsset selection, select a filtering option:ForSQL warehouse, click the dropdown to select the SQL warehouse you want to configure.To select the assets you want to include in crawling, clickInclude by hierarchyand filter for assets down to the database or schema level. (This defaults to all assets, if none are specified.)To have the crawler includeDatabases,Schemas, orTables & Viewsbased on a naming convention, clickInclude by regexand specify a regular expression - for example, specifyingATLAN_EXAMPLE_DB.*forDatabasesincludes all the matching databases and their child assets.To select the assets you want to exclude from crawling, clickExclude by hierarchyand filter for assets down to the database or schema level. (This defaults to no assets, if none are specified.)To have the crawler ignoreDatabases,Schemas, orTables & Viewsbased on a naming convention, clickExclude by regexand specify a regular expression - for example, specifyingATLAN_EXAMPLE_TABLES.*forTables & Viewsexcludes all the matching tables and views.Click+to add more filters. If you add multiple filters, assets are crawled based on matchingallthe filtering conditions you have set.Toimport tags from Databricks to Atlan, changeImport TagstoYes. Note that you must have aUnity Catalog-enabled workspaceto import Databricks tags in Atlan.Did you know?If an asset appears in both the include and exclude filters, the exclude filter takes precedence.

ForAsset selection, select a filtering option:

ForSQL warehouse, click the dropdown to select the SQL warehouse you want to configure.

To select the assets you want to include in crawling, clickInclude by hierarchyand filter for assets down to the database or schema level. (This defaults to all assets, if none are specified.)

To have the crawler includeDatabases,Schemas, orTables & Viewsbased on a naming convention, clickInclude by regexand specify a regular expression - for example, specifyingATLAN_EXAMPLE_DB.*forDatabasesincludes all the matching databases and their child assets.

ATLAN_EXAMPLE_DB.*

To select the assets you want to exclude from crawling, clickExclude by hierarchyand filter for assets down to the database or schema level. (This defaults to no assets, if none are specified.)

To have the crawler ignoreDatabases,Schemas, orTables & Viewsbased on a naming convention, clickExclude by regexand specify a regular expression - for example, specifyingATLAN_EXAMPLE_TABLES.*forTables & Viewsexcludes all the matching tables and views.

ATLAN_EXAMPLE_TABLES.*

Click+to add more filters. If you add multiple filters, assets are crawled based on matchingallthe filtering conditions you have set.

Toimport tags from Databricks to Atlan, changeImport TagstoYes. Note that you must have aUnity Catalog-enabled workspaceto import Databricks tags in Atlan.

If an asset appears in both the include and exclude filters, the exclude filter takes precedence.



#### Incremental extractionâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

Toggle incremental extraction, for a faster and more efficient metadata extraction.



### JDBC extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

The JDBC extraction method uses JDBC queries to extract metadata from your Databricks instance. This was the original extraction method provided by Databricks. This extraction method is only supported forpersonal access token authentication.

You can override the defaults for any of these options:

To select the assets you want to include in crawling, clickInclude Metadata. (This will default to all assets, if none are specified.)

To select the assets you want to exclude from crawling, clickExclude Metadata. (This will default to no assets if none are specified.)

To have the crawler ignore tables and views based on a naming convention, specify a regular expression in theExclude regex for tables & viewsfield.

ForView Definition Lineage, keep the defaultYesto generate upstream lineage for views based on the tables referenced in the views or clickNoto exclude from crawling.

ForAdvanced Config, keepDefaultfor the default configuration or clickAdvancedto further configure the crawler:To enable or disable schema-level filtering at source, clickEnable Source Level Filteringand selectTrueto enable it orFalseto disable it.

To enable or disable schema-level filtering at source, clickEnable Source Level Filteringand selectTrueto enable it orFalseto disable it.



### REST API extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

The REST API extraction method usesUnity Catalogto extract metadata from your Databricks instance. This extraction method is supported for all three authentication options:personal access token,AWS service principal, andAzure service principal.

This method is only supported byUnity Catalog-enabledworkspaces.

If you enable an existing workspace, you also need toupgrade your tables and views to Unity Catalog.

While REST APIs are used to extract metadata, JDBC queries are still used for querying purposes.

You can override the defaults for any of these options:

Change the extraction method underExtraction methodtoREST API.

To select the assets you want to include in crawling, clickInclude Metadata. (This will default to all assets, if none are specified.)

To select the assets you want to exclude from crawling, clickExclude Metadata. (This will default to no assets if none are specified.)

Toimport tags from Databricks to Atlan, changeImport TagstoYes. Note that you must have aUnity Catalog-enabled workspaceto import Databricks tags in Atlan.ForSQL warehouse, click the dropdown to select the SQL warehouse you have configured.

ForSQL warehouse, click the dropdown to select the SQL warehouse you have configured.

If an asset appears in both the include and exclude filters, the exclude filter takes precedence.



## Run the crawlerâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-databricks)

Follow these steps to run the Databricks crawler:

To check for anypermissions or other configuration issuesbefore running the crawler, clickPreflight checks.

You can either:To run the crawler once immediately, at the bottom of the screen, click theRunbutton.To schedule the crawler to run hourly, daily, weekly, or monthly, at the bottom of the screen, click theSchedule Runbutton.

To run the crawler once immediately, at the bottom of the screen, click theRunbutton.

To schedule the crawler to run hourly, daily, weekly, or monthly, at the bottom of the screen, click theSchedule Runbutton.

Once the crawler has completed running, you will see the assets in Atlan's asset page! ð

connectors

data

crawl

setup

Select the source

Provide credentials

Configure the connection

Configure the crawler

Run the crawler
