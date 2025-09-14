# Manage Databricks tags
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/manage-databricks-tags)

DatabricksGet StartedCross-workspace SetupCrawl Databricks AssetsOn-premises SetupPrivate Network SetupLineage and UsageTag managementManage Databricks tagsReferencesTroubleshooting

Get Started

Cross-workspace Setup

Crawl Databricks Assets

On-premises Setup

Private Network Setup

Lineage and Usage

Tag managementManage Databricks tags

Manage Databricks tags

References

Troubleshooting

Connect data

Data Warehouses

Databricks

Tag management

Manage Databricks tags

You must have aUnity Catalog-enabled workspaceto import Databricks tags in Atlan.

Atlan enables you to import yourDatabricks tags, update your Databricks assets with the imported tags, and push the tag updates back to Databricks:

Import tags-  crawl Databricks tags from Databricks to Atlan

Reverse sync-  sync Databricks tag updates from Atlan to Databricks

Once you'veimported your Databricks tagsto Atlan:

Your Databricks assets in Atlan will be automatically enriched with their Databricks tags.

Imported Databricks tagswill be mapped to correspondingAtlan tagsthrough case-insensitive name match   -  multiple Databricks tags can be matched to a single tag in Atlan.

You can alsoattach Databricks tags, including tag values, to your Databricks assets in Atlan   -  allowing you to categorize your assets at a more granular level.

You canfilter your assetsby Databricks tags and tag values.

You canenable reverse syncto push any tag updates for your Databricks assets back to Databricks   -  including tag values added to assets in Atlan.

Enabling reverse sync will only update existing tags in Databricks. It will neither create nor delete any tags in Databricks.



## Prerequisitesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/manage-databricks-tags)

You must have aUnity Catalog-enabled workspaceand SQL warehouse configured to import Databricks tags in Atlan.

Before you can import tags from andÂ push tag updates to Databricks usingpersonal access token,AWS service principal, orAzure service principalauthentication, you will need to do the following:

Ensure that you have aUnity Catalog-enabled workspaceand a SQL warehouse configured.

Create tagsor have existing tags in Databricks.

Grant permissionsto import tags from and push tag updates to Databricks.



## Import Databricks tags to Atlanâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/manage-databricks-tags)

You will need to be anadmin userin Atlan to import Databricks tags to Atlan. You will also need to work with your Databricks administrator to grantÂ permissions to import tags from Databricks   -  you may not have access yourself.

You can import your Databricks tags to Atlan through one-way tag sync. The synced Databricks tags will be matched to corresponding tags in Atlan through case-insensitive name match and your Databricks assets will be enriched with their synced tags from Databricks.

To import Databricks tags to Atlan, you can either:

Create a new Databricks workflow andconfigure the crawlerto import tags.

Modify the crawler's configurationfor an existing Databricks workflow to changeImport TagstoYes. If you subsequently modify the workflow to disable tag import, for any tags already imported, Atlan will preserve those tags.

Once the crawler has completed running, tags imported from Databricks will be available to use fortagging assets! ð



## View Databricks tags in Atlanâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/manage-databricks-tags)

Once you've imported your Databricks tags, you will be able to view and manage your Databricks tags in Atlan.

To view Databricks tags:

From the left menu of any screen, clickGovernance.

Under theGovernanceheading of the _Governance cente_r, clickTags.

(Optional) UnderTags, click the funnel icon to filter tags by source type. ClickDatabricksto filter for tags imported from Databricks.

From the left menu underTags, select a synced tag.

In theOverviewsection, you can view a total count of synced Databricks tags. To the right ofOverview, clickSynced tagsto view additional details   -  including tag name, description, tag values, total count of linked assets, connection, database, and schema names, and timestamp for last synced.

(Optional) Click theLinked assetstab to view linked assets for your Databricks tag.

(Optional) In the top right, click the pencil icon to add a description and change thetag icon. You cannot rename tags synced from Databricks.



## Push tag updates to Databricksâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/databricks/how-tos/manage-databricks-tags)

Anyadmin or member userin Atlan can configure reverse sync for tag updates to Databricks. You will also need to work with your Databricks administrator to grant additional permissions to push updates   -  you may not have access yourself.

You can enable reverse sync for your imported Databricks tags in Atlan and push all tag updates for your Databricks assets back to source. Once you have enabled reverse sync, any Databricks assets with tags updated in Atlan will also be updated in Databricks.

To enable reverse sync for imported Databricks tags:

From the left menu of any screen, clickGovernance.

Under theGovernanceheading of the _Governance cente_r, clickTags.

(Optional) UnderTags, click the funnel icon to filter tags by source type. ClickDatabricksto filter for tags imported from Databricks.

In the left menu underTags, select a synced Databricks tag   -  synced tags will display the Databricks icon next to the tag name.Â

On your selected tag page, to the right ofOverview, clickSynced tags.

UnderSynced tags, in the upper right, turn onEnable reverse syncto synchronize tag updates from Atlan to Databricks.

In the corresponding confirmation dialog, clickYes, enable itto enable reverse tag sync or clickCancel.

Now when youattach Databricks tagsto your Databricks assets in Atlan, these tag updates will also be pushed to Databricks! ð

Enabling reverse sync willnottrigger any updates in Databricks until synced tags are attached to Databricks assets in Atlan.

connectors

data

crawl

Prerequisites

Import Databricks tags to Atlan

View Databricks tags in Atlan

Push tag updates to Databricks
