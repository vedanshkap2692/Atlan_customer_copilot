# Add an alias
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/add-an-alias)

DiscoveryGet StartedAsset ManagementAccess archived assetsAdd an aliasStar assetsAdd ownersAdd descriptionsAdd certificatesAdd a resourceConfigurationConceptsReferencesFAQ

Get Started

Asset ManagementAccess archived assetsAdd an aliasStar assetsAdd ownersAdd descriptionsAdd certificatesAdd a resource

Access archived assets

Add an alias

Star assets

Add owners

Add descriptions

Add certificates

Add a resource

Configuration

Concepts

References

FAQ

Use data

Discovery

Asset Management

Add an alias

Anynon-guest userwithedit access to an asset's metadatacan add an alias. This only includes admin and member users.

An alias is a business-oriented, alternate name that you can specify for your assets in Atlan. You can either manually add a more descriptive and user-friendly alias or useAtlan AIto do the same, ifAtlan AI is enabled in your Atlan workspace. This can help you improve the readability of your asset names while providing useful context to your users.

Atlan recommends adding an alias that's unique to each asset, in a one-to-one relationship. To relate your assets, you can insteadattach tagsto group them by use case orlink termsto group them conceptually.

Atlan currently supports adding an alias to everything EXCEPT the following asset types:

Database

Schema

Connection

Process, includingConnectionProcessBIProcessColumnProcess

ConnectionProcess

BIProcess

ColumnProcess

Query



## Exampleâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/add-an-alias)

For an asset with a technical name likeFCT_SUPPLIER_TRANSACTIONS, you can addSupplier Transaction Recordsas an alias. Once you have added an alias, you can:

FCT_SUPPLIER_TRANSACTIONS

Supplier Transaction Records

Search for assetseither with their technical names or aliases, Atlan will match on the most relevant title.

Use theTitleproperty filterto filter for assets either by their technical names or aliases.

Setasset name display preferences for personas, choosing whether the technical name or alias should be displayed prominently in search and discovery.

View aliases insearch results, asset preview,asset profile,asset sidebar, andlineage graph.



## Add an aliasâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/add-an-alias)

To add an alias to your asset:

From the left menu of any screen in Atlan, clickAssets.

On theAssetspage, click any asset with a technical name. To add an alias, you can either:Open the asset profile, and to the right of the asset name, click the pencil icon.Navigate to theOverviewsidebar, and to the right of the asset name, click the pencil icon.

Open the asset profile, and to the right of the asset name, click the pencil icon.

Navigate to theOverviewsidebar, and to the right of the asset name, click the pencil icon.

In theAdd an aliasdialog, you can either:In theType a business-friendly namefield, enter an alias for your asset.IfAtlan AI is enabled, underAtlan AI Suggested, click an Atlan AI-suggested alias for your asset. (Optional) Click the refresh icon to regenerate Atlan AI suggestions and compare different sets of suggestions.

In theType a business-friendly namefield, enter an alias for your asset.

IfAtlan AI is enabled, underAtlan AI Suggested, click an Atlan AI-suggested alias for your asset. (Optional) Click the refresh icon to regenerate Atlan AI suggestions and compare different sets of suggestions.

ClickAddto save your preferred alias for the asset.

(Optional) Once you have added an alias, you can:Hover over the asset name to view both the technical name and alias in a popup.From the asset sidebar tabs on the right, click theActivitytab to viewalias activityby user and timestamp of update.To edit your alias, click the pencil icon to make any changes.From thefilters menuon the left, clickPropertiesand then clickTitleto filter assets by the technical name or alias.

Hover over the asset name to view both the technical name and alias in a popup.

From the asset sidebar tabs on the right, click theActivitytab to viewalias activityby user and timestamp of update.

To edit your alias, click the pencil icon to make any changes.

From thefilters menuon the left, clickPropertiesand then clickTitleto filter assets by the technical name or alias.

Your asset will now display an alias! ð

You can alsoset asset name display preferencesto technical name or alias for your personas. If no preference has been specified and an alias is available, then Atlan will display the alias over the technical name on an asset by default.

atlan

documentation

Example

Add an alias
