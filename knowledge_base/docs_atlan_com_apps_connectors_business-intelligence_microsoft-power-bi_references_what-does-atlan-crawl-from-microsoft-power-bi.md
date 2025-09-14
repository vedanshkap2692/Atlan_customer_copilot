# What does Atlan crawl from Microsoft Power BI?
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Microsoft Power BIGet StartedCrawl Power BI AssetsReferencesWhat does Atlan crawl from Microsoft Power BI?Preflight checks for Microsoft Power BIWhat lineage does Atlan extract from Microsoft Power BI?TroubleshootingFAQ

Get Started

Crawl Power BI Assets

ReferencesWhat does Atlan crawl from Microsoft Power BI?Preflight checks for Microsoft Power BIWhat lineage does Atlan extract from Microsoft Power BI?

What does Atlan crawl from Microsoft Power BI?

Preflight checks for Microsoft Power BI

What lineage does Atlan extract from Microsoft Power BI?

Troubleshooting

FAQ

Connect data

BI Tools

On-premises & Enterprise BI

Microsoft Power BI

References

What does Atlan crawl from Microsoft Power BI?

Atlan crawls and maps the following assets and properties from Microsoft Power BI.

Once you'vecrawled Microsoft Power BI, you canuse connector-specific filtersfor quick asset discovery. The following filters are currently supported for these assets:

Measures-  External measure filter

Currently Atlan only represents the assets marked with ð in lineage.

For your Microsoft Power BIreports, Atlan also provides asset previews to help with quick discovery and give you the context you need.



## Appsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan mapsAppsfrom Microsoft Power BI to itsPowerBIAppasset type.

PowerBIApp

name

name

id

powerBIAppId

description

description

publishedBy

sourceOwners

users   ( displayName, appUserAccessRight )

powerBIAppUsers

groups   ( displayName, appUserAccessRight )

powerBIAppGroups



## Workspacesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps workspaces from Microsoft Power BI to itsPowerBIWorkspaceasset type.

PowerBIWorkspace

name

name

description

description

reportCount

reportCount

dashboardCount

dashboardCount

datasetCount

datasetCount

dataflowCount

dataflowCount

webUrl

sourceURL



## Dashboards ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps dashboards from Microsoft Power BI to itsPowerBIDashboardasset type.

PowerBIDashboard

displayName

name

workspace_name

workspaceName

description

description

tileCount

tileCount

webUrl

sourceURL



## Data sourcesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps data sources from Microsoft Power BI to itsPowerBIDatasourceasset type.

PowerBIDatasource

name

name

connectionDetails

connectionDetails



## Datasets ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps datasets from Microsoft Power BI to itsPowerBIDatasetasset type.

PowerBIDataset

name

name

workspace_name

workspaceName

description

description

webUrl

sourceURL

configuredBy

sourceOwners

createdDate

sourceCreatedAt

endorsementDetails

certificateStatus (VERIFIED)

endorsementDetails (endorsement)

certificateStatusMessage

powerBIEndorsement

endorsementDetails (certifiedBy)

certificateUpdatedBy



## Dataflows ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps dataflows from Microsoft Power BI to itsPowerBIDataflowasset type. Atlan currently only supports dataflow lineage for the following SQL sources:

PowerBIDataflow

Microsoft SQL Server

Oracle

SAP HANA

Snowflake

name

name

workspace_name

workspaceName

description

description

webUrl

sourceURL

configuredBy

sourceOwners

modifiedDateTime

sourceUpdatedAt

endorsementDetails

certificateStatus (VERIFIED)

endorsementDetails (endorsement)

certificateStatusMessage

powerBIEndorsement

endorsementDetails (certifiedBy)

certificateUpdatedBy

modifiedBy

sourceUpdatedBy

days

powerBIDataflowRefreshScheduleFrequency

times

powerBIDataflowRefreshScheduleTimes

localTimeZoneId

powerBIDataflowRefreshScheduleTimeZone



## Dataflow entity columns ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps attributes of dataflow entities from Microsoft Power BI to itsPowerBIDataflowEntityColumnasset type.

PowerBIDataflowEntityColumn

attrbutes.name

name

entities.name

powerBIDataflowEntityName

attributes.$type

powerBIDataflowEntityColumnDataType



## Reports ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps reports from Microsoft Power BI to itsPowerBIReportasset type.

PowerBIReport

name

name

workspace_name

workspaceName

description

description

pageCount

pageCount

webUrl

sourceURL

createdDateTime

sourceCreatedAt

modifiedDateTime

sourceUpdatedAt

createdBy

sourceCreatedBy

sourceOwners

modifiedBy

sourceUpdatedBy

endorsementDetails

certificateStatus (VERIFIED)

endorsementDetails (endorsement)

certificateStatusMessage

powerBIEndorsement

endorsementDetails (certifiedBy)

certificateUpdatedBy



## Pages ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps pages from Microsoft Power BI to itsPowerBIPageasset type.

PowerBIPage

displayName

name

workspace_name

workspaceName

report_name

reportName



## Tiles ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps tiles from Microsoft Power BI to itsPowerBITileasset type.

PowerBITile

title

name

subTitle

description

workspace_name

workspaceName

dashboard_name

dashboardName



## Tables ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps tables from Microsoft Power BI to itsPowerBITableasset type.

PowerBITable

name

name

description

description

isHidden

isHidden

sourceExpressions

powerBITableSourceExpressions

columnCount

powerBITableColumnCount

measureCount

powerBITableMeasureCount



## Columns ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps columns from Microsoft Power BI to itsPowerBIColumnasset type.

PowerBIColumn

name

name

description

description

isHidden

powerBIIsHidden

dataCategory

powerBIColumnDataCategory

dataType

powerBIColumnDataType

formatString

powerBIFormatString

sortByColumn

powerBISortByColumn

summarizeBy

powerBIColumnSummarizeBy



## Measures ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-does-atlan-crawl-from-microsoft-power-bi)

Atlan maps measures from Microsoft Power BI to itsPowerBIMeasureasset type. Atlan supports PowerBI Measures for downstream lineage to a PowerBI Page.

PowerBIMeasure

name

name

description

description

isHidden

powerBIIsHidden

expression

powerBIMeasureExpression

isExternalMeasure

powerBIIsExternalMeasure

formatString

powerBIFormatString

connectors

crawl

Apps

Workspaces

Dashboards ð

Data sources

Datasets ð

Dataflows ð

Dataflow entity columns ð

Reports ð

Pages ð

Tiles ð

Tables ð

Columns ð

Measures ð
