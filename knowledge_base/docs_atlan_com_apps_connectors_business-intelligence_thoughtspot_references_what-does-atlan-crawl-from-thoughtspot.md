# What does Atlan crawl from ThoughtSpot?
(source: https://docs.atlan.com/apps/connectors/business-intelligence/thoughtspot/references/what-does-atlan-crawl-from-thoughtspot)

ThoughtSpotGet StartedCrawl ThoughtSpot AssetsReferencesWhat does Atlan crawl from ThoughtSpot?Troubleshooting

Get Started

Crawl ThoughtSpot Assets

ReferencesWhat does Atlan crawl from ThoughtSpot?

What does Atlan crawl from ThoughtSpot?

Troubleshooting

Connect data

BI Tools

Cloud-based BI

ThoughtSpot

References

What does Atlan crawl from ThoughtSpot?

Once you'vecrawled ThoughtSpot, you canuse connector-specific filtersfor quick asset discovery. The following filters are currently supported for all ThoughtSpot assets:

Tags and chart type filters

Atlan supports lineage for the following ThoughtSpot assets:

Answers-  upstream lineage to tables, views, or worksheets from multiple sources (if applicable), no downstream lineage

Visualizations-  upstream lineage to tables, views, or worksheets from multiple sources (if applicable)

Liveboards-  upstream lineage to visualizations

Tables-  upstream lineage to source tables, and column-level lineage between ThoughtSpot tables and worksheets

Views-  upstream lineage to ThoughtSpot tables or worksheets, and column-level lineage between ThoughtSpot views and worksheets

Worksheets-  upstream lineage to ThoughtSpot tables or views from multiple sources (if applicable)

Atlan crawls and maps the following assets and properties from ThoughtSpot.

Currently, Atlan only represents the assets marked with ð in lineage.



## Answers ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/thoughtspot/references/what-does-atlan-crawl-from-thoughtspot)

Atlan maps answers from ThoughtSpot to itsThoughtSpotAnswerasset type.

ThoughtSpotAnswer

metadata_header.name

name

metadata_header.description

description

metadata_header.created

sourceCreatedAt

metadata_header.modified

sourceUpdatedAt

metadata_header.authorDisplayName

sourceCreatedBy

question.text

thoughtspotQuestionText

metadata_header.tags

assetTags

visualisations.chart_type

thoughtspotChartType



## Visualizations ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/thoughtspot/references/what-does-atlan-crawl-from-thoughtspot)

Atlan maps visualizations from ThoughtSpot to itsThoughtspotDashletasset type.

ThoughtspotDashlet

metadata_header.name

name

metadata_header.description

description

metadata_header.created

sourceCreatedAt

metadata_header.modified

sourceUpdatedAt

metadata_header.authorDisplayName

sourceCreatedBy

question.text

thoughtspotQuestionText

visualisations.chart_type

thoughtspotChartType

metadata_header.name

thoughtspotLiveboardName



## Liveboards ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/thoughtspot/references/what-does-atlan-crawl-from-thoughtspot)

Atlan maps Liveboards from ThoughtSpot to itsThoughtspotLiveboardasset type.

ThoughtspotLiveboard

metadata_header.name

name

metadata_header.description

description

metadata_header.created

sourceCreatedAt

metadata_header.modified

sourceUpdatedAt

metadata_header.authorDisplayName

sourceCreatedBy

metadata_header.tags

assetTags



## Tables ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/thoughtspot/references/what-does-atlan-crawl-from-thoughtspot)

Atlan maps tables from ThoughtSpot to itsThoughtspotTableasset type.

ThoughtspotTable

metadata_header.name

name

metadata_header.description

description

metadata_header.created

sourceCreatedAt

metadata_header.modified

sourceUpdatedAt

metadata_header.authorDisplayName

sourceCreatedBy

length(metadata_detail.relationships[])

thoughtspotJoinCount

length(metadata_detail.columns[])

thoughtspotColumnCount

metadata_header.tags

assetTags



## Views ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/thoughtspot/references/what-does-atlan-crawl-from-thoughtspot)

Atlan maps views from ThoughtSpot to itsThoughtspotViewasset type.

ThoughtspotView

metadata_header.name

name

metadata_header.description

description

metadata_header.created

sourceCreatedAt

metadata_header.modified

sourceUpdatedAt

metadata_header.authorDisplayName

sourceCreatedBy

length(metadata_detail.relationships[])

thoughtspotJoinCount

length(metadata_detail.columns[])

thoughtspotColumnCount

metadata_header.tags

assetTags



## Worksheets ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/thoughtspot/references/what-does-atlan-crawl-from-thoughtspot)

Atlan maps worksheets from ThoughtSpot to itsThoughtspotWorksheetasset type.

ThoughtspotWorksheet

metadata_header.name

name

metadata_header.description

description

metadata_header.created

sourceCreatedAt

metadata_header.modified

sourceUpdatedAt

metadata_header.authorDisplayName

sourceCreatedBy

thoughtspotJoinCount

length(metadata_detail.columns[])

thoughtspotColumnCount

metadata_header.tags

assetTags



## Columns ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/thoughtspot/references/what-does-atlan-crawl-from-thoughtspot)

Atlan maps columns from ThoughtSpot to itsThoughtspotColumnasset type.

ThoughtspotColumn

metadata_header.name

name

metadata_header.description

description

metadata_detail.dataType

thoughtspotColumnDataType

metadata_detail.type

thoughtspotColumnType

connectors

crawl

Answers ð

Visualizations ð

Liveboards ð

Tables ð

Views ð

Worksheets ð

Columns ð
