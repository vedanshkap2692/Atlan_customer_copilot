# Set up Databricks
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

DatabricksGet StartedSet up DatabricksCross-workspace SetupCrawl Databricks AssetsOn-premises SetupPrivate Network SetupLineage and UsageTag managementReferencesTroubleshooting

Get StartedSet up Databricks

Set up Databricks

Cross-workspace Setup

Crawl Databricks Assets

On-premises Setup

Private Network Setup

Lineage and Usage

Tag management

References

Troubleshooting

Connect data

Data Warehouses

Databricks

Get Started

Set up Databricks

Atlan supports three authentication methods for fetching metadata from Databricks. You can set up any of the following authentication methods:

Personal access token authentication

AWS service principal authentication

Azure service principal authentication



## Personal access token authenticationâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

Check that you haveAdminandDatabricks SQL accessfor the Databricks workspace. This is required for both cluster options described below. If you don't have this access, contact your Databricks administrator.



### Grant user access to workspaceâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To grant workspace access to the user creating a personal access token:

From the left menu of the account console, clickWorkspacesand then select a workspace to which you want to add the user.

From the tabs along the top of your workspace page, click thePermissionstab.

In the upper right of thePermissionspage, clickAdd permissions.

In theAdd permissionsdialog, enter the following details:ForUser, group, or service principal, select the user to grant access.ForPermission, click the dropdown and select workspaceUser.

ForUser, group, or service principal, select the user to grant access.

ForPermission, click the dropdown and select workspaceUser.



### Generate a personal access tokenâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

You cangenerate a personal access tokenin your Databricks workspace to the authenticate theintegration in Atlan.

To generate a personal access token:

From the top right of your Databricks workspace, click your Databricks username, and then from the dropdown, clickUserSettings.

Under theSettingsmenu, clickDeveloper.

On theDeveloperpage, next toAccess tokens, clickManage.

On theAccess tokenspage, click theGenerate new tokenbutton.

In theGenerate new tokendialog:ForComment, enter a description of the token's intended use - for example,Atlan crawler.ForLifetime (days), consider removing the number. This enables the token to be used indefinitely - it won't need to be refreshed.Important!If you do enter a number, remember that you need to periodically regenerate it and update Atlan's crawler configuration with the new token each time.At the bottom of the dialog, clickGenerate.

ForComment, enter a description of the token's intended use - for example,Atlan crawler.

ForComment, enter a description of the token's intended use - for example,Atlan crawler.

Atlan crawler

ForLifetime (days), consider removing the number. This enables the token to be used indefinitely - it won't need to be refreshed.Important!If you do enter a number, remember that you need to periodically regenerate it and update Atlan's crawler configuration with the new token each time.

ForLifetime (days), consider removing the number. This enables the token to be used indefinitely - it won't need to be refreshed.

If you do enter a number, remember that you need to periodically regenerate it and update Atlan's crawler configuration with the new token each time.

At the bottom of the dialog, clickGenerate.

At the bottom of the dialog, clickGenerate.

Copy and save the generated token in a secure location, and then clickDone.



### Select a clusterâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

Atlan recommends using serverless SQL warehouses for instant compute availability. To enable serverless SQL warehouses, refer toDatabricks documentationfor AWS Databricks workspaces orMicrosoft documentationfor Azure Databricks workspaces.

You can set up personal access token authentication for your Databricks instance using one of the following cluster options:

Interactive cluster

SQL warehouse (formerly SQL endpoint)



#### Interactive clusterâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To confirm anall-purpose interactive clusteris configured:

From the left menu of any page of your Databricks instance, clickCompute.

Under theAll-purpose clusterstab, verify you have a cluster defined.

Click the link under theNamecolumn of the table to open your cluster.

Under theConfigurationtab, verify theAutopilot optionstoTerminate after ... minutesis enabled.

At the bottom of theConfigurationtab, expand theAdvanced optionsexpandable.Under theAdvanced optionsexpandable, open theJDBC/ODBCtab.Confirm that all of the fields in this tab are populated, and copy them for use in crawling:Server Hostname,Port, andHTTP Path.

Under theAdvanced optionsexpandable, open theJDBC/ODBCtab.

Confirm that all of the fields in this tab are populated, and copy them for use in crawling:Server Hostname,Port, andHTTP Path.



#### SQL warehouse (formerly SQL endpoint)â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To confirm aSQL warehouseis configured:

From the left menu of any page of your Databricks instance, open the dropdown just below thedatabrickslogo and change toSQL.

From the refreshed left menu, clickSQL Warehouses.

Click the link under theNamecolumn of the table to open your SQL warehouse.

Under theConnection detailstab, confirm that all of the fields are populated and copy them for use in crawling:Server hostname,Port, andHTTP path.



## AWS service principal authenticationâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

You need yourAWS Databricks account adminto create a service principal and manage OAuth credentials for the service principal and yourAWS Databricks workspace adminto add the service principal to your AWS Databricks workspace - you may not have access yourself.

You need the following to authenticate the connection in Atlan:

Client ID

Client secret



### Create a service principalâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

You can create a service principal directly in your Databricks account or from a Databricks workspace.

Identity federation enabled on your workspaces: Databricks recommends creating the service principal in the account and assigning it to workspaces.

Identity federation disabled on your workspaces: Databricks recommends that you create your service principal from a workspace.



#### Identity federation enabledâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To create a service principal from your Databricks account, with identify federation enabled:

Log in to your Databricksaccount consoleas an account admin.

From the left menu of the account console, clickUser management.

From the tabs along the top of theUser managementpage, click theService principalstab.

In the upper right of theService principalspage, clickAdd service principal.

On theAdd service principalpage, enter a name for the service principal and then clickAdd.

Once the service principal has been created, you can assign it to your identity federated workspace. From the left menu of the account console, clickWorkspacesand then select a workspace to which you want to add the service principal.

From the tabs along the top of your workspace page, click thePermissionstab.

In the upper right of thePermissionspage, clickAdd permissions.

In theAdd permissionsdialog, enter the following details:ForUser, group, or service principal, select the service principal you created.ForPermission, click the dropdown and select workspaceUser.

ForUser, group, or service principal, select the service principal you created.

ForPermission, click the dropdown and select workspaceUser.



#### Identity federation disabledâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To create a service principal from a Databricks workspace, with identity federation disabled:

Log in to your AWS Databricks workspace as a workspace admin.

From the top right of your workspace, click your username, and then from the dropdown, clickAdmin Settings.

In the left menu of theSettingspage, under theWorkspace adminsubheading, clickIdentity and access.

On theIdentity and accesspage, underManagement and permissions, next toService principals, clickManage.

In the upper right of theService principalspage, clickAdd service principal.

In theAdd service principaldialog, click theAdd newbutton.

ForNew service principal display name, enter a name for the service principal and then clickAdd.



### Create an OAuth secret for the service principalâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

You need to create an OAuth secret to authenticate to Databricks REST APIs.

To create an OAuth secret for theservice principal:

Log in to your Databricksaccount consoleas an account admin.

Log in to your Databricksaccount consoleas an account admin.

From the left menu of the account console, clickUser management.

From the left menu of the account console, clickUser management.

From the tabs along the top of theUser managementpage, click theService principalstab.

From the tabs along the top of theUser managementpage, click theService principalstab.

In the upper right of theService principalspage, select theservice principal you created.

In the upper right of theService principalspage, select theservice principal you created.

On the service principal page, underOAuth secrets, clickGenerate secret.

On the service principal page, underOAuth secrets, clickGenerate secret.

From theGenerate secretdialog, copy theSecretandClient IDand store it in a secure location.dangerNote that this secret is only revealed once during creation. The client ID is the same as the application ID of the service principal.

From theGenerate secretdialog, copy theSecretandClient IDand store it in a secure location.

Note that this secret is only revealed once during creation. The client ID is the same as the application ID of the service principal.

Once you've copied the client ID and secret, clickDone.

Once you've copied the client ID and secret, clickDone.



## Azure service principal authenticationâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

You need yourAzure Databricks account adminto create a service principal and yourAzure Databricks workspace adminto add the service principal to your Azure Databricks workspace - you may not have access yourself.

You need the following to authenticate the connection in Atlan:

Client ID (application ID)

Client secret

Tenant ID (directory ID)



### Create a service principalâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

Touse service principals on Azure Databricks, an admin user must create a new Microsoft Entra ID (formerly Azure Active Directory) application and then add it to the Azure Databricks workspace to use as a service principal.

To create a service principal:

Sign in to theAzure portal.

If you have access to multiple tenants, subscriptions, or directories, click theDirectories + subscriptions(directory with filter) icon in the top menu to switch to the directory in which you want to create the service principal.

In_Search resources, services, and docs_, search for and selectMicrosoft Entra ID.

Click**+ Addand selectApp registration**.

For_Name_, enter a name for the application.

In the_Supported account types_section, selectAccounts in this organizational directory only (Single tenant)and then clickRegister.

On the application page's_Overview_page, in the_Essentials_section, copy and store the following values in a secure location:Application (client) IDDirectory (tenant) ID

Application (client) ID

Directory (tenant) ID

To generate a client secret, within_Manage_, clickCertificates & secrets.

On the_Client secrets_tab, clickNew client secret.

In the_Add a client secret_dialog, enter the following details:

ForDescription, enter a description for the client secret.

For_Expires_, select an expiry time period for the client secret and then clickAdd.

Copy and store the client secret's_Value_in a secure place.



### Add a service principal to your accountâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To add a service principal to your Azure Databricks account:

Log in to yourAzure Databricks account consoleas an account admin.

From the left menu of the account console, clickUser management.

From the tabs along the top of theUser managementpage, click theService principalstab.

In the upper right of theService principalspage, clickAdd service principal.

On theAdd service principalpage, enter a name for the service principal.

UnderUUID, paste theApplication (client) IDfor the service principal.

ClickAdd.



### Assign a service principal to a workspaceâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To add users to a workspace using the account console, the workspace must be enabled for identity federation. Workspace admins can also assign service principals to workspaces using the workspace admin settings page.



#### Identity federation enabledâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To assign a service principal to your Azure Databricks account:

Log in to your Databricksaccount consoleas an account admin.

From the left menu of the account console, clickWorkspacesand then select a workspace to which you want to add the service principal.

From the tabs along the top of your workspace page, click thePermissionstab.

In the upper right of thePermissionspage, clickAdd permissions.

In theAdd permissionsdialog, enter the following details:ForUser, group, or service principal, select theservice principalyou created.ForPermission, click the dropdown to select workspaceUser.

ForUser, group, or service principal, select theservice principalyou created.

ForPermission, click the dropdown to select workspaceUser.



#### Identity federation disabledâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To assign a service principal to your Azure Databricks workspace:

Log in to your Azure Databricks workspace as a workspace admin.

From the top right of your workspace, click your username, and then from the dropdown, clickAdmin Settings.

In the left menu of theSettingspage, under theWorkspace adminsubheading, clickIdentity and access.

On theIdentity and accesspage, underManagement and permissions, next toService principals, clickManage.

In the upper right of theService principalspage, clickAdd service principal.

In theAdd service principaldialog, click theAdd newbutton.

ForNew service principal display name, paste theApplication (client) IDfor theservice principal, enter a display name, and then clickAdd.



## Grant permissions to crawl metadataâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

You must have a Unity Catalog-enabled Databricks workspace to crawl metadata in Atlan.

To extract metadata, you can grant theBROWSE privilege, currently in public preview. You no longer require theData Readerpreset that granted the following privileges on objects in the catalog -USE CATALOG,USE SCHEMA,EXECUTE,READ VOLUME, andSELECT.

USE CATALOG

USE SCHEMA

EXECUTE

READ VOLUME

SELECT

To grant permissions to a user or service principal:

Log in to your Databricks workspace as a workspace admin.

From the left menu of your workspace, clickCatalog.

In the left menu of theCatalog Explorerpage, select the catalog you want to crawl in Atlan.

From the tabs along the top of your workspace page, click thePermissionstab and then click theGrantbutton.

In theGrant on (workspace name)dialog, configure the following:UnderPrincipals, click the dropdown and then select the user or service principal.UnderPrivileges, check theBROWSEprivilege.At the bottom of the dialog, clickGrant.

UnderPrincipals, click the dropdown and then select the user or service principal.

UnderPrivileges, check theBROWSEprivilege.

At the bottom of the dialog, clickGrant.

(Optional) Repeat steps 3-5 for each catalog you want to crawl in Atlan.



### System tables extraction methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To crawl metadata via system tables, you must have a Unity Catalog-enabled workspace and a configured SQL warehouse. Follow these steps to extract metadata using system tables:

Create one of the following authentication methods:Personal access tokenAWS service principalAzure service principal

Create one of the following authentication methods:

Personal access token

AWS service principal

Azure service principal

Grant the following privileges to the identity you created:CAN_USEon a SQL warehouseUSE CATALOGonsystemcatalogUSE SCHEMAonsystem.information_schemaSELECTon the following tables:system.information_schema.catalogssystem.information_schema.schematasystem.information_schema.tablessystem.information_schema.columnssystem.information_schema.key_column_usagesystem.information_schema.table_constraints

Grant the following privileges to the identity you created:

CAN_USEon a SQL warehouse

CAN_USE

USE CATALOGonsystemcatalog

USE CATALOG

system

USE SCHEMAonsystem.information_schema

USE SCHEMA

system.information_schema

SELECTon the following tables:system.information_schema.catalogssystem.information_schema.schematasystem.information_schema.tablessystem.information_schema.columnssystem.information_schema.key_column_usagesystem.information_schema.table_constraints

SELECT

system.information_schema.catalogs

system.information_schema.catalogs

system.information_schema.schemata

system.information_schema.schemata

system.information_schema.tables

system.information_schema.tables

system.information_schema.columns

system.information_schema.columns

system.information_schema.key_column_usage

system.information_schema.key_column_usage

system.information_schema.table_constraints

system.information_schema.table_constraints



### Cross-workspace extractionâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To crawl metadata from all workspaces within a Databricks metastore using a single connection, seeSet up cross-workspace extractionfor instructions.



## (Optional) Grant permissions to query and preview dataâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

Atlan currently only supportsquerying dataandviewing sample data previewfor thepersonal access tokenauthentication method.

To grant permissions to query data and preview example data:

Log in to your Databricks workspace as a workspace admin.

From the left menu of your workspace, clickCatalog.

In the left menu of theCatalog Explorerpage, select the catalog you want to query and preview data from in Atlan.

From the tabs along the top of your workspace page, click thePermissionstab and then click theGrantbutton.

In theGrant on (workspace name)dialog, configure the following:UnderPrincipals, click the dropdown and then select the user or service principal.UnderPrivilege presets, click the dropdown and then clickData Readerto enable read-only access to the catalog. Doing so automatically selects the following privileges -USE CATALOG,USE SCHEMA,EXECUTE,READ VOLUME, andSELECT.At the bottom of the dialog, clickGrant.

UnderPrincipals, click the dropdown and then select the user or service principal.

UnderPrivilege presets, click the dropdown and then clickData Readerto enable read-only access to the catalog. Doing so automatically selects the following privileges -USE CATALOG,USE SCHEMA,EXECUTE,READ VOLUME, andSELECT.

USE CATALOG

USE SCHEMA

EXECUTE

READ VOLUME

SELECT

At the bottom of the dialog, clickGrant.

(Optional) Repeat steps 3-5 for each catalog you want to query and preview data from in Atlan.



## (Optional) Grant permissions to import and update tagsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

Toimport Databricks tags, you must have a Unity Catalog-enabled workspace and a SQL warehouse configured. Atlan supports importing Databricks tags using system tables for all three authentication methods.

Once you have created apersonal access token, anAWS service principal, or anAzure service principal, you will need to grant the following privileges:

CAN_USEon a SQL warehouse

CAN_USE

USE CATALOGonsystem catalog

USE CATALOG

system catalog

USE SCHEMAonsystem.information_schema

USE SCHEMA

system.information_schema

SELECTon the following tables:system.information_schema.catalog_tagssystem.information_schema.schema_tagssystem.information_schema.table_tagssystem.information_schema.column_tags

SELECT

system.information_schema.catalog_tags

system.information_schema.catalog_tags

system.information_schema.schema_tags

system.information_schema.schema_tags

system.information_schema.table_tags

system.information_schema.table_tags

system.information_schema.column_tags

system.information_schema.column_tags

To push tags updated for assets in Atlan to Databricks, you need to grant the followingprivileges:

APPLY TAGon the object

APPLY TAG

USE CATALOGon the object's parent catalog

USE CATALOG

USE SCHEMAon the object's parent schema

USE SCHEMA



## (Optional) Grant permissions to extract lineage and usage from system tablesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

You must have a Unity Catalog-enabled workspace to use system tables.

Atlan supports extracting the following for your Databricks assets usingsystem tables:

lineage

usage and popularity metrics



### Enable system.access schemaâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

You need your account admin to enable thesystem.accessschema using theSystemSchemas API. This enables Atlan to extract lineage using system tables.

system.access

In Atlan, one Databricks connection corresponds to one metastore. Repeat the following process for each metastore in your Databricks environment for which you want to extract lineage.

To verify that system schemas are enabled for each schema, follow the steps inDatabricks documentation:

List system schemasusing the SystemSchemas API to check the status.

If enabled for any given schema, thestateisEnableCompleted. This confirms that the schema has been enabled for that specific metastore.

EnableCompleted

Atlan can only extract lineage using system tables when the state is marked asEnableCompleted.

EnableCompleted



### (Optional) enablesystem.information_schema.tableâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

system.information_schema.table

To generate lineage with the target type set asPATHfor a table, Atlan uses metadata fromsystem.information_schema.tableto resolve table paths and dependencies. To enable this, you must grant the following permissions on the relevant catalog, schema, and tables.

PATH

system.information_schema.table



#### Grant permissionsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

You must be a metastore admin, have theMANAGEprivilege on the object, or be the owner of the catalog, schema, or table to grant these permissions.

MANAGE

In Atlan, one Databricks connection corresponds to one metastore. Repeat the following process for each metastore from which you want to extract lineage.

OpenCatalog Explorerin your Databricks workspace.

Navigate to the catalog (for example,main) and then to the appropriate schema (for example,sales).

main

sales

Click thePermissionstab.

ClickGrant.

Enter the user or group name (principal).

Assign the following permissions:USAGEon the catalogUSAGEon the schemaSELECTon each relevant table

USAGEon the catalog

USAGE

USAGEon the schema

USAGE

SELECTon each relevant table

SELECT

ClickGrantto apply the changes.

These privileges enable Atlan to read table definitions and other metadata from the metastore.



### (Optional) enable system.query schemaâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

This is only required if you also want to extractusage and popularity metricsfrom Databricks.

You need your account admin to enable thesystem.queryschema using theSystemSchemas API. This enables Atlan to mine query history using system tables for usage and popularity metrics.

system.query

To verify that system schemas is enabled for each schema, follow the steps inDatabricks documentation. If enabled for any given schema, thestateisEnableCompleted.

EnableCompleted

ðªDid you know?Can't grantSELECTpermissions on the system tables insystem.accessandsystem.query? Skip the previous steps and create cloned views in a separate catalog and schema. SeeCreate cloned views of system tables.

SELECT

system.access

system.query



### Grant permissionsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

Atlan supports extracting Databricks lineage and usage and popularity metrics using system tables forall three authentication methods.

Once you have created apersonal access token, anAWS service principal, or anAzure service principal, you will need to grant the following permissions:

CAN_USEon a SQL warehouse

CAN_USE

USE_CATALOGonsystemcatalog

USE_CATALOG

system

USE SCHEMAonsystem.accessschema

USE SCHEMA

system.access

USE SCHEMAonsystem.queryschema (tomine query history for usage and popularity metrics)

USE SCHEMA

system.query

SELECTon the following tables:system.query.history(to mine query history for usage and popularity metrics)system.access.table_lineagesystem.access.column_lineage

SELECT

system.query.history(to mine query history for usage and popularity metrics)

system.query.history

system.access.table_lineage

system.access.table_lineage

system.access.column_lineage

system.access.column_lineage

You need tocreate a Databricks connection in Atlanfor each metastore. You can use the hostname of your Unity Catalog-enabled workspace as theHostfor the connection.

ðªDid you know?Can't grantSELECTpermissions on the system tables insystem.accessandsystem.query? Skip the previous steps and create cloned views in a separate catalog and schema. SeeCreate cloned views of system tables.

SELECT

system.access

system.query



### (Optional) Create cloned views of system tablesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

When you don't want to grant access to system tables directly, you can create cloned views to expose lineage and popularity metrics through a separate schema.

Follow these steps to set up cloned views:

Create a catalog and schema to store cloned views. Use meaningful and unique namesâfor example,atlan_cloned_catalogandatlan_cloned_schema.

Create a catalog and schema to store cloned views. Use meaningful and unique namesâfor example,atlan_cloned_catalogandatlan_cloned_schema.

atlan_cloned_catalog

atlan_cloned_schema

Create cloned views for the following system tables:Lineage tablesCREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.column_lineageASSELECT*FROMsystem.access.column_lineage;CREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.table_lineageASSELECT*FROMsystem.access.table_lineage;Replace<cloned-catalog-name>and<cloned-schema-name>with the catalog and schema names used in your environment.Popularity metricsCREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.query_historyASSELECT*FROMsystem.query.history;Replace<cloned-catalog-name>and<cloned-schema-name>with the catalog and schema names used in your environment.

Create cloned views for the following system tables:

Lineage tablesCREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.column_lineageASSELECT*FROMsystem.access.column_lineage;CREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.table_lineageASSELECT*FROMsystem.access.table_lineage;Replace<cloned-catalog-name>and<cloned-schema-name>with the catalog and schema names used in your environment.

Lineage tables

CREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.column_lineageASSELECT*FROMsystem.access.column_lineage;CREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.table_lineageASSELECT*FROMsystem.access.table_lineage;

CREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.column_lineageASSELECT*FROMsystem.access.column_lineage;CREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.table_lineageASSELECT*FROMsystem.access.table_lineage;

Replace<cloned-catalog-name>and<cloned-schema-name>with the catalog and schema names used in your environment.

<cloned-catalog-name>

<cloned-schema-name>

Popularity metricsCREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.query_historyASSELECT*FROMsystem.query.history;Replace<cloned-catalog-name>and<cloned-schema-name>with the catalog and schema names used in your environment.

Popularity metrics

CREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.query_historyASSELECT*FROMsystem.query.history;

CREATEORREPLACEVIEW<cloned-catalog-name>.<cloned-schema-name>.query_historyASSELECT*FROMsystem.query.history;

Replace<cloned-catalog-name>and<cloned-schema-name>with the catalog and schema names used in your environment.

<cloned-catalog-name>

<cloned-schema-name>



#### Grant permissionsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

Grant the following permissions to enable access to the cloned views:

CAN_USEon a SQL warehouse

CAN_USE

USE CATALOGon the catalog (for example,<cloned-catalog-name>)

USE CATALOG

<cloned-catalog-name>

USE SCHEMAandSELECTon the schema (for example,<cloned-catalog-name>.<cloned-schema-name>)

USE SCHEMA

SELECT

<cloned-catalog-name>.<cloned-schema-name>

You mustcreate a Databricks connection in Atlanfor each metastore. You can use the hostname of your Unity Catalog-enabled workspace as theHostfor the connection.



### Locate warehouse IDâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

To extract lineage and usage and popularity metrics using system tables, you will also need thewarehouse ID of your SQL warehouse.

To locate the warehouse ID:

Log in to your Databricks workspace as a workspace admin.

From the left menu of your workspace, clickSQL Warehouses.

On theComputepage, select the warehouse you want to use.

From theOverviewtab of your warehouse page, next to theNameof your warehouse, copy the value for your SQL warehouseID. For example,example-warehouse (ID: 123ab4c5def67890), copy the value123ab4c5def67890and store it in a secure location.

example-warehouse (ID: 123ab4c5def67890)

123ab4c5def67890



## (Optional) Grant view permissions to access Databricks entities via APIsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

Atlan uses Databricks REST APIs to extract metadata for Notebooks, Queries, Jobs, and Pipelines. This information helps to understand which Databricks enitity was used to create a lineage between assets. Use the steps below for each object type to grantCAN VIEWpermission to the Databricks user or service principal configured in your integration:

Notebook API(/api/2.0/workspace/list): GrantCAN VIEWpermission on individual notebooks, or on the workspace folder containing the notebooks, or on the entire workspace. For more information, seeManage Access Control Lists with Folders.

Notebook API(/api/2.0/workspace/list): GrantCAN VIEWpermission on individual notebooks, or on the workspace folder containing the notebooks, or on the entire workspace. For more information, seeManage Access Control Lists with Folders.

/api/2.0/workspace/list

Queries API(/api/2.0/sql/queries): GrantCAN VIEWpermission on individual queries, or on the workspace folder containing the queries, or on the entire workspace. For more information, seeView Queries.

Queries API(/api/2.0/sql/queries): GrantCAN VIEWpermission on individual queries, or on the workspace folder containing the queries, or on the entire workspace. For more information, seeView Queries.

/api/2.0/sql/queries

Job API(/api/2.2/jobs/list): GrantCAN VIEWpermission on each job object directly.Databricks Jobs are distinct from notebooks or files and require permission set directly on the job object. For more information, seeControl Access to a Job.

Job API(/api/2.2/jobs/list): GrantCAN VIEWpermission on each job object directly.Databricks Jobs are distinct from notebooks or files and require permission set directly on the job object. For more information, seeControl Access to a Job.

/api/2.2/jobs/list

Pipeline API(/api/2.0/pipelines): GrantCAN VIEWpermission on each Delta Live Tables (DLT) pipeline object directly. For more information, seeConfigure Pipeline Permissions.

Pipeline API(/api/2.0/pipelines): GrantCAN VIEWpermission on each Delta Live Tables (DLT) pipeline object directly. For more information, seeConfigure Pipeline Permissions.

/api/2.0/pipelines



## (Optional) Grant permissions for views and materialized viewsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

Atlan requires the following permissions to to extract view definitions from and generate lineagefor views and materialized views:

Log in to your Databricks workspace as a workspace admin.

From the left menu of your workspace, clickCatalog.

In theCatalog Explorer, select the catalog you want to extract view definitions from and generate lineage for in Atlan.

From the tabs at the top, click thePermissionstab, and then clickGrant.

In theGrant on (workspace name)dialog, configure the following:Select theuserorservice principalunderPrincipals.Select the following privileges underPrivilege presets:USE CATALOGUSE SCHEMASELECT

Select theuserorservice principalunderPrincipals.

Select the following privileges underPrivilege presets:USE CATALOGUSE SCHEMASELECT

USE CATALOG

USE CATALOG

USE SCHEMA

USE SCHEMA

SELECT

SELECT

ClickGrantto apply the permissions.

Repeat steps 3â6 for each catalog you want to crawl in Atlan.

SELECTpermission is required to extract the definitions of views and materialized views. If you prefer not to grantSELECTat the catalog level, you can grant it on individual views and materialized views instead.

SELECT

SELECT



## (Optional) Grant permissions to mine query historyâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-databricks#optional-grant-permissions-to-mine-query-history)

Tomine query historyusing REST API, you will need to assign theCAN MANAGEpermission on your SQL warehouses to the user or service principal.

CAN MANAGE

To grant permissions to mine query history:

Log in to your Databricks workspace as a workspace admin.

From the left menu of your workspace, clickSQL Warehouses.

On theComputepage, for each SQL warehouse you want to mine query history, click the 3-dot icon and then clickPermissions.

In theManage permissionsdialog, configure the following:In theType to add multiple users or groupsfield, search for and select a user or service principal.Expand theCan usepermissions dropdown and then selectCan manage. This permission enables the service principal toview all queries for the warehouse.ClickAddto assign theCAN MANAGEpermission to the service principal.

In theType to add multiple users or groupsfield, search for and select a user or service principal.

Expand theCan usepermissions dropdown and then selectCan manage. This permission enables the service principal toview all queries for the warehouse.

ClickAddto assign theCAN MANAGEpermission to the service principal.

CAN MANAGE

data

authentication

Personal access token authentication

AWS service principal authentication

Azure service principal authentication

Grant permissions to crawl metadata

(Optional) Grant permissions to query and preview data

(Optional) Grant permissions to import and update tags

(Optional) Grant permissions to extract lineage and usage from system tables

(Optional) Grant view permissions to access Databricks entities via APIs

(Optional) Grant permissions for views and materialized views

(Optional) Grant permissions to mine query history
