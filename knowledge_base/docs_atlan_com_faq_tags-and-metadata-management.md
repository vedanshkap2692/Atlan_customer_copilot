# Tags and Metadata Management
(source: https://docs.atlan.com/faq/tags-and-metadata-management#why-does-tag-propagation-take-time-to-apply)

Frequently Asked QuestionsAdministration and ConfigurationAI and Automation FeaturesData Connections and IntegrationSecurity and ComplianceTags and Metadata ManagementUser Management and Access ControlWorkflows and Data Processing

Administration and Configuration

AI and Automation Features

Data Connections and Integration

Security and Compliance

Tags and Metadata Management

User Management and Access Control

Workflows and Data Processing

Configure Atlan

Frequently Asked Questions

Tags and Metadata Management

Complete guide to managing tags, classifications, and metadata in Atlan for effective data governance and organization.



### What are some examples of tags?â
(source: https://docs.atlan.com/faq/tags-and-metadata-management#why-does-tag-propagation-take-time-to-apply)

To learn more about examples of tags, seeWhat are tags?



### Why does tag propagation take time to apply?â
(source: https://docs.atlan.com/faq/tags-and-metadata-management#why-does-tag-propagation-take-time-to-apply)

Whentag propagation is enabled, it automatically triggers a background task in the metastore. This background task is created to reduce the API load and response time. After each background task has been created, the API simply returns a 200 OK response code.

Tag propagation is completed once the background tasks have been executed - includingtag attachmentorremovalby propagation.

The lifecycle of a background task:

When a background task is created for tag propagation, its status changes toPENDING. Multiple tasks may be in the samePENDINGstate, depending on the number of assets to be propagated.

PENDING

PENDING

As a task gets picked up, its status changes toIN PROGRESS. As each task is executed, the tag is propagated to an asset.

IN PROGRESS

Once the task is completed, its status changes toCOMPLETE. As the next task gets picked up, this cycle repeats until tag propagation is completed for all the assets.

COMPLETE



### How are tags propagated for new assets?â
(source: https://docs.atlan.com/faq/tags-and-metadata-management#why-does-tag-propagation-take-time-to-apply)

Tag propagationis disabled by default in Atlan. If you haveenabled tag propagation, tags are automatically propagated to a child or downstream asset created after running a workflow. This means that when a new asset is registered, tag propagation is automatically triggered in the metastore and runs as a background task.

For example, if a workflow adds an additional column to a table, a new background task for adding tags is created in the metastore. This new task is executed when all the previous tasks have been completed in the queue. The speed with which these tasks are completed depends on the number of pending tasks and the volume of tags to be added or removed. The same process also applies totag deletionand updating tags throughplaybooks.



### Can I delete a tag?â
(source: https://docs.atlan.com/faq/tags-and-metadata-management#why-does-tag-propagation-take-time-to-apply)

Tags can be deleted, but this requires careful consideration due to their impact on data governance. For detailed instructions on tag deletion, see thetag deletion guide.



### Is reverse tag sync supported for column-level tags?â
(source: https://docs.atlan.com/faq/tags-and-metadata-management#why-does-tag-propagation-take-time-to-apply)

Reverse tag sync capabilities depend on your data source and configuration. For specific data source support and configuration options, consult the connector documentation or contact Atlan support.

data

api

faq-metadata
