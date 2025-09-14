# What does Atlan crawl from dbt Cloud?
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-cloud)

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

What does Atlan crawl from dbt Cloud?

Atlan crawls and maps the following assets and properties from dbt Cloud. Atlan also supports lineage between the following:

dbt models

dbt seeds

dbt sources

SQL tables and views materialized by dbt models, dbt seeds, dbt sources

Column-level lineage for these entities

Atlan only crawls dbt assets that are in the âappliedâ (built) state in dbt Cloud. Models must be part of a successful run to be picked up during crawling; models that are only defined in your project files but havenât been executed wonât be included. For more information about project state, seeProject states in dbt Cloud.

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

Atlan's dbt connectivity also populates custom metadata to further enrich the assets in Atlan. TheAtlan dbt-specific propertycolumn in the tables below gives the name of the mapped custom metadata property in Atlan.

Atlan enables you tosync your dbt tagsand update your dbt assets with the synced tags. It's also possible tomap other metadata on Atlan's assets through your dbt models.



## Tablesâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-cloud)

Atlan maps tables from dbt Cloud to itsTableasset type.

Table

description

description

assetDbtTestStatus

alias

assetDbtAlias

meta

assetDbtMeta

uniqueId

assetDbtUniqueId

accountName

assetDbtAccountName

projectName

assetDbtProjectName

packageName

assetDbtPackageName

tags

assetDbtTags

environment.name (collected via REST API)

assetDbtEnvironmentName



## Columnsâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-cloud)

Atlan maps columns from dbt Cloud to itsColumnasset type.

Column

description

description

assetDbtTestStatus

alias

assetDbtAlias

meta

assetDbtMeta

uniqueId

assetDbtUniqueId

accountName

assetDbtAccountName

projectName

assetDbtProjectName

packageName

assetDbtPackageName

tags

assetDbtTags



## Modelsâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-cloud)

Atlan maps models from dbt Cloud to itsModelasset type.

Model

name

name

description

description

owner

sourceCreatedBy

sourceURL

alias

assetDbtAlias

meta

assetDbtMeta

uniqueId

assetDbtUniqueId

accountName

assetDbtAccountName

projectName

assetDbtProjectName

packageName

assetDbtPackageName

rawCode (available via REST API)

dbtRawSQL

compiledCode (available via REST API)

dbtCompiledSQL

tags

assetDbtTags

materializedType

dbtMaterializationType

stats

dbtStats

executionInfo.lastRunStatus

dbtJobRuns.dbtModelRunStatus

job.status (available via REST API)

dbtJobRuns.dbtJobRunStatus

job.name (available via REST API)

dbtJobRuns.dbtJobName

executionInfo.lastJobDefinitionId

dbtJobRuns.dbtJobId

executionInfo.lastRunId

dbtJobRuns.dbtJobRunId

executionInfo.lastRunGeneratedAt

dbtJobRuns.dbtJobRunCompletedAt

environmentId

dbtJobRuns.dbtEnvironmentId

environment.name (available via REST API)

dbtJobRuns.dbtEnvironmentName

compiledCode

dbtJobRuns.dbtCompiledCode



## Sourcesâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-cloud)

Atlan maps sources from dbt Cloud to itsDbtSourceasset type.

DbtSource

name

name

description

description

owner

sourceCreatedBy

sourceURL

alias

assetDbtAlias

meta

assetDbtMeta

uniqueId

assetDbtUniqueId

accountName

assetDbtAccountName

projectName

assetDbtProjectName

packageName

assetDbtPackageName

tags

assetDbtTags

stats

dbtStats

freshness

assetDbtSourceFreshnessCriteria

environmentId

dbtJobRuns.dbtEnvironmentId

environment.name

dbtJobRuns.dbtEnvironmentName



## Testsâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-cloud)

Atlan maps tests from dbt Cloud to itsTestasset type.

Test

name

name

description

description

sourceURL

alias

assetDbtAlias

meta

assetDbtMeta

uniqueId

assetDbtUniqueId

account (name)

assetDbtAccountName

project (name)

assetDbtProjectName

packageName

assetDbtPackageName

rawCode (available via REST API)

dbtTestRawCode

compiledCode (available via REST API)

dbtTestCompiledCode

tags

assetDbtTags

stats

dbtStats

executionInfo.lastRunError

dbtTestError

executionInfo.lastRunStatus

dbtJobRuns.dbtTestRunStatus

job.status (available via REST API)

dbtJobRuns.dbtJobRunStatus

job.name (available via REST API)

dbtJobRuns.dbtJobName

executionInfo.lastJobDefinitionId

dbtJobRuns.dbtJobId

executionInfo.lastRunId

dbtJobRuns.dbtJobRunId

executionInfo.lastRunGeneratedAt

dbtJobRuns.dbtJobRunCompletedAt

environmentId

dbtJobRuns.dbtEnvironmentId

environment.name (available via REST API)

dbtJobRuns.dbtEnvironmentName

compiledCode

dbtJobRuns.dbtCompiledCode



## Seedsâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/references/what-does-atlan-crawl-from-dbt-cloud)

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
