# extract lineage and usage from Databricks
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-lineage-and-usage-from-databricks)

DatabricksGet StartedCross-workspace SetupCrawl Databricks AssetsOn-premises SetupPrivate Network SetupLineage and UsageHow to extract lineage and usage from DatabricksHow to extract on-premises Databricks lineageTag managementReferencesTroubleshooting

Get Started

Cross-workspace Setup

Crawl Databricks Assets

On-premises Setup

Private Network Setup

Lineage and UsageHow to extract lineage and usage from DatabricksHow to extract on-premises Databricks lineage

How to extract lineage and usage from Databricks

How to extract on-premises Databricks lineage

Tag management

References

Troubleshooting

Connect data

Data Warehouses

Databricks

Lineage and Usage

How to extract lineage and usage from Databricks

Once you havecrawled assets from Databricks, you can retrieve lineage fromUnity Catalogandusage and popularity metricsfromquery historyor system tables. This is supported for allthree authentication methods: personal access token, AWS service principal, and Azure service principal.

Both Atlan and Databricks strongly recommend using the system tables method to extractlineageandusage and popularity metricsfrom Databricks.

Usage and popularity metricscan be retrieved for all Databricks users. However, your Databricks workspace must beUnity Catalog-enabledfor the retrieval of lineage and usage and popularity metrics to succeed. You may also need toupgrade existing tables and views to Unity Catalog, as well as reach out to your Databricks account executive to enable lineage in Unity Catalog. (As of publishing, the feature is still in preview from Databricks on AWS and Azure.)

To retrieve lineage and usage from Databricks, rev

iew theorder of operationsand then complete the following steps.



## Select the extractorâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-lineage-and-usage-from-databricks)

To select the Databricks lineage and usage extractor:

In the top right of any screen, navigate toÂNewand then clickÂNew Workflow.

From the filters along the top, clickMiner.

From the list of packages, selectDatabricks Minerand click onSetup Workflow.



## Configure the lineage extractorâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-lineage-and-usage-from-databricks)

Choose your lineage extraction method:

InREST API, Atlan connects to your database and extracts lineage directly.

InOffline, you will need to firstextract lineage yourselfandmake it available in S3.

InSystem Table, Atlan connects to your database andqueries system tablesto extract lineage directly.



### REST APIâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-lineage-and-usage-from-databricks)

To configure the Databricks lineage extractor:

ForConnection, select the connection to extract. (To select a connection,the crawlermust have already run.)

ClickNextto proceed.



### Offline extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-lineage-and-usage-from-databricks)

Atlan supports theoffline extraction methodfor extracting lineage from Databricks This method uses Atlan's databricks-extractor tool to extract lineage. You will need to firstextract lineage yourselfandmake it available in S3.

To enter your S3 details:

ForConnection, select the connection to extract. (To select a connection,the crawlermust have already run.)

ForBucket name, enter the name of your S3 bucket.

ForBucket prefix, enter the S3 prefix under which all the metadata files exist. These includeextracted-lineage/result-0.json,extracted-query-history/result-0.json, and so on.

extracted-lineage/result-0.json

extracted-query-history/result-0.json

ForBucket region, enter the name of the S3 region.

When complete, at the bottom of the screen, clickNext.



### System tableâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-lineage-and-usage-from-databricks)

To configure the Databricks lineage extractor:

ForConnection, select the connection to extract. (To select a connection,the crawlermust have already run.)

*Extraction Catalog Type:Default: Select to fetch lineage from the system catalog andaccessschema.Cloned_catalog: Select to fetch lineage from a cloned catalog and schema.Before proceeding, make sure the following prerequisites are met:You have already created cloned views namedcolumn_lineageandtable_lineagein your schema.If not, follow the steps inCreate cloned views of system tables.Theatlan-usermust haveSELECTpermissions on both views to access lineage data.Then, provide values for the following fields:Cloned Catalog Nameâ Catalog containing the cloned views.Cloned Schema Nameâ Schema containing the cloned views.

Default: Select to fetch lineage from the system catalog andaccessschema.

Default: Select to fetch lineage from the system catalog andaccessschema.

access

Cloned_catalog: Select to fetch lineage from a cloned catalog and schema.Before proceeding, make sure the following prerequisites are met:You have already created cloned views namedcolumn_lineageandtable_lineagein your schema.If not, follow the steps inCreate cloned views of system tables.Theatlan-usermust haveSELECTpermissions on both views to access lineage data.Then, provide values for the following fields:Cloned Catalog Nameâ Catalog containing the cloned views.Cloned Schema Nameâ Schema containing the cloned views.

Cloned_catalog: Select to fetch lineage from a cloned catalog and schema.Before proceeding, make sure the following prerequisites are met:

You have already created cloned views namedcolumn_lineageandtable_lineagein your schema.If not, follow the steps inCreate cloned views of system tables.

column_lineage

table_lineage

Theatlan-usermust haveSELECTpermissions on both views to access lineage data.

atlan-user

SELECT

Then, provide values for the following fields:

Cloned Catalog Nameâ Catalog containing the cloned views.

Cloned Schema Nameâ Schema containing the cloned views.

ForSQL Warehouse ID, enter theID you copied from your SQL warehouse.

ClickNextto proceed.



## (Optional) Configure the usage extractorâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-lineage-and-usage-from-databricks)

Atlan extractsusage and popularity metricsfrom:

Query history

System tables

This feature is currently limited to queries on SQL warehouses   -  queries on interactive clusters are not supported. Additionally, expensive queries and compute costs for Databricks assets are currently unavailable due to limitations of theDatabricks APIs.

To configure the Databricks usage and popularity extractor:

ForFetch Query History and Calculate Popularity, clickYesto retrieveusage and popularity metricsfor your Databricks assets.

ForPopularity Extraction Method: Choose one of the following methods to extract usage and popularity metrics::ClickREST APIto extract usage and popularity metrics from query history.ClickSystem tableto extract metrics directly from system tables:Extraction catalog type for popularity: Choose where to fetch popularity data from:Default: Uses the system catalog andqueryschema to fetch popularity metrics.Cloned_catalog: Select to fetch popularity from cloned views in a separate catalog and schema.Before proceeding:Thequery_historyview must exist in the provided schema.Theatlan-usermust haveSELECTpermission on the view.Then provide:Cloned Catalog Nameâ The catalog that contains thequery_historyview.Cloned Schema Nameâ The schema that contains thequery_historyview.For more information, seeCreate cloned views of system tables.ForSQL Warehouse ID, enter theID you copied from your SQL warehouse.

ClickREST APIto extract usage and popularity metrics from query history.

ClickSystem tableto extract metrics directly from system tables:Extraction catalog type for popularity: Choose where to fetch popularity data from:Default: Uses the system catalog andqueryschema to fetch popularity metrics.Cloned_catalog: Select to fetch popularity from cloned views in a separate catalog and schema.Before proceeding:Thequery_historyview must exist in the provided schema.Theatlan-usermust haveSELECTpermission on the view.Then provide:Cloned Catalog Nameâ The catalog that contains thequery_historyview.Cloned Schema Nameâ The schema that contains thequery_historyview.For more information, seeCreate cloned views of system tables.ForSQL Warehouse ID, enter theID you copied from your SQL warehouse.

Extraction catalog type for popularity: Choose where to fetch popularity data from:Default: Uses the system catalog andqueryschema to fetch popularity metrics.Cloned_catalog: Select to fetch popularity from cloned views in a separate catalog and schema.Before proceeding:Thequery_historyview must exist in the provided schema.Theatlan-usermust haveSELECTpermission on the view.Then provide:Cloned Catalog Nameâ The catalog that contains thequery_historyview.Cloned Schema Nameâ The schema that contains thequery_historyview.For more information, seeCreate cloned views of system tables.

Extraction catalog type for popularity: Choose where to fetch popularity data from:

Default: Uses the system catalog andqueryschema to fetch popularity metrics.

query

Cloned_catalog: Select to fetch popularity from cloned views in a separate catalog and schema.Before proceeding:

Thequery_historyview must exist in the provided schema.

query_history

Theatlan-usermust haveSELECTpermission on the view.

atlan-user

SELECT

Then provide:

Cloned Catalog Nameâ The catalog that contains thequery_historyview.

query_history

Cloned Schema Nameâ The schema that contains thequery_historyview.

query_history

For more information, seeCreate cloned views of system tables.

ForSQL Warehouse ID, enter theID you copied from your SQL warehouse.

ForSQL Warehouse ID, enter theID you copied from your SQL warehouse.

Configure the usage extractor: Â ÂForPopularity Window (days), 30 days is the maximum limit. You can set a shorter popularity window of less than 30 days.ForStart time, choose the earliest date from which to mine query history. If you're using theoffline extraction methodto extract query history from Databricks, skip to the next step.ForExcluded Users, type the names of users to be excluded while calculatingusage metricsfor Databricks assets. Pressenterafter each name to add more names.Â

ForPopularity Window (days), 30 days is the maximum limit. You can set a shorter popularity window of less than 30 days.

ForStart time, choose the earliest date from which to mine query history. If you're using theoffline extraction methodto extract query history from Databricks, skip to the next step.

ForExcluded Users, type the names of users to be excluded while calculatingusage metricsfor Databricks assets. Pressenterafter each name to add more names.Â

enter

If running the miner for the first time, Atlan recommends setting a start date around three days prior to the current date and then scheduling it daily to build up to two weeks of query history. Mining two weeks of query history on the first miner run may cause delays. For all subsequent runs, Atlan requires a minimum lag of 24 to 48 hours to capture all the relevant transformations that were part of a session. Learn more about the miner logichere.



## Run the extractorâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-lineage-and-usage-from-databricks)

To run the Databricks lineage and popularity extractor, after completing the steps above:

To check for anypermissions or other configuration issuesbefore running the crawler, clickPreflight checks. This isÂ currently only supported when using REST API and offline extraction methods. If you're using system tables, skip to step 2.

You can either:To run the crawler once immediately, at the bottom of the screen, click theRunbutton.To schedule the crawler to run hourly, daily, weekly, or monthly, at the bottom of the screen, click theSchedule Runbutton.

To run the crawler once immediately, at the bottom of the screen, click theRunbutton.

To schedule the crawler to run hourly, daily, weekly, or monthly, at the bottom of the screen, click theSchedule Runbutton.

Once the extractor has completed running, you will see lineage for Databricks assets! ð

connectors

data

crawl

api

authentication

Select the extractor

Configure the lineage extractor

(Optional) Configure the usage extractor

Run the extractor
