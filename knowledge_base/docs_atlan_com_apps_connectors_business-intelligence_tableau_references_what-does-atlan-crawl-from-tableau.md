# What does Atlan crawl from Tableau?
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

TableauGet StartedCrawl Tableau AssetsReferencesWhat does Atlan crawl from Tableau?Preflight checks for TableauTroubleshooting

Get Started

Crawl Tableau Assets

ReferencesWhat does Atlan crawl from Tableau?Preflight checks for Tableau

What does Atlan crawl from Tableau?

Preflight checks for Tableau

Troubleshooting

Connect data

BI Tools

On-premises & Enterprise BI

Tableau

References

What does Atlan crawl from Tableau?

Atlan crawls and maps the following assets and properties from Tableau.

Once you'vecrawled Tableau, you canuse connector-specific filtersfor quick asset discovery. The following filters are currently supported for these assets:

Projects   -  filter Tableau assets by projects, including nested projects

Data sources   -  Is published filter

For your Tableauworksheetsanddashboards, Atlan also provides asset previews to help with quick discovery and give you the context you need.

You may need todisable clickjack protectionfor Tableau asset previews to load.



## Lineageâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Did you know?Lineage to dashboards may appear incomplete or missing if worksheets are not crawled. Additionally, Tableau assets that haven't been refreshed since May 27, 2025, won't display the new column-level lineage (CLL) or updated lineage paths.

Atlan supports lineage for the following:

Asset Lineage- Datasource to Dashboard, Datasource to Worksheet, Datasource to Workbook

Column Level Lineage- Supported for Datasource to Worksheet and Worksheet to Dashboard



## Sitesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Atlan maps sites from Tableau to itsTableauSiteasset type.

TableauSite

name

name



## Projectsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Atlan maps projects from Tableau to itsTableauProjectasset type.

TableauProject

name

name

description

description

createdAt

sourceCreatedAt

owner

[sourceOwner](/apps/connectors/business-intelligence/tableau/troubleshooting/troubleshooting-tableau-connectivity)

updatedAt

sourceUpdatedAt

hierarchy

projectHierarchy

topLevelProject

isTopLevelProject



## Flowsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Due to limitations at source, Atlan won't be able to crawl Tableau flows if you use theJWT bearer authenticationmethod.

Atlan maps flows from Tableau to itsTableauFlowasset type.

TableauFlow

name

name

description

description

owner

[sourceOwner](/apps/connectors/business-intelligence/tableau/troubleshooting/troubleshooting-tableau-connectivity)

project_extra (hierarchy)

projectHierarchy



## Metricsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Tableau hasretired metrics methods in API 3.22for Tableau Cloud and Tableau Server version 2024.2. If you're using Tableau API version 3.22 or higher, metadata for metrics is unavailable in Atlan.

Atlan maps metrics from Tableau to itsTableauMetricasset type.

TableauMetric

name

name

description

description

createdAt

sourceCreatedAt

updatedAt

sourceUpdatedAt

project_extra (hierarchy)

projectHierarchy



## Workbooksâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Atlan maps workbooks from Tableau to itsTableauWorkbookasset type.

TableauWorkbook

name

name

description

description

webpageUrl

sourceURL

owner

[sourceOwner](/apps/connectors/business-intelligence/tableau/troubleshooting/troubleshooting-tableau-connectivity)

createdAt

sourceCreatedAt

updatedAt

sourceUpdatedAt

project_extra (hierarchy)

projectHierarchy



## Worksheetsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Atlan maps worksheets from Tableau to itsTableauWorksheetasset type.

TableauWorksheet

name

name

createdAt

sourceCreatedAt

updatedAt

sourceUpdatedAt

source_url

sourceURL

project_extra (hierarchy)

projectHierarchy



## Dashboardsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Atlan maps dashboards from Tableau to itsTableauDashboardasset type.

TableauDashboard

name

name

createdAt

sourceCreatedAt

updatedAt

sourceUpdatedAt

source_url

sourceURL

project_extra (hierarchy)

projectHierarchy



## Data sourcesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Atlan maps data sources (embedded and published) from Tableau to itsTableauDatasourceasset type.

TableauDatasource

name

name

description

description

owner

isPublished

isPublished

hasExtracts

hasExtracts

upstreamTables

upstreamTables

upstreamDatabases

upstreamDatabases

isCertified

VERIFIED

certifier

certifier

certificationNote

certificationStatusMessage

certifierDisplayName

certificateUpdatedBy

project_extra (hierarchy)

projectHierarchy



## Data source fieldsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Atlan maps data source fields and column fields from Tableau to itsTableauDatasourceFieldasset type.

TableauDatasourceField

name

name

description

description

upstreamTables

upstreamTables

upstreamColumns

upstreamColumns

dataCategory

tableauDatasourceFieldDataCategory

role

tableauDatasourceFieldRole

dataType

tableauDatasourceFieldDataType

formula

tableauDatasourceFieldFormula

binSize

tableauDatasourceFieldBinSize

__typename

datasourceFieldType

project_extra (hierarchy)

projectHierarchy



## Custom SQLâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Atlan parses custom SQL queries used in Tableau data sources to extract lineage information. This process identifies the relationships between data assets based on the SQL logic defined within Tableau.

downstreamDatasources

TableauDatasource

query

CustomSQLQuery



## Calculated fieldsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Atlan maps calculated fields from Tableau to itsTableauCalculatedFieldasset type.

TableauCalculatedField

name

name

description

description

dataCategory

dataCategory

role

role

dataType

tableauDataType

formula

formula

project_extra (hierarchy)

projectHierarchy



## Lineageâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/tableau/references/what-does-atlan-crawl-from-tableau)

Atlan calculates lineage for Tableau as follows:

Lineage is currently not supported for Tableauflowsandmetrics.

connectors

data

crawl

Lineage

Sites

Projects

Flows

Metrics

Workbooks

Worksheets

Dashboards

Data sources

Data source fields

Custom SQL

Calculated fields

Lineage
