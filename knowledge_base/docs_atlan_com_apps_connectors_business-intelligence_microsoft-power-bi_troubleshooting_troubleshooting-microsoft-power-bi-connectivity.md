# Troubleshooting Microsoft Power BI connectivity
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/troubleshooting/troubleshooting-microsoft-power-bi-connectivity)

Microsoft Power BIGet StartedCrawl Power BI AssetsReferencesTroubleshootingTroubleshooting Microsoft Power BI connectivityFAQ

Get Started

Crawl Power BI Assets

References

TroubleshootingTroubleshooting Microsoft Power BI connectivity

Troubleshooting Microsoft Power BI connectivity

FAQ

Connect data

BI Tools

On-premises & Enterprise BI

Microsoft Power BI

Troubleshooting

Troubleshooting Microsoft Power BI connectivity



#### What are the known limitations of the Microsoft Power BI connector?â
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/troubleshooting/troubleshooting-microsoft-power-bi-connectivity)

Atlan currently doesn't support the following:

Filtering hidden pages inreports-  known limitation ofPowerBI reports API

Crawling reports developed and published inPower BI Report Server



#### What are the limitations of the Microsoft PowerBI Connector, when only admin APIs are used?â
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/troubleshooting/troubleshooting-microsoft-power-bi-connectivity)

When the Microsoft PowerBI Connector is configured to use only admin APIs, it results in reduced metadata extraction and limited lineage capabilities compared to using a combination ofadmin & non-admin APIs.

The following limitations apply as mentioned below:

PowerBI Pages (which are a part of PowerBI Report) won't be catalogued.

Downstream Lineage from PowerBI Table Column / Measure -> PowerBI Page won't be available.



#### Can users who don't have access to a report still see the preview?â
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/troubleshooting/troubleshooting-microsoft-power-bi-connectivity)

Users can only see asset previews if the following conditions are met:

They have the necessary permissions in both Microsoft Power BI and Atlan.

They're logged into Atlan and Microsoft Power BI on the same browser.

Therefore, if a user lacks the permission to view a report in Microsoft Power BI, they won't be able to see the report preview in Atlan. Even if they do have the necessary permissions, they need to be logged into Microsoft Power BI on the same browser as their Atlan instance for asset previews to work.



#### Why can I not see previews for my Microsoft Power BI assets?â
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/troubleshooting/troubleshooting-microsoft-power-bi-connectivity)

Your Microsoft Power BI assets are updated with previews during the next run of your Microsoft Power BI workflow. If you have run the workflow and still don't see the previews, rerun the workflow. Once you've rerun the workflow, the previews are visible to all eligible users.



#### How does Atlan calculate views for Microsoft Power BI reports and dashboards?â
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/troubleshooting/troubleshooting-microsoft-power-bi-connectivity)

Atlan calculatesUsageviews based on the number of times users open a report or dashboard in Microsoft Power BI.

lineage

data-lineage

impact-analysis

upstream-dependencies

data-sources
