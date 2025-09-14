# Set up on-premises Databricks access
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

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

Set up on-premises Databricks access

You will need access to a machine that can run Docker on-premises. You will also need your Databricks instance details, including credentials.

In some cases you will not be able to expose your Databricks instance for Atlan to crawl and ingest metadata. For example, this may happen when security requirements restrict access to sensitive, mission-critical data.

In such cases you may want to decouple the extraction of metadata from its ingestion in Atlan. This approach gives you full control over your resources and metadata transfer to Atlan.



## Prerequisitesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

To extract metadata from your on-premises Databricks instance, you will need to use Atlan's databricks-extractor tool.

Atlan uses exactly the same databricks-extractor behind the scenes when it connects to Databricks in the cloud.



### Install Docker Composeâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

Docker Composeis a tool for defining and running applications composed of manyDockercontainers. (Any guesses where the name came from? ð)

To install Docker Compose:

Install Docker

Install Docker Compose

Instructions provided in this documentation should be enough even if you are completely new to Docker and Docker Compose. However, you can also walk through theGet started with Docker Composetutorial if you want to learn Docker Compose basics first.



### Get the databricks-extractor toolâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

To get the databricks-extractor tool:

Raise a support ticketto get the link to the latest version.

Raise a support ticketto get the link to the latest version.

Download the image using the link provided by support.

Download the image using the link provided by support.

Load the image to the server you'll use to crawl Databricks:sudo docker load -i /path/to/databricks-extractor-master.tar

Load the image to the server you'll use to crawl Databricks:

sudo docker load -i /path/to/databricks-extractor-master.tar

sudo docker load -i /path/to/databricks-extractor-master.tar



## Get the compose fileâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

Atlan provides you with aDocker compose filefor the databricks-extractor tool.

To get the compose file:

Download thelatest compose file.

Save the file to an empty directory on the server you'll use to access your on-premises Databricks instance.

The file isdocker-compose.yaml.

docker-compose.yaml



## Define Databricks connectionsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

The structure of the compose file includes three main sections:

x-templatescontains configuration fragments. You should ignore this section   -  do not make any changes to it.

x-templates

servicesis where you will define your Databricks connections.

services

volumescontains mount information. You should ignore this section as well   -  do not make any changes to it.

volumes



### Define servicesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

For each on-premises Databricks instance, define an entry underservicesin the compose file.

services

Each entry will have the following structure:

services:connection-name:<<: *extractenvironment:<<: *databricks-defaultsINCLUDE_FILTER: '{"DB_1": [], "DB_2": ["SCHEMA_1", "SCHEMA_2"]}'EXCLUDE_FILTER: '{"DB_1": ["SCHEMA_1", "SCHEMA_2"]}'TEMP_TABLE_REGEX: '.*temp.*|.*tmp.*|.*TEMP.*|.*TMP.*'SYSTEM_SCHEMA_REGEX: '^information_schema$'volumes:- ./output/connection-name:/output

services:connection-name:<<: *extractenvironment:<<: *databricks-defaultsINCLUDE_FILTER: '{"DB_1": [], "DB_2": ["SCHEMA_1", "SCHEMA_2"]}'EXCLUDE_FILTER: '{"DB_1": ["SCHEMA_1", "SCHEMA_2"]}'TEMP_TABLE_REGEX: '.*temp.*|.*tmp.*|.*TEMP.*|.*TMP.*'SYSTEM_SCHEMA_REGEX: '^information_schema$'volumes:- ./output/connection-name:/output

Replaceconnection-namewith the name of your connection.

connection-name

<<: *extracttells the databricks-extractor tool to run.

<<: *extract

environmentcontains all parameters for the tool.INCLUDE_FILTER-  specify the databases and schemas from which you want to extract metadata. Remove this line if you want to extract metadata from all databases and schemas.EXCLUDE_FILTER-  specify the databases and schemas you want to exclude from metadata extraction. This will take precedence overINCLUDE_FILTER. Remove this line if you do not want to exclude any databases or schemas.TEMP_TABLE_REGEX-  specify a regular expression for excluding temporary tables. Remove this line if you do not want to exclude any temporary tables.SYSTEM_SCHEMA_REGEX-  specify a regular expression for excluding system schemas. If unspecified,INFORMATION_SCHEMAwill be excluded from the extracted metadata by default.

environment

INCLUDE_FILTER-  specify the databases and schemas from which you want to extract metadata. Remove this line if you want to extract metadata from all databases and schemas.

INCLUDE_FILTER

EXCLUDE_FILTER-  specify the databases and schemas you want to exclude from metadata extraction. This will take precedence overINCLUDE_FILTER. Remove this line if you do not want to exclude any databases or schemas.

EXCLUDE_FILTER

INCLUDE_FILTER

TEMP_TABLE_REGEX-  specify a regular expression for excluding temporary tables. Remove this line if you do not want to exclude any temporary tables.

TEMP_TABLE_REGEX

SYSTEM_SCHEMA_REGEX-  specify a regular expression for excluding system schemas. If unspecified,INFORMATION_SCHEMAwill be excluded from the extracted metadata by default.

SYSTEM_SCHEMA_REGEX

INFORMATION_SCHEMA

volumesspecifies where to store results. In this example, the extractor will store results in the./output/connection-namefolder on the local file system.

volumes

./output/connection-name

You can add as many Databricks connections as you want.

Docker's documentationdescribes theservicesformat in more detail.

services



## Provide credentialsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

To define the credentials for your Databricks connections, you will need to provide a Databricks configuration file.

The Databricks configuration is a.inifile with the following format:

.ini

[DatabricksConfig]host = <host>port = <port># seconds to wait for a response from the servertimeout = 300# Databricks authentication type. Options: personal_access_token, aws_service_principalauth_type = personal_access_token# Required only if auth_type is personal_access_token.[PersonalAccessTokenAuth]personal_access_token = <personal_access_token># Required only if auth_type is aws_service_principal.[AWSServicePrincipalAuth]client_id = <client_id>client_secret = <client_secret>

[DatabricksConfig]host = <host>port = <port># seconds to wait for a response from the servertimeout = 300# Databricks authentication type. Options: personal_access_token, aws_service_principalauth_type = personal_access_token# Required only if auth_type is personal_access_token.[PersonalAccessTokenAuth]personal_access_token = <personal_access_token># Required only if auth_type is aws_service_principal.[AWSServicePrincipalAuth]client_id = <client_id>client_secret = <client_secret>



## Secure credentialsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)



### Using local filesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

If you decide to keep Databricks credentials in plaintext files, we recommend you restrict access to the directory and the compose file. For extra security, we recommend you useDocker secretsto store the sensitive passwords.

To specify the local files in your compose file:

secrets:databricks_config:file: ./databricks.ini

secrets:databricks_config:file: ./databricks.ini

Thissecretssection is at the same top-level as theservicessection described earlier. It is not a sub-section of theservicessection.

secrets

services

services



### Using Docker secretsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

To create and use Docker secrets:

Store the Databricks configuration file:sudo docker secret create databricks_config path/to/databricks.ini

Store the Databricks configuration file:

sudo docker secret create databricks_config path/to/databricks.ini

sudo docker secret create databricks_config path/to/databricks.ini

At the top of your compose file, add asecretselement to access your secret:secrets:databricks_config:external: truename: databricks_configThenameshould be the same one you used in thedocker secret createcommand above.Once stored as a Docker secret, you can remove the local Databricks configuration file.

At the top of your compose file, add asecretselement to access your secret:

secrets:databricks_config:external: truename: databricks_config

secrets:databricks_config:external: truename: databricks_config

Thenameshould be the same one you used in thedocker secret createcommand above.

name

docker secret create

Once stored as a Docker secret, you can remove the local Databricks configuration file.

Within theservicesection of the compose file, add a new secrets element and specify the name of the secret within your service to use it.

Within theservicesection of the compose file, add a new secrets element and specify the name of the secret within your service to use it.

service



## Exampleâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-on-premises-databricks-access)

Let's explain in detail with an example:

secrets:databricks_config:external: truename: databricks_configx-templates:# ...services:databricks-example:<<: *extractenvironment:<<: *databricks-defaultsINCLUDE_FILTER: '{"DB_1": [], "DB_2": ["SCHEMA_1", "SCHEMA_2"]}'EXCLUDE_FILTER: '{"DB_1": ["SCHEMA_1", "SCHEMA_2"]}'TEMP_TABLE_REGEX: '.*temp.*|.*tmp.*|.*TEMP.*|.*TMP.*'SYSTEM_SCHEMA_REGEX: '^information_schema$'volumes:- ./output/databricks-example:/outputsecrets:- databricks_config

secrets:databricks_config:external: truename: databricks_configx-templates:# ...services:databricks-example:<<: *extractenvironment:<<: *databricks-defaultsINCLUDE_FILTER: '{"DB_1": [], "DB_2": ["SCHEMA_1", "SCHEMA_2"]}'EXCLUDE_FILTER: '{"DB_1": ["SCHEMA_1", "SCHEMA_2"]}'TEMP_TABLE_REGEX: '.*temp.*|.*tmp.*|.*TEMP.*|.*TMP.*'SYSTEM_SCHEMA_REGEX: '^information_schema$'volumes:- ./output/databricks-example:/outputsecrets:- databricks_config

In this example, we've defined the secrets at the top of the file (you could also define them at the bottom). Thedatabricks_configrefers to an external Docker secret created using thedocker secret createcommand.

databricks_config

docker secret create

The name of this service isdatabricks-example. You can use any meaningful name you want.

databricks-example

The<<: *databricks-defaultssets the connection type to Databricks.

<<: *databricks-defaults

The./output/databricks-example:/outputÂ line tells the extractor where to store results. In this example, the extractor will store results in theÂ./output/databricks-exampledirectory on the local file system. We recommend you output the extracted metadata for different connections in separate directories.

./output/databricks-example:/output

./output/databricks-example

Thesecretssection withinservicestells the extractor which secrets to use for this service. Each of these refers to the name of a secret listed at the beginning of the compose file.

secrets

services

data

crawl

Prerequisites

Get the compose file

Define Databricks connections

Provide credentials

Secure credentials

Example
