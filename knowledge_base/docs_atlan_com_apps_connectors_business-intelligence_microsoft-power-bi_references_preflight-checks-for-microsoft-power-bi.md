# Preflight checks for Microsoft Power BI
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/preflight-checks-for-microsoft-power-bi)

Microsoft Power BIGet StartedCrawl Power BI AssetsReferencesWhat does Atlan crawl from Microsoft Power BI?Preflight checks for Microsoft Power BIWhat lineage does Atlan extract from Microsoft Power BI?TroubleshootingFAQ

Get Started

Crawl Power BI Assets

ReferencesWhat does Atlan crawl from Microsoft Power BI?Preflight checks for Microsoft Power BIWhat lineage does Atlan extract from Microsoft Power BI?

What does Atlan crawl from Microsoft Power BI?

Preflight checks for Microsoft Power BI

What lineage does Atlan extract from Microsoft Power BI?

Troubleshooting

FAQ

Connect data

BI Tools

On-premises & Enterprise BI

Microsoft Power BI

References

Preflight checks for Microsoft Power BI

Beforerunning the Microsoft Power BI crawler, you can runpreflight checksto perform the necessary technical validations. The following preflight checks will be completed:



## Credentials scopesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/preflight-checks-for-microsoft-power-bi)

âCheck successfulÂ

Check successful

â Source returned error

For example:Credentials Scopes: Failed with response{"error":"invalid_client","error_description":"AADSTS7000215: Invalid client secret provided. Ensure the secret being sent in the request is the client secret value, not the client secret ID, for a secret added to app '832d86c8-cd9b-43a5-b165-ab40fb49770b'.\r\nTrace ID: 654ce9b2-a626-4e0b-8598-0cac69970200\r\nCorrelation ID: 5be327fc-93cb-4bef-ab4e-0373f11a8017\r\nTimestamp: 2022-10-31 09:03:41Z","error_codes":[7000215],"timestamp":"2022-10-31 09:03:41Z","trace_id":"654ce9b2-a626-4e0b-8598-0cac69970200","correlation_id":"5be327fc-93cb-4bef-ab4e-0373f11a8017","error_uri":"https://login.microsoftonline.com/error?code=7000215"}#STATUS:401

Credentials Scopes: Failed with response{"error":"invalid_client","error_description":"AADSTS7000215: Invalid client secret provided. Ensure the secret being sent in the request is the client secret value, not the client secret ID, for a secret added to app '832d86c8-cd9b-43a5-b165-ab40fb49770b'.\r\nTrace ID: 654ce9b2-a626-4e0b-8598-0cac69970200\r\nCorrelation ID: 5be327fc-93cb-4bef-ab4e-0373f11a8017\r\nTimestamp: 2022-10-31 09:03:41Z","error_codes":[7000215],"timestamp":"2022-10-31 09:03:41Z","trace_id":"654ce9b2-a626-4e0b-8598-0cac69970200","correlation_id":"5be327fc-93cb-4bef-ab4e-0373f11a8017","error_uri":"https://login.microsoftonline.com/error?code=7000215"}#STATUS:401



## Workspace permissionsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/preflight-checks-for-microsoft-power-bi)

âCheck successful

Check successful

âNo workspaces available

No workspaces available



## Metadata scan and fetch refreshablesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/preflight-checks-for-microsoft-power-bi)

âCheck successfulÂ

Check successful

â Source returned error

For example:Permissions to scan metadata and fetch refreshables: Failed with response{"error":{"code":"PowerBINotAuthorizedException","pbi.error":{"code":"PowerBINotAuthorizedException","parameters":{},"details":[],"exceptionCulprit":1}}}#STATUS:401

Permissions to scan metadata and fetch refreshables: Failed with response{"error":{"code":"PowerBINotAuthorizedException","pbi.error":{"code":"PowerBINotAuthorizedException","parameters":{},"details":[],"exceptionCulprit":1}}}#STATUS:401

connectors

crawl

Credentials scopes

Workspace permissions

Metadata scan and fetch refreshables
