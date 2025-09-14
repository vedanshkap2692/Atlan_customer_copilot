# Snowflake warehouse configuration
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/best-practices/snowflake-warehouse-configuration)

SnowflakeGet StartedCrawl Snowflake AssetsManage Snowflake in AtlanReferencesTroubleshootingBest PracticesSnowflake warehouse configuration

Get Started

Crawl Snowflake Assets

Manage Snowflake in Atlan

References

Troubleshooting

Best PracticesSnowflake warehouse configuration

Snowflake warehouse configuration

Connect data

Data Warehouses

Snowflake

Best Practices

Snowflake warehouse configuration

Configure your Snowflake warehouses following these best practices to achieve optimal performance and reliability for Atlan data workflows. These recommendations establish predictable resource allocation and maximize workflow efficiency.



## Configure warehouse allocationâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/best-practices/snowflake-warehouse-configuration)

Use a dedicated warehouse for Atlan workflows: Assign a dedicated warehouse exclusively for Atlan operations. This approach separates warehouse performance from other workloads, enables precise cost tracking for Atlan operations, and provides consistent workflow performance.

Use a dedicated warehouse for Atlan workflows: Assign a dedicated warehouse exclusively for Atlan operations. This approach separates warehouse performance from other workloads, enables precise cost tracking for Atlan operations, and provides consistent workflow performance.

One warehouse per connection: Provision one Snowflake warehouse for each Atlan connection to maintain scoped capacity and predictable resource allocation.

One warehouse per connection: Provision one Snowflake warehouse for each Atlan connection to maintain scoped capacity and predictable resource allocation.



## Configure statement timeoutâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/best-practices/snowflake-warehouse-configuration)

Set appropriate timeout values: If your account enforces timeouts, configure bothSTATEMENT_TIMEOUT_IN_SECONDSandSTATEMENT_QUEUED_TIMEOUT_IN_SECONDSto at least 6 hours (21,600 seconds) for the Atlan user to accommodate comprehensive data cataloging workflows.

Set appropriate timeout values: If your account enforces timeouts, configure bothSTATEMENT_TIMEOUT_IN_SECONDSandSTATEMENT_QUEUED_TIMEOUT_IN_SECONDSto at least 6 hours (21,600 seconds) for the Atlan user to accommodate comprehensive data cataloging workflows.

STATEMENT_TIMEOUT_IN_SECONDS

STATEMENT_QUEUED_TIMEOUT_IN_SECONDS

Default values work well: By default, both parameters are set to0(no limit), which is optimal for Atlan operations. Only adjust if your organization requires specific timeout enforcement.

Default values work well: By default, both parameters are set to0(no limit), which is optimal for Atlan operations. Only adjust if your organization requires specific timeout enforcement.

0

Apply at user level: Configure timeouts at the user level for consistent behavior across all Atlan sessions rather than at warehouse or session level.

Apply at user level: Configure timeouts at the user level for consistent behavior across all Atlan sessions rather than at warehouse or session level.

snowflake

warehouse

configuration

Configure warehouse allocation

Configure statement timeout
