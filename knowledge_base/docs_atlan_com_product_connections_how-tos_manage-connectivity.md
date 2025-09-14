# Manage connectivity
(source: https://docs.atlan.com/product/connections/how-tos/manage-connectivity)

Connector FrameworkHow-tosManage connectivityMonitor connectivityConnect data sources for Azure-hosted Atlan instancesMine queries through S3How to order workflowsHow to provide SSL certificatesConceptsReferencesFAQ

How-tosManage connectivityMonitor connectivityConnect data sources for Azure-hosted Atlan instancesMine queries through S3How to order workflowsHow to provide SSL certificates

Manage connectivity

Monitor connectivity

Connect data sources for Azure-hosted Atlan instances

Mine queries through S3

How to order workflows

How to provide SSL certificates

Concepts

References

FAQ

Connect data

Connectivity Framework

Connector Framework

How-tos

Manage connectivity

Once you've scheduled or run a workflow you can modify its configuration at any time. The configuration that can be modified may vary by workflow but the general steps remain consistent.



## Modify connectivityâ
(source: https://docs.atlan.com/product/connections/how-tos/manage-connectivity)

To modify the configuration of an existing workflow, complete the following steps.

On the left of any screen, navigate toÂWorkflow.

UnderMonitorselect an existing workflow tile. (You may need to expand the run history or filter first.)

From theWorkflow Run Historytable, click on the previous run of the workflow you want to modify.

In the upper left of the screen, change to theConfigtab.

Modify the parts of the workflow configuration you require:Under<Connector>Credential, use theEdit Credentialsbutton to change the credentials for the source.dangerIf you're updating the connection credentials, you may also need to update the metadata filters before running the updated workflow. Atlan currently does not detect changes to your connection settings and update the metadata filters automatically.UnderConnection settings, use theEditÂ button to change the connection details:Modify whether or not querying or data previews are allowed for the source.Modify the query row limit to enableexporting large query results via email.Modify the query timeout limit   -  expandable up to 60 minutes.UnderConnection Admins, click the pencil icon to add or remove connection admins.dangerIf you do not specify any user or group, nobody will be able to manage the connection   -  not even admins.UnderMetadata, use the selectors to modify which metadata to include and exclude.To check for anypermissions or other configuration issuesbefore running the workflow, clickPreflight checks.

Under<Connector>Credential, use theEdit Credentialsbutton to change the credentials for the source.dangerIf you're updating the connection credentials, you may also need to update the metadata filters before running the updated workflow. Atlan currently does not detect changes to your connection settings and update the metadata filters automatically.

Under<Connector>Credential, use theEdit Credentialsbutton to change the credentials for the source.

<Connector>

If you're updating the connection credentials, you may also need to update the metadata filters before running the updated workflow. Atlan currently does not detect changes to your connection settings and update the metadata filters automatically.

UnderConnection settings, use theEditÂ button to change the connection details:Modify whether or not querying or data previews are allowed for the source.Modify the query row limit to enableexporting large query results via email.Modify the query timeout limit   -  expandable up to 60 minutes.

UnderConnection settings, use theEditÂ button to change the connection details:

Modify whether or not querying or data previews are allowed for the source.

Modify the query row limit to enableexporting large query results via email.

Modify the query timeout limit   -  expandable up to 60 minutes.

UnderConnection Admins, click the pencil icon to add or remove connection admins.dangerIf you do not specify any user or group, nobody will be able to manage the connection   -  not even admins.

UnderConnection Admins, click the pencil icon to add or remove connection admins.

If you do not specify any user or group, nobody will be able to manage the connection   -  not even admins.

UnderMetadata, use the selectors to modify which metadata to include and exclude.

UnderMetadata, use the selectors to modify which metadata to include and exclude.

To check for anypermissions or other configuration issuesbefore running the workflow, clickPreflight checks.

To check for anypermissions or other configuration issuesbefore running the workflow, clickPreflight checks.

Once you've made your updates, click theÂUpdatebutton to save the changes.You can optionally run the workflow with the new configuration immediately.You will need to confirm your changes by clicking theÂYesbutton. Note that some workflow changes may take a few minutes to come into effect.

You can optionally run the workflow with the new configuration immediately.

You will need to confirm your changes by clicking theÂYesbutton. Note that some workflow changes may take a few minutes to come into effect.

That's it   -  next time you run the workflow, or it runs on its schedule, it will use your changes! ð

If you modify theMetadataportion, any previously crawled metadata that is now excluded will bearchivedon the next workflow run.

integration

connectors

workflow

automation

orchestration

Modify connectivity
