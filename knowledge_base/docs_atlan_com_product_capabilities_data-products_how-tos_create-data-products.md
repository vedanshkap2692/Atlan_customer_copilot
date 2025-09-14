# Create data products
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

Data ProductsGet StartedStakeholder ManagementProduct ManagementCreate data productsDomain ManagementConcepts

Get Started

Stakeholder Management

Product ManagementCreate data products

Create data products

Domain Management

Concepts

Configure Atlan

Data Products

Product Management

Create data products

âAvailable via the Data Marketplace package

Before you can create a data product, you need your Atlan admin toenable the products module in your Atlan workspace. Once enabled, first review theorder of operations. You need to have create, update, and delete permissions throughdomain policiesfor the specific domain or subdomain to create and manage data products.

Data products help your data consumers easily discover and work with data assets. As you get started, here are some questions to consider:

What use case(s) are you trying to solve as an organization?

How to define a common vocabulary and approach for creating data products and ensuring interoperability across domains?

How to design data products to power discovery and drive usage among data consumers?

Data products in Atlan can be highly adaptable to the needs of your organization.



## Create a data productâ
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

You can either create a data product from the products module or lineage graph.

To create a data product, complete these steps.



#### From the products module:â
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

From the left menu of any screen in Atlan, clickProducts.

To select a domain or subdomain, you can either:From the navigation menu on theProductshomepage, use the search bar or select the relevant domain or subdomain.From the top right ofDiscover domains, select your data domain of interest. If you cannot find your data domain, click theSee allbutton to view more domains.

From the navigation menu on theProductshomepage, use the search bar or select the relevant domain or subdomain.

From the top right ofDiscover domains, select your data domain of interest. If you cannot find your data domain, click theSee allbutton to view more domains.

In the upper right of your data domain or subdomain page, click the+ Addbutton, and then from the dropdown, clickNew productto add a new data product.



#### From the lineage graph:â
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

From the left menu of any screen in Atlan, clickAssets.

(Optional) In theFiltersmenuon the left, expand thePropertiesmenu and then clickHas lineageto filter for assets with data lineage.

Select an asset, and from the top right of the asset card, click theView lineageicon to open the lineage graph.

On the lineage graph, select an asset to create a data product. Atlan will only include assets that are visible on the lineage graph. To include more assets:(Optional) Hover over the+button to the right of any asset and then click theExpand allbutton to include assets further upstream or downstream horizontally in the data product.(Optional) ClickShow allto include assets further upstream or downstream assets vertically in the data product.

(Optional) Hover over the+button to the right of any asset and then click theExpand allbutton to include assets further upstream or downstream horizontally in the data product.

(Optional) ClickShow allto include assets further upstream or downstream assets vertically in the data product.

From the top right of the lineage graph, click thebox with plus iconfor data products to create a data product from the lineage graph.

In theNew product via lineageform, configure the following:ForAdd assets, any assets that are visible on the lineage graph will be automatically included in the data product. Note thatprocess, child, andpartialassets are currently not supported for data product creation from the lineage graph. You can either keep all the asset selections or deselect any assets.(Optional) The asset you had selected on the lineage graph will be automatically set as an output port. You can keep that selection, clickOutput portto remove the current selection, or clickMark as output porton any other assets to set additional output ports.ClickContinueto proceed.

ForAdd assets, any assets that are visible on the lineage graph will be automatically included in the data product. Note thatprocess, child, andpartialassets are currently not supported for data product creation from the lineage graph. You can either keep all the asset selections or deselect any assets.

(Optional) The asset you had selected on the lineage graph will be automatically set as an output port. You can keep that selection, clickOutput portto remove the current selection, or clickMark as output porton any other assets to set additional output ports.

ClickContinueto proceed.



### Provide detailsâ
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

To provide details:

(Optional) ForCover, click theChangebutton to select an image from the gallery or upload an image of your own. ClickRepositionto drag and reposition the cover image and then clickSave positionto save your preferences.

ForName, enter a meaningful name for your data product   -  for example,Social Media Marketing. The character limit for a product name is 80 characters.

Social Media Marketing

ForDomain, select a data domain from the dropdown   -  for example,Customer Service.

Customer Service

(Optional) ForDescription, enter a description for your domain.

(Optional) ForCriticality, select a level of business criticality from the dropdown   -  choose fromHigh,Medium, andLow.

(Optional) ForSensitivity, assign a data sensitivity level from the dropdown   -  choose fromPublic,Internal, andConfidential.

(Optional) ForOwners, assign additional users or groups as data product owner.

(Optional) ForVisibility, select who can access and monitor the data product throughout its entire lifecycle:Private to members of this domain-  only members of a specific domain can access the data product.Private to selected members-  only members of a specific domain and other selected users or groups can access the data product.Public-  everyone in the organization can access the data product.

Private to members of this domain-  only members of a specific domain can access the data product.

Private to selected members-  only members of a specific domain and other selected users or groups can access the data product.

Public-  everyone in the organization can access the data product.

If creating a data product from the products module, in the top right of the screen, click theContinuebutton. If creating a data product from the lineage graph, at the bottom of the form, click theContinuebutton and skip to the Review the data product section.



### Add assetsâ
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

To select assets to include in the data product, you can select via the asset browser or using filters.



#### Add via browserâ
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

Click the checkbox to select individual assets to include in your data product.

(Optional) Use the search bar to search for assets by the technical name of the asset.

(Optional) Filter assets by specific asset types. Click the 3-dot icon to view more asset type filters.

(Optional) Click theShow: alldropdown and change toSelected assetsto only view your asset selection.

(Optional) Click theAll filtersdropdown, and then from theAll filterspane:ClickHierarchyto filter assets by connection, database, and schema.ClickCertificateto filter assets bycertification status.ClickOwnersto filter assets byasset owners.ClickTagsto filter assets by yourtagsin Atlan, includingimported tags.ClickTermsto filter assets bylinked terms.ClickPropertiesto filter assets bycommon asset properties.

ClickHierarchyto filter assets by connection, database, and schema.

ClickCertificateto filter assets bycertification status.

ClickOwnersto filter assets byasset owners.

ClickTagsto filter assets by yourtagsin Atlan, includingimported tags.

ClickTermsto filter assets bylinked terms.

ClickPropertiesto filter assets bycommon asset properties.

In the top right of the screen, click theContinuebutton.



#### Add via rulesâ
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

UnderSelect assets, clickAdd via filtersto add assets to your data product using asset filters.

To set a matching condition for the filters, selectMatch allorMatch any.Match allwill logicallyANDthe criteria, whileMatch anywill logicallyORthe criteria.

AND

OR

ForAttributes, select a relevant option:ClickConnectionand then select an existing connection. (Optional) To further refine your asset selection:ClickAll databasesto filter by databases in a selected connection.ClickAll schemasto filter by schemas in a selected connection.ClickConnectorto filter assets bysupported connectors.ClickAsset typeto filter by specific asset types   -  for example, tables, columns, queries, glossaries, and more.ClickCertificateto filter assets bycertification status.ClickOwnersto filter assets byasset owners.ClickTagsto filter assets by yourtagsin Atlan, includingimported tags.ClickGlossary, terms, & categoriesto filter by a specificglossaryorcategoryto bulk update all the nested terms or by multiple glossaries and categories.ClickLinked termsto filter assets bylinked terms.ClickSchema qualified Nameto filter assets by the qualified name of a given schema.ClickDatabase qualified Nameto filter assets by the qualified name of a given database.Clickdbtto filter assets by dbt-specific filters and then select adbt Cloudordbt Corefilter.ClickPropertiesto filter assets bycommon asset properties.ClickUsageto filter assets byusage metrics.ClickMonte Carloto filter assets byMonte Carlo-specific filters.ClickSodato filter assets bySoda-specific filters.ClickTable/Viewto filter tables or views by row count, column count, or size.ClickColumnto filter columns bycolumn-specific filters, including parent asset type or name, data type, orcolumn keys.ClickProcessto filterlineage processesby the SQL query.ClickQueryto filter assets by associatedvisual queries.ClickMeasureto filterMicrosoft Power BI measuresusing the external measures filter.

ClickConnectionand then select an existing connection. (Optional) To further refine your asset selection:ClickAll databasesto filter by databases in a selected connection.ClickAll schemasto filter by schemas in a selected connection.

ClickAll databasesto filter by databases in a selected connection.

ClickAll schemasto filter by schemas in a selected connection.

ClickConnectorto filter assets bysupported connectors.

ClickAsset typeto filter by specific asset types   -  for example, tables, columns, queries, glossaries, and more.

ClickCertificateto filter assets bycertification status.

ClickOwnersto filter assets byasset owners.

ClickTagsto filter assets by yourtagsin Atlan, includingimported tags.

ClickGlossary, terms, & categoriesto filter by a specificglossaryorcategoryto bulk update all the nested terms or by multiple glossaries and categories.

ClickLinked termsto filter assets bylinked terms.

ClickSchema qualified Nameto filter assets by the qualified name of a given schema.

ClickDatabase qualified Nameto filter assets by the qualified name of a given database.

Clickdbtto filter assets by dbt-specific filters and then select adbt Cloudordbt Corefilter.

ClickPropertiesto filter assets bycommon asset properties.

ClickUsageto filter assets byusage metrics.

ClickMonte Carloto filter assets byMonte Carlo-specific filters.

ClickSodato filter assets bySoda-specific filters.

ClickTable/Viewto filter tables or views by row count, column count, or size.

ClickColumnto filter columns bycolumn-specific filters, including parent asset type or name, data type, orcolumn keys.

ClickProcessto filterlineage processesby the SQL query.

ClickQueryto filter assets by associatedvisual queries.

ClickMeasureto filterMicrosoft Power BI measuresusing the external measures filter.

ForOperator, selectIs one offor values to include orIs notfor values to exclude. Depending on the selected attribute(s), you can also choose fromadditional operators:SelectEquals (=)orNot Equals (!=)to include or exclude assets through exact match search.SelectStarts WithorEnds Withto filter assets using the starting or ending sequence of values.SelectContainsorDoes not containto find assets with or without specified values contained within the attribute.SelectPatternto filter assets using supportedElastic DSL regular expressions.SelectIs emptyto filter assets with null values.

SelectEquals (=)orNot Equals (!=)to include or exclude assets through exact match search.

SelectStarts WithorEnds Withto filter assets using the starting or ending sequence of values.

SelectContainsorDoes not containto find assets with or without specified values contained within the attribute.

SelectPatternto filter assets using supportedElastic DSL regular expressions.

SelectIs emptyto filter assets with null values.

ForValues, select the relevant values. The values will vary depending on the selected attributes.

(Optional) To add more filters, clickAdd filterand selectFilterto add individual filters orFilterGroupto nest more filters in a group.

(Optional) To view all the assets that match your rules, in theFilterscard, clickViewassetsfor a preview.

In the top right of the screen, click theContinuebutton.



### (Optional) Select output portsâ
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

Output ports determine the relationships between your data products. These relationships are visually represented asbusiness lineage.

To select output ports:

From the list of assets, select output port(s) to allow your data consumers to consume the data product across domains. These assets will serve as the consumption layer for your data product.

ForInput ports, Atlan displays a total count of input ports for your data product. These assets are designated as output ports in other data products, and serve as input ports for your data product. ClickView assetsto view all input port assets.

In the top right of the screen, click theContinuebutton.



### Review the data productâ
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

Once you have reviewed your data product, you can either:

ClickSave as draftto save your changes in a draft version and publish when ready. Only you and any other users you add asownersto the product will be able to search for, view, and edit your draft products, depending on theirpermissions.

ClickCreate and publishto publish it immediately.

Congrats on creating a data product in Atlan! ð

You can also usegovernance workflowsto govern the creation and change in status of data products.



## Update a data productâ
(source: https://docs.atlan.com/product/capabilities/data-products/how-tos/create-data-products)

You canmove your data productswithin and across subdomains or domains to reorganize them as needed.

Once you have created a data product, you will also need to monitor and manage it during its entire lifecycle. This helps ensure that the data product stays fresh, up-to-date, and trustworthy. The data product profile in Atlan allows you to curate how your users can use the data product.

To update a data product:

From the left menu of any screen in Atlan, you can either:ClickProducts. To select a data product, you can:From the navigation menu on theProductshomepage, use the search bar or expand the relevant domain or subdomain.In theData productssection, select a trending or recently viewed data product. The list ofTrending productsis sorted by the total count of views on each product, with the most viewed product listed at the top.From the top right of any screen in Atlan, click thestar icon. From theStarred assetspopup, select a starred data product.From the left navigation menu orProductshomepage, clickMy draftsto continue working on your draft products. Products in draft mode are only visible to product owners until these are published.If your Atlan admin hasenabled theShow products in asset discoverytoggle, clickAssetsto search for data products fromasset discovery.

ClickProducts. To select a data product, you can:From the navigation menu on theProductshomepage, use the search bar or expand the relevant domain or subdomain.In theData productssection, select a trending or recently viewed data product. The list ofTrending productsis sorted by the total count of views on each product, with the most viewed product listed at the top.From the top right of any screen in Atlan, click thestar icon. From theStarred assetspopup, select a starred data product.From the left navigation menu orProductshomepage, clickMy draftsto continue working on your draft products. Products in draft mode are only visible to product owners until these are published.

From the navigation menu on theProductshomepage, use the search bar or expand the relevant domain or subdomain.

In theData productssection, select a trending or recently viewed data product. The list ofTrending productsis sorted by the total count of views on each product, with the most viewed product listed at the top.

From the top right of any screen in Atlan, click thestar icon. From theStarred assetspopup, select a starred data product.

From the left navigation menu orProductshomepage, clickMy draftsto continue working on your draft products. Products in draft mode are only visible to product owners until these are published.

If your Atlan admin hasenabled theShow products in asset discoverytoggle, clickAssetsto search for data products fromasset discovery.

On your data domain page, next to theOverviewtab, click theProductstab and select your data product of interest.(Optional) From the top right of the product profile, click thePublisheddropdown to update the status of your data product:Draft-  data product is only visible to product owners.Published-  data product is published for users to consume.Sunset-  data product is planned for retirement.Archived-  data product is archived and no longer visible to users. To restore an archived data product, click theRestore productbutton and then clickRestore. Atlan will restore the archived data product and it will reappear in product and asset discovery, domain profile, and product lineage.UnderSummary, view details about the data domain your data product belongs to, including criticality, sensitivity, and freshness.(Optional) Click the pencil icon to updateCriticalityto signify business impact:High-  high business impact_Medium   - _ moderate business impactLow-  internal or a non-business impact(Optional) Click the pencil icon to updateSensitivityto assign a data classification:Public-  may be freely accessibleInternal-  may only be distributed within the organizationConfidential-  may only be limited to a specific domain or team within the organization(Optional) ClickAdd resourcetoadd a resourceto your asset.UnderProduct Score, view ascorecardfor your data product, calculated based on metadata completeness.UnderAt A Glance, view a total count of linked assets and output ports.UnderReadme, click+ Addtoadd a READMEto your data product oruse Atlan AI for documentation.UnderDetails, you can view and update metadata for your data product   -  including visibility,terms,owners,tags,certificates, andcustom metadata. You can alsoset up playbooksto update product metadata in bulk.

(Optional) From the top right of the product profile, click thePublisheddropdown to update the status of your data product:Draft-  data product is only visible to product owners.Published-  data product is published for users to consume.Sunset-  data product is planned for retirement.Archived-  data product is archived and no longer visible to users. To restore an archived data product, click theRestore productbutton and then clickRestore. Atlan will restore the archived data product and it will reappear in product and asset discovery, domain profile, and product lineage.

Draft-  data product is only visible to product owners.

Published-  data product is published for users to consume.

Sunset-  data product is planned for retirement.

Archived-  data product is archived and no longer visible to users. To restore an archived data product, click theRestore productbutton and then clickRestore. Atlan will restore the archived data product and it will reappear in product and asset discovery, domain profile, and product lineage.

UnderSummary, view details about the data domain your data product belongs to, including criticality, sensitivity, and freshness.(Optional) Click the pencil icon to updateCriticalityto signify business impact:High-  high business impact_Medium   - _ moderate business impactLow-  internal or a non-business impact(Optional) Click the pencil icon to updateSensitivityto assign a data classification:Public-  may be freely accessibleInternal-  may only be distributed within the organizationConfidential-  may only be limited to a specific domain or team within the organization(Optional) ClickAdd resourcetoadd a resourceto your asset.

(Optional) Click the pencil icon to updateCriticalityto signify business impact:High-  high business impact_Medium   - _ moderate business impactLow-  internal or a non-business impact

High-  high business impact

_Medium   - _ moderate business impact

Low-  internal or a non-business impact

(Optional) Click the pencil icon to updateSensitivityto assign a data classification:Public-  may be freely accessibleInternal-  may only be distributed within the organizationConfidential-  may only be limited to a specific domain or team within the organization

Public-  may be freely accessible

Internal-  may only be distributed within the organization

Confidential-  may only be limited to a specific domain or team within the organization

(Optional) ClickAdd resourcetoadd a resourceto your asset.

UnderProduct Score, view ascorecardfor your data product, calculated based on metadata completeness.

UnderAt A Glance, view a total count of linked assets and output ports.

UnderReadme, click+ Addtoadd a READMEto your data product oruse Atlan AI for documentation.

UnderDetails, you can view and update metadata for your data product   -  including visibility,terms,owners,tags,certificates, andcustom metadata. You can alsoset up playbooksto update product metadata in bulk.

Switch to theAssetstab to view linked assets.(Optional) Click theEditbutton to add or remove assets from your data product.(Optional) Select an asset to view its asset profile in a sidebar.(Optional) Filter assets by asset types   -  for example, use theTablefilter to view table assets only.(Optional) ClickDisable as output portto remove an output port or clickSet as output portto set an asset as an output port.

(Optional) Click theEditbutton to add or remove assets from your data product.

(Optional) Select an asset to view its asset profile in a sidebar.

(Optional) Filter assets by asset types   -  for example, use theTablefilter to view table assets only.

(Optional) ClickDisable as output portto remove an output port or clickSet as output portto set an asset as an output port.

Switch to theLineagetab to viewbusiness lineagefor your data product.Hover over any data product to view the metadata popover for more context.Click theview output portsmenu to view output ports for your data product.In the upper right of the lineage graph, click thedownward arrowto download an image of the product lineage graph.

Hover over any data product to view the metadata popover for more context.

Click theview output portsmenu to view output ports for your data product.

In the upper right of the lineage graph, click thedownward arrowto download an image of the product lineage graph.

Switch to theActivitytab to view theactivity logfor your data product.View details about changes made to the data product andfilter for specific types of metadata changes.View top and recent users for your data product.View a list of data producers for your data product.

View details about changes made to the data product andfilter for specific types of metadata changes.

View top and recent users for your data product.

View a list of data producers for your data product.

Switch to theContractstab to view anylinked contractsfor the output ports in your data product.

From the top right of the data product profile:Click the user avatars to view a list of recently visited users, total views on your asset, total number of unique visitors, and total views by user.Use the days filter to filter asset views and user activity in the last 7, 30, and 90 days.This feature is turned on by default   -  admins canturn off user activity.Click the star button tostar your data productand bookmark it for easy access.Click theSlackorTeamsicon to post on aSlackorMicrosoft Teamschannel.Click the 3-dot icon toadd an announcementor aresourceto your data product.

Click the user avatars to view a list of recently visited users, total views on your asset, total number of unique visitors, and total views by user.Use the days filter to filter asset views and user activity in the last 7, 30, and 90 days.This feature is turned on by default   -  admins canturn off user activity.

Use the days filter to filter asset views and user activity in the last 7, 30, and 90 days.

This feature is turned on by default   -  admins canturn off user activity.

Click the star button tostar your data productand bookmark it for easy access.

Click theSlackorTeamsicon to post on aSlackorMicrosoft Teamschannel.

Click the 3-dot icon toadd an announcementor aresourceto your data product.

If you have enriched your draft products withtermsortags, your draft products will be visible to other users as linked assets when viewed from the term or tag profile, respectively. However, only a product owner with the requisite permissions to update the product can make any changes to the draft product.

To programmatically create, update, and manage data products using API, refer to ourdeveloper documentation.

lineage

data-lineage

impact-analysis

Create a data product

Update a data product
