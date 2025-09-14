# Discovery FAQs
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

DiscoveryGet StartedAsset ManagementConfigurationConceptsReferencesFAQDiscovery FAQs

Get Started

Asset Management

Configuration

Concepts

References

FAQDiscovery FAQs

Discovery FAQs

Use data

Discovery

FAQ

Discovery FAQs



## How does Atlan handle archived or deleted assets?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

If anasset is removed from a workflowor auser loses permissionsto an asset, the asset will bearchivedin Atlan. The asset will be unarchived with all the metadata intact if it isincludedin the next workflow run or users permissions are restored.

In Atlan, an asset'stypenameandqualifiedNamepair serves as a distinctive identifier. ThequalifiedNameis a string that has been concatenated and contains the asset's source, host, and hierarchy. The related asset in Atlan will not change unless a modification is made, such as changing the schema or table name.

typename

qualifiedName

qualifiedName



## Is it possible to search for fields across all data sources?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

If you know exactly what you're looking for, Atlan suggests using exact match search. Wrap the search terms within double quotation marks" "when typing it in the search bar. For example,"instacart_total_users".

" "

"instacart_total_users"

Forcontextual search, theAssetspage provides anumber of filtersto help you narrow down your search results. Filter data assets by various properties, asset types, and so on.

The search results in Atlan also provide a quick count of all the resulting data assets, organized by asset type. These counts will alter in real time as you apply filters.



## What is included in the "All assets" view?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

TheAll assetsview includesallassets in your Atlan data estate.

If your Atlan admin has turned offView "All assets" in Assets Discoveryfrom Labs in the admin center, you may be unable to see this view. In that case, you'll only be able to view the assets curated for the persona(s) or purpose(s) you belong to in Atlan. Admin users will still have full access to all assets, even when this default behavior is turned off.



## Can I search by a value to find assets with that value?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Atlan allows you to search and discover metadata, not data.

As a constantly updated data catalog of all your data assets and metadata, Atlan allows you to identify andaccess your data assetsas well as thetribal knowledge and business contextassociated with them. The powerful, intelligent search returns relevant search results.



## Why do I not see more results when searching with the search bar (or Cmd + K)?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

The search bar is meant to be a quick search option. It works best when you know the name of the asset. As such, it only loads 20 search results at a time. You can also quickly access yourrecently visitedstarred assetsfrom the search bar.

For more in-depth discovery,search from theAssetspage:

More results

Additional filters



## What is the timezone for data display?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

For asset properties such asLast updated (in Atlan),Last synced with source, orCreated (in Atlan), the timestamps are displayed in local timezones based on the user's browser location. To learn more, seeHow to interpret timestamps.



## Asset Profile FAQsâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)



### Can we replace or rename existing assets?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

The expected behavior will vary based on thesupported connectorand asset type. If the asset name is reflected in thequalifiedNameof the asset and you rename the asset, Atlan will create a net-new asset. This is because thequalifiedNamedeterminesasset uniquenessin Atlan.

qualifiedName

qualifiedName

Consider the following examples:

The name of a Snowflake table is part of itsqualifiedName. Any changes to the table name in Snowflake will result in a newqualifiedName, and thus the creation of a new asset in Atlan.

qualifiedName

qualifiedName

Conversely, thequalifiedNameof Microsoft Power BI reports are based on the UUIDs of the assets in Microsoft Power BI   -  no names are embedded. In this case, renaming a Microsoft Power BI report does not change its UUID in Microsoft Power BI. This means that thequalifiedNameof that report in Atlan will remain unchanged. Atlan will simply update the existing asset. However, this may not be the case where a Microsoft Power BI table is concerned, as the table name is included in thequalifiedNameof the asset.

qualifiedName

qualifiedName

qualifiedName

If your use case is to enable quick discovery in Atlan, consideradding a business-friendly aliasto the asset.



### What is an activity log?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

The activity log in the asset sidebar provides a changelog for your data assets. Having a record of all the changes made to an asset can help build trust in your data assets and promote transparency across your organization.



#### View the activity log of an assetâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

To view the activity log of an asset:

From the left menu of any screen in Atlan, clickAssets.

Click on an asset to view its asset profile.

From the asset sidebar to the right, click theActivitytab to view the activity log.

If an asset was updated fromGoogle SheetsorMicrosoft Excel, anUpdated using Google SheetsorUpdated using Microsoft Excelstamp will appear, respectively. (Optional) Click theGoogle SheetsorMicrosoft Excellink to view the source spreadsheet.

(Optional) To filter the activity log by a specific type of activity, underActivity, click the dropdown arrow and then:ClickAliasto viewalias activityby user and timestamp of update.ClickDescriptionto view any changes in thedescriptionof an asset.ClickStarredto viewstarred activityby user and timestamp.ClickAnnouncementto view any changes to theannouncementon an asset.ClickTermsto view any updates on linkedterms.ClickCertificateto view any changes in thecertification statusof an asset.ClickOwnersto view any changes to theownershipof an asset.ClickTag AddedorTag Removedto view any changes fortags directly addedto an asset.ClickTag Added (Propagation)orTag Removed (Propagation)to view any changes fortags propagatedto an asset.ClickColumn Added,Column Deleted, orColumn Updatedto view column changes.ClickReadme AddedorReadme Updatedto view when aREADME was createdfor an asset and which user created or updated it.

ClickAliasto viewalias activityby user and timestamp of update.

ClickDescriptionto view any changes in thedescriptionof an asset.

ClickStarredto viewstarred activityby user and timestamp.

ClickAnnouncementto view any changes to theannouncementon an asset.

ClickTermsto view any updates on linkedterms.

ClickCertificateto view any changes in thecertification statusof an asset.

ClickOwnersto view any changes to theownershipof an asset.

ClickTag AddedorTag Removedto view any changes fortags directly addedto an asset.

ClickTag Added (Propagation)orTag Removed (Propagation)to view any changes fortags propagatedto an asset.

ClickColumn Added,Column Deleted, orColumn Updatedto view column changes.

ClickReadme AddedorReadme Updatedto view when aREADME was createdfor an asset and which user created or updated it.

(Optional) Click theFilter by columnmenu to filter your activity logs by specific columns.

You can now view all the changes that were made to an asset in the activity log! ð

Activity logs for metadata changes are persisted throughout the lifecycle of the Atlan instance for your organization.



### Why do dbt descriptions keep getting deleted?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

If you notice that the descriptions from a Snowflake table, for example, get deleted when dbt is your source of truth, it is likely that you have the data source scheduled to run after the dbt run. Atlan recommends following the order of operations as documented inHow to order workflows.

You can also use dbt'spersist_docsfeature to ensure that your metadatapersists through workflow runs.

persist_docs



### What is the timeframe for recently verified assets?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Atlan displays up to 20 most recently verified assets at a time in theRecently verified assetssection on your Atlan homepage. You can scroll down further and clickLoad moreto view more recently verified assets. This is not based on any particular timeline. In fact, this list may include assets that were updated as long as a week ago, if no new assets were verified more recently.



### What signals Atlan to auto-add the deprecated certifications in Looker?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

These certifications are sourced from Looker. Once theLooker crawlerhas run successfully and detected that an asset was deleted, Atlan will attached aDeprecatedcertificate to the asset because it no longer exists at source. For example:

If tiles are deleted, the API response generated is titledLook Deleted. In this case, Atlan will add the deprecated certificate.

If Atlan crawls any models that do not have a project associated with them (indicated by a missingproject_namekey in the model API response), Atlan adds a deprecated certificate to the asset.

project_name



### Is it possible to add PDFs to an asset README?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Atlan currently does not support embedding a PDF file in an asset README. Alternatively, PDF files can belinked as a resource.



### How does version control work for description changes in source tools vs. Atlan?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Considering that users may update metadata in Atlan and the source tool, Atlanmanages descriptions in two fields-  populating either or both depending on where it was created or updated. This is the format Atlan follows:

Source descriptions are stored in thedescriptionfield

description

Any description added or updated in Atlan is stored in theuserDescriptionfield

userDescription

Separating them into two fields ensures that the connection package does not override the descriptions entered by users in Atlan every time the workflow runs and updates the asset. This way, the description field in Atlan becomes the source of truth.

There is one exception though. If the description field has not been edited at all in Atlan and the connection package only ever brings the descriptions from the source, the workflow will keep updating the description field with what is available at source   -  only source edits will come through.

Once thedescriptionfield is edited in Atlan, theuserDescriptionfield takes over. If you would like to restore the original source description, simply clear the description added in Atlan and it will automatically revert to the source description.

description

userDescription

As a best practice, we recommend all subsequent edits to the description be done in Atlan.

This is valid across all connector workflows.



### Can Atlan track schema changes?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Atlan tracks schema changes for SQL sources, which can be viewed in theactivity logof an asset. However, Atlan is not a schema registry or a data modeling tool such as dbt.



### Are different fonts supported for READMEs and descriptions?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Atlan currently does not support customizing the following for assetdescriptions,READMEs, andREADME templates:

Fonts

Font sizes

Font colors



### Can Atlan handle assets with a large number of rows and columns?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

You can safely catalog your assets in Atlan, regardless of the number of rows or columns. Since Atlan only extracts metadata, data volume is not a consideration. Note that if an asset has a large number of columns, thecolumn previewin the asset profile may take some time to load.



### Why do I not see any tables or columns under database, only schema?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

If you're viewing related assets for databases from theRelationstab in the asset sidebar, Atlan will only display schemas. You can click the schema asset and then open theRelationstab of the schema to view tables and views.

To find tables and views contained within a database, Atlan also recommends using thedatabase asset type filterfor quick discovery.



### Is the sample data preview cached?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

When previewing sample data on any asset, Atlan retrieves the sample data from source each time. No data is cached in Atlan.



### Delete an assetâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Have one or more assets in Atlan that you don't want to be there? You have several options for removing them.



#### Specific assetsâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

To remove targeted, specific assetsuse one of our SDKs or our open API.



#### Set of related assetsâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

To remove a set of related assets, such as an entire schema:

Modify the connector's configurationwith a filter to exclude the asset(s).

Re-run the connector's workflow with the new configuration.

This willarchivethe schema and its assets.



#### An entire connection's assetsâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

To remove an entire connection and all its assets, seeHow to delete a connection.



### If an asset is deleted via API, will workflows recreate the asset on the next run?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

If you delete an asset at source, Atlan willarchivethat asset in the next crawler run. Atlan recommends that you manage additions or deletions through source workflows. Considering that Atlan workflows run differential crawls, any changes to your assets will be reflected in subsequent crawler runs. This helps deliver faster runtimes and improves workflow performance.

If you delete an asset using APIs, there can be two scenarios:

Archived:Assets are soft-deleted, moving to anArchivedstate.The next workflow run will restore the asset only if any changes are made to any of its source metadata properties   -  for example, a new column was added.You can alsorestore archived assets.

Assets are soft-deleted, moving to anArchivedstate.

The next workflow run will restore the asset only if any changes are made to any of its source metadata properties   -  for example, a new column was added.

You can alsorestore archived assets.

Hard-deleted:The asset is completely removed from the metastore.The next workflow run creates a new asset if the previously deleted asset is still present or reintroduced in the source system. For example, this can happen if the asset was never actually removed from the source or if it was deleted and later recreated. However, the newly created asset doesn't retain any of its original Atlan metadata.Youcan'trestore hard-deleted assets.

The asset is completely removed from the metastore.

The next workflow run creates a new asset if the previously deleted asset is still present or reintroduced in the source system. For example, this can happen if the asset was never actually removed from the source or if it was deleted and later recreated. However, the newly created asset doesn't retain any of its original Atlan metadata.

Youcan'trestore hard-deleted assets.

Atlan recommends the deletion of assets to be managed by source workflows. The delete and restore endpoints are generally meant for assets created via APIs.



### Add a READMEâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

A README is an essential part of every code repository. The better the README, the more collaborators will want to work on your code. The same holds true for your data assets.

Each data asset should have its own README, which provides a description of its characteristics and other critical information. Atlan allows users to add a README for every data asset, using an intuitive, rich text editor.

You can document the tribal knowledge associated with each data asset in a README and reduce dependencies on your team members. The README appears right below each data table in the asset profile, displaying the data and the metadata on the same page and bridging the gap between the two.

Atlan currently supports the following file types for asset READMEs:

Google Docs

Google Sheets

Google Slides

Miro boards

FigJam boards

Lucidchart

dbdiagram

ERD Lab

Microsoft Word

Microsoft Excel

Microsoft PowerPoint

Google Data Studio

Google Looker Studio

Canva



#### Add a READMEâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

A README can be added to different types of data assets in Atlan, including BI dashboards, widgets, columns, databases, and schemas.

The character limit for READMEs is 100,000 characters. A portion of this limit is used to ensure compatibility with rich text formatting, slightly reducing the available character limit.

To add a README to an asset, follow these steps:

On the Atlan homepage, clickAssetsin the left menu.

Click on an asset to view its asset profile.

In theReadmesection of the asset profile, click+Add.

You can either:ClickBlank Pageto create a new README from scratch.ClickUseto select anexisting templateas a starting point.

ClickBlank Pageto create a new README from scratch.

ClickUseto select anexisting templateas a starting point.

Enter your knowledge into the README. Type/to use the text editor options to format your text, embed links, and more:ClickHeading 1to add a title or main heading.ClickHeading 2to add subheadings and create sections.ClickHeading 3to create subcategories within sections.ClickBulleted Listto create a bulleted list.ClickNumbered Listto create an ordered list.ClickChecklistto create a checklist of items.ClickFormulato add formulae from alist of supported functions.ClickCodeto add a code snippet.ClickImageto embed or upload an image.ClickQuoteto add block quotations.ClickMentionto tag another user in your Atlan workspace.ClickTableto create a table.ClickGoogle Docsto paste a Google Doc link and embed your online documents.ClickGoogle Sheetsto paste a Google Sheets link and embed your online spreadsheets.ClickGoogle Slidesto paste a Google Slides link and embed your online presentations.ClickMiro Boardto paste a Miro board link and embed your boards.ClickFigJamto paste a FigJam link and embed your boards.ClickLucidchartto paste a Lucidchart link and embed your documents or models.dangerTo embed a Lucidchart document or model, you will need to activate the embed code. Activating an embed code will disable password protection on published documents and make them accessible publicly.ClickDBDiagramto paste a dbdiagram link and embed your database diagrams.ClickERD Labto paste an ERD Lab link and embed your entity relationship diagrams.ClickMicrosoft Wordto paste a Microsoft Word link and embed your online documents.ClickMicrosoft Excelto paste a Microsoft Excel link and embed your online spreadsheets.ClickMicrosoft PowerPointto paste a Microsoft PowerPoint link and embed your online presentations.ClickGoogle Data StudioorGoogle Looker Studioto paste a Google Data Studio or Google Looker Studio link and embed your reports and dashboards.ClickCanvato paste a Canva link and embed your Canva graphics and presentations.

/

ClickHeading 1to add a title or main heading.

ClickHeading 1to add a title or main heading.

ClickHeading 2to add subheadings and create sections.

ClickHeading 2to add subheadings and create sections.

ClickHeading 3to create subcategories within sections.

ClickHeading 3to create subcategories within sections.

ClickBulleted Listto create a bulleted list.

ClickBulleted Listto create a bulleted list.

ClickNumbered Listto create an ordered list.

ClickNumbered Listto create an ordered list.

ClickChecklistto create a checklist of items.

ClickChecklistto create a checklist of items.

ClickFormulato add formulae from alist of supported functions.

ClickFormulato add formulae from alist of supported functions.

ClickCodeto add a code snippet.

ClickCodeto add a code snippet.

ClickImageto embed or upload an image.

ClickImageto embed or upload an image.

ClickQuoteto add block quotations.

ClickQuoteto add block quotations.

ClickMentionto tag another user in your Atlan workspace.

ClickMentionto tag another user in your Atlan workspace.

ClickTableto create a table.

ClickTableto create a table.

ClickGoogle Docsto paste a Google Doc link and embed your online documents.

ClickGoogle Docsto paste a Google Doc link and embed your online documents.

ClickGoogle Sheetsto paste a Google Sheets link and embed your online spreadsheets.

ClickGoogle Sheetsto paste a Google Sheets link and embed your online spreadsheets.

ClickGoogle Slidesto paste a Google Slides link and embed your online presentations.

ClickGoogle Slidesto paste a Google Slides link and embed your online presentations.

ClickMiro Boardto paste a Miro board link and embed your boards.

ClickMiro Boardto paste a Miro board link and embed your boards.

ClickFigJamto paste a FigJam link and embed your boards.

ClickFigJamto paste a FigJam link and embed your boards.

ClickLucidchartto paste a Lucidchart link and embed your documents or models.dangerTo embed a Lucidchart document or model, you will need to activate the embed code. Activating an embed code will disable password protection on published documents and make them accessible publicly.

ClickLucidchartto paste a Lucidchart link and embed your documents or models.

To embed a Lucidchart document or model, you will need to activate the embed code. Activating an embed code will disable password protection on published documents and make them accessible publicly.

ClickDBDiagramto paste a dbdiagram link and embed your database diagrams.

ClickDBDiagramto paste a dbdiagram link and embed your database diagrams.

ClickERD Labto paste an ERD Lab link and embed your entity relationship diagrams.

ClickERD Labto paste an ERD Lab link and embed your entity relationship diagrams.

ClickMicrosoft Wordto paste a Microsoft Word link and embed your online documents.

ClickMicrosoft Wordto paste a Microsoft Word link and embed your online documents.

ClickMicrosoft Excelto paste a Microsoft Excel link and embed your online spreadsheets.

ClickMicrosoft Excelto paste a Microsoft Excel link and embed your online spreadsheets.

ClickMicrosoft PowerPointto paste a Microsoft PowerPoint link and embed your online presentations.

ClickMicrosoft PowerPointto paste a Microsoft PowerPoint link and embed your online presentations.

ClickGoogle Data StudioorGoogle Looker Studioto paste a Google Data Studio or Google Looker Studio link and embed your reports and dashboards.

ClickGoogle Data StudioorGoogle Looker Studioto paste a Google Data Studio or Google Looker Studio link and embed your reports and dashboards.

ClickCanvato paste a Canva link and embed your Canva graphics and presentations.

ClickCanvato paste a Canva link and embed your Canva graphics and presentations.

ClickSave.

Your README is ready to be shared! ð

Although it may take some time to create, a README is a critical step for documenting any data asset and making it trustworthy.



#### Use README shortcutsâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Atlan supports keyboard and markdown shortcuts to supercharge your README documentation.



##### Keyboard shortcutsâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

In the table below,Modstands for modifier key   -Commandfor Mac andCtrlfor Windows.

Mod

Command

Ctrl

Mod + Shift + B

Mod + B

Mod + I

Mod + Shift + 8

Mod + E

Mod + Alt + C

Enter

â

Mod + Alt + 1

Mod + Alt + 2

Mod + Alt + 3

Mod + Alt + 4

Mod + Alt + 5

Mod + Alt + 1

Enter

Shift + Tab

Tab

Mod + Shift + 7

Mod + Alt + 0

Mod + Shift + X

Mod + U

Mod + Shift + 9

Mod + Shift + L

Mod + Shift + E

Mod + Shift + R

Mod + Shift + J

Mod + Shift + H

Tab

Shift + Tab

Backspace

Mod - Backspace

Delete

Mod - Delete



##### Markdown shortcutsâ
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Markdown shortcuts are triggered by pressing space after the shortcut   -  except for bold and italics. For example, to add a block quote, type>and then tap the spacebar.

>

>

**

**

__

*

*

_

-

`

```

~~~

#

##

###

####

#####

######

---

--

___

~~

[]

[x]

==



### Does Atlan support asset previews?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Yes, Atlan provides asset previews for supported tools to help with quick discovery and give you the context you need. Typically, theWhat does Atlan crawl from (connector name)?documentation will indicate whether asset previews are supported for a specific connector.

For example, Atlan supports asset previews for:

Tableau worksheets and dashboards

Microsoft Power BI reports

Google BigQuery tables, views, and materialized views

Sigma workbooks



### Can I search for assets by README, description, or other metadata?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

If the keywords you're searching by is present in the asset name ordescription, only then will the asset appear in your search results. You can also use avariety of filtersto narrow down your search.

Note that asset READMEs are currently not searchable in Atlan. This is because Atlan stores them as a relation to a data asset rather than as a direct metadata attribute.



### Can I add the Google Sheets extension for everyone in my organization?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Yes! To install the Google Sheets Atlan extension at the workspace level, follow the instructions in thisguide. You will need to be an administrator or have access to the admin console of your organization's Google account for this setup.

Once installed, users in your organization canconnect Atlan with Google Sheetsto start using the extension.



### Can I embed presentations or docs from SharePoint in a README?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Yes, you can embed links to your Microsoft Word, Excel, and PowerPoint files stored in SharePoint or OneDrive in READMEs. Refer toHow to add a READMEto learn more.



### Why can hard deleted assets be immediately restored after deletion?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

TheAPIis eventually consistent. This means that there is a short window of time, up to a few minutes, during which you can use the restore API endpoint to restore the asset that was hard deleted   -  even if it no longer appears on the UI.



### How can I make external documents and spreadsheets appear as assets in Atlan?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

Atlan supportscataloging filesthrough APIs. Thesupported file typesinclude DOC, Excel, PPT, CSV, TXT, JSON, XML, and ZIP files.



### Will Atlan send a notification if there's a new table added to my schema?â
(source: https://docs.atlan.com/product/capabilities/discovery/faq#delete-an-asset)

You can configure any of the following options to receive notifications on asset additions:

Create a webhook

Use the asset change notification custom package

discovery

faq

search

assets

data

faq-discovery

How does Atlan handle archived or deleted assets?

Is it possible to search for fields across all data sources?

What is included in the "All assets" view?

Can I search by a value to find assets with that value?

Why do I not see more results when searching with the search bar (or Cmd + K)?

What is the timezone for data display?

Asset Profile FAQsCan we replace or rename existing assets?What is an activity log?Why do dbt descriptions keep getting deleted?What is the timeframe for recently verified assets?What signals Atlan to auto-add the deprecated certifications in Looker?Is it possible to add PDFs to an asset README?How does version control work for description changes in source tools vs. Atlan?Can Atlan track schema changes?Are different fonts supported for READMEs and descriptions?Can Atlan handle assets with a large number of rows and columns?Why do I not see any tables or columns under database, only schema?Is the sample data preview cached?Delete an assetIf an asset is deleted via API, will workflows recreate the asset on the next run?Add a READMEDoes Atlan support asset previews?Can I search for assets by README, description, or other metadata?Can I add the Google Sheets extension for everyone in my organization?Can I embed presentations or docs from SharePoint in a README?Why can hard deleted assets be immediately restored after deletion?How can I make external documents and spreadsheets appear as assets in Atlan?Will Atlan send a notification if there's a new table added to my schema?

Can we replace or rename existing assets?

What is an activity log?

Why do dbt descriptions keep getting deleted?

What is the timeframe for recently verified assets?

What signals Atlan to auto-add the deprecated certifications in Looker?

Is it possible to add PDFs to an asset README?

How does version control work for description changes in source tools vs. Atlan?

Can Atlan track schema changes?

Are different fonts supported for READMEs and descriptions?

Can Atlan handle assets with a large number of rows and columns?

Why do I not see any tables or columns under database, only schema?

Is the sample data preview cached?

Delete an asset

If an asset is deleted via API, will workflows recreate the asset on the next run?

Add a README

Does Atlan support asset previews?

Can I search for assets by README, description, or other metadata?

Can I add the Google Sheets extension for everyone in my organization?

Can I embed presentations or docs from SharePoint in a README?

Why can hard deleted assets be immediately restored after deletion?

How can I make external documents and spreadsheets appear as assets in Atlan?

Will Atlan send a notification if there's a new table added to my schema?
