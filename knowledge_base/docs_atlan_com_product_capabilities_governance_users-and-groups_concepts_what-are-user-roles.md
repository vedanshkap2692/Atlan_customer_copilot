# What are user roles?
(source: https://docs.atlan.com/product/capabilities/governance/users-and-groups/concepts/what-are-user-roles)

Access controlGet startedManage users and groupsConceptsWhat are personas?What are purposes?What are groups?What are user roles?References

Get started

Manage users and groups

ConceptsWhat are personas?What are purposes?What are groups?What are user roles?

What are personas?

What are purposes?

What are groups?

What are user roles?

References

Configure Atlan

Access control

Concepts

What are user roles?



## Overviewâ
(source: https://docs.atlan.com/product/capabilities/governance/users-and-groups/concepts/what-are-user-roles)

All users in Atlan need to be assigned one of the following predefined roles.

User roles play a relatively small part in determining access to metadata and data. For more details on all the possible access control mechanisms, seeHow do I control access to metadata and data?



### Adminâ
(source: https://docs.atlan.com/product/capabilities/governance/users-and-groups/concepts/what-are-user-roles)

AnÂadminuser can manage Atlan:

Set up integrations with external collaboration tools

Set up data connections and run workflows

Manage users, groups, tags, and access policies

Maintain extensions to the metadata

Turn experimental features on and off

In addition, theÂadminuser can do everything theÂmemberuser can do.

There are two optional sub roles within theadminto delegate adminitration for workflows or governance without full platform level admin access.

Theseworkflow and governance sub rolescan be enabled by admins.



### Memberâ
(source: https://docs.atlan.com/product/capabilities/governance/users-and-groups/concepts/what-are-user-roles)

AÂmemberuser can discover, maintain, and query assets:

Find and view metadata for assets

Update metadata for specific assets (via personas and policies)   -  for example,attach tags

Suggest metadata updates for all other assets

Approve or reject suggested metadata changes (via personas and policies)

Preview sample data and query data in specific assets



### Guestâ
(source: https://docs.atlan.com/product/capabilities/governance/users-and-groups/concepts/what-are-user-roles)

AÂguestuser can only discover assets:

Find and view metadata for assets

Suggest updatesto metadata for any assets (ifenabled from the admin center)

Never update metadata for any assets

Preview sample data or query data in specific assets (via personas and policies)



## Detailed permissionsâ
(source: https://docs.atlan.com/product/capabilities/governance/users-and-groups/concepts/what-are-user-roles)

To understand the table of permissions, note the following:

The permission tomanageallows a user to create, read, update, and delete objects.

â   -  capability included.

â   -  capability will be a paid addition, reach out to your customer success manager for more information.

Basic metadata   -  read asset name, description, certificates, and more.Permission to act may be limited.

integration

connectors

Overview

Detailed permissions
