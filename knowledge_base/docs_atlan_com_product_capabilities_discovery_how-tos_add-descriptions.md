# Add descriptions
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/add-descriptions)

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

Add descriptions

You can add descriptions to your assets in Atlan, including tables, views, and individual columns. You can even add a description in the form of aREADME. Doing so will enrich your data asset with the relevant contextual information.

The description editor in Atlan also supports Markdown syntax. You can crawl descriptions in Markdown at source, view them in the asset sidebar and profile, and make edits in Markdown directly in Atlan.



## Add descriptions to your assetsâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/add-descriptions)

To add or update a description for your data asset, follow these steps:

From the left menu on any screen, clickAssets.

On theAssetspage, click on an asset to view itsOverviewin the right menu.

UnderDescription, click on the text box to add a description.

Once you've added new text or updated the existing one, click anywhere to automatically save your changes.

Your asset description is now live! ð

You can also add or edit asset descriptions directly from the asset profile.

The size limit for description values is 32766 bytes. Depending on the types of characters used, the character limit for descriptions can range from 8191 to 32766 characters.



## Add column descriptionsâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/add-descriptions)

You can also add a description for a single column rather than an entire data asset. To add column descriptions, follow these steps:

On theAssetspage, click on an asset to view its asset profile.

UnderColumn Previewin the asset profile, navigate to a column and click+AddunderDescription.

Once you've entered the text, click anywhere to save it.



## Search using asset descriptionsâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/add-descriptions)

You can also filter your assets by the keywords in your asset descriptions. Here are the steps:

In theFiltersmenu on theAssetspage, clickProperties.

Next, clickDescriptionfrom the dropdown menu.

In theDescriptionpopup display, enter a keyword in the text box.

Click on thedownward arrowand then select the preferred matching condition.

To add multiple description filters, click+in theDescriptionpopup.

TheAssetspage will now display a list of assets filtered by your description text. You can clickClear Allin theFiltersmenu at any time to remove all your filters.

If you're using integration code orcustom packagesto update asset descriptions, there may beadditional nuancesto consider since these can override either (or both) description attributes:descriptionanduserDescription.

description

userDescription

data

integration

crawl

asset-profile

Add descriptions to your assets

Add column descriptions

Search using asset descriptions
