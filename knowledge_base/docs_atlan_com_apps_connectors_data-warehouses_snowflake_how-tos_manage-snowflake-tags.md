# Manage Snowflake tags
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/manage-snowflake-tags)

SnowflakeGet StartedCrawl Snowflake AssetsManage Snowflake in AtlanManage Snowflake tagsConfigure Snowflake data metric functionsReferencesTroubleshootingBest Practices

Get Started

Crawl Snowflake Assets

Manage Snowflake in AtlanManage Snowflake tagsConfigure Snowflake data metric functions

Manage Snowflake tags

Configure Snowflake data metric functions

References

Troubleshooting

Best Practices

Connect data

Data Warehouses

Snowflake

Manage Snowflake in Atlan

Manage Snowflake tags

Note that object tagging in Snowflake currently requiresEnterprise Edition or higher.

Atlan enables you to import yourSnowflake tags, update your Snowflake assets with the imported tags, and push the tag updates back to Snowflake:

Import tags   -  crawl Snowflake tags from Snowflake to Atlan

Reverse sync   -  sync Snowflake tag updates from Atlan to Snowflake

Once you've imported your Snowflake tags to Atlan:

Your Snowflake assets in Atlan are automatically enriched with their Snowflake tags.

Imported Snowflake tags are mapped to correspondingAtlan tagsthrough case-insensitive name match   -  multiple Snowflake tags can be matched to a single tag in Atlan.

You can alsoattach Snowflake tags, including tag values, to your Snowflake assets in Atlan   -  allowing you to categorize your assets at a more granular level. Atlan supports:Allowed values: attach an allowed value from a predefined list of values imported from Snowflake.Tag values: enter any value in Atlan whileattaching or editing imported Snowflake tagson an asset.

Allowed values: attach an allowed value from a predefined list of values imported from Snowflake.

Tag values: enter any value in Atlan whileattaching or editing imported Snowflake tagson an asset.

You can enable reverse sync to push any tag updates for your Snowflake assets back to Snowflake   -  includingallowed and tag valuesadded to assets in Atlan.

You canfilter your assetsby Snowflake tags and tag and allowed values.

Enabling reverse sync only updates existing tags in Snowflake. It neither creates nor deletes any tags in Snowflake.



## Prerequisitesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/manage-snowflake-tags)

Additional privileges are only required when using theinformation schema methodfor fetching metadata. This is because Snowflakestores all tag objectsin theACCOUNT_USAGEschema. If you're using theaccount usage methodto crawl metadata in Atlan or you haveconfigured the Snowflake miner, any permissions required are already set.

ACCOUNT_USAGE



### Account usage methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/manage-snowflake-tags)

Before you can import tags from Snowflake, you need to do the following:

Create tagsor have existing tags in Snowflake.

Grant thesame permissionsas required for crawling Snowflake assets to import tags and push updated tags to Snowflake.



### Information schema methodâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/manage-snowflake-tags)

Before you can import tags from Snowflake, you need to do the following:

Create tagsor have existing tags in Snowflake.

Grant additional permissions toimport tagsfrom Snowflake.

Grant additional permissions topush updated tagsto Snowflake.



## Import Snowflake tags to Atlanâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/manage-snowflake-tags)

You need to be anadmin userin Atlan to import Snowflake tags to Atlan. You also need to work with your Snowflake administrator to grantadditional permissions to import tagsfrom Snowflake   -  you may not have access yourself.

You can import your Snowflake tags to Atlan through one-way tag sync. The synced Snowflake tags are matched to corresponding tags in Atlan through case-insensitive name match and your Snowflake assets are enriched with their synced tags from Snowflake.

To import Snowflake tags to Atlan, you can either:

Create a new Snowflake workflow andconfigure the crawlerto import tags.

Modify the crawler's configurationfor an existing Snowflake workflow to changeImport TagstoYes. If you subsequently modify the workflow to disable tag import, for any tags already imported, Atlan preserves those tags.

Once the crawler has completed running, tags imported from Snowflake are available to use for tagging assets! ð



## View Snowflake tags in Atlanâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/manage-snowflake-tags)

Once you've imported your Snowflake tags, you can view and manage your Snowflake tags in Atlan.

To view Snowflake tags:

From the left menu of any screen, clickGovernance.

Under theGovernanceheading of the _Governance cente_r, clickTags.

(Optional) UnderTags, click the funnel icon to filter tags by source type. ClickSnowflaketo filter for tags imported from Snowflake.

From the left menu underTags, select a synced tag   -  synced tags display the Snowflake âï¸ icon next to the tag name.

In theOverviewsection, you can view a total count of synced Snowflake tags. To the right ofOverview, clickSynced tagsto view additional details   -  including tag name, description, tag values, total count of linked assets, connection, database, and schema names, and timestamp for last synced.

(Optional) Click theLinked assetstab to view linked assets for your Snowflake tag.

(Optional) In the top right, click the pencil icon to add a description and change thetag icon. You can't rename tags synced from Snowflake.



## Push tag updates to Snowflakeâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/how-tos/manage-snowflake-tags)

Anyadmin or member userin Atlan can configure reverse sync for tag updates to Snowflake. You also need to work with your Snowflake administrator togrant additional permissions to push updates-  you may not have access yourself.

Reverse sync is currently only available for imported Snowflake tags in Atlan. The imported tags display a Snowflake âï¸ icon next to the tag name. If using theaccount usage method, expect adata latency of up to 3 hoursfor reverse tag sync to be successful.

You can enable reverse sync for your imported Snowflake tags in Atlan and push all tag updates for your Snowflake assets back to source. Once you have enabled reverse sync, any Snowflake assets with tags updated in Atlan are also updated in Snowflake.

To enable reverse sync for imported Snowflake tags:

From the left menu of any screen, clickGovernance.

Under theGovernanceheading of the _Governance cente_r, clickTags.

(Optional) UnderTags, click the funnel icon to filter tags by source type. ClickSnowflaketo filter for tags imported from Snowflake.

In the left menu underTags, select a synced Snowflake tag   -  synced tags display the Snowflake âï¸ icon next to the tag name.

On your selected tag page, to the right ofOverview, clickSynced tags.

UnderSynced tags, in the upper right, turn onEnable reverse syncto synchronize tag updates from Atlan to Snowflake.

In the advanced settings, you can also enableconcatenationto support multiple tag values for a single column. For detailed information about multiple tag values and concatenation, seeMultiple tag values and concatenation.

In the corresponding confirmation dialog, clickYes, enable itto enable reverse tag sync or clickCancel.

Now when youattach Snowflake tagsto your Snowflake assets in Atlan, these tag updates are also pushed to Snowflake! ð

Enabling reverse sync won't trigger any updates in Snowflake until synced tags are attached to Snowflake assets in Atlan. For any questions about managing Snowflake tags, head overhere.

connectors

data

crawl

Prerequisites

Import Snowflake tags to Atlan

View Snowflake tags in Atlan

Push tag updates to Snowflake
