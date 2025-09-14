# Preflight checks for Databricks
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/preflight-checks-for-databricks)

DatabricksGet StartedCross-workspace SetupCrawl Databricks AssetsOn-premises SetupPrivate Network SetupLineage and UsageTag managementReferencesWhat does Atlan crawl from Databricks?Preflight checks for DatabricksTroubleshooting

Get Started

Cross-workspace Setup

Crawl Databricks Assets

On-premises Setup

Private Network Setup

Lineage and Usage

Tag management

ReferencesWhat does Atlan crawl from Databricks?Preflight checks for Databricks

What does Atlan crawl from Databricks?

Preflight checks for Databricks

Troubleshooting

Connect data

Data Warehouses

Databricks

References

Preflight checks for Databricks

Beforerunning the Databricks crawler, you can runpreflight checksto perform the necessary technical validations. The following preflight checks will be completed:



## JDBCâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/preflight-checks-for-databricks)



### Schemasâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/preflight-checks-for-databricks)

âCheck successful

Check successful

âCheck failed for $missingObjectName

Check failed for $missingObjectName



## Rest API (Unity Catalog)â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/preflight-checks-for-databricks)



### User login/UC enabledâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/preflight-checks-for-databricks)

âCheck successful

Check successful

â Source returned error

For example:{"error_code":"403","message":"Invalid access token."}

{"error_code":"403","message":"Invalid access token."}



### Catalogâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/preflight-checks-for-databricks)

âCheck successful

Check successful

âCheck failed for $missingObjectName catalog

Check failed for $missingObjectName catalog



## Databricks lineage and usage (miner)â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/preflight-checks-for-databricks)

Once you have crawled assets from Databricks, you canextract lineage and usage and popularity metrics.



### Loginâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/preflight-checks-for-databricks)

âCheck successful

Check successful

âCheck failed

Check failed

For example:{"error_code":"403","message":"Invalid access token."}

{"error_code":"403","message":"Invalid access token."}



### Lineage APIâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/preflight-checks-for-databricks)

âCheck successful. Lineage API is enabled.

Check successful. Lineage API is enabled.

âCheck failed

Check failed

For example:Lineage is not enabled for this Databricks account: 47258391-b3c8-4ff9-a0d9-5afc02443806

Lineage is not enabled for this Databricks account: 47258391-b3c8-4ff9-a0d9-5afc02443806



### Query history API endpoint checkâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/references/preflight-checks-for-databricks)

âCheck successful

Check successful

âCheck failed

Check failed

connectors

data

crawl

api

JDBC

Rest API (Unity Catalog)

Databricks lineage and usage (miner)
