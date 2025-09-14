# What does Atlan crawl from Qlik Sense Cloud?
(source: https://docs.atlan.com/apps/connectors/business-intelligence/qlik-sense-cloud/references/what-does-atlan-crawl-from-qlik-sense-cloud)

Qlik Sense CloudGet StartedCrawl Qlik Sense Cloud AssetsReferencesWhat does Atlan crawl from Qlik Sense Cloud?Preflight checks for Qlik Sense CloudTroubleshooting

Get Started

Crawl Qlik Sense Cloud Assets

ReferencesWhat does Atlan crawl from Qlik Sense Cloud?Preflight checks for Qlik Sense Cloud

What does Atlan crawl from Qlik Sense Cloud?

Preflight checks for Qlik Sense Cloud

Troubleshooting

Connect data

BI Tools

Cloud-based BI

Qlik Sense Cloud

References

What does Atlan crawl from Qlik Sense Cloud?

Atlan crawls and maps the following assets and properties from Qlik Sense Cloud.

Once you'vecrawled Qlik Sense Cloud, you canuse connector-specific filtersfor quick asset discovery. The following filters are currently supported for these assets:

Apps

Sheets

Datasets



## Lineageâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/qlik-sense-cloud/references/what-does-atlan-crawl-from-qlik-sense-cloud)

Atlan only supports asset-level lineage for the following asset types:

Datasets --> Charts --> Sheets --> Apps



## Spacesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/qlik-sense-cloud/references/what-does-atlan-crawl-from-qlik-sense-cloud)

Atlan maps spaces from Qlik Sense Cloud to itsQlikSpaceasset type.

QlikSpace



## Appsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/qlik-sense-cloud/references/what-does-atlan-crawl-from-qlik-sense-cloud)

Atlan maps apps from Qlik Sense Cloud to itsQlikAppasset type.

QlikApp

Only theappresource type is retrieved. Other types, such asqvapporqlikview, are not crawled.

app

qvapp

qlikview



## Sheetsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/qlik-sense-cloud/references/what-does-atlan-crawl-from-qlik-sense-cloud)

Atlan maps sheets from Qlik Sense Cloud to itsQlikSheetasset type.

QlikSheet



## Chartsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/qlik-sense-cloud/references/what-does-atlan-crawl-from-qlik-sense-cloud)

Atlan maps charts from Qlik Sense Cloud to theQlikChartasset type and catalogs only those linked to dataset fields. For example, table charts are crawled because their columns represent dataset dimensions or measures. UI elements that do not reference dataset fields  - such as filters, buttons, and text elements  - are ignored.

QlikChart

These elements are not considered charts and are not crawled:filterpane,qlik-button-for-navigation,VizlibAdvancedTextObject,listbox,action-button,VizlibFilter,variable,text-image,VizlibLineObject.

filterpane

qlik-button-for-navigation

VizlibAdvancedTextObject

listbox

action-button

VizlibFilter

variable

text-image

VizlibLineObject



## Datasetsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/qlik-sense-cloud/references/what-does-atlan-crawl-from-qlik-sense-cloud)

Atlan maps datasets from Qlik Sense Cloud to theQlikDatasetasset type. Datasets loaded through the Data Load Editor are calledimplicit datasetsin Atlan and appear under this type.

QlikDataset

implicit datasets

connectors

data

crawl

Lineage

Spaces

Apps

Sheets

Charts

Datasets
