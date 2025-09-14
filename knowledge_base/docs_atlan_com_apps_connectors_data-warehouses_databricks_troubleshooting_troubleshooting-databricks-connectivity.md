# Troubleshooting Databricks connectivity
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

DatabricksGet StartedCross-workspace SetupCrawl Databricks AssetsOn-premises SetupPrivate Network SetupLineage and UsageTag managementReferencesTroubleshootingTroubleshooting Databricks connectivity

Get Started

Cross-workspace Setup

Crawl Databricks Assets

On-premises Setup

Private Network Setup

Lineage and Usage

Tag management

References

TroubleshootingTroubleshooting Databricks connectivity

Troubleshooting Databricks connectivity

Connect data

Data Warehouses

Databricks

Troubleshooting

Troubleshooting Databricks connectivity

The documentation refers to bothSQL endpointandinteractive clusterascompute enginebelow.



#### Does Atlan consider expensive queries and compute costs?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

No, Atlan doesn't factor in expensive queries or compute costs due to limitations in the Databricks APIs, which don't expose this information.



#### How does Atlan calculate popularity for Databricks assets?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Atlan calculates popularity fortables,views, andcolumnsin Databricks by analyzing query execution data. It retrieves query history from thesystem.query.historytable and specifically filters forexecution_status = 'FINISHED'andstatement_type = 'SELECT'to determine how frequently assets are accessed.

tables

views

columns

system.query.history

execution_status = 'FINISHED'

statement_type = 'SELECT'



#### How to debug test authentication and preflight check errors?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Hostname resolution error

Provided Host name cannot be resolved via DNS, please check and try again.

Provided Host name cannot be resolved via DNS, please check and try again.

The hostname you have provided can't be resolved through DNS. Check that the hostname is correct.

Verify that the DNS settings have been configured properly.

Invalid client ID or secret

Provided Client ID is invalid, please check and try again.

Provided Client ID is invalid, please check and try again.

The client ID or secret you have provided is either invalid or no longer working. Follow the steps forAWSorAzuresetup to generate new credentials.

Invalid tenant ID

Provided tenant ID is invalid, please check and try again.

Provided tenant ID is invalid, please check and try again.

The tenant ID you have provided is incorrect.

Ensure that the tenant ID you have provided corresponds to the one in yourMicrosoft Entra ID application.

Unity Catalog not linked

Configured Databricks instance doesn't have Unity Catalog linked. Please choose JDBC extraction instead of REST API in Atlan.

Configured Databricks instance doesn't have Unity Catalog linked. Please choose JDBC extraction instead of REST API in Atlan.

If you have not set up Unity Catalog in your Databricks workspace, you canchange the extraction method to JDBCinstead of REST API to crawl your Databricks assets in Atlan.

Connection timeout

Failed to connect to Databricks (connection timed out). Please check your host and port and try again.

Failed to connect to Databricks (connection timed out). Please check your host and port and try again.

The connection to the Databricks instance has timed out.

Verify that the host and port are correct.

Check that no firewall rules or network issues are blocking the connection.

Invalid HTTP path

Provided HTTP path is invalid, please check and try again.

Provided HTTP path is invalid, please check and try again.

TheHTTP pathyou have provided is invalid.

Ensure that the endpoint is properly configured and accessible, and the warehouse ID in the HTTP path is correct.

Invalid personal access token

PAT token is invalid, please check and try again.

PAT token is invalid, please check and try again.

The personal access token used for authentication is invalid.

Ensure that the token is valid and neither deleted nor expired.

You can also generate a newpersonal access token, if needed.

Insufficient permisions for crawling metadata

User doesn't have access to any schemas / dbs, please check the accesses provided to the atlan user and try again.

User doesn't have access to any schemas / dbs, please check the accesses provided to the atlan user and try again.

Check that the service principal or the user who's PAT token is being used has the necessary permissions provided. Refer to thesetup docto understand permissions required for different auth types.

Insufficient permisions for some of the included crawling metadata

Warning, user doesn't have access to the following objects anymore, or the objects no longer exist on the source!, check failed for ...

Warning, user doesn't have access to the following objects anymore, or the objects no longer exist on the source!, check failed for ...

user doesn't have access to one or more db objects from the include filter, (such as catalogs / schemas).

You can either remove these objects from the include filter if they no longer exist on the source.

Or check that the service principal or the user who's PAT token is being used has the necessary permissions provided. Refer to thesetup docto understand permissions required for different auth types.

Insufficient permisions to crawl tags

User doesn't have access to the following system tables

User doesn't have access to the following system tables

Check that you have sufficient permissions provided for thetags extraction.

User doesn't have permission to access warehouses

please check your credentials and warehouse access

please check your credentials and warehouse access

Check that the configured user / service principal hasCAN_USEon the configured SQL warehouse.

CAN_USE

Unable to access query history from the source, user doesn't have the access

Check thepermissions requiredfor the system tables based lineage extraction are provided.

System table extraction checks failing with

User doesn't have access to the following system tables

User doesn't have access to the following system tables

Check thepermissions requiredfor the system tables based extraction.

General connection failure

Unable to connect to the configured Databricks instance, please check your credentials and configs and then try again. If the problem persists, contact[email protected].

Unable to connect to the configured Databricks instance, please check your credentials and configs and then try again. If the problem persists, contact[email protected]

Check that you have entered the host and port correctly.

Verify that the credentials for the connection are correct.

Check that your Databricks instance is properly configured and available.

If the problem still persists after verifying all of the previous steps,contact Atlan support.



#### Why does the workflow take longer than usual in the extraction step?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Certain Databricks runtime versions don't have an easy way to extract some metadata (for example partitioning, table_type, and format). Extra operations must be performed to retrieve these, resulting in slower performance.

If you aren't already, you may want to try theUnity Catalog extraction method.



#### Why is some metadata missing?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

When using incremental extraction, consider running a one-time full extraction to capture any newly introduced metadata.

When using incremental extraction, consider running a one-time full extraction to capture any newly introduced metadata.

Currently, some metadata can't be extracted from Databricks:MetadataJDBCREST APISystem TablesViewCountandTableCount(on schemas)âââRowCount(on tables and views)âââTABLE_KIND(on tables and views)âââPARTITION_STRATEGY(on tables and views)âââCONSTRAINT_TYPE(on columns)âââPartition key (on columns)âââTable partitioning informationâââBYTES,SIZEINBYTES(table size)âââ

Currently, some metadata can't be extracted from Databricks:

ViewCount

TableCount

RowCount

TABLE_KIND

PARTITION_STRATEGY

CONSTRAINT_TYPE

BYTES

SIZEINBYTES

The team is exploring ways to bring this metadata into Atlan if Databricks supports extraction of the metadata.

The team is exploring ways to bring this metadata into Atlan if Databricks supports extraction of the metadata.



#### Why doesn't my SQL work when querying Databricks?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Atlan currently supportsSparkSQL on Databricks runtime 7.x and above.



#### Can I use Atlan when the Databricks compute engine isn't running?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Atlan needs the Databricks compute engine to be running for two activities:Crawling assets (normal and scheduled run)Querying assets (including data previews)

Crawling assets (normal and scheduled run)

Querying assets (including data previews)

If you don't need to perform the activities listed, your experience shouldn't be affected.

In any other case, you'll get a downgraded experience on Atlan if the compute engine isn't running. Queries won't work as expected and a scheduled workflow might fail after a couple of retries.

The team recommends turning off theTerminate after x minutes of inactivityoption in your cluster to avoid these problems. If you have this turned on, any of the listed activities triggers the cluster to come back online within about 30 seconds.



#### Why can't I see all the assets on Atlan that are available in Databricks?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Have youexcluded the database or schema when crawling?

Does theDatabricks user you configured for crawlinghave access to these other assets?



#### Why is the test authentication taking so long?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Please check the state of the compute engine. It must be in arunningstate for all operations, including authentication.



#### What limitations are there with the REST API (Unity Catalog) extraction method?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Currently, schema-level filtering and retrieving table partitioning information aren't supported.



#### Why has my workflow started to fail when it worked before?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

This can happen ifthe PAT you configuredthe workflow with has since expired.

You will need to create a new PAT in Databricks, and thenmodify the workflow configuration in Atlanwith this new PAT.

If you are unable to update the PAT, pause the workflow andreach out to us.



#### How do I migrate to Unity Catalog?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Currently Unity Catalog is in a public preview state.

The Databricks team is working on an automated migration to Unity Catalog.

Currently you must migrate individual tables manually.



#### Why are some notebooks missing from metadata extraction?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Notebooks stored inside hidden directories (names starting with "." such as.hidden_dir/) are generally not returned by the/api/2.0/workspace/listAPI endpoint. This may cause missing notebook details in Atlan.

.hidden_dir/

/api/2.0/workspace/list



#### Why is metadata missing for some Databricks entities?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

The Databricks APIs used provide data only within a single configured workspace. If an entity used in lineage creation exists outside this workspace, its details won't be available via these APIs.



#### Does Atlan support nested columns beyond level 30?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Atlan doesn't support nested columns beyond 30 levels for complex types such as Struct, Array, and Map. Columns exceeding this nesting depth aren't parsed. Instead, the deepest column level gets assigned the data type string, and its value contains a string representation of the remaining nested structure.

For example,LEVEL_31has the data type<LEVEL_32:STRUCT<LEVEL_33:STRUCT<...>>>.

LEVEL_31

<LEVEL_32:STRUCT<LEVEL_33:STRUCT<...>>>



#### What happens if the service principal loses access to one workspace?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

The crawler is resilient to this scenario. During the discovery phase, it fails to connect to that specific workspace, logs it as inaccessible, and simply skips it. The process continues for all other available workspaces without failing the entire run.



#### Why are assets from a specific catalog not appearing in Atlan?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

This is almost always a permission issue. Verify that the service principal has been grantedUSE CATALOG,BROWSE, andSELECTpermissions on the catalog and its contents (schemas, tables).

USE CATALOG

BROWSE

SELECT



#### Why is my lineage view incomplete?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/troubleshooting/troubleshooting-databricks-connectivity)

Check the source and target tables of the missing lineage link. The service principal must haveSELECTpermissions onbothtables for lineage to be captured.

SELECT

For more information on cross-workspace extraction setup, seeSet up cross-workspace extraction.

api

rest-api

graphql
