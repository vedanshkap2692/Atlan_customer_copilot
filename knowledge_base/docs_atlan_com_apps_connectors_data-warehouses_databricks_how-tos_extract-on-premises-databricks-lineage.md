# extract on-premises Databricks lineage
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-on-premises-databricks-lineage)

DatabricksGet StartedCross-workspace SetupCrawl Databricks AssetsOn-premises SetupPrivate Network SetupLineage and UsageHow to extract lineage and usage from DatabricksHow to extract on-premises Databricks lineageTag managementReferencesTroubleshooting

Get Started

Cross-workspace Setup

Crawl Databricks Assets

On-premises Setup

Private Network Setup

Lineage and UsageHow to extract lineage and usage from DatabricksHow to extract on-premises Databricks lineage

How to extract lineage and usage from Databricks

How to extract on-premises Databricks lineage

Tag management

References

Troubleshooting

Connect data

Data Warehouses

Databricks

Lineage and Usage

How to extract on-premises Databricks lineage

Once you haveset up the databricks-extractor tool, you can extract lineage from your on-premises Databricks instances by completing the following steps.



## Run databricks-extractorâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-on-premises-databricks-lineage)

To extract lineage for a specific Databricks connection using the databricks-extractor tool:

Log into the server with Docker Compose installed.

Change to the directory containing the compose file.

Run Docker Compose:sudo docker-compose up <connection-name>

sudo docker-compose up <connection-name>

(Replace<connection-name>with the name of the connection from theservicessection of the compose file.)

<connection-name>

services



## (Optional) Review generated filesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-on-premises-databricks-lineage)

The databricks-extractor tool will generate many folders with JSON files for eachservice. For example:

service

extracted-lineage

extracted-lineage

extracted-query-historyÂ (ifEXTRACT_QUERY_HISTORYis set to true)

extracted-query-history

EXTRACT_QUERY_HISTORY

You can inspect the lineage and usage metadata and make sure it is acceptable for providing metadata to Atlan.



## Upload generated files to S3â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-on-premises-databricks-lineage)

To provide Atlan access to the extracted lineage and usage metadata, you will need to upload the metadata to an S3 bucket.

We recommend uploading to the same S3 bucket as Atlan uses to avoid access issues. Reach out to your Data Success Manager to get the details of your Atlan bucket. To create your own bucket, refer to theCreate your own S3 bucketsection of the dbt documentation. (The steps will be exactly the same.)

To upload the metadata to S3:

Ensure that all files for a particular connection have the same prefix. For example,output/databricks-lineage-example/extracted-lineage/result-0.json,output/databricks-lineage-example/extracted-query-history/result-0.json, and so on.

output/databricks-lineage-example/extracted-lineage/result-0.json

output/databricks-lineage-example/extracted-query-history/result-0.json

Upload the files to the S3 bucketusing your preferred method.

For example, to upload all files using theAWS CLI:

aws s3 cp output/databricks-lineage-example s3://my-bucket/metadata/databricks-lineage-example --recursive

aws s3 cp output/databricks-lineage-example s3://my-bucket/metadata/databricks-lineage-example --recursive



## Extract lineage in Atlanâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/extract-on-premises-databricks-lineage)

Once you have extracted lineage on-premises and uploaded the results to S3, you can extract lineage in Atlan:

How to extract lineage and usage from Databricks

Be sure to selectOfflinefor theExtraction method.

connectors

data

Run databricks-extractor

(Optional) Review generated files

Upload generated files to S3

Extract lineage in Atlan
