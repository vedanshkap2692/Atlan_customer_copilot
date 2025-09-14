# What does Atlan crawl from Mode?
(source: https://docs.atlan.com/apps/connectors/business-intelligence/mode/references/what-does-atlan-crawl-from-mode)

ModeGet StartedCrawl Mode AssetsReferencesWhat does Atlan crawl from Mode?Preflight checks for ModeTroubleshooting

Get Started

Crawl Mode Assets

ReferencesWhat does Atlan crawl from Mode?Preflight checks for Mode

What does Atlan crawl from Mode?

Preflight checks for Mode

Troubleshooting

Connect data

BI Tools

Cloud-based BI

Mode

References

What does Atlan crawl from Mode?

Atlan crawls and maps the following assets and properties from Mode.



## Workspacesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/mode/references/what-does-atlan-crawl-from-mode)

Atlan maps workspaces from Mode to itsModeWorkspaceasset type.

ModeWorkspace

name

name

id

modeId

token

modeToken

username

modeWorkspaceUsername

space_count

modeCollectionCount

_links.web.href

sourceURL

created_at

sourceCreatedAt



## Collectionsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/mode/references/what-does-atlan-crawl-from-mode)

Atlan maps collections from Mode to itsModeCollectionasset type.

ModeCollection

name

name

description

description

id

modeId

token

modeToken

space_type

modeCollectionType

state

modeCollectionState

_links.creator

sourceCreatedBy

_links.web

sourceURL

extras.workspace.name

modeWorkspaceName

modeReports



## Reportsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/mode/references/what-does-atlan-crawl-from-mode)

Atlan maps reports from Mode to itsModeReportasset type.

ModeReport

name

name

description

description

id

modeId

token

modeToken

created_at

sourceCreatedAt

updated_at

sourceUpdatedAt

_links.creator

sourceCreatedBy

_links.web

sourceURL

space_token

modeCollectionToken

account_username

modeWorkspaceUsername

published_at

modeReportPublishedAt

query_count

modeQueryCount

chart_count

modeChartCount

query_preview

modeQueryPreview

public

modeIsPublic

shared

modeIsShared

view_count

popularityScore

archived

modeIsArchived

modeCollections



## Queriesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/mode/references/what-does-atlan-crawl-from-mode)

Atlan maps queries from Mode to itsModeQueryasset type.

ModeQuery

name

name

id

modeId

token

modeToken

created_at

sourceCreatedAt

updated_at

sourceUpdatedAt

_links.creator.href

sourceCreatedBy

raw_query

modeRawQuery

explorations_count

modeExplorationCount

report_imports_count

modeReportImportCount

data_source_id

modeDatasourceId

datasource.name

extras.datasource.name

modeDatasourceName

extras.report.name

modeReportName



## Chartsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/mode/references/what-does-atlan-crawl-from-mode)

Atlan maps charts from Mode to itsModeChartasset type.

ModeChart

name

name

description

description

token

modeToken

view_vegas.chartType

modeChartType

created_at

sourceCreatedAt

updated_at

sourceUpdatedAt

_links.creator.href

sourceCreatedBy

_links.report_viz_web.href

sourceURL

extras.query.name

modeQueryName

integration

connectors

Workspaces

Collections

Reports

Queries

Charts
