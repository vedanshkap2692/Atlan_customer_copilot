# What does Atlan crawl from Looker?
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

LookerGet StartedCrawl Looker AssetsReferencesWhat does Atlan crawl from Looker?Preflight checks for LookerTroubleshooting

Get Started

Crawl Looker Assets

ReferencesWhat does Atlan crawl from Looker?Preflight checks for Looker

What does Atlan crawl from Looker?

Preflight checks for Looker

Troubleshooting

Connect data

BI Tools

Cloud-based BI

Looker

References

What does Atlan crawl from Looker?

Atlan crawls and maps the following assets and properties from Looker.

Atlan also supports the following lineage:

Asset-level lineage for views, models, looks, dashboards, tiles, and explores.

Field-level lineage for views, explores, looks, tiles, and dashboards.

Lineage between explore fields and dashboards. This allows you to view all the fields used in a given dashboard and trace their upstream lineage to SQL columns.

Cross-project lineage for Looker assets. For example, if an explore includes a view from an imported project, Atlan will parseproject manifest filesto generate lineage.

Looker refinementsfor views and explores. Atlan will parseproject manifest filesto generate lineage. Refined fields for views and explores are displayed with aRefinementlabel in Atlan.

Currently Atlan only represents the assets marked with ð in lineage.



## Connectionsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps connections from Looker to itsConnectionasset type.

Connection

name

name

host

host

port

port

database

database

schema

schema

dialect_name

dialect_name

created_at

sourceCreatedAt



## Projectsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps projects from Looker to itsLookerProjectasset type.

LookerProject

name

name



## Views ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps views from Looker to itsLookerViewasset type. To trace the upstream lineage of these views, Atlan currently supportsSQL-based derived tables. Persistent derived tables (PDTs) and Liquid parameterized tables are currently not supported. However, Atlan will always catalog the associated views.

LookerView

Atlan also supportsview refinements. Atlan includes the fields from refinements in the parent view asset, and marks the fields with aRefinementlabel. You can hover over the label to view the file path and line number where the refinement is defined.

name

name

description

description

project_name

projectName



## Models ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps models from Looker to itsLookerModelasset type.

LookerModel

label

name

project_name

projectName

certificateStatus (DEPRECATED)

certificateStatusMessage ("Project attached to this model was not found by the workflow in Looker.")



## Foldersâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps folders from Looker to itsLookerFolderasset type.

LookerFolder

name

name

content_metadata_id

sourceContentMetadataId

creator_id

sourceCreatorId

child_count

sourceChildCount

parent_id

sourceParentID

created_at

sourceCreatedAt



## Fields ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)



### For exploresâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps fields for explores from Looker to itsLookerFieldasset type.

LookerField

label

name

description

description

category

subType

project_name

projectName

model_name

modelName

lookerFieldIsRefined

lookerFieldRefinementFilePath

lookerFieldRefinementLineNumber



### For viewsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps fields for views from Looker to itsLookerFieldasset type.

LookerField

name

name

category

subType

project_name

projectName

lookerFieldIsRefined

lookerFieldRefinementFilePath

lookerFieldRefinementLineNumber



### For looksâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps fields for looks from Looker to itsLookerFieldasset type.

LookerField

name

name

look

look



### For tilesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps fields for tiles from Looker to itsLookerFieldasset type.

LookerField

name

name

tile

tile



### For dashboardsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps fields for dashboards from Looker to itsLookerFieldasset type.

LookerField

name

name

dashboard

dashboard



## Looks ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps looks from Looker to itsLookerLookasset type.

LookerLook

title

name

description

description

folder_name

folderName

user_id

sourceUserId

view_count

sourceViewCount

last_updater_id

sourceLastUpdaterId

last_updater_name

sourceUpdatedBy

user_name

sourceOwners

content_metadata_id

sourceContentMetadataId

query_id

lookerSourceQueryId

last_accessed_at

sourceLastAccessedAt

last_viewed_at

sourceLastViewedAt

created_at

sourceCreatedAt

updated_at

sourceUpdatedAt



## Dashboards ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps dashboards from Looker to itsLookerDashboardasset type.

LookerDashboard

title

name

description

description

slug

lookerSlug

folder_name

folderName

user_id

sourceUserId

view_count

sourceViewCount

last_updater_id

sourceLastUpdaterId

last_updater_name

sourceUpdatedBy

user_name

sourceOwners

content_metadata_id

sourceMetadataId

last_accessed_at

sourceLastAccessedAt

last_viewed_at

sourceLastViewedAt

created_at

sourceCreatedAt

updated_at

sourceUpdatedAt



## Tiles ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps tiles from Looker to itsLookerTileasset type.

LookerTile

title

name

title

Look Deleted

certificateStatus (DEPRECATED)

title

Look Deleted

certificateStatusMessage ("Look attached to this tile has been deleted. This tile might be unusable.")

body_text

description

lookml_link_id

lookml_link_id

merge_result_id

merge_result_id

note_text

noteText

query_id

lookerQueryID

result_maker_id

resultMakerID

look_id

lookId

subtitle_text

subtitleText

type

subType



## Explores ðâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/looker/references/what-does-atlan-crawl-from-looker)

Atlan maps explores from Looker to itsLookerExploreasset type.

LookerExplore

Atlan also supportsexplore refinements:

For explores defined in the same model, Atlan includes the fields from refinements in the parent explore asset.

For explores with the same name that are defined in a different model, Atlan will create a new explore asset.

In both cases, Atlan marks the fields with aRefinementlabel. You can hover over the label to view the file path and line number where the refinement is defined.

title

name

id

name

description

description

model_name

modelName

connection_name

sourceConnectionName

user_name

sourceOwners

view_name

viewName

sql_table_name

sqlTableName

project_name

projectName

crawl

model

Connections

Projects

Views ð

Models ð

Folders

Fields ð

Looks ð

Dashboards ð

Tiles ð

Explores ð
