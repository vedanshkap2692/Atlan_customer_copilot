# Preflight checks for Snowflake
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/preflight-checks-for-snowflake)

SnowflakeGet StartedCrawl Snowflake AssetsManage Snowflake in AtlanReferencesMultiple tag values and concatenationWhat does Atlan crawl from Snowflake?Preflight checks for SnowflakeTroubleshootingBest Practices

Get Started

Crawl Snowflake Assets

Manage Snowflake in Atlan

ReferencesMultiple tag values and concatenationWhat does Atlan crawl from Snowflake?Preflight checks for Snowflake

Multiple tag values and concatenation

What does Atlan crawl from Snowflake?

Preflight checks for Snowflake

Troubleshooting

Best Practices

Connect data

Data Warehouses

Snowflake

References

Preflight checks for Snowflake

Beforerunning the Snowflake crawler, you can runpreflight checksto perform the necessary technical validations. The following preflight checks will be completed:



## Database and schema checkâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/preflight-checks-for-snowflake)



### Information schemaâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/preflight-checks-for-snowflake)

âCheck successful

Check successful

âCheck failed for $missingObjectName

Check failed for $missingObjectName



### Account usageâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/preflight-checks-for-snowflake)

âCheck successful

Check successful

âCheck failed for $missingObjectName

Check failed for $missingObjectName



## Warehouse accessâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/preflight-checks-for-snowflake)

âCheck successful

Check successful

âOperation cannot be performed/User is not authorized to perform this action/Cannot be resumed because resource monitor has exceeded its quota

Operation cannot be performed

User is not authorized to perform this action

Cannot be resumed because resource monitor has exceeded its quota



## Minerâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/preflight-checks-for-snowflake)

Once you have crawled assets from Snowflake, you canmine query history.



### Query history viewâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/preflight-checks-for-snowflake)

âCheck successful

Check successful

âCannot access query history table. Please run the command in your Snowflake instance: GRANT IMPORTED PRIVILEGES ON DATABASE snowflake TO ROLE atlan_user_role;

Cannot access query history table. Please run the command in your Snowflake instance: GRANT IMPORTED PRIVILEGES ON DATABASE snowflake TO ROLE atlan_user_role;



### Access history viewâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/preflight-checks-for-snowflake)

âCheck successful

Check successful

âCheck failed. Something went wrong with your request.

Check failed. Something went wrong with your request.



### Sessions viewâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/preflight-checks-for-snowflake)

âCheck successful

Check successful

âCheck failed. Something went wrong with your request.

Check failed. Something went wrong with your request.



### S3â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/preflight-checks-for-snowflake)

âCheck successfulif the bucket, region, and prefix combination is valid and the S3 credential passed is accessible.

Check successful

âCheck failed with error code <AWS error code> - <AWS SDK ERR message>

Check failed with error code <AWS error code> - <AWS SDK ERR message>

For example:Miner S3 credentials: failed with error code: NoSuchBucket

Miner S3 credentials: failed with error code: NoSuchBucket

connectors

data

crawl

Database and schema check

Warehouse access

Miner
