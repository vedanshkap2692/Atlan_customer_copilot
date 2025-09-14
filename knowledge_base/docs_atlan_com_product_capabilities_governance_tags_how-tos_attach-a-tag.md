# Attach a tag
(source: https://docs.atlan.com/product/capabilities/governance/tags/how-tos/attach-a-tag)

TagsGet StartedTag ManagementDelete a tagAttach a tagRemove a tagConcepts

Get Started

Tag ManagementDelete a tagAttach a tagRemove a tag

Delete a tag

Attach a tag

Remove a tag

Concepts

Build governance

Tags

Tag Management

Attach a tag

Atlan allows users to addtagsto assets. You can use them to identify key characteristics of assets or group them together for usage or data protection.

Atlan also supports attaching tags imported from the following supported sources:

Databricks

dbt

Google BigQuery

Snowflake

For tags created in Atlan, these are displayed in sentence case by design in the governance center, asset sidebar, and tags filter. For imported tags, Atlan will display the source version only in the tag popover when you hover over the tag in the asset sidebar.

Tag propagation is disabled by default in Atlan. You canenable tag propagationto child and downstream assets.



## Directly tag an assetâ
(source: https://docs.atlan.com/product/capabilities/governance/tags/how-tos/attach-a-tag)

To directly tag an asset:

In the left menu from any screen in Atlan, clickAssets.

In the left menu from any screen in Atlan, clickAssets.

On theAssetspage, click an asset to view its asset profile.

On theAssetspage, click an asset to view its asset profile.

UnderTagsÂ in the right menu, click the+icon.

UnderTagsÂ in the right menu, click the+icon.

In the popup, check the boxes to select one or more tags for the asset.

In the popup, check the boxes to select one or more tags for the asset.

No propagationis the default setting. Next to your selected tag(s) in the popup, clickEditÂ to configure the propagation of tags:ClickHierarchy & lineageto allow propagation of tags to the child and downstream assets.ÂClickHierarchy only (no lineage)to allow propagation of tags to the child assets only.ClickNo propagationto disallow any propagation of tags.

No propagationis the default setting. Next to your selected tag(s) in the popup, clickEditÂ to configure the propagation of tags:

ClickHierarchy & lineageto allow propagation of tags to the child and downstream assets.Â

ClickHierarchy only (no lineage)to allow propagation of tags to the child assets only.

ClickNo propagationto disallow any propagation of tags.

(Optional) For tags imported from supported sources, you can configure the following:ForSnowflake assets, you can attach aSnowflake tag. Ifreverse sync is enabled, any updates made in Atlan will also be synced to Snowflake. If reverse sync is disabled, updates will be restricted to Atlan. UnderSnowflake tags, select asynced Snowflake tagand then:Click theSelect tag valuedropdown to attach anallowed valuefrom a predefined list, if available.ForAdd value, enter a tag value of your choice, if no predefined allowed values are present. Tag values added in Atlan are case-sensitive.Fordbt Cloudordbt Coreassets, you can attach adbt tag.ForGoogle BigQueryassets, you can attach aGoogle BigQuery tag.ForDatabricksassets, you can attach aDatabricks tagand tag values. Ifreverse sync is enabled, any updates made in Atlan will also be synced to Databricks. If reverse sync is disabled, updates will be restricted to Atlan.dangerIf there are multiple synced tags mapped to anAtlan tag, you will only be able to select one synced tag. You can also only select imported tags that belong to the same connection as the selected asset.

(Optional) For tags imported from supported sources, you can configure the following:

ForSnowflake assets, you can attach aSnowflake tag. Ifreverse sync is enabled, any updates made in Atlan will also be synced to Snowflake. If reverse sync is disabled, updates will be restricted to Atlan. UnderSnowflake tags, select asynced Snowflake tagand then:Click theSelect tag valuedropdown to attach anallowed valuefrom a predefined list, if available.ForAdd value, enter a tag value of your choice, if no predefined allowed values are present. Tag values added in Atlan are case-sensitive.

Click theSelect tag valuedropdown to attach anallowed valuefrom a predefined list, if available.

ForAdd value, enter a tag value of your choice, if no predefined allowed values are present. Tag values added in Atlan are case-sensitive.

Fordbt Cloudordbt Coreassets, you can attach adbt tag.

ForGoogle BigQueryassets, you can attach aGoogle BigQuery tag.

ForDatabricksassets, you can attach aDatabricks tagand tag values. Ifreverse sync is enabled, any updates made in Atlan will also be synced to Databricks. If reverse sync is disabled, updates will be restricted to Atlan.

If there are multiple synced tags mapped to anAtlan tag, you will only be able to select one synced tag. You can also only select imported tags that belong to the same connection as the selected asset.

ClickUpdateto confirm your selections.

ClickUpdateto confirm your selections.

ClickSaveto save the tag(s) to your asset.

ClickSaveto save the tag(s) to your asset.

(Optional) Hover over the attached tag to view tag propagation details in a popover, including username of the user who applied the tag, mode of tag propagation, and when the tag was configured.

(Optional) Hover over the attached tag to view tag propagation details in a popover, including username of the user who applied the tag, mode of tag propagation, and when the tag was configured.

(Optional) Filter tagged assets byattached tags, including tags imported from supported sources.

(Optional) Filter tagged assets byattached tags, including tags imported from supported sources.

For reverse sync to work for tags imported fromSnowflakeandDatabricks, first ensure that reverse sync is enabled on the imported tag and then you must attach the imported tag to the asset (complete step 6 above).

You canremove tagsfrom your tagged assets. You can alsoadd tags to your column assetsdirectly from Google Sheets.

connectors

data

Directly tag an asset
