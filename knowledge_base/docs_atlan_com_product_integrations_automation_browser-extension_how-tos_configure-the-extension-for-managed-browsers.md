# Configure the extension for managed browsers
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/configure-the-extension-for-managed-browsers#microsoft-edge)

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

Configure the extension for managed browsers

If you're using managed browsers, you can install and configure the Atlan browser extension for all users in your organization. To do so, you will need to bulk install the extension and deploy a configuration script.

Atlan supports managing the Atlan browser extension for the following:

Operating systems: macOS and Microsoft Windows

Browsers: Google Chrome and Microsoft Edge

The deployment scripts   -  .mobileconfig file for macOS and PowerShell script for Microsoft Windows   -  are designed to make only the most necessary modifications required for the Atlan browser extension to function properly. Both deployment methods adhere to the principle of least privilege:

The .mobileconfig file for macOS only includes the configuration settings required to install and operate the Atlan browser extension.

The PowerShell script creates essential registry keys required for the Atlan browser extension to operate on Microsoft Windows systems.

To configure the Atlan browser extension for a managed browser, you must complete these steps in the following order:

Configure the browser extension

Bulk install the browser extension

Deploy the configuration script

(Optional)Verify and monitor the installation



## Configure the browser extensionâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/configure-the-extension-for-managed-browsers#microsoft-edge)

You will need to be anadminin Atlan to configure the browser extension for users in your organization. You will also need inputs and approval from the IT administrator of your organization.

You can configure the browser extension and then download a configuration script to bulk install and deploy it for everyone in your organization.

To configure the browser extension, from within Atlan:

From the left menu on any screen, clickAdmin.

UnderWorkspace, clickIntegrations.

UnderApps, expand theBrowser extensiontile.

In theÂBrowser extensiontile, forBulk install the browser extension, click theSet up nowbutton.

In theSet up browser extensionform, enter the following details:ForChoose browser, the browser and operating system values will be prefilled based on what you're currently using   -  you can modify the fields, if required.ForYourAtlan domain, enter the URL of your Atlan instance   -  for example,https://(instance_name).atlan.com.infoðªDid you know?If you enable multiple Atlan domains, your users will be able to select the most relevant Atlan domain from a dropdown menu while using the browser extension. The default value in the dropdown will be the Atlan instance entered asYour Atlan domain. If your organization does not have multiple Atlan domains, only the default selection will be displayed.(Optional) ForAdvanced settings, you can configure the following:If you have multiple Atlan instances, toggle onMultiple Atlan domainsand then enter the URLs of your additional Atlan instances. Click+Addto add more Atlan domains.If your data tools are hosted on custom domains rather than the standard SaaS domain of each tool, toggle onCustom data sourcedomain. Click+ AddÂ to add more custom domains for data sources.ForConnector, select asupported toolfor the browser extension.In the adjacent field, enter the URL of your custom data source domain.infoðªDid you know?For anysupported toolsconfigured while setting up the managed browser extension, your users will not be able to update or remove these selections. They can, however, add additional custom domains for data sources.Click theDownload Scriptbutton to download the corresponding configuration script. The IT administrator(s) in your organization will need to install this configuration file in your organization's devices using a mobile device management (MDM) software. Administrative permissions to the MDM platform are required to complete the setup. Based on your operating system, the downloaded file can be one of the following two types:.mobileconfig-  use this file to configure profiles with specific settings inmacOS devices..ps1-  use this PowerShell script to create registry keys inMicrosoft Windows devices.

ForChoose browser, the browser and operating system values will be prefilled based on what you're currently using   -  you can modify the fields, if required.

ForChoose browser, the browser and operating system values will be prefilled based on what you're currently using   -  you can modify the fields, if required.

ForYourAtlan domain, enter the URL of your Atlan instance   -  for example,https://(instance_name).atlan.com.infoðªDid you know?If you enable multiple Atlan domains, your users will be able to select the most relevant Atlan domain from a dropdown menu while using the browser extension. The default value in the dropdown will be the Atlan instance entered asYour Atlan domain. If your organization does not have multiple Atlan domains, only the default selection will be displayed.

ForYourAtlan domain, enter the URL of your Atlan instance   -  for example,https://(instance_name).atlan.com.

https://(instance_name).atlan.com

ðªDid you know?If you enable multiple Atlan domains, your users will be able to select the most relevant Atlan domain from a dropdown menu while using the browser extension. The default value in the dropdown will be the Atlan instance entered asYour Atlan domain. If your organization does not have multiple Atlan domains, only the default selection will be displayed.

(Optional) ForAdvanced settings, you can configure the following:If you have multiple Atlan instances, toggle onMultiple Atlan domainsand then enter the URLs of your additional Atlan instances. Click+Addto add more Atlan domains.If your data tools are hosted on custom domains rather than the standard SaaS domain of each tool, toggle onCustom data sourcedomain. Click+ AddÂ to add more custom domains for data sources.ForConnector, select asupported toolfor the browser extension.In the adjacent field, enter the URL of your custom data source domain.infoðªDid you know?For anysupported toolsconfigured while setting up the managed browser extension, your users will not be able to update or remove these selections. They can, however, add additional custom domains for data sources.

(Optional) ForAdvanced settings, you can configure the following:

If you have multiple Atlan instances, toggle onMultiple Atlan domainsand then enter the URLs of your additional Atlan instances. Click+Addto add more Atlan domains.

If you have multiple Atlan instances, toggle onMultiple Atlan domainsand then enter the URLs of your additional Atlan instances. Click+Addto add more Atlan domains.

If your data tools are hosted on custom domains rather than the standard SaaS domain of each tool, toggle onCustom data sourcedomain. Click+ AddÂ to add more custom domains for data sources.ForConnector, select asupported toolfor the browser extension.In the adjacent field, enter the URL of your custom data source domain.infoðªDid you know?For anysupported toolsconfigured while setting up the managed browser extension, your users will not be able to update or remove these selections. They can, however, add additional custom domains for data sources.

If your data tools are hosted on custom domains rather than the standard SaaS domain of each tool, toggle onCustom data sourcedomain. Click+ AddÂ to add more custom domains for data sources.

ForConnector, select asupported toolfor the browser extension.

In the adjacent field, enter the URL of your custom data source domain.

ðªDid you know?For anysupported toolsconfigured while setting up the managed browser extension, your users will not be able to update or remove these selections. They can, however, add additional custom domains for data sources.

Click theDownload Scriptbutton to download the corresponding configuration script. The IT administrator(s) in your organization will need to install this configuration file in your organization's devices using a mobile device management (MDM) software. Administrative permissions to the MDM platform are required to complete the setup. Based on your operating system, the downloaded file can be one of the following two types:.mobileconfig-  use this file to configure profiles with specific settings inmacOS devices..ps1-  use this PowerShell script to create registry keys inMicrosoft Windows devices.

Click theDownload Scriptbutton to download the corresponding configuration script. The IT administrator(s) in your organization will need to install this configuration file in your organization's devices using a mobile device management (MDM) software. Administrative permissions to the MDM platform are required to complete the setup. Based on your operating system, the downloaded file can be one of the following two types:

.mobileconfig-  use this file to configure profiles with specific settings inmacOS devices.

.mobileconfig

.ps1-  use this PowerShell script to create registry keys inMicrosoft Windows devices.

.ps1



## Bulk install the browser extensionâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/configure-the-extension-for-managed-browsers#microsoft-edge)

You will need to have administrator access to your organization's mobile device management (MDM) software with the permission to add and deploy new policies to all users. You will also need inputs and approval from your Atlan admin.

You will need to configure theExtensionInstallForcelistbrowser policy for either Google Chrome or Microsoft Edge to force-install the extension for everyone in your organization.

ExtensionInstallForcelist

TheExtensionInstallForcelistbrowser policy:

ExtensionInstallForcelist

Governs extensions that can be silently installed and automatically enabled for all users.

Provides extension IDs that the browser will automatically install and enable when a user logs in.



### Google Chromeâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/configure-the-extension-for-managed-browsers#microsoft-edge)

To bulk install the Atlan browser extension in Google Chrome, follow the steps in Google documentation:Force install apps and extensions.



### Microsoft Edgeâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/configure-the-extension-for-managed-browsers#microsoft-edge)

To bulk install the Atlan browser extension in Microsoft Edge, follow the steps in Microsoft documentation:Force-install an extension.

For theExtension/App IDs and update URLs to be silently installed (Device)field, copy and paste the following value:

fipjfjlalpnbejlmmpfnmlkadjgaaheg;https://clients2.google.com/service/update2/crx

fipjfjlalpnbejlmmpfnmlkadjgaaheg;https://clients2.google.com/service/update2/crx

fipjfjlalpnbejlmmpfnmlkadjgaahegis theextension-idfor the Atlan browser extension.

fipjfjlalpnbejlmmpfnmlkadjgaaheg

extension-id

https://clients2.google.com/service/update2/crxindicates that it needs to be installed from the Chrome Web Store.

https://clients2.google.com/service/update2/crx



## Deploy the configuration scriptâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/configure-the-extension-for-managed-browsers#microsoft-edge)

You will need to have administrator access to your organization's mobile device management (MDM) software with the permission to add and deploy new policies to all users. You will also need inputs and approval from your Atlan admin.

The browser extension relies on managed storage for configuring domains in the Atlan extension. The values for managed storage can be configured through:

A configuration profile in macOS

Registry keys in Microsoft Windows

Although Atlan's solution is platform-agnostic, the following example pertains toMicrosoft Intune.



### macOSâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/configure-the-extension-for-managed-browsers#microsoft-edge)

You will need to create a custom managed profile to configure the domains for the Atlan browser extension.

To deploy the.mobileconfigfile for your organization, you can use any MDM platform.

.mobileconfig

For example:

Microsoft Intune   -  follow the steps inCustom configuration profile settings.



### Microsoft Windowsâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/configure-the-extension-for-managed-browsers#microsoft-edge)

You will need to create registry keys to deploy the extension. You can create the required registry keys with a PowerShell script, which can then be deployed to your usersâ devices using an MDM software.

To deploy the PowerShell configuration script for your organization, you can use any MDM platform.

For example:

Microsoft Intune   -  follow the steps inCreate a script policy and assign it. ForScript settings, enter the following details:Script location-  upload the.ps1configuration script downloaded from Atlan.Run this script using the logged on credentials-  change toNo.Enforce script signature checkÂ   -  change toNo.Run script in 64 bit PowerShell HostÂ   -  change toYes.

Script location-  upload the.ps1configuration script downloaded from Atlan.

.ps1

Run this script using the logged on credentials-  change toNo.

Enforce script signature checkÂ   -  change toNo.

Run script in 64 bit PowerShell HostÂ   -  change toYes.



## Verify and monitor the installationâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/how-tos/configure-the-extension-for-managed-browsers#microsoft-edge)

To ensure that the Atlan browser extension has been successfully deployed across all selected devices in your organization, you can:

Verify the installation   -  after you have deployed the policies, check a few target devices to ensure that the extension was installed and configured correctly.

Monitor compliance   -  monitor the compliance status of the policy and troubleshoot any issues.

Your users will now be able to use the Atlan browser extension in a managed browser! ð

Once the managed browser has synced with the latest configuration changes for your organization, the Atlan browser extension will be automatically installed and a new tab will open to indicate that the Atlan browser extension is now active.

atlan

documentation

Configure the browser extension

Bulk install the browser extension

Deploy the configuration script

Verify and monitor the installation
