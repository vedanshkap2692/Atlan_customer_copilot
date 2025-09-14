# Set up cross-workspace extraction
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-cross-workspace-extraction)

DatabricksGet StartedCross-workspace SetupSet up cross-workspace extractionCrawl Databricks AssetsOn-premises SetupPrivate Network SetupLineage and UsageTag managementReferencesTroubleshooting

Get Started

Cross-workspace SetupSet up cross-workspace extraction

Set up cross-workspace extraction

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

Cross-workspace Setup

Set up cross-workspace extraction

Eliminate the need for separate crawler configurations by using a single service principal to crawl metadata from all workspaces within a Databricks metastore. This guide walks you through configuring the necessary permissions to enable cross-workspace extraction.

Cross-workspace extraction isn't supported for REST API or JDBC extraction methods.



## Prerequisitesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-cross-workspace-extraction)

Before you begin, make sure you have:

A Unity Catalog-enabled Databricks workspace

Account admin access to create and manage service principals

Workspace admin access to grant permissions across all target workspaces

At least one active SQL warehouse in each workspace you intend to crawl

Set up Databricks authenticationcompleted with one of the supported authentication methods

System table extraction enabledfor lineage and usage extraction



## Permissions requiredâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-cross-workspace-extraction)

The service principal needs the following permissions to enable cross-workspace extraction:

CAN_USEon SQL warehouses in each workspace

CAN_USE

SELECTonsystem.access.workspace_latesttable

SELECT

system.access.workspace_latest

USE CATALOG,BROWSE, andSELECTon all catalogs you want to crawl

USE CATALOG

BROWSE

SELECT



## Add service principal to all workspacesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-cross-workspace-extraction)

You must use asingle, common service principalthat has been granted access toallDatabricks workspaces you intend to crawl within the metastore.

Log in to your Databricks account console as an account admin

From the left menu, clickWorkspacesand select a workspace

From the tabs along the top, click thePermissionstab

In the upper right, clickAdd permissions

In theAdd permissionsdialog:ForUser, group, or service principal, select your service principalForPermission, select workspaceUserClickAdd

ForUser, group, or service principal, select your service principal

ForPermission, select workspaceUser

ClickAdd

Repeat steps 2-5 for each workspace you intend to crawl



## Grant permissionsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-cross-workspace-extraction)

Configure the necessary permissions for the service principal to access and extract metadata from all workspaces within the metastore.

SQL workspace permissions:The service principal must have usage permissions onat least one active SQL warehouse within each workspace. The extractor uses the smallest available warehouse to run its discovery queries.Via SQLVia UIConnect to your Databricks workspace using a SQL client or the SQL editorRun the following command for each workspace, replacing the placeholders:GRANTCAN_USEONWAREHOUSE<warehouse_name>TO`<service_principal_id>`;Replace<warehouse_name>with your actual warehouse nameReplace<service_principal_id>with your service principal's application IDExampleGRANTCAN_USEONWAREHOUSE production-warehouseTO`12345678-1234-1234-1234-123456789012`;Log in to your Databricks workspace as a workspace adminFrom the left menu, clickSQL WarehousesOn theComputepage, for each SQL warehouse, click the 3-dot icon and then clickPermissionsIn theManage permissionsdialog:In theType to add multiple users or groupsfield, search for and select your service principalSelectCan usepermissionClickAddto assign the permission

SQL workspace permissions:The service principal must have usage permissions onat least one active SQL warehouse within each workspace. The extractor uses the smallest available warehouse to run its discovery queries.

Via SQL

Via UI

Connect to your Databricks workspace using a SQL client or the SQL editor

Connect to your Databricks workspace using a SQL client or the SQL editor

Run the following command for each workspace, replacing the placeholders:GRANTCAN_USEONWAREHOUSE<warehouse_name>TO`<service_principal_id>`;Replace<warehouse_name>with your actual warehouse nameReplace<service_principal_id>with your service principal's application IDExampleGRANTCAN_USEONWAREHOUSE production-warehouseTO`12345678-1234-1234-1234-123456789012`;

Run the following command for each workspace, replacing the placeholders:

GRANTCAN_USEONWAREHOUSE<warehouse_name>TO`<service_principal_id>`;

GRANTCAN_USEONWAREHOUSE<warehouse_name>TO`<service_principal_id>`;

Replace<warehouse_name>with your actual warehouse name

<warehouse_name>

Replace<service_principal_id>with your service principal's application ID

<service_principal_id>

GRANTCAN_USEONWAREHOUSE production-warehouseTO`12345678-1234-1234-1234-123456789012`;

GRANTCAN_USEONWAREHOUSE production-warehouseTO`12345678-1234-1234-1234-123456789012`;

Log in to your Databricks workspace as a workspace admin

From the left menu, clickSQL Warehouses

On theComputepage, for each SQL warehouse, click the 3-dot icon and then clickPermissions

In theManage permissionsdialog:In theType to add multiple users or groupsfield, search for and select your service principalSelectCan usepermissionClickAddto assign the permission

In theType to add multiple users or groupsfield, search for and select your service principal

SelectCan usepermission

ClickAddto assign the permission

System table permissions:Access to the system schema is essential for workspace and lineage discovery.Via SQLVia UIConnect to your Databricks workspace using a SQL client or the SQL editorRun the following command, replacing the placeholder:GRANTSELECTONTABLEsystem.access.workspace_latestTO`<service_principal_id>`;Replace<service_principal_id>with your service principal's application IDExampleGRANTSELECTONTABLEsystem.access.workspace_latestTO`12345678-1234-1234-1234-123456789012`;Log in to your Databricks workspace as a workspace adminFrom the left menu, clickCatalogIn theCatalog Explorer, navigate tosystem>accessClick on theworkspace_latesttableClick thePermissionstab and then clickGrantIn theGrant permissionsdialog:UnderPrincipals, select your service principalUnderPrivileges, checkSELECTClickGrantto apply the permissions

System table permissions:Access to the system schema is essential for workspace and lineage discovery.

Via SQL

Via UI

Connect to your Databricks workspace using a SQL client or the SQL editor

Connect to your Databricks workspace using a SQL client or the SQL editor

Run the following command, replacing the placeholder:GRANTSELECTONTABLEsystem.access.workspace_latestTO`<service_principal_id>`;Replace<service_principal_id>with your service principal's application IDExampleGRANTSELECTONTABLEsystem.access.workspace_latestTO`12345678-1234-1234-1234-123456789012`;

Run the following command, replacing the placeholder:

GRANTSELECTONTABLEsystem.access.workspace_latestTO`<service_principal_id>`;

GRANTSELECTONTABLEsystem.access.workspace_latestTO`<service_principal_id>`;

Replace<service_principal_id>with your service principal's application ID

<service_principal_id>

GRANTSELECTONTABLEsystem.access.workspace_latestTO`12345678-1234-1234-1234-123456789012`;

GRANTSELECTONTABLEsystem.access.workspace_latestTO`12345678-1234-1234-1234-123456789012`;

Log in to your Databricks workspace as a workspace admin

From the left menu, clickCatalog

In theCatalog Explorer, navigate tosystem>access

Click on theworkspace_latesttable

Click thePermissionstab and then clickGrant

In theGrant permissionsdialog:UnderPrincipals, select your service principalUnderPrivileges, checkSELECTClickGrantto apply the permissions

UnderPrincipals, select your service principal

UnderPrivileges, checkSELECT

ClickGrantto apply the permissions

Asset permissions:The service principal requires permissions to "see" and "read" the metadata for all data assets you wish to extract. These grants must be applied to all private, public, and shared catalogs that are in scope for crawling.Important!For private catalogs, grant permissions from each workspace. For public catalogs, grant from any workspace.Via SQLVia UIConnect to your Databricks workspace using a SQL client or the SQL editorGrant catalog-level permissions (required even when using BROWSE - BROWSE automatically grants access to all schemas and tables):GRANTUSECATALOGONCATALOG<catalog_name>TO`<service_principal_id>`;GRANTBROWSEONCATALOG<catalog_name>TO`<service_principal_id>`;Replace<catalog_name>with your actual catalog nameReplace<service_principal_id>with your service principal's application IDIf not using BROWSE, along with catalog permissions, grant additional permissions:Grant schema-level permissions:GRANTUSESCHEMAONSCHEMA<catalog_name>.<schema_name>TO`<service_principal_id>`;Replace<catalog_name>and<schema_name>with your actual valuesReplace<service_principal_id>with your service principal's application IDExampleGRANTUSECATALOGONCATALOG mainTO`12345678-1234-1234-1234-123456789012`;GRANTBROWSEONCATALOG mainTO`12345678-1234-1234-1234-123456789012`;Log in to your Databricks workspace as a workspace adminFrom the left menu, clickCatalogIn theCatalog Explorer, navigate to the catalog you want to grant permissions on (for example,main)Click thePermissionstab and then clickGrantIn theGrant permissionsdialog:UnderPrincipals, select your service principalUnderPrivileges, check the following permissions:USE CATALOGUSE SCHEMABROWSESELECTClickGrantto apply the permissionsRepeat steps 3-5 for each catalog you want to crawl in Atlan

Asset permissions:The service principal requires permissions to "see" and "read" the metadata for all data assets you wish to extract. These grants must be applied to all private, public, and shared catalogs that are in scope for crawling.

For private catalogs, grant permissions from each workspace. For public catalogs, grant from any workspace.

Via SQL

Via UI

Connect to your Databricks workspace using a SQL client or the SQL editor

Connect to your Databricks workspace using a SQL client or the SQL editor

Grant catalog-level permissions (required even when using BROWSE - BROWSE automatically grants access to all schemas and tables):GRANTUSECATALOGONCATALOG<catalog_name>TO`<service_principal_id>`;GRANTBROWSEONCATALOG<catalog_name>TO`<service_principal_id>`;Replace<catalog_name>with your actual catalog nameReplace<service_principal_id>with your service principal's application ID

Grant catalog-level permissions (required even when using BROWSE - BROWSE automatically grants access to all schemas and tables):

GRANTUSECATALOGONCATALOG<catalog_name>TO`<service_principal_id>`;GRANTBROWSEONCATALOG<catalog_name>TO`<service_principal_id>`;

GRANTUSECATALOGONCATALOG<catalog_name>TO`<service_principal_id>`;GRANTBROWSEONCATALOG<catalog_name>TO`<service_principal_id>`;

Replace<catalog_name>with your actual catalog name

<catalog_name>

Replace<service_principal_id>with your service principal's application ID

<service_principal_id>

If not using BROWSE, along with catalog permissions, grant additional permissions:Grant schema-level permissions:GRANTUSESCHEMAONSCHEMA<catalog_name>.<schema_name>TO`<service_principal_id>`;Replace<catalog_name>and<schema_name>with your actual valuesReplace<service_principal_id>with your service principal's application ID

If not using BROWSE, along with catalog permissions, grant additional permissions:

Grant schema-level permissions:GRANTUSESCHEMAONSCHEMA<catalog_name>.<schema_name>TO`<service_principal_id>`;Replace<catalog_name>and<schema_name>with your actual valuesReplace<service_principal_id>with your service principal's application ID

Grant schema-level permissions:

GRANTUSESCHEMAONSCHEMA<catalog_name>.<schema_name>TO`<service_principal_id>`;

GRANTUSESCHEMAONSCHEMA<catalog_name>.<schema_name>TO`<service_principal_id>`;

Replace<catalog_name>and<schema_name>with your actual values

<catalog_name>

<schema_name>

Replace<service_principal_id>with your service principal's application ID

<service_principal_id>

GRANTUSECATALOGONCATALOG mainTO`12345678-1234-1234-1234-123456789012`;GRANTBROWSEONCATALOG mainTO`12345678-1234-1234-1234-123456789012`;

GRANTUSECATALOGONCATALOG mainTO`12345678-1234-1234-1234-123456789012`;GRANTBROWSEONCATALOG mainTO`12345678-1234-1234-1234-123456789012`;

Log in to your Databricks workspace as a workspace admin

From the left menu, clickCatalog

In theCatalog Explorer, navigate to the catalog you want to grant permissions on (for example,main)

main

Click thePermissionstab and then clickGrant

In theGrant permissionsdialog:UnderPrincipals, select your service principalUnderPrivileges, check the following permissions:USE CATALOGUSE SCHEMABROWSESELECTClickGrantto apply the permissions

UnderPrincipals, select your service principal

UnderPrivileges, check the following permissions:

USE CATALOG

USE SCHEMA

BROWSE

SELECT

ClickGrantto apply the permissions

Repeat steps 3-5 for each catalog you want to crawl in Atlan



## Need help?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-cross-workspace-extraction)

CheckTroubleshooting Databricks connectivityfor common issues

Contact Atlan supportfor help with setup or integration



## Next stepsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/set-up-cross-workspace-extraction)

Crawl Databricks

databricks

setup

cross-workspace-extraction

Prerequisites

Permissions required

Add service principal to all workspaces

Grant permissions

Need help?

Next steps
