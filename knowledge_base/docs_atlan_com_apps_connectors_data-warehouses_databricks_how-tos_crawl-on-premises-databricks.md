# Crawl on-premises Databricks
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-on-premises-databricks)

DatabricksGet StartedCross-workspace SetupCrawl Databricks AssetsOn-premises SetupSet up on-premises Databricks accessCrawl on-premises DatabricksSet up on-premises Databricks lineage extractionPrivate Network SetupLineage and UsageTag managementReferencesTroubleshooting

Get Started

Cross-workspace Setup

Crawl Databricks Assets

On-premises SetupSet up on-premises Databricks accessCrawl on-premises DatabricksSet up on-premises Databricks lineage extraction

Set up on-premises Databricks access

Crawl on-premises Databricks

Set up on-premises Databricks lineage extraction

Private Network Setup

Lineage and Usage

Tag management

References

Troubleshooting

Connect data

Data Warehouses

Databricks

On-premises Setup

Crawl on-premises Databricks

Once you haveset up the databricks-extractor tool, you can extract metadata from your on-premises Databricks instances by completing the following steps.



## Run databricks-extractorâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-on-premises-databricks)



### Crawl all Databricks connectionsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-on-premises-databricks)

To crawl all Databricks connections using the databricks-extractor tool:

Log into the server with Docker Compose installed.

Change to the directory containing the compose file.

Run Docker Compose:sudo docker-compose up

sudo docker-compose up



### Crawl a specific connectionâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-on-premises-databricks)

To crawl a specific Databricks connection using the databricks-extractor tool:

Log into the server with Docker Compose installed.

Change to the directory containing the compose file.

Run Docker Compose:sudo docker-compose up <connection-name>

sudo docker-compose up <connection-name>

(Replace<connection-name>with the name of the connection from theservicessection of the compose file.)

<connection-name>

services



## (Optional) Review generated filesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-on-premises-databricks)

The databricks-extractor tool will generate many folders with JSON files for eachservice. For example:

service

catalogs

catalogs

schemas

schemas

tables

tables

You can inspect the metadata and make sure it is acceptable for providing metadata to Atlan.



## Upload generated files to S3â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-on-premises-databricks)

To provide Atlan access to the extracted metadata, you will need to upload the metadata to an S3 bucket.

We recommend uploading to the same S3 bucket as Atlan uses to avoid access issues. Reach out to your Data Success Manager to get the details of your Atlan bucket. To create your own bucket, refer to theCreate your own S3 bucketsection of the dbt documentation. (The steps will be exactly the same.)

To upload the metadata to S3:

Ensure that all files for a particular connection have the same prefix. For example,output/databricks-example/catalogs/success/result-0.json,output/databricks-example/schemas/{{catalog_name}}/success/result-0.json,output/databricks-example/tables/{{catalog_name}}/success/result-0.json, and so on.

output/databricks-example/catalogs/success/result-0.json

output/databricks-example/schemas/{{catalog_name}}/success/result-0.json

output/databricks-example/tables/{{catalog_name}}/success/result-0.json

Upload the files to the S3 bucketusing your preferred method.

For example, to upload all files using theAWS CLI:

aws s3 cp output/databricks-example s3://my-bucket/metadata/databricks-example --recursive

aws s3 cp output/databricks-example s3://my-bucket/metadata/databricks-example --recursive



## Crawl metadata in Atlanâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/crawl-on-premises-databricks)

Once you have extracted metadata on-premises and uploaded the results to S3, you can crawl the metadata into Atlan:

How to crawl Databricks

Be sure to selectOfflinefor theExtraction method.

connectors

data

crawl

Run databricks-extractor

(Optional) Review generated files

Upload generated files to S3

Crawl metadata in Atlan
