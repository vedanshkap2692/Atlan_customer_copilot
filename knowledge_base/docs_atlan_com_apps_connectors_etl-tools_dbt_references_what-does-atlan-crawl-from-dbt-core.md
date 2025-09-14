# What does Atlan crawl from dbt Core?
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-core)

dbtGet StartedCrawl dbt AssetsManage dbt in AtlanImpact AnalysisReferencesWhat does Atlan crawl from dbt Cloud?What does Atlan crawl from dbt Core?Troubleshooting

Get Started

Crawl dbt Assets

Manage dbt in Atlan

Impact Analysis

ReferencesWhat does Atlan crawl from dbt Cloud?What does Atlan crawl from dbt Core?

What does Atlan crawl from dbt Cloud?

What does Atlan crawl from dbt Core?

Troubleshooting

Connect data

ETL Tools

dbt

References

What does Atlan crawl from dbt Core?

Atlan crawls and maps the following assets and properties from dbt Core. Atlan also supports lineage between the following:

dbt models

dbt seeds

dbt sources

SQL tables and views materialized by dbt models, dbt seeds, dbt sources

Column-level lineage for these entities

Once you'vecrawled dbt, you canuse dbt-specific filtersfor quick asset discovery:

Test status-  filterdbt teststhat passed, failed, or have a warning or error

Test status

Alias-  filter by the name of a dbt model's identifier in the dbt project

Alias

Unique id-  filter by the unique node identifier of a dbt model

Unique id

Project name-  filter by dbt project name, only supported fordbt Core version 1.6+

Project name

Environment name-  filter by dbt environment name

Environment name

Job status-  filter by dbt job status

Job status

Last job run-  filter by the last run of the dbt job

Last job run

Atlan's dbt crawler also populates custom metadata to further enrich the assets in Atlan. TheAtlan dbt-specific propertycolumn in the tables below gives the name of the mapped custom metadata property in Atlan.

Atlan lets yousync your dbt tagsand update your dbt assets with the synced tags. You can alsomap other metadata to Atlan's assets through your dbt models.



## Tablesâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-core)

Atlan maps tables from dbt Core to itsTableasset type.

Table

description

description

config (alias)

alias

stats (row_count)

rowCount

stats (bytes)

sizeBytes

stats (last_modified)

sourceUpdatedAt

project (name)

assetDbtProjectName

uniqueId

assetDbtUniqueId

raw_sql

raw_code

dbtRawSQL

tags

assetDbtTags

packageName

assetDbtPackageName

alias

assetDbtAlias

description

description

created_at

sourceCreatedAt

compiled_sql

compiled_code

dbtCompiledSQL

freshness_data (criteria)

assetDbtSourceFreshnessCriteria



## Columnsâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-core)

Atlan maps columns from dbt Core to itsColumnasset type.

Column

description

description

meta

assetDbtMeta

tags

assetDbtTags

packageName

assetDbtPackageName

description

description

created_at

sourceCreatedAt



## Modelsâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-core)

Atlan maps models from dbt Core to itsModelasset type.

Model

name

name

description

description

executeCompletedAt

sourceUpdatedAt

owner

sourceCreatedBy

status

dbtJobRuns.dbtModelRunStatus

alias

assetDbtAlias

meta

assetDbtMeta

uniqueId

assetDbtUniqueId

raw_sql

raw_code

dbtRawSQL

compiled_sql

compiled_code

dbtCompiledSQL

stats

dbtStats

config.materialized

dbtMaterializationType



## Sourcesâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-core)

Atlan maps sources from dbt Core to itsDbtSourceasset type.

DbtSource

name

name

description

description

owner

sourceCreatedBy

alias

assetDbtAlias

meta

assetDbtMeta

uniqueId

assetDbtUniqueId

tags

assetDbtTags

criteria

assetDbtSourceFreshnessCriteria

stats

dbtStats

state

dbtState



## Testsâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-core)

For dbt Core, upload therun_results.jsonfile to crawl dbt tests. It's recommended to place the file in the same folder as themanifest.jsonfile.

run_results.json

manifest.json

Atlan maps tests from dbt Core to itsTestasset type.

Test

name

name

description

description

name

assetDbtAlias

meta

assetDbtMeta

uniqueId

assetDbtUniqueId

tags

assetDbtTags

status

dbtTestStatus

state

dbtTestState

error

dbtTestError

raw_code

dbtTestRawCode

raw_sql

dbtTestRawSQL

compiled_code

dbtTestCompiledCode

compiled_sql

dbtTestCompiledSQL

language

dbtTestLanguage



## Seedsâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-core)

Atlan maps models from dbt Core to itsSeedasset type.

Seed

name

name

description

description

executeCompletedAt

sourceUpdatedAt

owner

sourceCreatedBy

status

dbtJobRuns.dbtModelRunStatus

alias

assetDbtAlias

meta

assetDbtMeta

uniqueId

assetDbtUniqueId

stats

dbtSeedStats

filePath

dbtSeedfilePath

Tables

Columns

Models

Sources

Tests

Seeds
