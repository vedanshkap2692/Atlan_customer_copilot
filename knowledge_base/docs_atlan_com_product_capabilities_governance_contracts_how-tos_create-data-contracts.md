# Create data contractsPrivate Preview
(source: https://docs.atlan.com/product/capabilities/governance/contracts/how-tos/create-data-contracts#view-a-data-contract)

ContractsGet StartedCreate data contractsImpact Analysis

Get StartedCreate data contracts

Create data contracts

Impact Analysis

Build governance

Contracts

Get Started

Create data contracts

A data contract is an agreement between a data producer and consumer that specifies requirements for generating and using high-quality, reliable data. As a powerful tool for data management, data contracts can help you standardize contractual obligations between data producers and consumers, organize your assets with embeddable contract metadata, and enforce them with data quality rules.

In Atlan, you can directly add a data contract to supported assets and provide helpful context to your downstream users.

For a data contract to help build trust in your assets, it should be:

Templatized and easily comprehensible   -  use Atlan's YAML contract template to create standardized contracts and push to Atlan.

Version-controlled   -  continuously validate and monitor your data contracts either in runtime or real-time.

Embeddable   -  embed the contract as metadata for a supported asset.

Enforceable   -  enforce your contracts with data quality rules.

Extensible   -  identify new specifications, generate new versions, and then compare and contrast them.

You cancreate webhooks for data contractsand receive notifications for when a contract is added or updated to a URL of your choice.



## Supported asset typesâ
(source: https://docs.atlan.com/product/capabilities/governance/contracts/how-tos/create-data-contracts#view-a-data-contract)

You can create data contracts for the following asset types:

Tables

Views

Materialized views

Output port assets of data products



## Supported asset metadataâ
(source: https://docs.atlan.com/product/capabilities/governance/contracts/how-tos/create-data-contracts#view-a-data-contract)

Atlan maps the following asset metadata properties to it contract properties:

name

dataset

typeName

type

userDescription

description

description

ownerUsers

owner.users

ownerGroups

owners.groups

certificateStatus

certification.status

certificateStatusMessage

certification.message

announcementType

announcement.type

announcementTitle

announcement.title

announcementMessage

announcement.description

meaningNames

terms

classificationDef.displayName

tags.name

classifications.propagate

tags.propagate

classifications.restrict_propagation_through_lineage

tags.restrict_propagation_through_lineage

classifications.restrict_propagation_through_hierarchy

tags.restrict_propagation_through_hierarchy

column.name

columns.name

column.userDescription

column.description

columns.description

column.dataType

columns.data_type

column.isPrimary

columns.primary

!column.isNullable

columns.required

column.precision

columns.precision

column.numericScale

columns.scale

columns.tags

column.meaningNames

columns.terms

custom_metadata.<CM>



## Add a data contract to an assetâ
(source: https://docs.atlan.com/product/capabilities/governance/contracts/how-tos/create-data-contracts#view-a-data-contract)

Any non-guest user withedit access to an asset's metadatacan create, deploy, and manage data contracts. This only includesadmin and member usersin Atlan.

To add a data contract to an asset, you can either:

Create a contract directly in Atlan from theContractstab of the asset profile. You can create and maintain data contracts as easily as editing a word document.

Use Atlan CLI to import an existing contract from your local machine to Atlan directly or through a CI/CD pipeline.Atlan CLIis a command-line tool that you can download directly from Atlan to your local machine to create and push data contracts to Atlan. Once you have published the contract, you can alsosync metadatafrom a contract to the governed asset in Atlan.

Once created, you will be able to monitor and manage your data contracts in Atlan.

To add a data contract:

From the left menu of any screen in Atlan, clickAssets.

(Optional) From theFiltersmenu on the left, clickPropertiesand then clickHas contract. ClickNoto filter for assets without a contract.

From theAssetspage, select an asset to open the asset sidebar.

In the leftOverviewsidebar, clickAdd contract.

In theContracttab of the asset profile, you can either:ClickCreate contractto create a draft contract directly in Atlan based on asset metadata.ClickImport contractto useAtlan CLIto import an existing contract from your local environment to Atlan. You will first need to install and connect Atlan CLI and then push the contract to Atlan. Refer to ourdeveloper documentationto complete the steps.

ClickCreate contractto create a draft contract directly in Atlan based on asset metadata.

ClickImport contractto useAtlan CLIto import an existing contract from your local environment to Atlan. You will first need to install and connect Atlan CLI and then push the contract to Atlan. Refer to ourdeveloper documentationto complete the steps.

(Optional) Click theEditbutton to edit the contract.

Congrats on adding a data contract in Atlan! ð



## View a data contractâ
(source: https://docs.atlan.com/product/capabilities/governance/contracts/how-tos/create-data-contracts#view-a-data-contract)

To view a data contract:

From the left menu of any screen in Atlan, clickAssets.

From theAssetspage, select an asset to open the asset sidebar.

From the leftOverviewsidebar, clickView contractto navigate to theContractÂ tab in the asset profile.

(Optional) In theContracttab, you can view the contract specifications for your asset in a YAML format. You can also:Click theDocumenticon to open a read-only, simplified view of your contract.Next toPublished version, click the version dropdown to view the latest version of the contract. Select an older version and then clickCompareÂ with published versionto compare them side by side.Click theEditbutton to edit the contract.Click the clipboard icon to copy the YAML code.UnderTimeline, view a timeline for the evolution of your contract.UnderSummary, view details of who last updated your contract and when.

Click theDocumenticon to open a read-only, simplified view of your contract.

Next toPublished version, click the version dropdown to view the latest version of the contract. Select an older version and then clickCompareÂ with published versionto compare them side by side.

Click theEditbutton to edit the contract.

Click the clipboard icon to copy the YAML code.

UnderTimeline, view a timeline for the evolution of your contract.

UnderSummary, view details of who last updated your contract and when.

atlan

documentation

Supported asset types

Supported asset metadata

Add a data contract to an asset

View a data contract
