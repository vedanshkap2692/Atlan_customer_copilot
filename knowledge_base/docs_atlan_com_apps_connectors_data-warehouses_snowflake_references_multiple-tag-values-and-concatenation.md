# Multiple tag values and concatenation
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/multiple-tag-values-and-concatenation)

SnowflakeGet StartedCrawl Snowflake AssetsManage Snowflake in AtlanReferencesMultiple tag values and concatenationWhat does Atlan crawl from Snowflake?Preflight checks for SnowflakeTroubleshootingBest Practices

Get Started

Crawl Snowflake Assets

Manage Snowflake in Atlan

ReferencesMultiple tag values and concatenationWhat does Atlan crawl from Snowflake?Preflight checks for Snowflake

Multiple tag values and concatenation

What does Atlan crawl from Snowflake?

Preflight checks for Snowflake

Troubleshooting

Best Practices

Connect data

Data Warehouses

Snowflake

References

Multiple tag values and concatenation

Atlan supports assigning multiple tag values to a single Snowflake object. When multiple tag values are assigned, Atlan concatenates them into a single string using a configurable delimiter.



## Requirementsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/multiple-tag-values-and-concatenation)

Bothreverse syncandconcatenationmust be enabled for multi-value synchronization to work.



## Constraintsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/multiple-tag-values-and-concatenation)

When configuring multiple tag values, keep the following constraints in mind:

The chosen delimitercan'tappear inside any tag value to prevent parsing errors.

The concatenated tag values length must not exceed256 characters.

If theallowed listis enabled for a tag in Snowflake, concatenated tag values that you attach to Snowflake objects must come from the tagâs predefined list. To use a new value, add it to the list.

Each tag supports up to300 values. For more information, seeSnowflake tag quota for objects.



## How concatenation worksâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/multiple-tag-values-and-concatenation)

Tag concatenation is an Atlan feature. Concatenated values created in Atlan are synced to Snowflake. However, if you concatenate tag values in Snowflake workflows, those concatenated references won't be synced back to Atlan.

Atlan manages multiple tag values by concatenating them into a single string that can be synchronized back to Snowflake. The process involves sorting, concatenation, and synchronization behaviors described below.



### Single valuesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/multiple-tag-values-and-concatenation)

When only one value is assigned to a tag, no concatenation occurs. The single value is sent as-is to Snowflake.

For example, if you have a tagcost_centerand assign only the valuefinanceto an object, the result in Snowflake is the single valuefinancewithout any concatenation.

cost_center

finance

finance



### Multiple valuesâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/multiple-tag-values-and-concatenation)

You can assign multiple values to a single tag for any object in Atlan. When multiple values are assigned, they're concatenated into a single string using a delimiter character.

For example, if you have a tagcost_centerand assign the valuesfinance,engineering, andsalesto an object with comma as the delimiter, the result is the concatenated stringengineering,finance,sales.

cost_center

finance

engineering

sales

engineering,finance,sales



#### Sortingâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/multiple-tag-values-and-concatenation)

Tag values are sorted alphabetically before concatenation to maintain consistent ordering.

For example, if you have a tagenvironmentwith valuesproduction,development, andstagingassigned to an object and use a comma (,) as your delimiter, Atlan sorts them alphabetically (development,production,staging) and concatenates them as:development,production,staging.

environment

production

development

staging

,

development

production

staging

development,production,staging



### Reverse syncâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/multiple-tag-values-and-concatenation)

Concatenation and reverse sync apply at the schema level for imported Snowflake tags. When reverse sync is enabled, the concatenated tag values are synchronized back to the corresponding objects in Snowflake.



#### Updates and removalsâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/multiple-tag-values-and-concatenation)

When you update or remove tag assignments in Atlan, these changes can be synchronized back to Snowflake and depend on the combination of reverse sync and concatenation settings:

Whenreverse sync is OFF: Snowflake isn't updated

Whenreverse sync is ONbutconcatenation is OFF: Only one tag value (typically the latest) is sent to Snowflake

Whenboth reverse sync and concatenation are ON: All tag values are concatenated and sent as a single string



## See alsoâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/references/multiple-tag-values-and-concatenation)

Snowflake object tagging introduction- Learn about Snowflake's tag capabilities, quotas, and supported objects

multiple-concatenation

snowflake

Requirements

Constraints

How concatenation works

See also
