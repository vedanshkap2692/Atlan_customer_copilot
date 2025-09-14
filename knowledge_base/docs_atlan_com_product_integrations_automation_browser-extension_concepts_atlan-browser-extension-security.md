# Atlan browser extension security
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/concepts/atlan-browser-extension-security)

IntegrationsAutomationAWS LambdaAlways OnBrowser ExtensionHow-tosConceptsAtlan browser extension securityTroubleshootingFAQConnectionsWebhooksCollaborationCommunicationIdentity ManagementProject Management

AutomationAWS LambdaAlways OnBrowser ExtensionHow-tosConceptsAtlan browser extension securityTroubleshootingFAQConnectionsWebhooks

AWS Lambda

Always On

Browser ExtensionHow-tosConceptsAtlan browser extension securityTroubleshootingFAQ

How-tos

ConceptsAtlan browser extension security

Atlan browser extension security

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

Concepts

Atlan browser extension security

Atlan adheres to strict security standards for thebrowser extension. Atlan mandates security throughout the extension coding lifecycle:

Hardening configurations through content security policies,

Validating all inputs,

Requiring least privileges,

Employing defense-in-depth techniques like code obfuscation to frustrate reverse engineering,

Accessing customer resources over secure HTTPS channels after SSL certificate verification to prevent tampering.

Atlan follows proven CI/CD methodologies used for our SaaS application, enabling rapid and frequent updates to Atlan's Chrome extension. This allows:

Patching identified vulnerabilities faster through new releases while simultaneously upholding stability.

Mandatory code reviews specifically focused on analyzing security to help with identifying issues before these can impact customers.

Once ready, both static and dynamic scanning tools rigorously test the extension codebase for any weaknesses before distribution. Atlan is committed to transparency. If any post-deployment points of concern arise, Atlan will notify impacted customers promptly and address their concerns responsibly.

By incorporating security into each phase   -  secure architecture, peer reviews, robust testing, and responsible disclosure   -  Atlan strives to build browser extensions with both user needs and enterprise risks top of mind.Reach out to Atlan supportfor any questions.



## Permissionsâ
(source: https://docs.atlan.com/product/integrations/automation/browser-extension/concepts/atlan-browser-extension-security)

When using Atlan's browser extension in asupported tool, Atlan will read:

the URL of your browser tab

Document Object Model (DOM) elements such as asset title, hierarchy information, text,data-test-idattributes, and more to locate an asset in asupported source tool. This list may vary depending on the source tool.

data-test-id

If you're using Atlan's browser extension on anywebsite, it will only read the favicon, page title, and URL of your browser tab.

Atlan uses the following permissions for the browser extension to work in a supported tool:

activeTab-  theactiveTab permissionallows the browser extension to temporarily access the content of the active tab as you interact with the extension. This enables Atlan to display the Atlan badge and read the URL and DOM elements to locate the asset for displaying asset metadata in the sidebar.

activeTab

storage-  thestorage permissionallows Atlan to store information about the locally domains configured. This enables the browser extension to remember the sites that you want to use it on, even when you close and reopen your browser.

storage

cookies-  thecookies permissionallows Atlan to manage cookies for maintaining session states or user preferences for a supported tool. These login cookies are only shared between your Atlan tenant and the browser extension.

cookies

contextMenus-  thecontextMenus permissionallows Atlan to add context menu options (for example, right-click menus) to help you interact with the extension's features, namelysearch in Atlan, directly from any website.

contextMenus

host_permissions-  thehost permissionsallow the browser extension to work specifically with Atlan tenants, which is the host in this case. For example,https://atlan.com/*,https://atlan.dev/*.

host_permissions

https://atlan.com/*

https://atlan.dev/*

"content_scripts": [ { "matches": ["http://*/*", "https://*/*"]-  thecontent_scripts keyallows Atlan to inject Atlan's content script to any website you visit. Although this content script will be injected into all webpages, it will neither be executed nor any DOM elements captured if the webpage is not a supported tool.

"content_scripts": [ { "matches": ["http://*/*", "https://*/*"]

integration

connectors

security

access-control

permissions

Permissions
