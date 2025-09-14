# What does Atlan crawl from Databricks?
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/what-does-atlan-crawl-from-databricks)

DatabricksGet StartedCross-workspace SetupCrawl Databricks AssetsOn-premises SetupPrivate Network SetupLineage and UsageTag managementReferencesWhat does Atlan crawl from Databricks?Preflight checks for DatabricksTroubleshooting

Get Started

Cross-workspace Setup

Crawl Databricks Assets

On-premises Setup

Private Network Setup

Lineage and Usage

Tag management

ReferencesWhat does Atlan crawl from Databricks?Preflight checks for Databricks

What does Atlan crawl from Databricks?

Preflight checks for Databricks

Troubleshooting

Connect data

Data Warehouses

Databricks

References

What does Atlan crawl from Databricks?

Atlan crawls and maps the following assets and properties from Databricks.

The following properties aren't crawled by theSystem tablesextraction method:

Table properties:partitionList,partitionCount

partitionList

partitionCount

Column properties:maxLength,precision

maxLength

precision



## Databasesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/what-does-atlan-crawl-from-databricks)

Atlan maps databases from Databricks to itsDatabaseasset type.

Database

TABLE_CATALOG

name

SCHEMA_COUNT

schemaCount



## Schemasâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/what-does-atlan-crawl-from-databricks)

Atlan maps schemas from Databricks to itsSchemaasset type.

Schema

TABLE_SCHEMA

name

TABLE_COUNT

tableCount

VIEW_COUNT

viewsCount

TABLE_CATALOG

databaseName



## Tablesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/what-does-atlan-crawl-from-databricks)

Atlan maps tables from Databricks to itsTableasset type.

Table

TABLE_NAME

name

REMARKS, DESCRIPTION

description

COLUMN_COUNT

columnCount

LOCATION

externalLocation

FORMAT

externalLocationFormat

OWNER

Created (in Databricks)

CREATEDAT

sourceCreatedAt

UPDATED_BY

Last updated

LASTMODIFIED

sourceUpdatedAt

PARTITIONS

isPartitioned

partitionCount

partitionList



## Viewsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/what-does-atlan-crawl-from-databricks)

Atlan maps views from Databricks to itsViewasset type.

View

TABLE_NAME

name

REMARKS

description

COLUMN_COUNT

columnCount

CREATETAB_STMT

definition

OWNER

Created (in Databricks)

CREATEDAT

sourceCreatedAt

UPDATED_BY

Last updated

LASTMODIFIED

sourceUpdatedAt



## Materialized viewsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/what-does-atlan-crawl-from-databricks)

Atlan maps materialized views from Databricks to itsMaterialisedViewasset type.

MaterialisedView

TABLE_NAME

name

REMARKS

description

COLUMN_COUNT

columnCount

CREATETAB_STMT

definition

OWNER

Created (in Databricks)

CREATEDAT

sourceCreatedAt

UPDATED_BY

Last updated

LASTMODIFIED

sourceUpdatedAt



## Columnsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/what-does-atlan-crawl-from-databricks)

To help you work seamlessly with STRUCT data types, Atlan supportsnested columns up to level 30in Databricks. You can view these columns in the Tree view or the asset sidebar of your table assets, and also explore child columns of STRUCTs nested within MAPs or ARRAYs. However,lineagefor nested columnsisn'tsupported.

Atlan maps columns from Databricks to itsColumnasset type.

Column

PRIMARY KEY

isPrimary

FOREIGN KEY

isForeign

COLUMN_NAME

name

REMARKS

description

ORDINAL_POSITION

order

TYPE_NAME

dataType

PARTITION_INDEX

isPartition

NULLABLE

isNullable

CHAR_OCTET_LENGTH

maxLength

DECIMAL_DIGITS

precision

data

crawl

api

Databases

Schemas

Tables

Views

Materialized views

Columns
