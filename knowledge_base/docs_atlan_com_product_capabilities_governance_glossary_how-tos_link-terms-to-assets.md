# Link terms to assets
(source: https://docs.atlan.com/product/capabilities/governance/glossary/how-tos/link-terms-to-assets)

GlossaryGet StartedTerm ManagementBulk upload terms in the glossaryLink terms to assetsConceptsTroubleshootingFAQ

Get Started

Term ManagementBulk upload terms in the glossaryLink terms to assets

Bulk upload terms in the glossary

Link terms to assets

Concepts

Troubleshooting

FAQ

Build governance

Glossary

Term Management

Link terms to assets

Once you'veset up a glossary, you can link terms from your glossary to your data assets in Atlan.

Linking glossary terms with your data assets can help you:

Provide additional context for your assets to other users in your organization.

Create common definitions once and apply them many times to multiple assets.

Offer an abstract point for applyingtagsto be propagated to all linked assets   -  including their downstream and child assets   -  ifpropagation is enabled.



## Exampleâ
(source: https://docs.atlan.com/product/capabilities/governance/glossary/how-tos/link-terms-to-assets)

If your data assets include personal information   -  for example, email addresses   -  you can link your assets to anEmail Addressterm to provide context to your users.

Email Address

You can define the termEmail Addressonce in the glossary.

Email Address

You can link the term to all the columns where an individual's email address appears.

You can also tag the term asPII-  and all of the linked assets will betaggedasPII.

PII

PII



## Link terms to your assetsâ
(source: https://docs.atlan.com/product/capabilities/governance/glossary/how-tos/link-terms-to-assets)

You will first need tocreate a glossaryand add terms to it before you can link terms to your assets.

To link a term to an asset:



### From a termâ
(source: https://docs.atlan.com/product/capabilities/governance/glossary/how-tos/link-terms-to-assets)

From the left menu on any screen, clickGlossary.

UnderGlossaryin the left menu, click the name of your glossary.

Under your glossary name, click the category in which your term is nested and then click the term you would like to link to your assets.

In the term profile, next toOverview, clickLinked assets.

Click+Link Assetsto get started.Â

(Optional) In the sidebar on the right, under the search bar, click an asset type to filter your assets   -  for example,Column.

In the sidebar on the right, select the asset(s) to which you would like to link the term.

At the bottom of the sidebar, clickLink asset(s)to confirm your selections.

(Optional) UnderLinked Assets, next to the search bar, click the export icon toexport linked assetsfor terms to spreadsheets.



### From an assetâ
(source: https://docs.atlan.com/product/capabilities/governance/glossary/how-tos/link-terms-to-assets)

From the left menu on any screen, clickAssets.

On theAssetspage, select the asset to which you would like to link a term.

UnderTermsin the asset sidebar, click the+sign to add a term to your asset.

In the dialog, expand the glossary menu and then click the term you would like to link to your assets.

ClickSaveto confirm your selections.

You can now view linked assets for your glossary term! ð

You can alsoset up playbooksto automate the task of updating asset metadata, such as terms and more.



## Unlink terms from your assetsâ
(source: https://docs.atlan.com/product/capabilities/governance/glossary/how-tos/link-terms-to-assets)

To unlink a term from an asset:



### From a termâ
(source: https://docs.atlan.com/product/capabilities/governance/glossary/how-tos/link-terms-to-assets)

From the left menu on any screen, clickGlossary.

UnderGlossaryin the left menu, click the name of your glossary.

Under your glossary name, click the category in which your term is nested and then click the term you would like to unlink from your assets.

In the term profile, next toOverview, clickLinked assets.

(Optional) UnderLinked Assets, next to the search bar, click the export icon toexport linked assetsfor terms to spreadsheets before unlinking them.

UnderLinked assets, navigate to the asset(s) from which you would like to unlink the term.

To the right of the asset name, click thethree dotsand then clickUnlink asset.



### From an assetâ
(source: https://docs.atlan.com/product/capabilities/governance/glossary/how-tos/link-terms-to-assets)

From the left menu on any screen, clickAssets.

On theAssetspage, select the asset from which you would like to unlink a term.

UnderTermsin the asset sidebar, hover over the term, and in the top right of the term popover, click theunlink buttonto unlink the term from the asset.

Your assets will now be unlinked from the glossary term.

glossary

business-terms

definitions

Example

Link terms to your assets

Unlink terms from your assets
