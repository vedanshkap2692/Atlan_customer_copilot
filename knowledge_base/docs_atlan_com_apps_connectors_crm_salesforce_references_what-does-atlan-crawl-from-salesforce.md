# What does Atlan crawl from Salesforce?
(source: https://docs.atlan.com/apps/connectors/crm/salesforce/references/what-does-atlan-crawl-from-salesforce)

SalesforceGet StartedCrawl Salesforce AssetsReferencesWhat does Atlan crawl from Salesforce?Preflight checks for SalesforceTroubleshootingFAQ

Get Started

Crawl Salesforce Assets

ReferencesWhat does Atlan crawl from Salesforce?Preflight checks for Salesforce

What does Atlan crawl from Salesforce?

Preflight checks for Salesforce

Troubleshooting

FAQ

Connect data

CRM

Salesforce

References

What does Atlan crawl from Salesforce?

Atlan only performsGETrequests on these five endpoints:

GET

sObject Basic Information

Query

Reports

Dashboards

Folders

Each endpoint will be set in its own OAuth client session. For every API request, it will hit the Salesforce login endpoint, which means there will be at least five (same as the number of endpoints above) login entries in your Salesforce account's login history within the duration of the scheduled workflow run.

Atlan crawls and maps the following assets and properties from Salesforce.

Once you'vecrawled Salesforce, you canuse connector-specific filtersfor quick asset discovery. The following filters are currently supported for these assets:

Fields-  Is encrypted and Is required filters



## Organizationsâ
(source: https://docs.atlan.com/apps/connectors/crm/salesforce/references/what-does-atlan-crawl-from-salesforce)

Atlan maps organizations from Salesforce to itsSalesforceOrganizationasset type.

SalesforceOrganization

id

sourceId

name

name

description

description

webUrl

sourceURL

createdDate

sourceCreatedAt

lastModifiedDate

sourceUpdatedAt

createdBy

sourceCreatedBy

lastModifiedBy

sourceUpdatedBy



## Objectsâ
(source: https://docs.atlan.com/apps/connectors/crm/salesforce/references/what-does-atlan-crawl-from-salesforce)

Atlan maps objects from Salesforce to itsSalesforceObjectasset type.

SalesforceObject

label

name

name

apiName

description

description

custom

isCustom

mergable

isMergable

queryable

isQueryable

fieldCount

fieldCount

webUrl

sourceURL

lastModifiedDate

sourceUpdatedAt

lastModifiedBy

sourceUpdatedBy



## Fieldsâ
(source: https://docs.atlan.com/apps/connectors/crm/salesforce/references/what-does-atlan-crawl-from-salesforce)

Atlan maps fields from Salesforce to itsSalesforceFieldasset type.

SalesforceField

label

name

name

apiName

type

dataType

description

description

lastModifiedDate

sourceUpdatedAt

lastModifiedBy

sourceUpdatedBy

calculated

isCalculated

calculatedFormula

formula

defaultValue

defaultValue

caseSensitive

isCaseSensitive

custom

isCustom

encrypted

isEncrypted

nillable

isNullable

polymorphicForeignKey

isPolymorphicForeignKey

order

order

length

maxLength

precision

precision

scale

numericScale

unique

isUnique

inlineHelpText

inlineHelpText

picklistValues

picklistValues



## Reportsâ
(source: https://docs.atlan.com/apps/connectors/crm/salesforce/references/what-does-atlan-crawl-from-salesforce)

Atlan maps reports from Salesforce to itsSalesforceReportasset type.

SalesforceReport

id

sourceId

name

name

reportType

reportType

detailColumns

detailColumns

description

description

webUrl

sourceURL

createdDate

sourceCreatedAt

lastModifiedDate

sourceUpdatedAt

createdBy

sourceCreatedBy

lastModifiedBy

sourceUpdatedBy



## Dashboardsâ
(source: https://docs.atlan.com/apps/connectors/crm/salesforce/references/what-does-atlan-crawl-from-salesforce)

Atlan maps dashboards from Salesforce to itsSalesforceDashboardasset type.

SalesforceDashboard

id

sourceId

name

name

dashboardType

dashboardType

reportCount

reportCount

description

description

webUrl

sourceURL

crawl

salesforce

api

Organizations

Objects

Fields

Reports

Dashboards
