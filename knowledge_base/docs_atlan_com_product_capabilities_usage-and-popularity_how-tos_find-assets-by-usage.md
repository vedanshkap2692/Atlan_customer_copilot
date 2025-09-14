# Find assets by usage
(source: https://docs.atlan.com/product/capabilities/usage-and-popularity/how-tos/find-assets-by-usage)

Usage & PopularityGet StartedHow to find assets by usageAnalysisTroubleshooting

Get StartedHow to find assets by usage

How to find assets by usage

Analysis

Troubleshooting

Use data

Usage & Popularity

Get Started

How to find assets by usage

Data teams often lack clarity on which data assets can be considered trustworthy, whether these are frequently used, the freshness of the data itself, or how critical these are for enrichment and governance.

With Atlan's usage and popularity metadata, you'll be able to check off all these boxes! You can view usage metrics for your assets collected over the last 30 days.

Atlan currently supports usage and popularity metrics for the following connectors:

Amazon Redshift-  tables, views, and columns. Expensive queries and compute costs for Amazon Redshift assets are currently unavailable due to limitations at source.

Databricks-  tables, views, and columns. Expensive queries and compute costs for Databricks assets are currently unavailable due to limitations of theDatabricks APIs.

Google BigQuery-  tables, views, and columns

Microsoft Power BI-  reports and dashboards

Snowflake-  tables, views, and columns



## Filter assets by usageâ
(source: https://docs.atlan.com/product/capabilities/usage-and-popularity/how-tos/find-assets-by-usage)

Use the usage filters to filter your assets by usage metadata. For instance, you'll be able to filter assets with zero queries and archive them or find costly assets to better optimize your operations.

To filter assets by usage metadata:

From the left menu in Atlan, clickAssets.

In theFiltersmenu inAssets, clickUsageto expand the list of filters.

From theUsagemenu:ForSQLassets, use the following filters:ClickNumber of queriesto filter by the number of queries at source in the last 30 days.ClickNumber of usersto filter by the number of users who queried an asset at source in the last 30 days.ClickLast queriedto filter by the last queried timestamp at source.ClickLast row updated atto filter by the last row updated timestamp at source.To filter assets bycompute cost, clickSnowflake creditsfor Snowflake assets or clickBigQuery query costfor Google BigQuery assets.ForBIassets, use the following filters:ClickViews countto filter by the number of views at source in the last 30 days.ClickNumber of usersto filter by the number of users who viewed an asset at source in the last 30 days.ClickLast viewedto filter by the last viewed timestamp at source.

ForSQLassets, use the following filters:ClickNumber of queriesto filter by the number of queries at source in the last 30 days.ClickNumber of usersto filter by the number of users who queried an asset at source in the last 30 days.ClickLast queriedto filter by the last queried timestamp at source.ClickLast row updated atto filter by the last row updated timestamp at source.To filter assets bycompute cost, clickSnowflake creditsfor Snowflake assets or clickBigQuery query costfor Google BigQuery assets.

ClickNumber of queriesto filter by the number of queries at source in the last 30 days.

ClickNumber of usersto filter by the number of users who queried an asset at source in the last 30 days.

ClickLast queriedto filter by the last queried timestamp at source.

ClickLast row updated atto filter by the last row updated timestamp at source.

To filter assets bycompute cost, clickSnowflake creditsfor Snowflake assets or clickBigQuery query costfor Google BigQuery assets.

ForBIassets, use the following filters:ClickViews countto filter by the number of views at source in the last 30 days.ClickNumber of usersto filter by the number of users who viewed an asset at source in the last 30 days.ClickLast viewedto filter by the last viewed timestamp at source.

ClickViews countto filter by the number of views at source in the last 30 days.

ClickNumber of usersto filter by the number of users who viewed an asset at source in the last 30 days.

ClickLast viewedto filter by the last viewed timestamp at source.

Your search results will now be filtered by usage metadata! ð



## Sort assets by popularityâ
(source: https://docs.atlan.com/product/capabilities/usage-and-popularity/how-tos/find-assets-by-usage)

Sort your data assets by popularity metadata to view the most or least used tables, views, or columns. For example, sorting your assets by popularity can help you deprecate unused or stale data assets, helping you reduce operational costs for your organization.

To sort assets by popularity:

From the left menu in Atlan, clickAssets.

ForConnectoron theAssetspage, select a supported connector   -  for this example, we'll selectSnowflake.

Next to the search bar on theAssetspage, click the sort button.

From thePopularitysorting menu, clickMost popularto view most used assets orLeast popularto view least used assets.

Your assets in the search results will now be sorted by popularity of usage! ð

You can alsodeep dive into usage metricsfor Snowflake, Databricks, Google BigQuery, and Microsoft Power BI in Atlan.

connectors

data

Filter assets by usage

Sort assets by popularity
