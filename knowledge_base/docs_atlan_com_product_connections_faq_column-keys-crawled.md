# What column keys does Atlan crawl?
(source: https://docs.atlan.com/product/connections/faq/column-keys-crawled)

Connector FrameworkHow-tosConceptsReferencesFAQCan I connect to any source with an ODBC/JDBC driver?Can the Hive crawler connect to an independent Hive metastore?How often does Atlan crawl Snowflake?What column keys does Atlan crawl?What's the difference between connecting to Athena and Glue?

How-tos

Concepts

References

FAQCan I connect to any source with an ODBC/JDBC driver?Can the Hive crawler connect to an independent Hive metastore?How often does Atlan crawl Snowflake?What column keys does Atlan crawl?What's the difference between connecting to Athena and Glue?

Can I connect to any source with an ODBC/JDBC driver?

Can the Hive crawler connect to an independent Hive metastore?

How often does Atlan crawl Snowflake?

What column keys does Atlan crawl?

What's the difference between connecting to Athena and Glue?

Connect data

Connectivity Framework

Connector Framework

FAQ

What column keys does Atlan crawl?

If the following column keys are defined in the SQL database at source, Atlan will crawl and display them as attributes for your assets:

Primary key-  uniquely identifies each row in a table.

Foreign key-  links together two tables.

Partition key-  determines logical partitions in a table.

Sort key-  determines the order in which rows are stored in a table.

Index key-  defines the order for an index in the database.

Cluster key-  determines the order in which the database is partitioned.

Distributed key-  determines where data is stored in a database.



## View column keysâ
(source: https://docs.atlan.com/product/connections/faq/column-keys-crawled)

Navigate to the left menu of any screen in Atlan and clickAssetsto begin:



### From the asset previewâ
(source: https://docs.atlan.com/product/connections/faq/column-keys-crawled)

To view column keys in the asset preview:

From theAssetspage, navigate to the asset preview section. The asset preview for column assets will display available column keys.



### From the asset profileâ
(source: https://docs.atlan.com/product/connections/faq/column-keys-crawled)

To view column keys in the asset profile:

From theAssetspage, right-click a table or a column asset and selectOpen profile.

Navigate toColumn previewto view available column keys.



### From the sidebarâ
(source: https://docs.atlan.com/product/connections/faq/column-keys-crawled)

To view column keys in the sidebar:

From theAssetspage, click a table or a column asset.

In the sidebar to the right, click theColumnstab to view available column keys in the sidebar.



## Create foreign key relationshipsâ
(source: https://docs.atlan.com/product/connections/faq/column-keys-crawled)

You can create foreign key relationships only through APIs for your column assets in Atlan. You can use theforeignKeyToandforeignKeyFromstatements to create column references for your foreign keys and maintain the referential integrity of your assets. Refer to ourdeveloper documentationto assign foreign key relationships.

foreignKeyTo

foreignKeyFrom

Once you have created foreign key relationships, your users will be able to view the column references and better understand the relationships between assets.



## Filter assets by column keysâ
(source: https://docs.atlan.com/product/connections/faq/column-keys-crawled)

You can filter your asset search results bytype-specific propertyfilters, such as column keys for your column assets.Â

To filter column assets by column keys:

From the left menu on any screen in Atlan, clickAssets.

Under the search bar on theAssetspage, click theColumntab to filter for column assets.

In theFiltersmenu on the left, click theColumnfilter.

To add atype-specific propertyfilter to refine your search, select a column-type property filter   -  for example,Primary key.

In the filter dialog, clickYesto view column assets with a primary key or clickNoto only view column assets without a primary key.



## Supported sourcesâ
(source: https://docs.atlan.com/product/connections/faq/column-keys-crawled)

Atlan supports column keys for the following connectors:

Amazon Athena

Amazon Redshift

AWS Glue

Databricks

Google BigQuery

Hive

Microsoft Azure Synapse Analytics

Microsoft SQL Server

MySQL

Oracle

PostgreSQL

SAP HANA

Snowflake

Teradata

atlan

documentation

faq-connections

View column keys

Create foreign key relationships

Filter assets by column keys

Supported sources
