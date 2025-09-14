# What does Atlan crawl from Monte Carlo?Private Preview
(source: https://docs.atlan.com/apps/connectors/observability/monte-carlo/references/what-does-atlan-crawl-from-monte-carlo)

Monte CarloGet StartedCrawl Monte Carlo AssetsReferencesWhat does Atlan crawl from Monte Carlo?Preflight checks for Monte Carlo

Get Started

Crawl Monte Carlo Assets

ReferencesWhat does Atlan crawl from Monte Carlo?Preflight checks for Monte Carlo

What does Atlan crawl from Monte Carlo?

Preflight checks for Monte Carlo

Connect data

Data Quality & Observability

Monte Carlo

References

What does Atlan crawl from Monte Carlo?

Atlan supports both automated and custom monitors as native assets for search and discovery. Atlan also supports crawling incidents for alltypes of monitors.

Once you'vecrawled Monte Carlo, you canuse connector-specific filtersÂ to search for your Monte Carlo assets as well as assets from other supported sources to which Monte Carlo monitors have been applied   -  for example, Snowflake tables.

The following filters are currently supported for Monte Carlo assets:

Monitor type   -  filter monitors by type of monitor

Monitor status   -  filter monitors by monitor status

Incident count   -  filter monitors by the total count of incidents

Last synced in Atlan   -  filter monitors by timestamp for last updated in Atlan

The following Monte Carlo filters are currently available for supported SQL assets:

Monitor status   -  filter SQL assets associated with any monitors by monitor status

Monitor type   -  filter SQL assets associated with any monitors by type of monitor

Alert priority   -  filter SQL assets by priority level of alerts, ranging from 1 to 4

Alert type   -  filter SQL assets by specific types of alerts

Incident severity   -  filter SQL assets by severity level of incidents, ranging from 1 to 4

Alert subtype   -  filter SQL assets by alert subtypes

Alert status   -  filter SQL assets by specificalert statuses

Alert owner   -  filter SQL assets by alert owners

Last synced in Atlan   -  filter SQL assets by timestamp for when any associated monitors and incidents were updated in Atlan

Atlan crawls and maps the following assets and properties from Monte Carlo.



## Monitorsâ
(source: https://docs.atlan.com/apps/connectors/observability/monte-carlo/references/what-does-atlan-crawl-from-monte-carlo)

Atlan maps automated and custom monitors from Monte Carlo to itsMCMonitorasset type.

MCMonitor

name

name

Audience

mcLabels

uuid

mcMonitorId

monitorStatus

mcMonitorStatus

monitorType

mcMonitorType

warehouseName

mcMonitorWarehouse

scheduleType

mcMonitorScheduleType

namespace

mcMonitorNamespace

ruleType

mcMonitorRuleType

ruleSql

mcMonitorRuleCustomSql

scheduleConfig

mcMonitorRuleScheduleConfig

ruleComparisons

mcMonitorRuleComparisons

monitorUrl

sourceUrl

breachRate

mcMonitorBreachRate

scheduleConfig

mcMonitorRuleScheduleConfigHumanized

alertCondition

mcMonitorAlertCondition

priority

mcMonitorPriority

isOotbMonitor

mcMonitorIsOotb



## Alerts and incidentsâ
(source: https://docs.atlan.com/apps/connectors/observability/monte-carlo/references/what-does-atlan-crawl-from-monte-carlo)

Atlan maps alerts and incidents from Monte Carlo to itsMCIncidentasset type.

MCIncident

Alerts inherit priority levels from custom monitors. If an alert is confirmed as an issue or requires resolution, Monte Carlo enables you to mark it as an incident and apply a severity level. Atlan will display the status of your assets at source. Refer toMonte Carlo documentationto learn more.

name

name

tableLinked

mcAssetReferences

uuid

mcIncidentId

incidentType

mcIncidentType

incidentSubTypes

mcIncidentSubTypes

severity

mcIncidentSeverity

feedback

mcIncidentState

warehouse.name

mcIncidentWarehouse

incidentOwner

sourceOwners

incidentUrl

sourceUrl

priority

mcIncidentPriority

connectors

crawl

Monitors

Alerts and incidents
