import dspy
from dspy import Example
from dspy_essentials.models import classification

examples = [
    Example(
        id="TICKET-245",
        subject="Connecting Snowflake to Atlan - required permissions?",
        body="Hi team, we're trying to set up our primary Snowflake production database as a new source in Atlan, but the connection keeps failing. We've tried using our standard service account, but it's not working. Our entire BI team is blocked on this integration for a major upcoming project, so it's quite urgent. Could you please provide a definitive list of the exact permissions and credentials needed on the Snowflake side to get this working? Thanks.",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-275",
        subject="How to configure Redshift connector for incremental metadata sync?",
        body="Hi, we\u2019ve set up our Redshift connector in Atlan, but we\u2019re noticing that metadata updates are not syncing incrementally. Every crawl pulls the full dataset, which is slowing things down. Is there a way to configure the connector for incremental syncs? Our data team is eager to optimize this process.",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-276",
        subject="Missing lineage for dbt models in Atlan",
        body="We\u2019re using dbt for our transformations, but the lineage for our models isn\u2019t showing up in Atlan. We\u2019ve double-checked the integration settings, but something\u2019s off. This is critical for our compliance reporting. Can you help us troubleshoot this issue?",
        parsed_document=classification(
            topics=["Lineage", "Connector"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-277",
        subject="Best practices for managing glossary terms across teams",
        body="Our organization has multiple teams creating glossary terms, and we\u2019re worried about inconsistencies. What are the best practices for standardizing term creation and ensuring alignment across departments? We want to avoid duplicate or conflicting terms.",
        parsed_document=classification(
            topics=["Best practices", "Glossary"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-278",
        subject="API endpoint for bulk updating asset descriptions",
        body="We need to update descriptions for hundreds of assets programmatically. Does the Atlan API provide an endpoint for bulk updates? If so, can you share an example request payload? This is a high-priority task for our metadata cleanup project.",
        parsed_document=classification(
            topics=["API/SDK", "Product"],
            sentiment="Neutral",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-279",
        subject="SSO configuration with Azure AD failing",
        body="We\u2019ve been trying to set up SSO with Azure AD, but the authentication keeps failing with a vague error code. Our IT team is frustrated, and this is blocking user access. Can you provide a step-by-step guide to debug and fix this?",
        parsed_document=classification(
            topics=["SSO", "How-to"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-280",
        subject="How to tag sensitive data fields automatically?",
        body="Our compliance team needs to identify and tag fields containing PII across our datasets. Does Atlan support automatic detection of sensitive data? If so, how can we configure it to apply tags like \u2018PII\u2019 or \u2018Confidential\u2019?",
        parsed_document=classification(
            topics=["Sensitive data", "How-to"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-281",
        subject="Exporting glossary terms to CSV",
        body="We need to export our entire glossary for an external audit. Is there a way to export all terms and their linked assets to a CSV file? The manual process is too time-consuming for our team.",
        parsed_document=classification(
            topics=["Glossary", "How-to"],
            sentiment="Frustrated",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-282",
        subject="Snowflake crawler timing out",
        body="Our Snowflake crawler keeps timing out after 30 minutes, and no metadata is ingested. This is critical as our analytics team relies on fresh metadata. Where can we find logs to diagnose this, and what settings can we adjust to prevent timeouts?",
        parsed_document=classification(
            topics=["Connector"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-283",
        subject="How to use Atlan\u2019s Python SDK for querying assets?",
        body="I\u2019m new to Atlan\u2019s Python SDK and want to query assets programmatically. Can you provide a sample script to fetch all tables in a specific schema? This would help our data engineers get started quickly.",
        parsed_document=classification(
            topics=["API/SDK", "How-to"],
            sentiment="Curious",
            priority="p2",
        ),
    ),
    Example(
        id="TICKET-284",
        subject="Lineage not updating after schema change",
        body="We recently modified a table schema in our PostgreSQL database, but the lineage in Atlan hasn\u2019t updated to reflect this. Our analysts are confused by the outdated lineage. How can we force a refresh of the lineage data?",
        parsed_document=classification(
            topics=["Lineage", "Product"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-285",
        subject="Configuring Okta SSO for specific user roles",
        body="We\u2019re setting up Okta SSO and need to assign specific roles to users based on their department. How can we map Okta groups to Atlan roles? We need to ensure only certain users get admin access.",
        parsed_document=classification(
            topics=["SSO", "How-to"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-286",
        subject="Best practices for managing large datasets in Atlan",
        body="We\u2019re onboarding a massive dataset with millions of rows. What are the best practices for managing such large datasets in Atlan to ensure performance isn\u2019t impacted? Our team is new to this scale.",
        parsed_document=classification(
            topics=["Best practices", "Product"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-287",
        subject="Automating asset ownership assignments",
        body="We want to automate the assignment of asset owners based on department tags. Is there a way to set up rules in Atlan to handle this? Manual assignments are becoming a bottleneck for us.",
        parsed_document=classification(
            topics=["How-to", "Best practices"],
            sentiment="Frustrated",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-288",
        subject="PII detection not working for certain columns",
        body="Atlan\u2019s PII detection is missing some columns that clearly contain sensitive data, like email addresses. This is a major issue for our compliance team. Can you explain why this is happening and how to fix it?",
        parsed_document=classification(
            topics=["Sensitive data"],
            sentiment="Angry",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-289",
        subject="How to integrate Atlan with Tableau?",
        body="We use Tableau for our dashboards and want to integrate it with Atlan to pull in metadata. How do we set up this connector, and what metadata can we expect to see in Atlan from Tableau?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-290",
        subject="Exporting lineage as JSON via API",
        body="Our data team needs to export lineage data for a specific table as JSON for a custom application. Is there an API endpoint for this, and can you provide a sample request to get started?",
        parsed_document=classification(
            topics=["API/SDK", "Lineage"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-291",
        subject="Glossary term approval workflow",
        body="We need a process to approve glossary terms before they\u2019re published. Does Atlan support a term approval workflow, and if so, how can we configure it to involve multiple stakeholders?",
        parsed_document=classification(
            topics=["Glossary", "How-to"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-292",
        subject="Crawler failing for BigQuery with permission errors",
        body="Our BigQuery crawler is failing with a permission error, even though we\u2019ve granted the service account all required roles. This is halting our metadata sync. Can you help us identify the missing permissions?",
        parsed_document=classification(
            topics=["Connector"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-293",
        subject="How to set up alerts for metadata changes?",
        body="We want to get notified when metadata for our critical assets changes, like schema updates or new tags. Is there a way to set up alerts in Atlan for this? We need this for governance.",
        parsed_document=classification(
            topics=["How-to", "Product"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-294",
        subject="Lineage not reflecting Airflow DAG changes",
        body="We updated our Airflow DAGs, but the lineage in Atlan still shows the old transformations. This is causing confusion for our analysts. How can we ensure lineage updates promptly?",
        parsed_document=classification(
            topics=["Lineage", "Connector"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-295",
        subject="Using Atlan API to create custom tags",
        body="We need to create custom tags for our assets via the API. Can you share the endpoint and payload structure for this? We\u2019re building an automation to tag assets dynamically.",
        parsed_document=classification(
            topics=["API/SDK", "How-to"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-296",
        subject="Best practices for user onboarding",
        body="We\u2019re rolling out Atlan to a new team. What are the recommended best practices for onboarding users to ensure they adopt the platform quickly and effectively?",
        parsed_document=classification(
            topics=["Best practices"],
            sentiment="Curious",
            priority="p2",
        ),
    ),
    Example(
        id="TICKET-297",
        subject="SSO user attribute mapping issue",
        body="Our SSO setup with Okta is not mapping user attributes correctly, so roles aren\u2019t being assigned as expected. This is blocking several users. Can you guide us on fixing the attribute mapping?",
        parsed_document=classification(
            topics=["SSO"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-298",
        subject="How to visualize data lineage for presentations?",
        body="I need to present our data lineage to stakeholders. Is there a way to export a clean, high-quality lineage diagram from Atlan for use in PowerPoint?",
        parsed_document=classification(
            topics=["How-to", "Lineage"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-299",
        subject="Sensitive data masking options",
        body="We\u2019ve identified PII fields in our database, but we\u2019re unsure how to apply masking in Atlan to protect them. What are the available masking options, and how do we configure them?",
        parsed_document=classification(
            topics=["Sensitive data", "How-to"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-300",
        subject="Fivetran connector setup guide",
        body="We\u2019re integrating Fivetran with Atlan for the first time. Can you provide a detailed guide on setting up the connector and ensuring metadata flows correctly?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-301",
        subject="Automating glossary term linkage via API",
        body="We want to link glossary terms to assets programmatically. Is there an API endpoint for this, and can you provide a Python example for linking a term to an asset?",
        parsed_document=classification(
            topics=["API/SDK", "Glossary"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-302",
        subject="Performance issues with large glossary",
        body="Our glossary has grown to over 1,000 terms, and the UI is starting to lag when browsing or searching terms. This is frustrating our team. Are there settings to optimize performance?",
        parsed_document=classification(
            topics=["Glossary", "Product"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-303",
        subject="Best practices for connector scheduling",
        body="We have multiple connectors running daily, but we\u2019re seeing overlaps causing performance issues. What are the best practices for scheduling connectors to avoid conflicts?",
        parsed_document=classification(
            topics=["Best practices", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-304",
        subject="How to restrict access to sensitive assets?",
        body="We need to restrict access to assets containing sensitive data to only specific teams. How can we configure role-based access control in Atlan to enforce this?",
        parsed_document=classification(
            topics=["How-to", "Sensitive data"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-305",
        subject="Lineage export failing for large datasets",
        body="When we try to export lineage for a large dataset, the process fails with a timeout error. This is critical for our audit. Can you suggest a workaround or fix?",
        parsed_document=classification(
            topics=["Lineage"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-306",
        subject="API authentication token expiration",
        body="Our API scripts are failing because the authentication token expires too quickly. How can we configure token expiration or automate token refresh in Atlan?",
        parsed_document=classification(
            topics=["API/SDK", "How-to"],
            sentiment="Frustrated",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-307",
        subject="SSO setup for Google Workspace",
        body="We\u2019re trying to configure SSO with Google Workspace. Can you provide a step-by-step guide for setting this up in Atlan, including any specific SAML settings we need?",
        parsed_document=classification(
            topics=["SSO", "How-to"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-308",
        subject="How to monitor crawler performance?",
        body="We want to monitor the performance of our connectors\u2019 crawlers to ensure they\u2019re running efficiently. Does Atlan provide metrics or dashboards for this?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p2",
        ),
    ),
    Example(
        id="TICKET-309",
        subject="Glossary term versioning support",
        body="Does Atlan support versioning for glossary terms? We need to track changes to terms over time for audit purposes. If available, how do we enable this feature?",
        parsed_document=classification(
            topics=["Glossary", "Product"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-310",
        subject="Best practices for data lineage documentation",
        body="We\u2019re documenting our data lineage for regulatory purposes. What are the best practices for structuring and maintaining lineage documentation in Atlan?",
        parsed_document=classification(
            topics=["Best practices", "Lineage"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-311",
        subject="Sensitive data scanning performance issues",
        body="The sensitive data scanner is taking too long to process our large database. Our compliance team is frustrated as this delays our reporting. Can we optimize the scanning process?",
        parsed_document=classification(
            topics=["Sensitive data", "Product"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-312",
        subject="How to integrate Atlan with Power BI?",
        body="We\u2019re using Power BI for reporting and want to integrate it with Atlan. How do we set up the connector, and what kind of metadata can we expect to see?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-313",
        subject="API for retrieving user activity logs",
        body="We need to pull user activity logs for a compliance audit. Is there an API endpoint to retrieve these logs, and what\u2019s the structure of the response?",
        parsed_document=classification(
            topics=["API/SDK", "Product"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-314",
        subject="SSO login redirect loop issue",
        body="Our SSO setup with Okta is causing a redirect loop for some users, preventing them from logging in. This is urgent as it\u2019s affecting our team\u2019s productivity. How can we resolve this?",
        parsed_document=classification(
            topics=["SSO"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-315",
        subject="How to create custom dashboards in Atlan?",
        body="We want to create custom dashboards to track metadata usage and adoption. Does Atlan support this, and can you provide guidance on setting it up?",
        parsed_document=classification(
            topics=["How-to", "Product"],
            sentiment="Curious",
            priority="p2",
        ),
    ),
    Example(
        id="TICKET-316",
        subject="Lineage not capturing stored procedures",
        body="Our SQL Server database uses stored procedures, but Atlan isn\u2019t capturing their lineage. This is critical for our data flow analysis. What could be the issue?",
        parsed_document=classification(
            topics=["Lineage", "Connector"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-317",
        subject="Best practices for managing multiple connectors",
        body="We\u2019re using connectors for Snowflake, Redshift, and BigQuery. What are the best practices for managing multiple connectors to avoid performance bottlenecks?",
        parsed_document=classification(
            topics=["Best practices", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-318",
        subject="How to bulk delete unused assets?",
        body="Our catalog has many unused assets from old tests. Is there a way to bulk delete them in Atlan to clean up our catalog? We need to do this before our next audit.",
        parsed_document=classification(
            topics=["How-to", "Product"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-319",
        subject="Sensitive data tags not syncing across connectors",
        body="We\u2019ve tagged sensitive data in one connector, but the tags aren\u2019t syncing to other connectors for the same dataset. This is a compliance issue. How do we fix this?",
        parsed_document=classification(
            topics=["Sensitive data", "Connector"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-320",
        subject="API for updating glossary terms",
        body="We need to update glossary term definitions programmatically. Can you share the API endpoint and a sample payload for updating a term\u2019s description?",
        parsed_document=classification(
            topics=["API/SDK", "Glossary"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-321",
        subject="How to configure notifications for failed crawlers?",
        body="We\u2019ve had a few crawler failures recently, and we want to set up notifications to alert us immediately when a crawler fails. How can we configure this in Atlan?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-322",
        subject="Glossary term relationships not displaying",
        body="We\u2019ve set up relationships between glossary terms, but they\u2019re not showing in the UI. This is confusing our team. Is there a specific setting we need to enable?",
        parsed_document=classification(
            topics=["Glossary", "Product"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-323",
        subject="Best practices for tagging assets",
        body="We\u2019re new to Atlan and want to ensure our assets are tagged correctly. What are the best practices for creating and applying tags to assets effectively?",
        parsed_document=classification(
            topics=["Best practices"],
            sentiment="Curious",
            priority="p2",
        ),
    ),
    Example(
        id="TICKET-324",
        subject="SSO group sync not updating roles",
        body="Our SSO group sync is running, but user roles aren\u2019t updating when their group membership changes. This is causing access issues. How do we troubleshoot this?",
        parsed_document=classification(
            topics=["SSO"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-325",
        subject="How to export metadata for external analysis?",
        body="We need to export metadata for analysis in an external tool. What are the options for exporting metadata from Atlan, and what formats are supported?",
        parsed_document=classification(
            topics=["How-to", "Product"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-326",
        subject="Lineage visualization too cluttered",
        body="The lineage view for our main dataset is too complex and hard to read. Are there ways to simplify or filter the lineage visualization in Atlan?",
        parsed_document=classification(
            topics=["Lineage", "Product"],
            sentiment="Frustrated",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-327",
        subject="Sensitive data report generation",
        body="We need a report listing all assets tagged as sensitive data for our compliance audit. How can we generate this report in Atlan?",
        parsed_document=classification(
            topics=["Sensitive data", "How-to"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-328",
        subject="Connector setup for AWS S3",
        body="We\u2019re trying to connect our AWS S3 bucket to Atlan. What are the required permissions and steps to set up this connector?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-329",
        subject="API rate limits for automation",
        body="Our automation scripts are hitting API rate limits in Atlan. What are the rate limits, and how can we manage them to avoid disruptions?",
        parsed_document=classification(
            topics=["API/SDK"],
            sentiment="Frustrated",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-330",
        subject="Best practices for governance policies",
        body="We\u2019re setting up governance policies in Atlan. What are the recommended best practices for creating policies that ensure compliance and usability?",
        parsed_document=classification(
            topics=["Best practices"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-331",
        subject="SSO user provisioning delays",
        body="New users added via SSO are taking hours to appear in Atlan. This is slowing down our onboarding process. How can we reduce this delay?",
        parsed_document=classification(
            topics=["SSO"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-332",
        subject="How to set up lineage for custom ETL jobs?",
        body="We have custom ETL jobs running outside of supported connectors. How can we configure Atlan to capture lineage for these jobs?",
        parsed_document=classification(
            topics=["How-to", "Lineage"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-333",
        subject="Glossary term search performance",
        body="Searching for glossary terms is slow, especially with our large term set. This is frustrating our users. Are there ways to improve search performance?",
        parsed_document=classification(
            topics=["Glossary", "Product"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-334",
        subject="Sensitive data access audit",
        body="We need to audit who has accessed sensitive data assets in the past month. How can we generate this report in Atlan?",
        parsed_document=classification(
            topics=["Sensitive data", "How-to"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-335",
        subject="Connector for Databricks setup",
        body="We\u2019re using Databricks and want to integrate it with Atlan. What are the steps to set up the connector, and what metadata will it capture?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-336",
        subject="API for deleting assets",
        body="We need to delete outdated assets programmatically. Is there an API endpoint for this, and what\u2019s the correct request format?",
        parsed_document=classification(
            topics=["API/SDK", "How-to"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-337",
        subject="Best practices for metadata validation",
        body="How can we validate metadata accuracy in Atlan to ensure our catalog is reliable? Are there recommended practices or tools for this?",
        parsed_document=classification(
            topics=["Best practices", "Product"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-338",
        subject="SSO logout issues",
        body="Some users are not being logged out properly from Atlan after signing out from our SSO provider. This is a security concern. How do we fix this?",
        parsed_document=classification(
            topics=["SSO"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-339",
        subject="How to track lineage changes over time?",
        body="We need to track how lineage for our datasets has changed over time for audit purposes. Does Atlan support lineage versioning or history?",
        parsed_document=classification(
            topics=["Lineage", "How-to"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-340",
        subject="Glossary term import errors",
        body="We tried importing glossary terms via CSV, but some terms failed to import with an unclear error message. This is blocking our migration. Can you help troubleshoot?",
        parsed_document=classification(
            topics=["Glossary"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-341",
        subject="Sensitive data export restrictions",
        body="We need to ensure sensitive data fields are not included in metadata exports. How can we configure Atlan to exclude these fields?",
        parsed_document=classification(
            topics=["Sensitive data", "How-to"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-342",
        subject="Connector for MySQL setup",
        body="We\u2019re setting up a MySQL connector in Atlan. What are the required configurations, and how do we ensure it captures all metadata?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-343",
        subject="API for retrieving asset relationships",
        body="We need to fetch relationships between assets via the API for a custom dashboard. Can you provide the endpoint and a sample request?",
        parsed_document=classification(
            topics=["API/SDK", "Product"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-344",
        subject="Best practices for asset naming conventions",
        body="We\u2019re seeing inconsistencies in asset names across our catalog. What are the best practices for establishing naming conventions in Atlan?",
        parsed_document=classification(
            topics=["Best practices"],
            sentiment="Curious",
            priority="p2",
        ),
    ),
    Example(
        id="TICKET-345",
        subject="SSO session timeout configuration",
        body="Our SSO sessions are timing out too quickly, causing user frustration. How can we adjust the session timeout settings in Atlan?",
        parsed_document=classification(
            topics=["SSO", "How-to"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-346",
        subject="How to prioritize crawler runs?",
        body="We have multiple crawlers running, but some are more critical than others. How can we prioritize certain crawlers to run first in Atlan?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-347",
        subject="Glossary term duplication issues",
        body="We\u2019re seeing duplicate glossary terms being created accidentally. This is cluttering our catalog. How can we prevent this from happening?",
        parsed_document=classification(
            topics=["Glossary", "Product"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-348",
        subject="Sensitive data classification accuracy",
        body="Atlan\u2019s sensitive data classifier is incorrectly tagging some fields as PII. This is causing compliance issues. How can we improve its accuracy?",
        parsed_document=classification(
            topics=["Sensitive data"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-349",
        subject="How to integrate Atlan with Apache Kafka?",
        body="We want to integrate Atlan with our Kafka pipelines to capture metadata. What are the steps to set up this connector?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-350",
        subject="API for batch tagging assets",
        body="We need to tag multiple assets at once via the API. Can you provide the endpoint and a sample script for batch tagging?",
        parsed_document=classification(
            topics=["API/SDK", "How-to"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-351",
        subject="Best practices for audit log management",
        body="We need to manage audit logs for compliance. What are the best practices for storing and accessing audit logs in Atlan?",
        parsed_document=classification(
            topics=["Best practices", "Product"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-352",
        subject="SSO multi-factor authentication setup",
        body="We want to enable multi-factor authentication with our SSO setup in Atlan. How do we configure this with our identity provider?",
        parsed_document=classification(
            topics=["SSO", "How-to"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-353",
        subject="Lineage for external data sources",
        body="We have external data sources not natively supported by Atlan connectors. How can we manually define lineage for these sources?",
        parsed_document=classification(
            topics=["Lineage", "How-to"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-354",
        subject="Glossary term approval delays",
        body="The approval process for glossary terms is taking too long, delaying our governance tasks. How can we streamline this process in Atlan?",
        parsed_document=classification(
            topics=["Glossary"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-355",
        subject="Sensitive data export compliance",
        body="We need to ensure our metadata exports comply with sensitive data regulations. How can we configure Atlan to enforce these restrictions?",
        parsed_document=classification(
            topics=["Sensitive data", "How-to"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-356",
        subject="Connector for Oracle database",
        body="We\u2019re setting up a connector for our Oracle database. What are the steps and prerequisites for this integration in Atlan?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-357",
        subject="API for monitoring crawler status",
        body="We want to monitor crawler status programmatically. Is there an API endpoint to check the status of ongoing crawler runs?",
        parsed_document=classification(
            topics=["API/SDK", "Connector"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-358",
        subject="Best practices for team collaboration",
        body="How can we improve collaboration between teams in Atlan to ensure consistent metadata management? Any recommended workflows?",
        parsed_document=classification(
            topics=["Best practices"],
            sentiment="Curious",
            priority="p2",
        ),
    ),
    Example(
        id="TICKET-359",
        subject="SSO user role conflicts",
        body="Some users are getting conflicting roles from SSO, causing access issues. How can we resolve these conflicts in Atlan?",
        parsed_document=classification(
            topics=["SSO"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-360",
        subject="How to validate lineage accuracy?",
        body="We need to ensure our lineage data is accurate. What tools or methods does Atlan provide to validate lineage information?",
        parsed_document=classification(
            topics=["Lineage", "How-to"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-361",
        subject="Glossary term bulk update errors",
        body="We tried bulk updating glossary terms via API, but some updates failed without clear errors. This is blocking our project. Can you help debug?",
        parsed_document=classification(
            topics=["Glossary", "API/SDK"],
            sentiment="Frustrated",
            priority="p0",
        ),
    ),
    Example(
        id="TICKET-362",
        subject="Sensitive data field encryption",
        body="Can Atlan encrypt sensitive data fields in the metadata catalog to enhance security? If so, how do we enable this?",
        parsed_document=classification(
            topics=["Sensitive data", "How-to"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-363",
        subject="Connector for Azure Data Lake",
        body="We\u2019re integrating Azure Data Lake with Atlan. What are the steps to configure the connector and ensure metadata capture?",
        parsed_document=classification(
            topics=["How-to", "Connector"],
            sentiment="Curious",
            priority="p1",
        ),
    ),
    Example(
        id="TICKET-364",
        subject="API for retrieving glossary relationships",
        body="We need to fetch relationships between glossary terms via the API. Can you provide the endpoint and a sample request?",
        parsed_document=classification(
            topics=["API/SDK", "Glossary"],
            sentiment="Neutral",
            priority="p1",
        ),
    ),
]
