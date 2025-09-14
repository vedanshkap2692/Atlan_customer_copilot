# Lineage
(source: https://docs.atlan.com/product/capabilities/lineage/concepts/what-is-lineage)

LineageGet StartedManage lineageConceptsWhat is column-level lineage?What is lineage?What are partial assets?What are processes?ReferencesFAQTroubleshooting

Get Started

Manage lineage

ConceptsWhat is column-level lineage?What is lineage?What are partial assets?What are processes?

What is column-level lineage?

What is lineage?

What are partial assets?

What are processes?

References

FAQ

Troubleshooting

Use data

Lineage

Concepts

What is lineage?

Data lineagecaptures how data moves across your data landscape. This information is useful to:

Trace data's origins, to assist with root cause analysis

Trace data's destinations, to assist with impact analysis

Automate the propagation of metadata to derived assets

Tag propagation is disabled by default in Atlan. You canenable tag propagationto child and downstream assets.



### Root cause analysisâ
(source: https://docs.atlan.com/product/capabilities/lineage/concepts/what-is-lineage)

Root cause analysis is about identifying the underlying causes of a data problem. You want to know where the data camefromand whathappenedto it before it got to you. With root cause analysis, your focus is on theseupstreamsources and transformations.



### Impact analysisâ
(source: https://docs.atlan.com/product/capabilities/lineage/concepts/what-is-lineage)

Impact analysis is about identifying potential consequences of changes. You want to know where the data isgoingand whatcould happento others if you change it. With impact analysis, the primary focus is on thesedownstreamsystems and consumers.

When viewing lineage in Atlan, hover over any asset to view a metadata popover. The metadata popovers display relevant metadata for the asset, providing you with more context for your analysis. For example, database and schema names for Snowflake assets, project names for dbt models, and more.



## How does it work?â
(source: https://docs.atlan.com/product/capabilities/lineage/concepts/what-is-lineage)

Atlan constructslineageby combining assets and processes:

Assets represent the inputs and outputs of processes   -  databases, dashboards, and so on.

Processesrepresent the activities that move or transform data between the assets. (Processes are the lines between the assets in Atlan's graphical view.)

Atlan chains these together into a flow of data from various resources:



### SQL parsingâ
(source: https://docs.atlan.com/product/capabilities/lineage/concepts/what-is-lineage)

Atlan parses SQL queries to determine how data stores have created or transformed assets. Examples of this include:

Amazon Redshift

dbt

Generic query logs (via S3 objects)

Google BigQuery

Snowflake



### API crawlingâ
(source: https://docs.atlan.com/product/capabilities/lineage/concepts/what-is-lineage)

Atlan also retrieves lineage information for assets from APIs. Examples of this include:

Databricks (Unity Catalog)

Looker

Microsoft Power BI

Tableau



### API ingestionâ
(source: https://docs.atlan.com/product/capabilities/lineage/concepts/what-is-lineage)

Atlan provides built-in lineage extraction for the tools above. But you can also extend lineage with your own information using Atlan'sopen APIs. You can use these to integrate lineage from your own home-grown tools or orchestration suites likeApache AirflowandDagster.

lineage

data-lineage

impact-analysis

faq

troubleshooting

How does it work?
