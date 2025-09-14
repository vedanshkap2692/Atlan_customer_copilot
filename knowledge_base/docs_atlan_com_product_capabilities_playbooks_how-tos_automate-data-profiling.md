# Automate data profiling
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/automate-data-profiling)

PlaybooksGet StartedManagementManage playbooksAutomate data profilingTroubleshooting

Get Started

ManagementManage playbooksAutomate data profiling

Manage playbooks

Automate data profiling

Troubleshooting

Configure Atlan

Playbooks

Management

Automate data profiling

âAvailable via the Data Quality Studio package

ð¤ Who can do this?You need to be anadmin userin Atlan to create profiling playbooks.

Monitoring and improving data quality is critical to building trust in your data assets. Atlan solves for this with profiling playbooks!

Profiling playbooks help power data observability for your assets in Atlan. You can create profiling playbooks to scan your assets at scale, identify any issues or inconsistencies, and improve the data quality of your assets.



## Supported sourcesâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/automate-data-profiling)

Atlan currently supports column profiling for the following connectors:

Amazon Athena

Amazon Redshift

Databricks

Google BigQuery

Microsoft SQL Server

MySQL

PostgreSQL

Snowflake

Trino



## Create a profiling playbookâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/automate-data-profiling)

To create a profiling playbook:

In the left menu in Atlan, clickGovernance.

Under theGovernanceheading of theGovernance center, clickPlaybooks.

To the right of theCreate Newbutton, click the downward arrow and then selectProfiling Playbook.

In theCreate new profiling playbookdialog, enter the following details:ForName, enter a name for the task to be accomplished   -  for example,Tables scan. (Atlan recommends that the length of a playbook name must be no longer than 46 characters.)ForConnection, select asupported connectionfrom the dropdown menu   -  in this example, we'll select a Google BigQuery connectiondevelopment.(Optional) ForDescription, enter a description for your playbook.(Optional) Select an icon for your playbook.

ForName, enter a name for the task to be accomplished   -  for example,Tables scan. (Atlan recommends that the length of a playbook name must be no longer than 46 characters.)

Tables scan

ForConnection, select asupported connectionfrom the dropdown menu   -  in this example, we'll select a Google BigQuery connectiondevelopment.

development

(Optional) ForDescription, enter a description for your playbook.

(Optional) Select an icon for your playbook.

ClickCreateto save your playbook.



## Set up rules as filtersâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/automate-data-profiling)

The assets to be scanned are pre-filled based on your selected connection.

To set up rules as filters for your profiling playbook:

In theBuild Rulespage of your profiling playbook, clickFilters.

For the name field, add a name to your filter   -  for example,Profiling action.

To set a matching condition for the filters, selectMatch allorMatch any.Match allwill logicallyANDthe criteria, whileMatch anywill logicallyORthe criteria.

AND

OR

ForAttributes, select the relevant option. For this example, we'll selectNamelisted underProperties. (Optional) To further refine your asset selection:ClickConnectionto select a specific connection.ÂClickAll databasesto filter by databases in a selected connection.ClickAll schemasto filter by schemas in a selected connection.ClickConnectorto filter assets bysupported connectors.ClickAsset typeto filter by specific asset types   -  for example, tables, columns, queries, glossaries, and more.ClickCertificateto filter assets bycertification status.ClickOwnersto filter assets byasset owners.ClickTagsto filter assets by yourtagsin Atlan, including importedSnowflakeanddbttags.(Optional) ForSnowflake tagsonly, to the left of the checkbox, clickSelect value, and then from theSelect tag valuedialog, select any value(s) to filter assets by tag value.ClickGlossary, terms, & categoriesto filter by a specificglossaryorcategoryto bulk update all the nested terms or by multiple glossaries and categories.ClickLinked termsto filter assets bylinked terms.ClickSchema qualified Nameto filter assets by the qualified name of a given schema.ClickDatabase qualified Nameto filter assets by the qualified name of a given database.Clickdbtto filter assets by dbt-specific filters and then select adbt Cloudordbt Corefilter.ClickPropertiesto filter assets bycommon asset properties.ClickUsageto filter assets byusage metrics.ClickMonte Carloto filter assets byMonte Carlo-specific filters.ClickSodato filter assets bySoda-specific filters.ClickTable/Viewto filter tables or views by row count, column count, or size.ClickColumnto filter columns bycolumn-specific filters, including parent asset type or name, data type, orcolumn keys.ClickProcessto filterlineage processesby the SQL query.ClickQueryto filter assets by associatedvisual queries.ClickMeasureto filterMicrosoft Power BI measuresusing the external measures filter.

ClickConnectionto select a specific connection.ÂClickAll databasesto filter by databases in a selected connection.ClickAll schemasto filter by schemas in a selected connection.

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

(Optional) To view all the assets that match your rules, in theFilterscard, clickViewallfor a preview.



## Confirm profiling actionsâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/automate-data-profiling)

Column profiling is currently only supported for number and text data types. The profiled column assets will be populated with preconfigured metrics.

To select the actions to be performed based on your rules:

The default profiling actions to be performed include:Base metrics:Distinct count   -  number of rows that contain distinct values, relative to the column.Missing count   -  number of rows that do not contain specific values.Numeric metrics:Minimum and maximum values   -  smallest and greatest values in a numeric column.Average   -  calculated average of values in a numeric column.Standard deviation   -  calculated standard deviation of values in a numeric column.Variance   -  calculated variance of values in a numeric column.String metrics:Average length   -  average length of string values in a column.Minimum and maximum length   -  minimum and maximum length of string values in a column.

Base metrics:Distinct count   -  number of rows that contain distinct values, relative to the column.Missing count   -  number of rows that do not contain specific values.

Distinct count   -  number of rows that contain distinct values, relative to the column.

Missing count   -  number of rows that do not contain specific values.

Numeric metrics:Minimum and maximum values   -  smallest and greatest values in a numeric column.Average   -  calculated average of values in a numeric column.Standard deviation   -  calculated standard deviation of values in a numeric column.Variance   -  calculated variance of values in a numeric column.

Minimum and maximum values   -  smallest and greatest values in a numeric column.

Average   -  calculated average of values in a numeric column.

Standard deviation   -  calculated standard deviation of values in a numeric column.

Variance   -  calculated variance of values in a numeric column.

String metrics:Average length   -  average length of string values in a column.Minimum and maximum length   -  minimum and maximum length of string values in a column.

Average length   -  average length of string values in a column.

Minimum and maximum length   -  minimum and maximum length of string values in a column.

ClickNextto proceed to the next step.

In theOptimize your Profiling querypopup, the following message will appear:This Profiling playbook will queryxrows acrossyassets. To avoid significant computing costs, review your applied filters before proceeding. ClickReview filtersto review your existing filters or clickContinue anywayto proceed.

x

y

Note that Atlan is working to support sampling functionality in the future.



## Run the playbookâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/automate-data-profiling)

If you'd like to continue working on your playbook, you can save it as a draft. If your playbook is ready, you can proceed to running it.

To run the playbook:

You can either:To run the playbook once immediately, clickRun once.To schedule the playbook to run hourly, daily, weekly, or monthly, clickScheduleand choose the preferred frequency, timezone, and time.

To run the playbook once immediately, clickRun once.

To schedule the playbook to run hourly, daily, weekly, or monthly, clickScheduleand choose the preferred frequency, timezone, and time.

ClickCompleteto confirm your selections.

In the resulting screen, clickGo to profileto view your playbook profile.

Once your playbook run is completed, you will see the data profile updated for your assets! ð



## View profiled assetsâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/automate-data-profiling)

To view the profiled assets for your playbook:

In theOverviewpage of your playbook, to the right ofProfiling action, click the total count of profiled assets.

In the sidebar to the right, profiled assets will be indicated with a bar graph icon. Click any profiled asset to proceed to viewing profiling data.

From the table sidebar, click theColumntab to view column assets and then select any of the profiled columns.

In the column sidebar to the right, clickProfileto view profiling data for the selected column asset.

Once you've created a profiling playbook, you canmonitor, modify, or deleteit at any time.

connectors

data

crawl

Supported sources

Create a profiling playbook

Set up rules as filters

Confirm profiling actions

Run the playbook

View profiled assets
