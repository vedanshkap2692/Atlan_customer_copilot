# Use the filters menu
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

DiscoveryGet StartedAsset ManagementConfigurationConfigure language settingsHow to use the filters menuAdd custom metadataHow do I use the filters menu?ConceptsReferencesFAQ

Get Started

Asset Management

ConfigurationConfigure language settingsHow to use the filters menuAdd custom metadataHow do I use the filters menu?

Configure language settings

How to use the filters menu

Add custom metadata

How do I use the filters menu?

Concepts

References

FAQ

Use data

Discovery

Configuration

How to use the filters menu

You can refine the search for your assets in Atlan using the filters menu. Add filters to your asset search to find assets that are more relevant to you.

Once you have added filters, you can also:

Bookmark your search results with applied filters for quick access.

Copy the browser URL with applied filters and share it with other users in your organization   -  they may need to log into Atlan first to view the search results.

Export filtered assets to spreadsheetsand enrich asset metadata in bulk.

You can resize the filters panel. Hover over the edge of the panel and then click and drag the slider arrow to resize it. Atlan will remember your preferred size for the duration of your session. The panel will be returned to the default size when you log in again.

Use the following filters to help with asset disco

very. Start by either clickingAssetsin the left panel or the search bar from any screen in Atlan:



## Sourceâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

You can usesource-specificfilters to curate a list of relevant assets to search from.

To filter by a specific source:

In theFiltersmenu on the left, clickSource.

ClickChoose connectionto filter by asupported connector.

(Optional) Select an existing connection for a selected connector:ClickAll Databasesto filter by databases for a selected connection.ClickAll Schemasto filter by schemas for a selected connection.

ClickAll Databasesto filter by databases for a selected connection.

ClickAll Schemasto filter by schemas for a selected connection.



## Asset typeâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

You can filter your search results by specific types of assets. The asset type filter also includes a quick count of all the resulting assets grouped by type. You can select multiple asset types to group search results by asset types.

For example, if you would only like to view column assets:

Under the search bar on theAssetspage, click theAsset typedropdown.

From theAsset typedropdown, click theColumntab to only view column assets. Only column assets will be displayed in the results, with the tab showing a total count of the column assets.

(Optional) In theFiltersmenu on the left, underAsset Type Filters, clickColumnto add a type-specific property filter to further refine your search:ClickParent asset typeto filter columns by a parent asset type   -  tables and views.ClickParent asset nameto filter columns by the name of a table or view, or set a matching condition such as pattern match.ClickData typeto filter columns by data types.Click any of thecolumn keysto filter by column keys.

ClickParent asset typeto filter columns by a parent asset type   -  tables and views.

ClickParent asset nameto filter columns by the name of a table or view, or set a matching condition such as pattern match.

ClickData typeto filter columns by data types.

Click any of thecolumn keysto filter by column keys.

(Optional) If an asset type you're filtering for does not match the search keywords but there are other asset types that match, clickCheck other matchesto view those assets or clickClear searchto clear your search and start over.



## Domainsâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

Domainsprovide a logical way of mapping and organizing assets within a specific domain or business entity. You can filter assets by a single domain, multiple domains, or no domains.

To filter assets by domains:

In theFiltersmenu on the left, clickDomainsto expand the menu.

UnderDomains, to filter assets by domains:Check the boxes to select one or more domains or subdomains to filter your assets.ClickNo domainsto filter assets not mapped to any domain.

Check the boxes to select one or more domains or subdomains to filter your assets.

ClickNo domainsto filter assets not mapped to any domain.



## Metadata filtersâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)



### Certificateâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

You can filter your asset search based on thecertificateattached to the data assets   -Verified,Draft,Deprecated, andNo certificate.

For example, if you would only like to view verified assets:

In theFiltersmenu on the left, clickCertificateto expand the menu.

UnderCertificate, clickVerifiedto only view verified assets in your search results.Â



### Ownersâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

You can filter your asset search by selecting one or moreowners. You can also toggle between individual users and groups to filter results based on a group of users. Or, selectNo Ownersin the owners filter to view assets that currently do not have any owners and assign them if needed.

For example, if you would like to filter assets by a group of owners:

In theFiltersmenu on the left, clickOwnersto expand the menu.

UnderOwners, click thegroupicon.

Click the group name by which you want to filter your assets.



### Tagsâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

You can filter your assets by user-generatedtags, such aspublic,PII, and more. You can also selectNo Tagin the tags filter to view assets that currently do not have any tags and add them if needed.

public

PII

For example, if you would like to filter assets for a data compliance check:

In theFiltersmenu on the left, clickTagsto expand the menu.

UnderTags, click the relevant option   -  for example,PII.

PII

(Optional) Filter for assets by tags imported from supported sources:Select asynced Snowflake tagto view tagged Snowflake assets only.To filter by Snowflake tag values, next to the tag name, click the rightward arrow to open the tag value menu.In theFilter by tag valuedialog, click theSelect tag valuedropdown and then select a tag value to filter assets. You can either search by predefinedÂallowed valuesor tag values.Select asynced dbt tagto view tagged dbt Cloud or dbt Core assets only.Select asynced Databricks tagto view tagged Databricks assets only. You can also filter by Databricks tag values.

Select asynced Snowflake tagto view tagged Snowflake assets only.To filter by Snowflake tag values, next to the tag name, click the rightward arrow to open the tag value menu.In theFilter by tag valuedialog, click theSelect tag valuedropdown and then select a tag value to filter assets. You can either search by predefinedÂallowed valuesor tag values.

To filter by Snowflake tag values, next to the tag name, click the rightward arrow to open the tag value menu.

In theFilter by tag valuedialog, click theSelect tag valuedropdown and then select a tag value to filter assets. You can either search by predefinedÂallowed valuesor tag values.

Select asynced dbt tagto view tagged dbt Cloud or dbt Core assets only.

Select asynced Databricks tagto view tagged Databricks assets only. You can also filter by Databricks tag values.



### Termsâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

You can filter your asset search by terms from yourglossaries. You can also selectNo Termsin the terms filter to view assets that currently do not have any linked terms and add them if needed.

For example, if you would like find assets linked to a specific term:

In theFiltersmenu on the left, clickTermsto expand the menu.

UnderTerms, click the relevant term   -  for example,Marketing Analysis-  to discover assets linked to that term.

Marketing Analysis

(Optional) Next to the search bar in theTermsfilter, click theAdvanced optionsicon to set a matching condition. Click the operators dropdown, and then:ClickOrto filter assets that match any selected term(s).ClickAndto filter assets that match all selected terms.ClickNone ofto filter assets that do not match any of the selected term(s).ClickNot emptyto filter assets that have one or morelinked terms.ClickEmptyto filter assets without anylinked terms.

ClickOrto filter assets that match any selected term(s).

ClickAndto filter assets that match all selected terms.

ClickNone ofto filter assets that do not match any of the selected term(s).

ClickNot emptyto filter assets that have one or morelinked terms.

ClickEmptyto filter assets without anylinked terms.



### Propertiesâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

Properties offer a variety of filters to narrow down your asset search. You can filter your assets by common asset properties, such as name, description, last updated, and more.Â

To search by common asset properties:

In theFiltersmenu on the left, clickPropertiesÂ to expand the menu.

From thePropertiesmenu, you can:ClickTitleto search by the technical name oraliasof an asset. From the dialog, set your preferred matching condition (seeDescriptionfilter).ClickDescriptionto search by the description of an asset in Atlan or from the source.Â To set a matching condition, from theDescriptionÂ dialog, click the operators dropdown to:ClickEquals (=)orNot Equals (!=)to include or exclude assets through exact match search.ClickStarts WithorEnds Withto filter assets using the starting or ending sequence of values.ClickContainsto find assets with specified values contained within the property.ClickPatternto filter assets using supportedElastic DSL regular expressions.ClickIs EmptyorIs Not Emptyto filter assets with or without null values.ClickStarred assetsto filter for all yourstarred assets.ClickHas lineageto filter for assets with or withoutdata lineage.ClickHas readmeto filter for assets with or withoutREADME files.ClickHas resourcesto filter for assets with or withoutresources.ClickAnnouncementto find assets with a specificannouncementtype. From theAnnouncementdialog, click the dropdown menu to selectInformation,Issue,Warning, orNo announcement.ClickUnique identifierto find assets with a unique ID. From the dialog, select your preferred matching condition and type the relevant information.ClickQualified nameto filter by a unique name for the asset. From the dialog, select your preferred matching condition and type the relevant information (seeDescriptionfilter).ClickLast updated (in source)orLast updated (in Atlan)to find assets by when they were last updated and where. From the dialog, set the condition toBeforeorAfterand then select a date.ClickCreated (in source)orCreated (in Atlan)to find assets by when they were created and where. From the dialog, set the condition toBeforeorAfterand then select a date.ClickCreated by (Atlan)orLast updated by(Atlan)to filter assets by a user who created or last updated the asset in Atlan. From the dialog, from theSelect userdropdown, select the user name.ClickIs archivedto viewarchived assetsin the search results.

ClickTitleto search by the technical name oraliasof an asset. From the dialog, set your preferred matching condition (seeDescriptionfilter).

ClickDescriptionto search by the description of an asset in Atlan or from the source.Â To set a matching condition, from theDescriptionÂ dialog, click the operators dropdown to:ClickEquals (=)orNot Equals (!=)to include or exclude assets through exact match search.ClickStarts WithorEnds Withto filter assets using the starting or ending sequence of values.ClickContainsto find assets with specified values contained within the property.ClickPatternto filter assets using supportedElastic DSL regular expressions.ClickIs EmptyorIs Not Emptyto filter assets with or without null values.

ClickEquals (=)orNot Equals (!=)to include or exclude assets through exact match search.

ClickStarts WithorEnds Withto filter assets using the starting or ending sequence of values.

ClickContainsto find assets with specified values contained within the property.

ClickPatternto filter assets using supportedElastic DSL regular expressions.

ClickIs EmptyorIs Not Emptyto filter assets with or without null values.

ClickStarred assetsto filter for all yourstarred assets.

ClickHas lineageto filter for assets with or withoutdata lineage.

ClickHas readmeto filter for assets with or withoutREADME files.

ClickHas resourcesto filter for assets with or withoutresources.

ClickAnnouncementto find assets with a specificannouncementtype. From theAnnouncementdialog, click the dropdown menu to selectInformation,Issue,Warning, orNo announcement.

ClickUnique identifierto find assets with a unique ID. From the dialog, select your preferred matching condition and type the relevant information.

ClickQualified nameto filter by a unique name for the asset. From the dialog, select your preferred matching condition and type the relevant information (seeDescriptionfilter).

ClickLast updated (in source)orLast updated (in Atlan)to find assets by when they were last updated and where. From the dialog, set the condition toBeforeorAfterand then select a date.

ClickCreated (in source)orCreated (in Atlan)to find assets by when they were created and where. From the dialog, set the condition toBeforeorAfterand then select a date.

ClickCreated by (Atlan)orLast updated by(Atlan)to filter assets by a user who created or last updated the asset in Atlan. From the dialog, from theSelect userdropdown, select the user name.

ClickIs archivedto viewarchived assetsin the search results.

(Optional) Click the+sign to add more filtering options   -  currently only available with theTitle,Description,Unique identifier,Qualified name,Last updated(in source and Atlan), andCreated(in source and Atlan) filters.



### dbtâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

The dbt filters will only appear in the filters menu ifdbt assets have been crawled.

The dbt filters allow you to filter yourdbt Cloudanddbt Coreassets to find the most relevant results. For example, if you need to find assets from a specific project in dbt:

In theFiltersmenu on the left, clickdbtto expand the menu.

Underdbt, clickProject nameto filter by a specific project.

In theProject namedialog:Select the relevant matching condition.ForType, type the project name to filter your assets   -  for example,food-beverage.

Select the relevant matching condition.

ForType, type the project name to filter your assets   -  for example,food-beverage.

food-beverage

(Optional) Click the+sign to add more filtering options. (Note: This may not be available for all the dbt filters).



### Usageâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

The usage filters allow you tofilter your assets by usagemetadata. For example, you can:

Filter assets with zero queries and archive them.

Find costly assets to better optimize your operations.

Discover recently updated assets and follow up on the updates.Â



## Custom metadata filtersâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

You first need to set up custom metadata properties and toggle on theShow in filterslider during setup.

When youadd custom metadatain Atlan, you can also choose to set custom metadata properties as filters to help with quicker asset discovery.

For example, if you would like to filter your assets by custom user roles metadata:

In theFiltersmenu on the left, click the custom metadata filter   -  for example,Stewards.

Stewards

Under the custom metadata filter, select the custom metadata property   -  such asData Steward.

Data Steward

In the property dialog, select the matching condition and user to filter your assets.

(Optional) Forcustom metadata option propertiesonly:You can either:For custom metadata properties with five or fewer options, click the operators dropdown.For custom metadata properties with more than five options, next to the search bar, click theAdvanced optionsicon and then click the operators dropdown.From the operators dropdown, you can:ClickOrto filter assets that match any selected value(s).ClickAndto filter assets that match all selected values   -  only supported ifmultiple values are allowedfor custom metadata options.ClickNone ofto filter assets that do not match any of the selected value(s)   -  only supported ifmultiple values are allowedfor custom metadata options.ClickNot emptyto filter assets that have one or more assigned values for the selected property.ClickEmptyto filter assets without any assigned values for the selected property.

You can either:For custom metadata properties with five or fewer options, click the operators dropdown.For custom metadata properties with more than five options, next to the search bar, click theAdvanced optionsicon and then click the operators dropdown.

For custom metadata properties with five or fewer options, click the operators dropdown.

For custom metadata properties with more than five options, next to the search bar, click theAdvanced optionsicon and then click the operators dropdown.

From the operators dropdown, you can:ClickOrto filter assets that match any selected value(s).ClickAndto filter assets that match all selected values   -  only supported ifmultiple values are allowedfor custom metadata options.ClickNone ofto filter assets that do not match any of the selected value(s)   -  only supported ifmultiple values are allowedfor custom metadata options.ClickNot emptyto filter assets that have one or more assigned values for the selected property.ClickEmptyto filter assets without any assigned values for the selected property.

ClickOrto filter assets that match any selected value(s).

ClickAndto filter assets that match all selected values   -  only supported ifmultiple values are allowedfor custom metadata options.

ClickNone ofto filter assets that do not match any of the selected value(s)   -  only supported ifmultiple values are allowedfor custom metadata options.

ClickNot emptyto filter assets that have one or more assigned values for the selected property.

ClickEmptyto filter assets without any assigned values for the selected property.



## Asset type filtersâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

You can choose from two different sets of filters   -  type-specific or connector-specific.



### Type-specific filtersâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

If you'refiltering by a specific asset type, you can select type-specific property filters to further refine your search. For example, if you're filtering by:

Tables or views   -  you can filter these asset types by a specific row or column count.

Columns   -  you can filter column assets by parent asset type and name, data type, orcolumn keys.

Process   -  you can filterprocess assetsby the SQL query.

Query   -  you can filter saved queries byvisual queries.



### Connector-specific filtersâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/use-the-filters-menu)

Connector-specific filters will appear in the filters menu only if there are crawled assets for a supported source and asset-type filters specific to the connector are applied.

Connector-specific filters are currently supported for the following sources:

Anomalo

Apache Kafka,Confluent Kafka,Aiven Kafka,Redpanda Kafka, andAmazon MSK

Apache Airflow/OpenLineage,Amazon MWAA,Astronomer,Google Cloud Composer, andApache Spark

Google BigQuery

Matillion

Microsoft Azure Cosmos DB

Microsoft Azure Event Hubs

Microsoft Power BI

MicroStrategy

MongoDB

Monte Carlo

Redash

Salesforce

Sisense

Snowflake

Soda

Tableau

ThoughtSpot

Qlik Sense CloudandQlik Sense Enterprise on Windows

Google Cloud Storagebuckets and objects

Microsoft Azure Data Lake Storageaccounts, containers, and objects

Presetdatasets, dashboards, and workspaces

APIpaths

Files-  supported file types include DOC, Excel, PPT, CSV, TXT, JSON, XML, and ZIP files

To use a connector-specific filter:

From theAssetspage, click theAsset typefilter, and then from the dropdown, select an asset type from a supported connector   -  in this example, we'll select SodaChecks.

In theFiltersmenu on the left, click theSodafilter to expand the menu.

From theSodafilter menu, filter your Soda checks by check status, owner, or last scanned at date.

(Optional) For properties that allow selecting multiple values, you can set your preferred matching condition. Click the operators dropdown and then:ClickOrto filter assets that match any selected value(s).ClickAndto filter assets that match all selected values.ClickNone ofto filter assets that do not match any selected value(s).ClickNot emptyto filter assets that have one or more assigned values for the selected property.ClickEmptyto filter assets without any assigned values for the selected property.

ClickOrto filter assets that match any selected value(s).

ClickAndto filter assets that match all selected values.

ClickNone ofto filter assets that do not match any selected value(s).

ClickNot emptyto filter assets that have one or more assigned values for the selected property.

ClickEmptyto filter assets without any assigned values for the selected property.

data

integration

Source

Asset type

Domains

Metadata filters

Custom metadata filters

Asset type filters
