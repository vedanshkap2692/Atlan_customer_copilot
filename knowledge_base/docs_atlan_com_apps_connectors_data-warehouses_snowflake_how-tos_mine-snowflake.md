# Mine Snowflake
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/mine-snowflake)

SnowflakeGet StartedCrawl Snowflake AssetsCrawl SnowflakeMine SnowflakeManage Snowflake in AtlanReferencesTroubleshootingBest Practices

Get Started

Crawl Snowflake AssetsCrawl SnowflakeMine Snowflake

Crawl Snowflake

Mine Snowflake

Manage Snowflake in Atlan

References

Troubleshooting

Best Practices

Connect data

Data Warehouses

Snowflake

Crawl Snowflake Assets

Mine Snowflake

Once you havecrawled assets from Snowflake, you can mine its query history to construct lineage.

To mine lineage from Snowflake, review theorder of operationsand then complete the following steps.



## Select the minerâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/mine-snowflake)

To select the Snowflake miner:

In the top right of any screen, navigate toÂNewand then clickÂNew Workflow.

From the filters along the top, clickMiner.

From the list of packages, selectSnowflake Minerand then clickSetup Workflow.



## Configure the minerâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/mine-snowflake)

To configure the Snowflake miner:

ForConnection, select the connection to mine. (To select a connection,the crawlermust have already run.)

ForConnection, select the connection to mine. (To select a connection,the crawlermust have already run.)

ForMiner Extraction Method, selectSource,Agent, or see the separate instructions for theS3 miner.

ForMiner Extraction Method, selectSource,Agent, or see the separate instructions for theS3 miner.

ForSnowflake Database:If the connection is configured withaccess to the snowflake database, chooseDefault.If the connection can onlyaccess a separate cloned database, chooseCloned Database.

ForSnowflake Database:

If the connection is configured withaccess to the snowflake database, chooseDefault.

If the connection can onlyaccess a separate cloned database, chooseCloned Database.

If you are using a cloned database, enter the name of the cloned database inDatabase Nameand the name of the cloned schema inSchema Name.

If you are using a cloned database, enter the name of the cloned database inDatabase Nameand the name of the cloned schema inSchema Name.

ForStart time, choose the earliest date from which to mine query history.infoðªDid you know?The miner restricts you to only querying the past two weeks of query history. If you need to query more history, for example in an initial load, consider using theS3 minerfirst. After the initial load, you canmodify the miner's configurationto use query history extraction.

ForStart time, choose the earliest date from which to mine query history.

ðªDid you know?The miner restricts you to only querying the past two weeks of query history. If you need to query more history, for example in an initial load, consider using theS3 minerfirst. After the initial load, you canmodify the miner's configurationto use query history extraction.

To check for any permissions or other configuration issues before running the miner, clickPreflight checks.

To check for any permissions or other configuration issues before running the miner, clickPreflight checks.

At the bottom of the screen, clickNextto proceed.

At the bottom of the screen, clickNextto proceed.



### Agent extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/mine-snowflake)

Atlan supports using a Secure Agent for mining query history from Snowflake. To use a Secure Agent, follow these steps:

Query redaction is a compute-intensive operation and can impact workflow performance. To use this feature effectively, assign at least 4 CPU cores to the agent.

Select theAgenttab.

Configure Query Redaction: By default, Query Redaction is turned off. You may choose to configure query redaction:SetEnable Query Redactionflag to true if you want to redact PII data from query history before ingesting it to Atlan.Configure PII Patterns for Query Redaction: Define patterns to identify and redact sensitive information using the following JSON format:{"pii_patterns":[{"name":"email","regex":"\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b","replacement":"[EMAIL]"}]}

SetEnable Query Redactionflag to true if you want to redact PII data from query history before ingesting it to Atlan.

Enable Query Redaction

Configure PII Patterns for Query Redaction: Define patterns to identify and redact sensitive information using the following JSON format:{"pii_patterns":[{"name":"email","regex":"\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b","replacement":"[EMAIL]"}]}

{"pii_patterns":[{"name":"email","regex":"\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b","replacement":"[EMAIL]"}]}

{"pii_patterns":[{"name":"email","regex":"\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b","replacement":"[EMAIL]"}]}

Configure the Snowflake data source by adding the secret keys for your secret store. For details on the required fields, refer to the connection configuration used whencrawling Snowflake.

Complete the Secure Agent configuration by following the instructions in theHow to configure Secure Agent for workflow executionguide.

ClickNextafter completing the configuration.

If running the miner for the first time, Atlan recommends setting a start date around three days prior to the current date and then scheduling it daily to build up to two weeks of query history. Mining two weeks of query history on the first miner run may cause delays. For all subsequent runs, Atlan requires a minimum lag of 24 to 48 hours to capture all the relevant transformations that were part of a session. Learn more about the miner logichere.



## Configure the miner behaviorâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/mine-snowflake)

To configure the Snowflake miner behavior:

(Optional) ForCalculate popularity, keepTrueto retrieveusage and popularity metricsfor your Snowflake assets from query history.ForExcluded Users, type the names of users to be excluded while calculatingusage metricsfor Snowflake assets. PressEnterafter each name to add more names.Â

ForExcluded Users, type the names of users to be excluded while calculatingusage metricsfor Snowflake assets. PressEnterafter each name to add more names.Â

Enter

(Optional) ForAdvanced Config, keepDefaultfor the default configuration or clickCustomto configure the miner:If Atlan support has provided you with a custom control configuration,Â enter the configuration into theÂCustom Configbox.You can also enter{âignore-all-caseâ: true}to enable crawling assets with case-sensitive identifiers.ForPopularity Window (days), 90 days is the maximum limit. You can set a shorter popularity window of less than 90 days.

If Atlan support has provided you with a custom control configuration,Â enter the configuration into theÂCustom Configbox.

You can also enter{âignore-all-caseâ: true}to enable crawling assets with case-sensitive identifiers.

{âignore-all-caseâ: true}

ForPopularity Window (days), 90 days is the maximum limit. You can set a shorter popularity window of less than 90 days.



## Run the minerâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/mine-snowflake)

To run the Snowflake miner, after completing the configuration steps:

To run the miner once immediately, at the bottom of the screen, click theRunbutton.

To schedule the miner to run hourly, daily, weekly, or monthly, at the bottom of the screen, click theSchedule & Runbutton.

Once the miner has completed running, you can see lineage for Snowflake assets that were created in Snowflake between the start time and when the miner ran! ð

connectors

data

crawl

setup

Select the miner

Configure the miner

Configure the miner behavior

Run the miner
