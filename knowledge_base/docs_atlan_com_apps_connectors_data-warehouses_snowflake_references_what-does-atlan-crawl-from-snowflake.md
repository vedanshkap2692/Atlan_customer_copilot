# What does Atlan crawl from Snowflake?
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

SnowflakeGet StartedCrawl Snowflake AssetsManage Snowflake in AtlanReferencesMultiple tag values and concatenationWhat does Atlan crawl from Snowflake?Preflight checks for SnowflakeTroubleshootingBest Practices

Get Started

Crawl Snowflake Assets

Manage Snowflake in Atlan

ReferencesMultiple tag values and concatenationWhat does Atlan crawl from Snowflake?Preflight checks for Snowflake

Multiple tag values and concatenation

What does Atlan crawl from Snowflake?

Preflight checks for Snowflake

Troubleshooting

Best Practices

Connect data

Data Warehouses

Snowflake

References

What does Atlan crawl from Snowflake?

Atlan crawls and maps the following assets and properties from Snowflake.

Once you'vecrawled Snowflake, you canuse connector-specific filtersfor quick asset discovery. The following filters are currently supported for Snowflake assets:

Streams-  Source type and Stale filters

Functions-  Language, Function type, Is secure, and Is external filters

Snowflake tags and tag values



## Lineageâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan supports lineage for the following asset types:



### External Named Stagesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Table

Pipe â Table

External Table

Iceberg Table



### Internal Named Stagesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Table

Pipe â Table (auto-ingest not recommended)

Not supported for External or Iceberg Tables



## Databasesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps databases from Snowflake to itsDatabaseasset type.

Database

DATABASES.DATABASE_NAME

name

DATABASE.COMMENT

description

SCHEMATA

schemaCount

DATABASES.DATABASE_OWNER

DATABASES.CREATED

sourceCreatedAt

DATABASES.LAST_ALTERED

sourceUpdatedAt



## Schemasâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps schemas from Snowflake to itsSchemaasset type.

Schema

SCHEMATA.SCHEMA_NAME

name

SCHEMA.COMMENT

description

TABLES

tableCount

TABLES

viewsCount

SCHEMATA.CATALOG_NAME

databaseName

SCHEMATA.SCHEMA_OWNER

SCHEMATA.CREATED

sourceCreatedAt

SCHEMATA.LAST_ALTERED

sourceUpdatedAt



## Tablesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps tables from Snowflake to itsTableasset type.

Table

TABLES.TABLE_NAME

name

TABLES.COMMENT

description

COLUMNS

columnCount

TABLES.ROW_COUNT

rowCount

TABLES.BYTES

sizeBytes

TABLES.TABLE_OWNER

TABLES.CREATED

sourceCreatedAt

TABLES.LAST_ALTERED

sourceUpdatedAt



### For Iceberg tablesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

In addition to the table metadata above, Atlan supports additional metadata for Iceberg tables crawled from Snowflake. Atlan currently supports fetching metadata for Iceberg tables only for the information schema extraction method.

TABLES.IS_ICEBERG

tableType

ICEBERG_TABLES.CATALOG_NAME

icebergCatalogName

ICEBERG_TABLES.ICEBERG_TABLE_TYPE

icebergTableType

CATALOG_INTEGRATION.CATALOG_SOURCE

icebergCatalogSource

ICEBERG_TABLES.CATALOG_TABLE_NAME

icebergCatalogTableName

ICEBERG_TABLES.CATALOG_NAMESPACE

icebergCatalogTableNamespace

ICEBERG_TABLES.EXTERNAL_VOLUME_NAME

tableExternalVolumeName

ICEBERG_TABLES.BASE_LOCATION

icebergTableBaseLocation

TABLES.RETENTION_TIME

tableRetentionTime



## Viewsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps views from Snowflake to itsViewasset type.

View

TABLES.TABLE_NAME

name

TABLES.COMMENT

description

COLUMNS

columnCount

VIEWS.VIEW_DEFINITION

definition

TABLES.TABLE_OWNER

TABLES.CREATED

sourceCreatedAt

TABLES.LAST_ALTERED

sourceUpdatedAt



## Materialized viewsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps materialized views from Snowflake to itsMaterialisedViewasset type.

MaterialisedView

TABLES.TABLE_NAME

name

TABLES.COMMENT

description

COLUMNS

columnCount

TABLES.ROW_COUNT

rowCount

TABLES.BYTES

sizeBytes

VIEWS.VIEW_DEFINITION

definition

TABLES.TABLE_OWNER

TABLES.CREATED

sourceCreatedAt

TABLES.LAST_ALTERED

sourceUpdatedAt



## External tablesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps external tables from Snowflake to itsTableasset type.

Table

TABLES.TABLE_NAME

name

TABLES.COMMENT

description

COLUMNS

columnCount

TABLES.ROW_COUNT

rowCount

TABLES.BYTES

sizeBytes

EXTERNAL_TABLES.LOCATION

externalLocation

STAGES.STAGE_REGION

externalLocationRegion

EXTERNAL_TABLES.FILE_FORMAT_TYPE

externalLocationFormat

TABLES.TABLE_OWNER

TABLES.CREATED

sourceCreatedAt

TABLES.LAST_ALTERED

sourceUpdatedAt



## Columnsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps columns from Snowflake to itsColumnasset type.

Column

COLUMNS.COLUMN_NAME

name

COLUMNS.COMMENT

description

COLUMNS.ORDINAL_POSITION

order

COLUMNS.DATA_TYPE

dataType

PRIMARY KEY

isPrimary

COLUMNS.IS_NULLABLE

isNullable

COLUMNS.CHARACTER_MAXIMUM_LENGTH

maxLength

COLUMNS.NUMERIC_PRECISION

precision



## Stagesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps stages from Snowflake to itsStageasset type.

Stage

Stages.STAGE_NAME

name

Stages.COMMENT

description

Stages.STAGE_SCHEMA

schemaName

Stages.STAGE_CATALOG

databaseName

Stages.STAGE_URL

snowflakeStageExternalLocation

Stages.STAGE_REGION

snowflakeStageExternalLocationRegion

Stages.STAGE_TYPE

snowflakeStageType

Stages.STAGE_OWNER

sourceOwners

Stages.CREATED

sourceCreatedAt

Stages.LAST_ALTERED

sourceUpdatedAt

Stages.STORAGE_INTEGRATION

snowflakeStageStorageIntegration



## Streamsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps streams from Snowflake to itsStreamasset type.

Stream

STREAMS.NAME

name

STREAMS.COMMENT

description

STREAMS.OWNER

sourceOwners

STREAMS.DATABASE_NAME

databaseName

STREAMS.SCHEMA_NAME

schemaName

STREAMS.SOURCE_TYPE

snowflakeStreamSourceType

STREAMS.STALE

snowflakeStreamIsStale

STREAMS.MODE

snowflakeStreamMode

STREAMS.STALE_AFTER

snowflakeStreamStaleAfter



## Pipesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps pipes from Snowflake to itsPipeasset type.

Pipe

PIPES.PIPE_NAME

name

PIPES.COMMENT

description

PIPES.DEFINITION

definition

PIPES.PIPE_OWNER

sourceOwners

PIPES.PIPE_CATALOG

databaseName

PIPES.PIPE_SCHEMA

schemaName

PIPES.IS_AUTOINGEST_ENABLED

snowflakePipeIsAutoIngestEnabled

PIPES.NOTIFICATION_CHANNEL_NAME

snowflakePipeNotificationChannelName



## User-defined functionsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps user-defined functions (UDFs) from Snowflake to itsFunctionasset type. Atlan currently does not support lineage for user-defined functions from Snowflake.

Function

NAME

name

FUNCTION_DEFINITION

functionDefinition

COMMENT

description

FUNCTION_CATALOG

databaseName

FUNCTION_SCHEMA

schemaName

FUNCTION_OWNER

CREATED

sourceCreatedAt

LAST_ALTERED

sourceUpdatedAt

FUNCTION_LANGUAGE

functionLanguage

DATA_TYPE

functionReturnType

IS_SECURE

functionIsSecure

IS_EXTERNAL

functionIsExternal

IS_MEMOIZABLE

functionIsMemoizable

ARGUMENT_SIGNATURE

functionArguments



## Dynamic tablesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/what-does-atlan-crawl-from-snowflake)

Atlan maps dynamic tables from Snowflake to itsDynamicTableasset type.

DynamicTable

TABLES.TABLE_NAME

name

TABLES.COMMENT

description

COLUMNS

columnCount

TABLES.DEFINITION

definition

TABLES.ROW_COUNT

rowCount

TABLES.BYTES

sizeBytes

TABLES.TABLE_OWNER

TABLES.CREATED

sourceCreatedAt

TABLES.LAST_ALTERED

sourceUpdatedAt

connectors

data

crawl

Lineage

Databases

Schemas

Tables

Views

Materialized views

External tables

Columns

Stages

Streams

Pipes

User-defined functions

Dynamic tables
