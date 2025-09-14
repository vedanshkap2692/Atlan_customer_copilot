# Set up playbooks
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/set-up-playbooks#run-the-playbook)

PlaybooksGet StartedSet up playbooksManagementTroubleshooting

Get StartedSet up playbooks

Set up playbooks

Management

Troubleshooting

Configure Atlan

Playbooks

Get Started

Set up playbooks

ð¤ Who can do this?You will need to be an admin user in Atlan to create playbooks.

A common question that data teams often face is how to automate metadata at scale.

Having started out as a data team ourselves, we know that automating repetitive tasks can help data teams maximize the value they provide to their organization. One way of doing so is through Atlan's playbooks!

Playbooks help power metadata automation for your data assets in Atlan. You can create rule-based automations at scale and update metadata in bulk, helping you streamline your workflows.

You can update the following asset metadata using playbooks:

Certificates

Descriptions

Owners

Terms

Tags

Domains

Custom metadata

For example, imagine your organization needs to transfer ownership of several data assets. Instead of your data team manually updating the ownership of each and every asset, you can create a playbook to automate this process and update the metadata of your assets at scale.



## Playbook recommendationsâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/set-up-playbooks#run-the-playbook)

Before you begin, review some general guidelines on running playbooks in Atlan:

Avoid running multiple playbooks simultaneously on the same set of assets. Allow one playbook run to be completed before proceeding with another operation on the same set of assets. Otherwise, you may experience performance issues and inconsistencies.

Review and understand the depth of your asset lineage or hierarchy prior to enabling atag propagationplaybook. For assets with complex lineage,tag propagation may take longerto complete than the playbook runtime. You may want to review and judiciously select a list of assets that need to be tagged directly. For their child and/or downstream assets, Atlan recommends that youenable tag propagation.



## Create a playbookâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/set-up-playbooks#run-the-playbook)

To create a playbook in Atlan:

From the left menu in Atlan, you can either:ClickAssetsto navigate to the assets page.From theFiltersmenu on the left or the tabs along the top,apply any asset filters.Next to the search bar, click the 3-dot icon and then clickCreate playbookto create a playbook for the filtered assets   -  this option is only visible to admin users.ClickGovernanceto navigate to the governance center.Under theGovernanceheading of theGovernance center, clickPlaybooks.ClickCreate Newto get started.

ClickAssetsto navigate to the assets page.From theFiltersmenu on the left or the tabs along the top,apply any asset filters.Next to the search bar, click the 3-dot icon and then clickCreate playbookto create a playbook for the filtered assets   -  this option is only visible to admin users.

From theFiltersmenu on the left or the tabs along the top,apply any asset filters.

Next to the search bar, click the 3-dot icon and then clickCreate playbookto create a playbook for the filtered assets   -  this option is only visible to admin users.

ClickGovernanceto navigate to the governance center.Under theGovernanceheading of theGovernance center, clickPlaybooks.ClickCreate Newto get started.

Under theGovernanceheading of theGovernance center, clickPlaybooks.

ClickCreate Newto get started.

In theCreate new playbookdialog box, enter the following details:ForName, enter a name for the task to be accomplished   -  for example,Update ownership. (Atlan recommends that the length of a playbook name must be no longer than 46 characters.)(Optional) ForDescription, enter a description.(Optional) Select an icon for your playbook.

ForName, enter a name for the task to be accomplished   -  for example,Update ownership. (Atlan recommends that the length of a playbook name must be no longer than 46 characters.)

Update ownership

(Optional) ForDescription, enter a description.

(Optional) Select an icon for your playbook.

ClickCreateto save your playbook.



## Set up rules as filtersâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/set-up-playbooks#run-the-playbook)

To set up rules as filters for your playbook:

In theBuild Rulespage of your playbook, clickFilters.

For name, add a name to your filter.

To set a matching condition for the filters, selectMatch allorMatch any.Match allwill logicallyANDthe criteria, whileMatch anywill logicallyORthe criteria.

AND

OR

ForAttributes, select a relevant option:For this example, we'll clickConnectionand then select a Snowflake connection. (Optional) To further refine your asset selection:ClickAll databasesto filter by databases in a selected connection.ClickAll schemasto filter by schemas in a selected connection.ClickConnectorto filter assets bysupported connectors.ClickAsset typeto filter by specific asset types   -  for example, tables, columns, queries, glossaries, and more.ClickCertificateto filter assets bycertification status.ClickOwnersto filter assets byasset owners.ClickTagsto filter assets by yourtagsin Atlan, including importedSnowflakeanddbttags.(Optional) ForSnowflake tagsonly, to the left of the checkbox, clickSelect value, and then from theSelect tag valuedialog, select any value(s) to filter assets by tag value.ClickGlossary, terms, & categoriesto filter by a specificglossaryorcategoryto bulk update all the nested terms or by multiple glossaries and categories.ClickLinked termsto filter assets bylinked terms.ClickDomainsto filter by specificdomains or subdomainsto bulk update all the assets included in those data domains or subdomains.ClickProductsto filter fordata productsby specific data domains or subdomains.ClickSchema qualified Nameto filter assets by the qualified name of a given schema.ClickDatabase qualified Nameto filter assets by the qualified name of a given database.Clickdbtto filter assets by dbt-specific filters and then select adbt Cloudordbt Corefilter.ClickPropertiesto filter assets bycommon asset properties.ClickUsageto filter assets byusage metrics.ClickMonte Carloto filter assets byMonte Carlo-specific filters.ClickSodato filter assets bySoda-specific filters.ClickTable/Viewto filter tables or views by row count, column count, or size.ClickColumnto filter columns bycolumn-specific filters, including parent asset type or name, data type, orcolumn keys.ClickProcessto filterlineage processesby the SQL query.ClickQueryto filter assets by associatedvisual queries.ClickMeasureto filterMicrosoft Power BI measuresusing the external measures filter.

For this example, we'll clickConnectionand then select a Snowflake connection. (Optional) To further refine your asset selection:ClickAll databasesto filter by databases in a selected connection.ClickAll schemasto filter by schemas in a selected connection.

ClickAll databasesto filter by databases in a selected connection.

ClickAll schemasto filter by schemas in a selected connection.

ClickConnectorto filter assets bysupported connectors.

ClickAsset typeto filter by specific asset types   -  for example, tables, columns, queries, glossaries, and more.

ClickCertificateto filter assets bycertification status.

ClickOwnersto filter assets byasset owners.

ClickTagsto filter assets by yourtagsin Atlan, including importedSnowflakeanddbttags.(Optional) ForSnowflake tagsonly, to the left of the checkbox, clickSelect value, and then from theSelect tag valuedialog, select any value(s) to filter assets by tag value.

(Optional) ForSnowflake tagsonly, to the left of the checkbox, clickSelect value, and then from theSelect tag valuedialog, select any value(s) to filter assets by tag value.

ClickGlossary, terms, & categoriesto filter by a specificglossaryorcategoryto bulk update all the nested terms or by multiple glossaries and categories.

ClickLinked termsto filter assets bylinked terms.

ClickDomainsto filter by specificdomains or subdomainsto bulk update all the assets included in those data domains or subdomains.

ClickProductsto filter fordata productsby specific data domains or subdomains.

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

ForOperator, selectIs one offor values to include orIs notfor values to exclude. Depending on the selected attribute(s), you can also choose fromadditional operators:SelectEquals (=)orNot Equals (!=)to include or exclude assets through exact match search.SelectStarts WithorEnds Withto filter assets using the starting or ending sequence of values.SelectContainsorDoes not containto find assets with or without specified values contained within the attribute.SelectPatternto filter assets using supportedElastic DSL regular expressions.SelectIs emptyto filter assets with null values.SelectBelongs toorDoesn't belong toto filterdata productsby specificdata domains or subdomains.

SelectEquals (=)orNot Equals (!=)to include or exclude assets through exact match search.

SelectStarts WithorEnds Withto filter assets using the starting or ending sequence of values.

SelectContainsorDoes not containto find assets with or without specified values contained within the attribute.

SelectPatternto filter assets using supportedElastic DSL regular expressions.

SelectIs emptyto filter assets with null values.

SelectBelongs toorDoesn't belong toto filterdata productsby specificdata domains or subdomains.

ForValues, select the relevant values. The values will vary depending on the selected attributes.

(Optional) To add more filters, clickAdd filterand selectFilterto add individual filters orFilterGroupto nest more filters in a group.

(Optional) To view all the assets that match your rules, in theFilterscard, clickViewallfor a preview.

(Optional) To remove a playbook filter, to the right of any filter, click the three horizontal dots and then clickDelete.

(Optional) To turn off a playbook filter, to the right of any filter, click the three horizontal dots and then clickDisable. ClickEnableto turn on any disabled filters.



## Select the actionsâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/set-up-playbooks#run-the-playbook)

To select the actions to be performed based on your rules:

In theBuild Rulespage of your playbook, clickActions.

ForSelect Action, select the relevant metadata option to update:ClickCertificateto update thecertification statusof assets toVerified,Draft,Deprecated, orNo certificate.ClickDescriptionto update thedescriptionof your assets.ClickOwnersto add, remove, or replaceasset owners. In this example, we'll update the ownership of the assets.ClickTermsto addtermsto your assets or remove or replace them fromlinked assets.ClickTagsto addtagsto your assets or remove or replace them fromtaggedorpropagatedassets. Note that if there are multiple tag actions to be performed, Atlan will execute them in the following order:ADD,REMOVE, and thenREPLACE.ClickDomaintoadd your assets to a specific domain or subdomainor remove them from an existing linkeddomain or subdomain.Click anycustom metadata structureand then select acustom metadata propertyto update or unlink it from your assets.

ClickCertificateto update thecertification statusof assets toVerified,Draft,Deprecated, orNo certificate.

ClickDescriptionto update thedescriptionof your assets.

ClickOwnersto add, remove, or replaceasset owners. In this example, we'll update the ownership of the assets.

ClickTermsto addtermsto your assets or remove or replace them fromlinked assets.

ClickTagsto addtagsto your assets or remove or replace them fromtaggedorpropagatedassets. Note that if there are multiple tag actions to be performed, Atlan will execute them in the following order:ADD,REMOVE, and thenREPLACE.

ADD

REMOVE

REPLACE

ClickDomaintoadd your assets to a specific domain or subdomainor remove them from an existing linkeddomain or subdomain.

Click anycustom metadata structureand then select acustom metadata propertyto update or unlink it from your assets.

ForSelect operator, select the relevant option. The operators will vary depending on the selected action.

ForValues, select the relevant option(s). The values will vary depending on the selected actions.

(Optional) To add more actions, clickAddAction.

You can control tag propagation when adding tags as an action in playbooks.Tag propagationis disabled by default. If you enable tag propagation, you will also be able toconfigure how tags are propagated.



## Run the playbookâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/set-up-playbooks#run-the-playbook)

If you'd like to continue working on your playbook, you can save it as a draft. If your playbook is ready, you can proceed to running it.

To run the playbook:

You can either:To run the playbook once immediately, clickRun once.To schedule the playbook to run hourly, daily, weekly, or monthly, clickScheduleand choose the preferred frequency, timezone, and time.dangerIf you're scheduling multiple playbooks, Atlan recommends spacing out the schedules as much as possible to minimize any overlap between the playbook workflow runs. For more about workflows in general, seeworkflow recommendations.

You can either:

To run the playbook once immediately, clickRun once.

To run the playbook once immediately, clickRun once.

To schedule the playbook to run hourly, daily, weekly, or monthly, clickScheduleand choose the preferred frequency, timezone, and time.dangerIf you're scheduling multiple playbooks, Atlan recommends spacing out the schedules as much as possible to minimize any overlap between the playbook workflow runs. For more about workflows in general, seeworkflow recommendations.

To schedule the playbook to run hourly, daily, weekly, or monthly, clickScheduleand choose the preferred frequency, timezone, and time.

If you're scheduling multiple playbooks, Atlan recommends spacing out the schedules as much as possible to minimize any overlap between the playbook workflow runs. For more about workflows in general, seeworkflow recommendations.

ClickCompleteto run the playbook.

ClickCompleteto run the playbook.

In the resulting screen, clickGo to profileto view your playbook profile.

In the resulting screen, clickGo to profileto view your playbook profile.

Once your playbook has completed its run, you will see the metadata updated for your assets! ð

If you have any questions about setting up playbooks, head overhere.

atlan

documentation

Playbook recommendations

Create a playbook

Set up rules as filters

Select the actions

Run the playbook
