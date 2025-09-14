# Use the Atlan browser extension
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/use-the-atlan-browser-extension#add-a-resource)

IntegrationsAutomationAWS LambdaAlways OnBrowser ExtensionHow-tosConfigure the extension for managed browsersHow to use the Atlan browser extensionEnable embedded metadata in TableauConceptsTroubleshootingFAQConnectionsWebhooksCollaborationCommunicationIdentity ManagementProject Management

AutomationAWS LambdaAlways OnBrowser ExtensionHow-tosConfigure the extension for managed browsersHow to use the Atlan browser extensionEnable embedded metadata in TableauConceptsTroubleshootingFAQConnectionsWebhooks

AWS Lambda

Always On

Browser ExtensionHow-tosConfigure the extension for managed browsersHow to use the Atlan browser extensionEnable embedded metadata in TableauConceptsTroubleshootingFAQ

How-tosConfigure the extension for managed browsersHow to use the Atlan browser extensionEnable embedded metadata in Tableau

Configure the extension for managed browsers

How to use the Atlan browser extension

Enable embedded metadata in Tableau

Concepts

Troubleshooting

FAQ

Connections

Webhooks

Collaboration

Communication

Identity Management

Project Management

Configure Atlan

Integrations

Automation

Browser Extension

How-tos

How to use the Atlan browser extension

The Atlan browser extension provides metadata context directly in yoursupported data tools. You can use the extension in the following Chromium-based browsers: Google Chrome and Microsoft Edge.



## Install the extensionâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/use-the-atlan-browser-extension#add-a-resource)

To install the Atlan browser extension, first log into your Atlan instance. Atlan saves your Atlan domain in a cookie when you log in.

To install Atlan's browser extension:

You can either:Find the extension in the Chrome Web Store:https://chrome.google.com/webstore/detail/atlan/fipjfjlalpnbejlmmpfnmlkadjgaahegFrom the upper right of any screen in Atlan, navigate to your name and then clickProfile.Click the four dots icon in the resulting dialog to get to integrations.UnderApps, forBrowser extension, clickInstall.

Find the extension in the Chrome Web Store:https://chrome.google.com/webstore/detail/atlan/fipjfjlalpnbejlmmpfnmlkadjgaaheg

From the upper right of any screen in Atlan, navigate to your name and then clickProfile.Click the four dots icon in the resulting dialog to get to integrations.UnderApps, forBrowser extension, clickInstall.

Click the four dots icon in the resulting dialog to get to integrations.

UnderApps, forBrowser extension, clickInstall.

To install the Atlan browser extension:For Google Chrome, in the upper right of your screen, clickAdd to Chrome. When prompted for confirmation, click theAdd extensionbutton.For Microsoft Edge, follow the steps inAdd an extension to Microsoft Edge from the Chrome Web Store.

For Google Chrome, in the upper right of your screen, clickAdd to Chrome. When prompted for confirmation, click theAdd extensionbutton.

For Microsoft Edge, follow the steps inAdd an extension to Microsoft Edge from the Chrome Web Store.

Currently, you can't install the browser extension on mobile devices or tablets.

You can also install Atlan's browser extension at theworkspace level. To set this up, you need to be an administrator or have access to the admin console of your organization's Google account. If your organization uses managed browsers, you canconfigure the extension for managed browsers.



## Configure the extensionâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/use-the-atlan-browser-extension#add-a-resource)

Once installed, configure the Atlan browser extension to get started. Optionally, Atlan admins canpreconfigure custom domains for data sources, if any.



### Configure the extension as a userâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/use-the-atlan-browser-extension#add-a-resource)

To configure the browser extension, once installed:

If you are logged into your Atlan instance, skip to the next step. If you haven't logged into Atlan, log in to your Atlan instance when prompted.

In theOptionspage, to enter the URL of your Atlan instance:If your organization uses an Atlan domain (for example,_mycompany_.atlan.com), the Atlan instance URL appears preselected. ClickGet started. (Optional) Switch to a different Atlan domain, if required.If your organization uses a custom domain (for example,_atlan_.mycompany.com), enter the URL of your Atlan instance and then clickGet started.

If your organization uses an Atlan domain (for example,_mycompany_.atlan.com), the Atlan instance URL appears preselected. ClickGet started. (Optional) Switch to a different Atlan domain, if required.

_mycompany_.atlan.com

If your organization uses a custom domain (for example,_atlan_.mycompany.com), enter the URL of your Atlan instance and then clickGet started.

_atlan_.mycompany.com

After a successful login, the messageUpdated successfullyappears.

(Optional) If your data tools are hosted on custom domains, rather than the standard SaaS domain of each tool:Click theConfigure custom domainlink at the bottom.In the dropdown on the left, select your data tool.In the text box on the right, enter the custom domain you use for that tool.Repeat these steps for each tool hosted on a custom domain.Click theSavebutton when finished.If your Atlan admin haspreconfigured custom domains for data sources, you won't be able to update or remove these selections. Click+ Addto configure custom domains for additional data sources as required.

Click theConfigure custom domainlink at the bottom.In the dropdown on the left, select your data tool.In the text box on the right, enter the custom domain you use for that tool.Repeat these steps for each tool hosted on a custom domain.Click theSavebutton when finished.

In the dropdown on the left, select your data tool.

In the text box on the right, enter the custom domain you use for that tool.

Repeat these steps for each tool hosted on a custom domain.

Click theSavebutton when finished.

If your Atlan admin haspreconfigured custom domains for data sources, you won't be able to update or remove these selections. Click+ Addto configure custom domains for additional data sources as required.

You can now close theOptionstab.

The extension is now ready to use! ð



### (Optional) Configure custom domains as an adminâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/use-the-atlan-browser-extension#add-a-resource)

You need to be an admin user in Atlan to configure custom domains for data sources from the admin center.

To configure custom domains, from within Atlan:

From the left menu of any screen, clickAdmin.

UnderWorkspace, clickIntegrations.

UnderApps, expand theBrowser extensiontile.

In theÂBrowser extensiontile, forSet up your custom data source..., if your data tools are hosted on custom domains rather than the standard SaaS domain of each tool, click theConfigurelink to configure them for users in your organization.ForConnector, select asupported toolfor the browser extension.In the adjacent field, enter the URL of the custom domain for your data source.(Optional) Click+ Addto add more.ClickSaveto save your configuration.infoðªDid you know?For anysupported toolsthat you have configured, your users won't be able to update or remove these selections. They can, however, add additional custom domains for data sources.

ForConnector, select asupported toolfor the browser extension.

In the adjacent field, enter the URL of the custom domain for your data source.

(Optional) Click+ Addto add more.

ClickSaveto save your configuration.

ðªDid you know?For anysupported toolsthat you have configured, your users won't be able to update or remove these selections. They can, however, add additional custom domains for data sources.

(Optional) ForDownload Atlan extension or share with your team, you can either install the Atlan browser extension for your own use or share the link with your users.



## Usageâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/use-the-atlan-browser-extension#add-a-resource)

Anyone with access to Atlanâany admin, member, or guest userâand a supported tool can use the browser extension. First, log into Atlan.

When using Atlan's browser extension in asupported tool, the extension only reads the URL of your browser tabâno other data is accessed. If using Atlan's browser extension on anywebsite, it only reads the favicon, page title, and URL of your browser tab. Learn more aboutAtlan browser extension security.



### Access and enrich context in-flowâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/use-the-atlan-browser-extension#add-a-resource)

To access context for an asset, from within a supported tool:

Log into the supported tool.

Open any supported asset.

In the lower-right corner of the page, click the small Atlan icon.dangerThe icon to activate Atlan isnotthe extension icon that appears at the top of your Chrome browser. This small Atlan icon in the lower right corner of the page is the only way to access the metadata for the asset you are viewing in another tool.

The icon to activate Atlan isnotthe extension icon that appears at the top of your Chrome browser. This small Atlan icon in the lower right corner of the page is the only way to access the metadata for the asset you are viewing in another tool.

In the sidebar that appears:Click the tabs and links to view all context about the asset.Make changes to any of the metadata you'd like.

Click the tabs and links to view all context about the asset.

Make changes to any of the metadata you'd like.

Now you can understand and enrich assets without leaving your data tools themselves! ð

The Atlan sidebar automatically reloads as you browse your assets in a supported tool to show details about the asset you're currently viewing.

Your permissions in Atlan control what metadata you can see and change in the extension.



### Search for metadataâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/use-the-atlan-browser-extension#add-a-resource)

To search for context for any information onanywebsite:

Select the text you'd like to search on the web page you're viewing.

Right-click, and then selectSearch in Atlan ð¡.

The extension opens a new browser tab on Atlan's discovery page, with the results for that text! ð



### Add a resourceâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/use-the-atlan-browser-extension#add-a-resource)

You can link any web page as aresourceto your assets in Atlan using the browser extension.

To add a web page as a resource to an asset:

In the top right of the web page you're viewing, click theAtlan Chrome extension.

In the resource clipper menu, underLink this page to an asset, select the asset to which you'd like to add the web page as a resource.

ClickSaveto confirm your selection.

(Optional) Once the resource has been linked successfully, click theOpen in Atlanbutton to view the linked asset directly in Atlan.

You can now add resources to your assets in Atlan from any website! ð

The Tableau extension offers native embeddings directly in your dashboards. SeeEnable embedded metadata in Tableaufor more information.



## Supported toolsâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/use-the-atlan-browser-extension#add-a-resource)

Currently, the Atlan browser extension supports assets in the following tools:

Amazon QuickSight: analyses, dashboards, and datasets

Databricks: databases, schemas, views, and tables

dbt Cloud: models and sources in the model editor and dbt docs

Google BigQuery: datasets, schemas, views, and tables

IBM Cognos Analytics: folders, dashboards, packages, explorations, reports, files, data sources, and modules

Looker: dashboards, explores, and folders

Microsoft Power BI: dashboards, reports, dataflows, and datasets

Mode: collections, reports, queries, and charts

Qlik Sense Cloud: apps, datasets, sheets, and spaces

Redash: queries, dashboards, and visualizations

Salesforce: objects

Sigma: datasets, pages, and data elements

Snowflake(via Snowsight schema explorer): databases, schemas, tables, views, dynamic tables, streams, and pipes

Tableau: dashboards, data sources, workbooks, and metrics. Additionally, you can choose to switch the Tableau extension to offer native embeddings directly in your dashboards. SeeEnable embedded metadata in Tableaufor more information.

ThoughtSpot: liveboards, answers, visualizations, and tables

MicroStrategy: dossiers, reports, documents

atlan

documentation

Install the extension

Configure the extension

Usage

Supported tools
