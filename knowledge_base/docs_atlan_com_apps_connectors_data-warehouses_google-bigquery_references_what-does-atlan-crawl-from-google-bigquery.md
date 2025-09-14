# What does Atlan crawl from Google BigQuery?
(source: https://docs.atlan.com/apps/connectors/data-warehouses/google-bigquery/references/what-does-atlan-crawl-from-google-bigquery)

Google BigQueryGet StartedCrawl BigQuery AssetsManage BigQuery in AtlanReferencesWhat does Atlan crawl from Google BigQuery?Preflight checks for Google BigQueryTroubleshooting

Get Started

Crawl BigQuery Assets

Manage BigQuery in Atlan

ReferencesWhat does Atlan crawl from Google BigQuery?Preflight checks for Google BigQuery

What does Atlan crawl from Google BigQuery?

Preflight checks for Google BigQuery

Troubleshooting

Connect data

Data Warehouses

Google BigQuery

References

What does Atlan crawl from Google BigQuery?

Once you havecrawled Google BigQuery, you canuse connector-specific filtersfor quick asset discovery. The following filters are currently supported for these assets:

Tables-  BigQuery labels andIs shardedfilters

Atlan doesn't run any table scans. Atlan leverages the table preview options fromGoogle BigQueryÂ that enable you to view data for free and without affecting any quotas using thetabledata.listAPI. Hence,tableasset previews in Atlan are already cost-optimized. However, this doesn't apply toviewsandmaterialized views.

tabledata.list

For Google BigQueryviewsandmaterialized views, Atlan sends you a cost nudge before viewing a sample data preview. This informs you about the precise bytes that are spent during the execution of the query, helping you decide if you still want to run the preview.

You also receive a cost nudge beforequerying your Google BigQuery assets.

Atlan crawls and maps the following assets and properties from Google BigQuery.



## Databasesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/google-bigquery/references/what-does-atlan-crawl-from-google-bigquery)

Atlan maps projects from Google BigQuery to itsDatabaseasset type.

Database

Project ID

name



## Schemasâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/google-bigquery/references/what-does-atlan-crawl-from-google-bigquery)

Atlan maps datasets from Google BigQuery to itsSchemaasset type.

Schema

TABLE_SCHEMA

name

TABLE_COUNT

tableCount

VIEW_COUNT

viewsCount

TABLE_CATALOG

databaseName

REMARKS

description

CREATED

sourceCreatedAt

MODIFIED

sourceUpdatedAt



## Tablesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/google-bigquery/references/what-does-atlan-crawl-from-google-bigquery)

Tableasset previews are already cost-optimized.Google BigQueryenables you to use the table preview options to view data for free and without affecting any quotas. Note that this isn't currently supported forGoogle BigQuery views and materialized viewsin Atlan.

Atlan maps tables from Google BigQuery to itsTableasset type.

Table

TABLE_NAME

name

REMARKS

description

COLUMN_COUNT

columnCount

ROW_COUNT

rowCount

SIZE_BYTES

sizeBytes

TABLE_TYPE

subType

LABELS

assetTags

CREATED

sourceCreatedAt

MODIFIED

sourceUpdatedAt

OPTION_NAMES (require_partition_filter)

isPartitioned



## Viewsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/google-bigquery/references/what-does-atlan-crawl-from-google-bigquery)

Atlan maps views from Google BigQuery to itsViewasset type.

View

TABLE_NAME

name

REMARKS

description

COLUMN_COUNT

columnCount

TABLE_TYPE

subType

CREATED

sourceCreatedAt

MODIFIED

sourceUpdatedAt

OPTION_NAMES (require_partition_filter)

isPartitioned

DDL

definition



## Materialized viewsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/google-bigquery/references/what-does-atlan-crawl-from-google-bigquery)

Atlan maps materialized views from Google BigQuery to itsMaterialisedViewasset type.

MaterialisedView

TABLE_NAME

name

REMARKS

description

COLUMN_COUNT

columnCount

ROW_COUNT

rowCount

SIZE_BYTES

sizeBytes

TABLE_TYPE

subType

CREATED

sourceCreatedAt

MODIFIED

sourceUpdatedAt

OPTION_NAMES (require_partition_filter)

isPartitioned

DDL

definition



## Columnsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/google-bigquery/references/what-does-atlan-crawl-from-google-bigquery)

Atlan supportsnested columns up to level 1for Google BigQuery to help you enrich your semi-structured data types. You can view nested columns in the asset sidebar for your table assets. Atlan maps columns from Google BigQuery to itsColumnasset type.

Column

Atlan doesn't crawl primary key (PK) and foreign key (FK) information from Google BigQuery.

COLUMN_NAME

name

REMARKS, DESCRIPTION

description

ORDINAL_POSITION

order

TYPE_NAME

dataType

IS_NULLABLE

isNullable

IS_PARTITIONING_COLUMN

isPartition

CLUSTERING_COLUMN_LIST

isClustered



## Stored proceduresâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/google-bigquery/references/what-does-atlan-crawl-from-google-bigquery)

Atlan maps stored procedures from Google BigQuery to itsProcedureasset type.

Procedure

PROCEDURE_NAME

name

REMARKS

description

PROCEDURE_TYPE

subType

ROUTINE_DEFINITION

definition

CREATED

sourceCreatedAt

MODIFIED

sourceUpdatedAt

connectors

data

crawl

Databases

Schemas

Tables

Views

Materialized views

Columns

Stored procedures
