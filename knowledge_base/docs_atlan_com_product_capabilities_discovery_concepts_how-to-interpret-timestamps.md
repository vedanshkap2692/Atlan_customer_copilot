# How to interpret timestamps
(source: https://docs.atlan.com/product/capabilities/discovery/concepts/how-to-interpret-timestamps)

DiscoveryGet StartedAsset ManagementConfigurationConceptsHow to interpret timestampsWhat are asset profiles?ReferencesFAQ

Get Started

Asset Management

Configuration

ConceptsHow to interpret timestampsWhat are asset profiles?

How to interpret timestamps

What are asset profiles?

References

FAQ

Use data

Discovery

Concepts

How to interpret timestamps

Atlan displays timestamps for assets in local timezones based on the location of your browser. The date and time display includes a combination of the following components:

Relative time   -  for example,2 hours ago,1 day ago,3 months ago

Absolute time   -  for example,Mar 14, 2024, 9:40:01 AM

Atlan displays the following timestamps in the asset sidebar:



## Overview tabâ
(source: https://docs.atlan.com/product/capabilities/discovery/concepts/how-to-interpret-timestamps)

Usage-  timestamp for the number of read queries on an asset atsourcewithin a specific date range, as fetched from the miner run. This also includes an absolute time value forLast usage data updated (in Atlan). Only applicable to data sources for which Atlan supports mining query history.

Last queried-  timestamp for the latest read query on an assetÂ atsourceas fetched from the miner run or in Atlan within a specific date range. Only applicable to data sources for which Atlan supports mining query history.

dbt run status-  status and timestamp for the last run of the dbt job updating an asset in dbt, as fetched from adbt crawlerrun.



## Usage tabâ
(source: https://docs.atlan.com/product/capabilities/discovery/concepts/how-to-interpret-timestamps)

Row update frequency-  timestamps for recent row updates on an asset atsourcewithin a specific date range, as fetched from the miner run. Only applicable to data sources for which Atlan supports mining query history. Up to five recent row updates will be displayed, if available.



## Properties tabâ
(source: https://docs.atlan.com/product/capabilities/discovery/concepts/how-to-interpret-timestamps)

Last updated (in Atlan)-  timestamp for when any metadata attribute of the asset was last updated in Atlan. For example, when youlinked a termoradded a certificateto an asset in Atlan.

Last synced with sourceÂ   -  timestamp for when a workflow run last checked for this asset atsource. This timestamp also includes a link to the connection workflow.

Created (in Atlan)-  timestamp for when this asset was first created and published in Atlan during a crawler run.

Last updated (on source)-  timestamp for when any metadata for the asset was last altered atsource, as fetched from the crawler run.

Created at (on source)-  timestamp for when the asset was first created atsource, as fetched from the crawler run.



## Frequently asked questionsâ
(source: https://docs.atlan.com/product/capabilities/discovery/concepts/how-to-interpret-timestamps)



#### Why are metrics missing after miner runs?â
(source: https://docs.atlan.com/product/capabilities/discovery/concepts/how-to-interpret-timestamps)

If you notice a time lag from when your miner workflows last ran, note that Atlan requires a minimum lag of 24 to 48 hours to capture all the relevant transformations that were part of a session. (Read more about miner logichere.) This may also depend on when your miner workflow was scheduled to run, which you canmodifyat any time.



#### Why do some timestamps have variable time ranges?â
(source: https://docs.atlan.com/product/capabilities/discovery/concepts/how-to-interpret-timestamps)

Miners have a configurable property that governs the window of time for which metrics are reported. If a miner has been failing consistently, Atlan may reduce this window from 30 to only 14 days for reporting metrics. This is applicable to all date and time properties populated by miners.



#### Is last updated in Atlan the same as last synced with source?â
(source: https://docs.atlan.com/product/capabilities/discovery/concepts/how-to-interpret-timestamps)

No,Last updated (in Atlan)records the time when any metadata is updated on the asset in Atlan whileLast synced with sourcerecords the time when a workflow ran successfully updating the asset with changes from source, if any. If no metadata updates were made on the asset in Atlan before the next scheduled workflow run,ÂLast synced with sourceÂ may be considered as the more current timestamp reflecting any or no changes on the asset as fetched from source.



#### Why are there discrepancies in time for some miner-related timestamps?â
(source: https://docs.atlan.com/product/capabilities/discovery/concepts/how-to-interpret-timestamps)

For timestamps related to miner runs:

If no one has queried the asset at source, the timestamp forLast queriedmay be older than the date range recorded forUsage.

If no one has used the asset at source for the duration of time that query history was mined,Row update frequencymay not display any time value.

Even when a miner run fails, it partially publishes assets, resulting in inconsistencies. For example, the date range in theLast queriedtooltip may be for a successful miner run but the absolute time may be a different value if the asset had been partially published.

atlan

documentation

Overview tab

Usage tab

Properties tab

Frequently asked questions
