# Crawl Microsoft Power BI
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/crawl-microsoft-power-bi)

Microsoft Power BIGet StartedCrawl Power BI AssetsCrawl Microsoft Power BIMine Microsoft Power BIReferencesTroubleshootingFAQ

Get Started

Crawl Power BI AssetsCrawl Microsoft Power BIMine Microsoft Power BI

Crawl Microsoft Power BI

Mine Microsoft Power BI

References

Troubleshooting

FAQ

Connect data

BI Tools

On-premises & Enterprise BI

Microsoft Power BI

Crawl Power BI Assets

Crawl Microsoft Power BI

Once you have configured theMicrosoft Power BI user permissions, you can establish a connection between Atlan and Microsoft Power BI.

To crawl metadata from Microsoft Power BI, review

theorder of operationsand then complete the following steps.



## Select the sourceâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/crawl-microsoft-power-bi)

To select Microsoft Power BI as your source:

In the top right of any screen, navigate toÂNewand then clickÂNew Workflow.

From the list of packages, selectÂPower BI Assetsand click onÂSetup Workflow.



## Provide credentialsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/crawl-microsoft-power-bi)

To enter your Microsoft Power BI credentials:

ForAuthentication,choose the method you want to use to access Microsoft Power BI:ForService Principalauthentication, enter theTenant Id,Client Id, andClient Secretyou configured whensetting up Microsoft Power BI. Use theEnable Only Admin API Accessoption to control how metadata is extracted. When enabled, the crawler uses only admin APIs. If disabled, both admin and non-admin APIs are used.ForDelegated Userauthentication, enter theUsername,Password,Tenant Id,Client Id, andClient Secretyou configured whensetting up Microsoft Power BI.

ForService Principalauthentication, enter theTenant Id,Client Id, andClient Secretyou configured whensetting up Microsoft Power BI. Use theEnable Only Admin API Accessoption to control how metadata is extracted. When enabled, the crawler uses only admin APIs. If disabled, both admin and non-admin APIs are used.

ForDelegated Userauthentication, enter theUsername,Password,Tenant Id,Client Id, andClient Secretyou configured whensetting up Microsoft Power BI.

At the bottom of the form, click theTest Authenticationbutton to confirm connectivity to Microsoft Power BI using these details.

Once successful, at the bottom of the screen click theNextbutton.



## Configure connectionâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/crawl-microsoft-power-bi)

To complete the Microsoft Power BI connection configuration:

Provide aConnection Namethat represents your source environment. For example, you might want to use values likeproduction,development,gold, oranalytics.

Provide aConnection Namethat represents your source environment. For example, you might want to use values likeproduction,development,gold, oranalytics.

production

development

gold

analytics

(Optional) To change the users able to manage this connection, change the users or groups listed underConnection Admins.dangerIf you don't specify any user or group, nobody can manage the connection   -  not even admins.

(Optional) To change the users able to manage this connection, change the users or groups listed underConnection Admins.

If you don't specify any user or group, nobody can manage the connection   -  not even admins.

At the bottom of the screen, click theNextbutton to proceed.

At the bottom of the screen, click theNextbutton to proceed.



## Configure the crawlerâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/crawl-microsoft-power-bi)

Before running the Microsoft Power BI crawler, configure metadata extraction and advanced options. You can override the default settings for the following fields.



### Configure metadataâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/crawl-microsoft-power-bi)

Include Workspaces: Select Microsoft Power BI workspaces to include. Defaults to all workspaces when left blank. UseAdvanced Searchto filter workspaces using the following options:Contains: Matches workspaces that contain the given substring.Starts with: Matches workspaces that begin with the specified text.Ends with: Matches workspaces that end with the specified text.Regex pattern: Matches workspaces based on a regular expression.All selected filters apply using anANDcondition.

Include Workspaces: Select Microsoft Power BI workspaces to include. Defaults to all workspaces when left blank. UseAdvanced Searchto filter workspaces using the following options:

Contains: Matches workspaces that contain the given substring.

Starts with: Matches workspaces that begin with the specified text.

Ends with: Matches workspaces that end with the specified text.

Regex pattern: Matches workspaces based on a regular expression.

All selected filters apply using anANDcondition.

AND

Exclude Workspaces: Select workspaces to exclude. No workspaces are excluded by default.Advanced Searchis also available for exclusion, with the same filtering options as mentioned previously.

Exclude Workspaces: Select workspaces to exclude. No workspaces are excluded by default.Advanced Searchis also available for exclusion, with the same filtering options as mentioned previously.

Include Dashboard and Reports Regex: Use a regular expression to include dashboards and reports based on naming patterns. Includes all by default.

Include Dashboard and Reports Regex: Use a regular expression to include dashboards and reports based on naming patterns. Includes all by default.

Exclude Dashboard and Reports Regex: Use a regular expression to exclude dashboards and reports based on naming patterns. Excludes none by default.

Exclude Dashboard and Reports Regex: Use a regular expression to exclude dashboards and reports based on naming patterns. Excludes none by default.

Attach Endorsements from Power BI: Automatically certify assets endorsed in Power BI. To manually review before applying, change this setting toSend a Request. For more details, seeWhat does Atlan crawl from Microsoft Power BI?

Attach Endorsements from Power BI: Automatically certify assets endorsed in Power BI. To manually review before applying, change this setting toSend a Request. For more details, seeWhat does Atlan crawl from Microsoft Power BI?



### Configure advanced settingsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/crawl-microsoft-power-bi)

Source Connections: When your tenant has multiple connections available for the same source system that share the similar metadata, confirm the advanced options and choose the correct connections from theSource Connectionslist drop down to avoid creating duplicate lineage to such connections.

Source Connections

Enable ODBC DSN Connectivity Mapping: Power BI provides multiple ways of connecting to a SQL source, including ODBC connectivity for building Reports and Dashboards. When datasets are populated using ODBC, provide a mapping of the DSN ( Data Source Name ) names to their appropriate database qualified names after enabling this toggle.

If a workspace appears in both the include and exclude filters, the exclude filter takes precedence.



## Run the crawlerâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/crawl-microsoft-power-bi)

To run the Microsoft Power BI crawler:

To check for anypermissions or other configuration issuesbefore running the crawler, clickPreflight checks.

You can either:To run the crawler once immediately, at the bottom of the screen, click theRunbutton.To schedule the crawler to run hourly, daily, weekly, or monthly, at the bottom of the screen, click theSchedule Runbutton.

To run the crawler once immediately, at the bottom of the screen, click theRunbutton.

To schedule the crawler to run hourly, daily, weekly, or monthly, at the bottom of the screen, click theSchedule Runbutton.

Once the crawler has completed running, you can see the assets in Atlan's asset page! ð

connectors

data

crawl

Select the source

Provide credentials

Configure connection

Configure the crawler

Run the crawler
