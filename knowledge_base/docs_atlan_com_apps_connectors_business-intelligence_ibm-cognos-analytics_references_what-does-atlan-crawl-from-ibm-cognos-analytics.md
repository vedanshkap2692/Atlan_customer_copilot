# What does Atlan crawl from IBM Cognos Analytics?
(source: https://docs.atlan.com/apps/connectors/business-intelligence/ibm-cognos-analytics/references/what-does-atlan-crawl-from-ibm-cognos-analytics)

IBM Cognos AnalyticsGet StartedCrawl Cognos Analytics AssetsReferencesWhat does Atlan crawl from IBM Cognos Analytics?Troubleshooting

Get Started

Crawl Cognos Analytics Assets

ReferencesWhat does Atlan crawl from IBM Cognos Analytics?

What does Atlan crawl from IBM Cognos Analytics?

Troubleshooting

Connect data

BI Tools

On-premises & Enterprise BI

IBM Cognos Analytics

References

What does Atlan crawl from IBM Cognos Analytics?

Atlan crawls and maps the following assets and properties from IBM Cognos Analytics.

Atlan also supports lineage:

For packages, files, reports, and modules.

To upstream sources   -  Microsoft SQL Server and Snowflake.

Field-level lineage is currently not supported.

Atlan generates thesourceURLproperty for IBM Cognos Analytics assets using a combination of the host, port, andidof the asset. This allows Atlan to help you view your assets directly in IBM Cognos Analytics from the asset profile.

sourceURL

id

Direct extraction-  in addition toid, Atlan obtains the host and port values from the credentials you provided while setting up a crawler workflow.

id

Offline extraction-  in addition toid, Atlan obtains the host and port values from the parameters with which the offline extractor is executed.

id

Assets marked with ð includes lineage and column-level lineage.

Assets marked with ð display column information.



## Foldersâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/ibm-cognos-analytics/references/what-does-atlan-crawl-from-ibm-cognos-analytics)

Atlan maps folders from IBM Cognos Analytics to itsCognosFolderasset type.

CognosFolder

defaultName

name

defaultDescription

description

id

cognosId

searchPath

cognosPath

type

cognosType

version

cognosVersion

hidden

cognosIsHidden

creationTime

sourceCreatedAt

modificationTime

sourceUpdatedAt

owner

sourceOwners



## Dashboards ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/ibm-cognos-analytics/references/what-does-atlan-crawl-from-ibm-cognos-analytics)

Atlan maps dashboards from IBM Cognos Analytics to itsCognosDashboardasset type.

CognosDashboard

defaultName

name

defaultDescription

description

id

cognosId

searchPath

cognosPath

type

cognosType

version

cognosVersion

hidden

cognosIsHidden

creationTime

sourceCreatedAt

modificationTime

sourceUpdatedAt

owner

sourceOwners



## Packages ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/ibm-cognos-analytics/references/what-does-atlan-crawl-from-ibm-cognos-analytics)

Atlan maps packages from IBM Cognos Analytics to itsCognosPackageasset type.

CognosPackage

defaultName

name

defaultDescription

description

id

cognosId

searchPath

cognosPath

type

cognosType

version

cognosVersion

hidden

cognosIsHidden

creationTime

sourceCreatedAt

modificationTime

sourceUpdatedAt

owner

sourceOwners



## Explorations ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/ibm-cognos-analytics/references/what-does-atlan-crawl-from-ibm-cognos-analytics)

Atlan maps explorations from IBM Cognos Analytics to itsCognosExplorationasset type.

CognosExploration

defaultName

name

defaultDescription

description

id

cognosId

searchPath

cognosPath

type

cognosType

version

cognosVersion

hidden

cognosIsHidden

creationTime

sourceCreatedAt

modificationTime

sourceUpdatedAt

owner

sourceOwners



## Reports ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/ibm-cognos-analytics/references/what-does-atlan-crawl-from-ibm-cognos-analytics)

Atlan maps reports from IBM Cognos Analytics to itsCognosReportasset type.

CognosReport

defaultName

name

defaultDescription

description

id

cognosId

searchPath

cognosPath

type

cognosType

version

cognosVersion

hidden

cognosIsHidden

creationTime

sourceCreatedAt

modificationTime

sourceUpdatedAt

owner

sourceOwners



## Files ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/ibm-cognos-analytics/references/what-does-atlan-crawl-from-ibm-cognos-analytics)

Atlan maps files from IBM Cognos Analytics to itsCognosFileasset type.

CognosFile

defaultName

name

defaultDescription

description

id

cognosId

searchPath

cognosPath

type

cognosType

version

cognosVersion

hidden

cognosIsHidden

creationTime

sourceCreatedAt

modificationTime

sourceUpdatedAt

owner

sourceOwners



## Data sourcesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/ibm-cognos-analytics/references/what-does-atlan-crawl-from-ibm-cognos-analytics)

Atlan maps data sources from IBM Cognos Analytics to itsCognosDatasourceasset type.

CognosDatasource

defaultName

name

defaultDescription

description

id

cognosId

searchPath

cognosPath

type

cognosType

version

cognosVersion

hidden

cognosIsHidden

creationTime

sourceCreatedAt

modificationTime

sourceUpdatedAt

owner

sourceOwners

connectionString

cognosDatasourceConnectionString



## Modules ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/ibm-cognos-analytics/references/what-does-atlan-crawl-from-ibm-cognos-analytics)

Atlan maps modules from IBM Cognos Analytics to itsCognosModuleasset type.

CognosModule

defaultName

name

defaultDescription

description

id

cognosId

searchPath

cognosPath

type

cognosType

version

cognosVersion

modificationTime

sourceUpdatedAt



## Columnsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/ibm-cognos-analytics/references/what-does-atlan-crawl-from-ibm-cognos-analytics)

Atlan maps fields from IBM Cognos Analytics to its CognosColumns asset type. Based on the asset type, some attributes may not be extracted:

cognosColumnRegularAggregateappears only for reports and datasets.

cognosColumnRegularAggregate

cognosColumnDatatypeappears only for modules.

cognosColumnDatatype

label

name

datatype

cognosDatatype

regularAggregate

cognosRegularAggregate

connectors

crawl

Folders

Dashboards ð

Packages ð

Explorations ð

Reports ð

Files ð

Data sources

Modules ð

Columns
