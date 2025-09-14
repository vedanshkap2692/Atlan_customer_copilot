# order workflows
(source: https://docs.atlan.com/product/connections/how-tos/order-workflows#workflow-recommendations)

Connector FrameworkHow-tosManage connectivityMonitor connectivityConnect data sources for Azure-hosted Atlan instancesMine queries through S3How to order workflowsHow to provide SSL certificatesConceptsReferencesFAQ

How-tosManage connectivityMonitor connectivityConnect data sources for Azure-hosted Atlan instancesMine queries through S3How to order workflowsHow to provide SSL certificates

Manage connectivity

Monitor connectivity

Connect data sources for Azure-hosted Atlan instances

Mine queries through S3

How to order workflows

How to provide SSL certificates

Concepts

References

FAQ

Connect data

Connectivity Framework

Connector Framework

How-tos

How to order workflows

Theorder of operationsyou run in Atlan is important. Follow the specific workflow sequence outlined below when crawlingdata tools. The right order particularly ensures that lineage is constructed without needing to rerun crawlers.



## Order of operationsâ
(source: https://docs.atlan.com/product/connections/how-tos/order-workflows#workflow-recommendations)

To have lineage across tools, you need to:

Crawl data stores first-  for example,SQL data sources,NoSQL data sources,event buses, andschema registries.

Run data quality tools-  for example,Monte CarloandSoda.

Mine query logs-mine queries through S3or run miner packages for supported sources.

Run extract-load tools-  for example,Fivetran,Airflow/OpenLineageandother supported distributions, and data processing tools likeApache Spark/OpenLineage,Alteryx.

Run transformation tools-  for example,dbtandMatillion.

Crawl business intelligence tools last-  for example,supported BI toolslikeLooker,Microsoft Power BI,Tableau, and more.

If you use a different order, the upstream assets (data stores) might not yet exist when you load the BI metadata. In that case, you may see lineage within the BI metadata, but not between the BI metadata and data sources. If this happens, no worriesâjust rerun your existing workflows following the recommended order and Atlan can resolve it.

As a general rule of thumb, start by crawling the data sourceâincluding BI toolsâbefore mining query logs. For example, when aiming to mine Microsoft Power BI, begin with a crawl of Microsoft Power BI.



## Workflow recommendationsâ
(source: https://docs.atlan.com/product/connections/how-tos/order-workflows#workflow-recommendations)

The following are general guidelines and best practices for running workflows in Atlan:

Schedule your workflows based on how often you want your metadata in Atlan to be updated   -  weekly, monthly, and so on. To configure custom cron schedules, learn morehere.

Avoid any overlaps between workflow schedules to ensure consistent workflow run times.

Remember that the first workflow run can typically take much longer than subsequent runs. The first run establishes the connection, queries the source, extracts and transforms the metadata, and then publishes your assets for the first time in Atlan.

If running a miner for the first time, set a start date around 3 days prior to the current date and then schedule it daily to build up to two weeks of query history. Mining two weeks of query history on the first miner run may cause workflows to time out or hit resource consumption errors.

For all subsequent miner runs, Atlan requires a minimum lag of 24 to 48 hours to capture all the relevant transformations that were part of a session. Learn more about the miner logichere.

Runpreflight checksbefore running the crawler to check for any permissions or other configuration issues, including testing authentication.



## Troubleshooting tipsâ
(source: https://docs.atlan.com/product/connections/how-tos/order-workflows#workflow-recommendations)

Here are a few tips to help you troubleshoot workflow failures in Atlan:

If test authentication orpreflight checksfail, check the source to ensure that your credentials are correct and you have requisite access to crawl the metadata.

If you're connecting to Atlan via private link and experience any network-related errors or timeouts during test authentication, it may mean that there is a network connectivity issue between the source and Atlan.Reach out to Atlan supportto help you investigate further.

If both test authentication and preflight checks fail and succeed intermittently when tried multiple times, this may mean that your cluster is in an unstable state and needs to be restarted.Notify Atlan supportto restart your cluster.

connectors

data

crawl

Order of operations

Workflow recommendations

Troubleshooting tips
