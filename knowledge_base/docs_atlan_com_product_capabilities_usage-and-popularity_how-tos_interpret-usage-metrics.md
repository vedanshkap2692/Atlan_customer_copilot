# Interpret usage metrics
(source: https://docs.atlan.com/product/capabilities/usage-and-popularity/how-tos/interpret-usage-metrics)

Usage & PopularityGet StartedAnalysisHow to interpret usage metricsTroubleshooting

Get Started

AnalysisHow to interpret usage metrics

How to interpret usage metrics

Troubleshooting

Use data

Usage & Popularity

Analysis

How to interpret usage metrics

Atlan currently supports usage and popularity metrics for the following connectors:

Amazon Redshift-  tables, views, and columns. Expensive queries and compute costs for Amazon Redshift assets are currently unavailable due to limitations at source.

Databricks-  tables, views, and columns. Expensive queries and compute costs for Databricks assets are currently unavailable due to limitations of theDatabricks APIs.

Google BigQuery-  tables, views, and columns

Microsoft Power BI-  reports and dashboards

Snowflake-  tables, views, and columns

Powered by Atlan's enhanced query-mining capabilities, you can view popularity metrics for supported assets:

Thepopularity scoreof an asset is computed using both the number of queries and the number of users who have queried that asset in the last 30 days. The popularity score of an asset helps determine its relative popularity. All assets with a popularity score are then slotted into one of four percentile groups   -Least popular,Less popular,Popular, andMost popular.Popularity score is calculated using the following formula:number of distinct users * log (total number of read queries)Time period = 30 days

Popularity score is calculated using the following formula:number of distinct users * log (total number of read queries)

Popularity score is calculated using the following formula:

number of distinct users * log (total number of read queries)

number of distinct users * log (total number of read queries)

Time period = 30 days

Time period = 30 days

Thepopularity indicatoris displayed for all supported assets that have been queried in the last 30 days. This indicator visualizes the relative popularity of an asset on a scale of 1 to 4 blue bars   -  1 being the lowest score and 4 being the highest.

Apopularity popoverwill appear when hovering over the popularity indicator. It displays additional information pertaining to an asset, such as a graph for trends in the data, last queried and by whom, and when the data was last updated.



## View popularity metricsâ
(source: https://docs.atlan.com/product/capabilities/usage-and-popularity/how-tos/interpret-usage-metrics)

To view popularity metrics for your assets, complete these steps.



### Identify popular assetsâ
(source: https://docs.atlan.com/product/capabilities/usage-and-popularity/how-tos/interpret-usage-metrics)

Being able to identify your most relevant and trusted data assets can help you increase their adoption and drive usage within your organization.

To view popularity metrics for an asset:

From the left menu in Atlan, clickAssets.

ForConnectoron theAssetspage, select a supported connector   -  for this example, we'll selectSnowflake.

Next to the search bar on theAssetspage, click the sort button.

From thePopularitysorting menu, clickMost popularto view most used assets orLeast popularto view least used assets.

Your assets will now have a popularity indicator. To view the popularity popover for an asset, click or hover over thepopularityindicator.Â

You'll now be able to see all the relevant popularity metrics for your asset! ð



### View usage metrics in the asset sidebarâ
(source: https://docs.atlan.com/product/capabilities/usage-and-popularity/how-tos/interpret-usage-metrics)

The newUsagetab in the asset sidebar helps you view usage metadata for your assets.

For example, if you'd like to appoint a data steward for your data assets, you'll be able to determine the right candidate based on the top users for that asset. You'll also be able to review popular queries or users for a particular table while checking for data compliance.

To view usage details for an asset:

From the left menu in Atlan, clickAssets.

ForConnectoron theAssetspage, select a supported connector   -  for this example, we'll selectSnowflake.

Next to the search bar on theAssetspage, click the sort button.

From thePopularitysorting menu, clickMost popularto view most used assets orLeast popularto view least used assets.

In the bottom right of any asset card, click or hover over thepopularityindicatorto open the popularity popover.Â

In the popularity popover, clickView usage detailsto view the following:ForUsage, view top and recent users in the last 30 days.ForQueries, view top five queries by context   -Popular,Slow, andExpensive. Only read queries orSELECTstatements are shown for these queries.ForCompute, view the totalcompute costfor an asset. The compute cost is split between read and write queries, allowing you to better understand the cost breakdown for individual assets:Read queries   -SELECTstatements.Write queries   -  all non-SELECTstatements, for example,UPDATE,INSERT,CREATE, and more.

ForUsage, view top and recent users in the last 30 days.

ForQueries, view top five queries by context   -Popular,Slow, andExpensive. Only read queries orSELECTstatements are shown for these queries.

SELECT

ForCompute, view the totalcompute costfor an asset. The compute cost is split between read and write queries, allowing you to better understand the cost breakdown for individual assets:Read queries   -SELECTstatements.Write queries   -  all non-SELECTstatements, for example,UPDATE,INSERT,CREATE, and more.

Read queries   -SELECTstatements.

SELECT

Write queries   -  all non-SELECTstatements, for example,UPDATE,INSERT,CREATE, and more.

SELECT

UPDATE

INSERT

CREATE

The usage details for the asset will now appear in the asset sidebar! ð



### View and sort columns by popularityâ
(source: https://docs.atlan.com/product/capabilities/usage-and-popularity/how-tos/interpret-usage-metrics)

For any Snowflake, Databricks, or Google BigQuery table or view sorted by popularity, you'll also be able to view and sort the columns by popularity in the asset profile.

To view column assets by popularity:

From the left menu in Atlan, clickAssets.

ForConnectoron theAssetspage, select a supported connector   -  for this example, we'll selectSnowflake.

Next to the search bar on theAssetspage, click the sort button.

From thePopularitysorting menu, clickMost popularto view most used assets orLeast popularto view least used assets.

Click any asset to open to its asset profile.

In theColumn previewtab of the asset profile, hover over the popularity indicator to view the popularity popover for your columns.

(Optional) In the search bar underColumn preview, click thesort iconand then clickMost popularorLeast popularto sort columns by popularity.

You'll now be able to view the popularity score, number of queries and users, and timestamp for last queried for your columns! ð



## View queries by contextâ
(source: https://docs.atlan.com/product/capabilities/usage-and-popularity/how-tos/interpret-usage-metrics)

Get the context you need before querying an asset to help you optimize your queries. Query popular, slow, or expensive queries from theUsagetab directly in Insights.

To view and work with queries by context:

From the left menu in Atlan, clickAssets.

ForConnectoron theAssetspage, select a supported connector   -  for this example, we'll selectSnowflake.

Next to the search bar on theAssetspage, click the sort button.

From thePopularitysorting menu, clickMost popularto view most used assets orLeast popularto view least used assets.

In the bottom right of any asset card, click or hover over thepopularityindicatorto open the popularity popover.Â

In the popularity popover, clickView usage details.

In theUsagetab in the asset sidebar, navigate toQueriesand depending on the type of query you'd like to see:ClickPopularÂ to see the top five most popular queries.ÂClickSlowto see queries sorted by average duration and last run.ClickExpensiveto see the top five most expensive queries.Â

ClickPopularÂ to see the top five most popular queries.Â

ClickSlowto see queries sorted by average duration and last run.

ClickExpensiveto see the top five most expensive queries.Â

Once you've selected the relevant query type, hover over a query card to:Click theexpand iconto see the query details.Click thecopy iconto copy the query and use it as a template for writing your own queries.Click thecode iconto open the query directly inInsightsand run it.

Click theexpand iconto see the query details.

Click thecopy iconto copy the query and use it as a template for writing your own queries.

Click thecode iconto open the query directly inInsightsand run it.

If you have any questions about usage and popularity metrics, head overhere.

connectors

data

api

View popularity metrics

View queries by context
