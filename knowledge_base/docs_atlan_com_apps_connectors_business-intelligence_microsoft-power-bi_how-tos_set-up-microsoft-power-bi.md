# Set up Microsoft Power BI
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

Microsoft Power BIGet StartedSet up Microsoft Power BICrawl Power BI AssetsReferencesTroubleshootingFAQ

Get StartedSet up Microsoft Power BI

Set up Microsoft Power BI

Crawl Power BI Assets

References

Troubleshooting

FAQ

Connect data

BI Tools

On-premises & Enterprise BI

Microsoft Power BI

Get Started

Set up Microsoft Power BI

Depending on the authentication method you choose, you may need a combination of yourCloud Application AdministratororApplication Administratorfor Microsoft Entra ID, Microsoft 365 administrator for Microsoft 365, andFabric Administrator(formerly known as Power BI Administrator) for Microsoft Power BI to complete these tasks -> you may not have access yourself.

This guide outlines how to set up Microsoft Power BI so it can connect with Atlan for metadata extraction and lineage tracking.



## Before you beginâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)



### Register application in Microsoft Entra IDâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

You need yourCloud Application AdministratororApplication Administratorto complete these stepsâ> you may not have access yourself. This is required if the creation of registered applications isn't enabled for the entire organization.

To register a new application in Microsoft Entra ID:

Log in to theAzure portal.

Search forMicrosoft Entra IDand select it.

ClickApp registrationsfrom the left menu.

Click+ New registration.

Enter a name for your client application and clickRegister.

From the Overview screen, copy and securely store:Application (client) IDDirectory (tenant) ID

Application (client) ID

Directory (tenant) ID

ClickCertificates & secretsfrom the left menu.

UnderClient secrets, click+ New client secret.

Enter a description, select an expiry time, and clickAdd.

Copy and securely store the client secretValue.



### Create security group in Microsoft Entra IDâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

You need yourCloud Application AdministratororApplication Administratorto complete these steps - you may not have access yourself.

To create a security group for your application:

Log in to theAzure portal.

Search forMicrosoft Entra IDand select it.

ClickGroupsunder the Manage section.

ClickNew group.

Set the Group type toSecurity.

Enter a Group name and optional description.

ClickNo members selected.

Add the appropriate member:For Delegated User authentication: search for the user and select it.For Service Principal authentication: search for the application registration created earlier and select it.

For Delegated User authentication: search for the user and select it.

For Service Principal authentication: search for the application registration created earlier and select it.

ClickSelectand thenCreate.

By the end of these steps, you have registered an application with Microsoft Entra ID and created a Security Group with the appropriate member.



## Configure authentication optionsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

Atlan supports two authentication methods for fetching metadata from Microsoft Power BI:



### Service principal authentication (recommended)â
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

When using Service Principal authentication, you must decide how the connector shall access metadata to catalog assets and build lineage. There are two supported options:



#### Admin API onlyâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

This option grants permissions that let the service principal to access only admin-level Power BI APIs. In this mode, Atlan extracts metadata exclusively using administrative endpoints. This option is recommended for stricter access control environments.

You need yourFabric Administrator(formerly known as Power BI Administrator) to complete these tasks - you may not have access yourself.

To configure admin API access:

Log in to thePower BI admin portal.

ClickTenant settingsunder Admin portal.

UnderAdmin API settings:ExpandEnable service principals to use read-only Power BI admin APIsand set toEnabledAdd your security group underSpecific security groupsClickApplyExpandEnhance admin APIs responses with detailed metadataand set toEnabledAdd your security groupClickApplyExpandEnhance admin APIs responses with DAX and mashup expressionsand set toEnabledAdd your security groupClickApply

ExpandEnable service principals to use read-only Power BI admin APIsand set toEnabledAdd your security group underSpecific security groupsClickApply

Add your security group underSpecific security groups

ClickApply

ExpandEnhance admin APIs responses with detailed metadataand set toEnabledAdd your security groupClickApply

Add your security group

ClickApply

ExpandEnhance admin APIs responses with DAX and mashup expressionsand set toEnabledAdd your security groupClickApply

Add your security group

ClickApply



#### Admin and non-admin APIsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

This option grants permissions that let the service principal to access both admin and non-admin Power BI APIs. This enables Atlan to extract richer metadata and build detailed lineage across Power BI assets.



##### Assign security group to Power BI workspaces in PowerBI service portalâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

You need to be at least a member of the Microsoft Power BI workspace to which you want to add the security group to complete these steps - you may not have access yourself. Make sure that you add the security group from the homepage and not the admin portal.

To assign a Microsoft Power BI workspace role to the security group:

Open theMicrosoft Power BI homepage.

OpenWorkspacesand select the workspace you want to access from Atlan.

ClickAccess.

In the panel:Enter the name of your security group where it saysEnter email addressesChoose one of the following roles:Viewer: For workspaces without parametersContributor: For workspaces with semantic models containing parameters or to generate lineage for measuresMember: To generate lineage for dataflowsClickAdd.

Enter the name of your security group where it saysEnter email addresses

Choose one of the following roles:Viewer: For workspaces without parametersContributor: For workspaces with semantic models containing parameters or to generate lineage for measuresMember: To generate lineage for dataflows

Viewer: For workspaces without parameters

Contributor: For workspaces with semantic models containing parameters or to generate lineage for measures

Member: To generate lineage for dataflows

ClickAdd.



##### Configure admin and non-admin API access in PowerBI Service Portalâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

You need yourFabric Administrator(formerly known as Power BI Administrator) to complete these tasks - you may not have access yourself.

To enable both admin and non-admin API access:

Log in to thePower BI admin portal.

ClickTenant settingsunder Admin portal.

UnderDeveloper settings:ExpandService principals can use Fabric APIsand set toEnabledAdd your security group underSpecific security groupsClickApply

ExpandService principals can use Fabric APIsand set toEnabledAdd your security group underSpecific security groupsClickApply

Add your security group underSpecific security groups

ClickApply

UnderAdmin API settings:ExpandEnable service principals to use read-only Power BI admin APIsand set toEnabledAdd your security groupClickApplyExpandEnhance admin APIs responses with detailed metadataand set toEnabledAdd your security groupClickApplyExpandEnhance admin APIs responses with DAX and mashup expressionsand set toEnabledAdd your security groupClickApply

ExpandEnable service principals to use read-only Power BI admin APIsand set toEnabledAdd your security groupClickApply

Add your security group

ClickApply

ExpandEnhance admin APIs responses with detailed metadataand set toEnabledAdd your security groupClickApply

Add your security group

ClickApply

ExpandEnhance admin APIs responses with DAX and mashup expressionsand set toEnabledAdd your security groupClickApply

Add your security group

ClickApply

After making these changes, you typically need to wait 15-30 minutes for the settings to take effect across Microsoft's services.



### Delegated user authenticationâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

Atlan doesn't recommend using delegated user authentication as it's also not recommended by Microsoft.



#### Fabric administrator role assignmentâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

You need your Microsoft 365 administrator to complete these steps - you may not have access yourself.

To assign the delegated user to theFabric Administratorrole:

Open theMicrosoft 365 admin portal.

ClickUsersand thenActive usersfrom the left menu.

Select the delegated user.

UnderRoles, clickManage roles.

ExpandShow all by category.

UnderCollaboration, selectFabric Administrator.

ClickSave changes.



#### API permissionsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

You need yourCloud Application AdministratororApplication Administratorto complete these steps, you may not have access yourself.

The following permissions are only required for delegated user authentication. If using service principal authentication, you don't need to configure any delegated permissions for a service principalâit'srecommendedthat you avoid adding these permissions. These are never used and can cause errors that may be hard to troubleshoot.

To add permissions for theregistered application:

In your app registration, clickAPI permissionsunder the Manage section.

ClickAdd a permission.

Search for and selectPower BI Service.

ClickDelegated permissionsand select:Capacity.Read.AllDataflow.Read.AllDataset.Read.AllReport.Read.AllTenant.Read.AllWorkspace.Read.All

Capacity.Read.All

Capacity.Read.All

Dataflow.Read.All

Dataflow.Read.All

Dataset.Read.All

Dataset.Read.All

Report.Read.All

Report.Read.All

Tenant.Read.All

Tenant.Read.All

Workspace.Read.All

Workspace.Read.All

ClickGrant Admin consent(If you only see theAdd permissionsbutton, you aren't an administrator).



#### Admin API settings configurationâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/how-tos/set-up-microsoft-power-bi#admin-api-settings-configuration)

You need yourFabric Administrator(formerly known as Power BI Administrator) to complete these tasks, you may not have access yourself.

To enable the Microsoft Power BI admin API:

Log in to thePower BI admin portal.

ClickTenant settingsunder Admin portal.

UnderAdmin API settings:ExpandEnhance admin APIs responses with detailed metadataand set toEnabledAdd your security groupClickApplyExpandEnhance admin APIs responses with DAX and mashup expressionsand set toEnabledAdd your security groupClickApply.

ExpandEnhance admin APIs responses with detailed metadataand set toEnabledAdd your security groupClickApply

Add your security group

ClickApply

ExpandEnhance admin APIs responses with DAX and mashup expressionsand set toEnabledAdd your security groupClickApply.

Add your security group

ClickApply.

data

authentication

Before you begin

Configure authentication options
