# Manage dbt tags
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/how-tos/manage-dbt-tags)

dbtGet StartedCrawl dbt AssetsManage dbt in AtlanManage dbt tagsEnrich Atlan through dbtMigrate from dbt to Atlan actionImpact AnalysisReferencesTroubleshooting

Get Started

Crawl dbt Assets

Manage dbt in AtlanManage dbt tagsEnrich Atlan through dbtMigrate from dbt to Atlan action

Manage dbt tags

Enrich Atlan through dbt

Migrate from dbt to Atlan action

Impact Analysis

References

Troubleshooting

Connect data

ETL Tools

dbt

Manage dbt in Atlan

Manage dbt tags

If you have already set up and crawled dbt, you donotneed to make any modifications to yourdbt Cloudordbt Coresetup. You only need to configure thedbt crawlerto import dbt tags. Atlan will then import your existing dbt tags automatically for you.

Atlan imports yourdbt tagsand allows you to update your dbt assets with the imported tags.

Once you'vecrawled dbt:

Your dbt assets in Atlan will be automatically enriched with their dbt tags.

Imported dbt tags will be mapped to correspondingAtlan tagsthrough case-insensitive name match   -  multiple dbt tags can be matched to a single tag in Atlan.Â

You can alsoattach dbt tagsto your dbt assets in Atlan   -  allowing you to categorize your assets at a more granular level.

You canfilter your assetsby dbt tags.



## Import dbt tags to Atlanâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/how-tos/manage-dbt-tags)

You will need to be anadmin userin Atlan to import dbt tags. You will also need to work with your dbt Cloud or dbt Core administrator for additional inputs and approval.

Atlan imports existing dbt tags through one-way tag sync. The imported dbt tags are matched to corresponding tags in Atlan through case-insensitive name match and your dbt assets enriched with the tags synced from dbt.

To allow Atlan to import and sync dbt tags, you will need to do the following:

Create tagsor have existing tags in dbt.

Set updbt Cloudordbt Coreto integrate with Atlan.

Configure the dbt crawlerto import existing tags from dbt to Atlan. ForImport Tags, clickYesto import dbt tags or clickNoto disable it. If you subsequently modify the workflow to disabletag import, for any tags already imported, Atlan will preserve those tags.

Once the crawler has completed running, tags synced from dbt will be available to use fortagging assets! ð



## View dbt tags in Atlanâ
(source: https://docs.atlan.com/apps/connectors/etl-tools/dbt/how-tos/manage-dbt-tags)

Once you've crawleddbt Cloudordbt Core, you will be able to view and manage your dbt tags in Atlan.

To view synced dbt tags:

From the left menu of any screen, clickGovernance.

Under theGovernanceheading of the _Governance cente_r, clickTags.

(Optional) UnderTags, click the funnel icon to filter tags by source type. Clickdbtto filter for tags imported from dbt.

In theOverviewsection, you can view a total count of synced dbt tags. To the right ofOverview, clickSynced tagsto view additional details   -  including tag name, description, total count of linked assets, connection name, and timestamp for last synced.

(Optional) Click theLinked assetstab to view linked assets for your dbt tag.

(Optional) In the top right, click the pencil icon to add a description and change thetag icon. Tags synced from dbt cannot be renamed.

You can nowattach dbt tagsto your dbt assets in Atlan! ð

connectors

crawl

setup

Import dbt tags to Atlan

View dbt tags in Atlan
