# Control access to metadata and data?
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

Custom MetadataGet StartedAccess ManagementControl access to metadata and data?Disable data accessBadge ManagementStructure ManagementReferencesConceptsFAQ

Get Started

Access ManagementControl access to metadata and data?Disable data access

Control access to metadata and data?

Disable data access

Badge Management

Structure Management

References

Concepts

FAQ

Build governance

Custom Metadata

Access Management

Control access to metadata and data?

You can customize access for users through several mechanisms.



## User rolesâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

The most general mechanism is aÂuser role. These define the very broad permissions a user has in Atlan   -  for example, whether they can administer other users, or only discover metadata. When it comes towhatmetadata and data a user can access, though, we need to use the additional mechanisms below.



## Connection adminsâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

Connection admins are users who manage connectivity to a data source. By default, these users can:

Read and write all metadata on assets from that connection.

Preview and query the data in all data assets from that connection.

Manage access policies to grant others access to the assets from that connection.

You define the connection admin when crawling a new data source for the first time. A connection admin can also extend the list of connection admins on their connection at any time.



## Access policiesâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

A user must be both anadmin userand a connection admin to define access policies for the connection's assets.

Access policies either allow or restrict access to certain assets. These allow you to be much more creative (and granular) about access than the all-or-nothing privileges of connection admins.

You start by defining which assets to control with each policy. There are two complementary mechanisms to do this in Atlan   -personasandpurposes.

Once you have defined the subset of assets, you can then define granular access to both metadata and data:



### Metadata policiesâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

Metadata policies control what users can do with the assets' metadata. Through them, you can control who can:

Read: view an asset's activity log, custom metadata, and SQL queries

Update: change asset metadata, including description, certification, owners, README, and resources

Update Custom Metadata Valuesfor the assets

Add Tagsto the assets

Remove Tagsfrom the assets

Add Termsto the assets

Remove Termsfrom the assets

Create: create new assets within the selected connection (via API)

Delete: delete assets within the selected connection (via API)



### Data policiesâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

Data policies control what users can do with the assets' data. Through them, you can control who can:

Query and preview the data within the assets

Whether to hide any data, through various masking techniques:Show first 4: replaces all the data withXexcept the first 4 characters of data. For example1234 5678 9012 3456would become1234XXXX.Show last 4: replaces all the data with X except the last 4 characters of data. For example1234 5678 9012 3456would becomeXXXX3456.Hash: replaces the data with a consistent hashed value. Because the hash is consistent you can still join on it across assets. For example1234 5678 9012 3456would becomef43jknscakc12nk21ak.Nullify: replaces the data with the null value. For example1234 5678 9012 3456would becomenull.Redact: replaces all alphabetic data with x and all numeric data with 0. For example1234 Street Namewould become0000 Xxxxxx Xxxx.

Show first 4: replaces all the data withXexcept the first 4 characters of data. For example1234 5678 9012 3456would become1234XXXX.

X

1234 5678 9012 3456

1234XXXX

Show last 4: replaces all the data with X except the last 4 characters of data. For example1234 5678 9012 3456would becomeXXXX3456.

1234 5678 9012 3456

XXXX3456

Hash: replaces the data with a consistent hashed value. Because the hash is consistent you can still join on it across assets. For example1234 5678 9012 3456would becomef43jknscakc12nk21ak.

1234 5678 9012 3456

f43jknscakc12nk21ak

Nullify: replaces the data with the null value. For example1234 5678 9012 3456would becomenull.

1234 5678 9012 3456

null

Redact: replaces all alphabetic data with x and all numeric data with 0. For example1234 Street Namewould become0000 Xxxxxx Xxxx.

1234 Street Name

0000 Xxxxxx Xxxx



### Glossary policiesâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

Glossary policies control what users can do with glossary metadata   -  terms and categories. Through them, you can control who can do the following against each glossary:

Read permission on terms, categories, and glossaries exists by default and cannot be modified. Glossary policies do not restrict users from viewing any glossary and its contents within theGlossarysection.

Create terms and categories inside the glossary

Update descriptions, certification, owners, READMEs, and resources for the glossary, terms and categories

Link terms in the glossary with all other assets

Delete terms and categories inside the glossary

Add tags to the terms

Remove tags from the terms

Update custom metadata values for the terms and categories inside the glossary

Glossary policies can only be defined through personas.



## Interactionsâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

All the mechanisms above can coexist. This is powerful, but can also be a bit overwhelming to think about.Â What takes priority when a user is under the control of all these mechanisms? ðµâð«

It's actually not as bad as you might think   -  only these three rules:



### Access is denied by default (implicitly)â
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

By default, users will not have the permissions listed above. This remains true until you explicitly grant a user a permission.

For example, imagine you have not set up any access policies and a new user joins.

They will not have any of the permissions above againstanyassets in Atlan.

Users have read permission on terms, categories, and glossaries by default in Atlan.



### Explicit grants (allows) are combinedâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

When you grant a user a permission, this is combined with all other permissions you have granted the user.

Continuing our example, imagine you add the new user to a group defined as the connection admins for Snowflake.

The user will now have full read/write access to all metadata for Snowflake assets, and be able to query and preview the data in those assets.

Then you add the user to a persona that gives read/write access to a Looker project.

The user will now have access to all Snowflake assets and a Looker project's assets.



### Explicit restrictions (denies) take priorityâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/control-access-metadata-data)

When you explicitly deny a user a permission, this takes priority over all other permissions you have granted the user.

Continuing our example, imagine you define a purpose with a data policy that masks PII data.

The user will still have full read/write access to all metadata for Snowflake assets and a Looker project's assets.

In general, they will still be able to query and preview the data in the Snowflake assets.

However, any PII data in Snowflake will now be masked.

Then you add a metadata policy to the purpose that denies permission to remove the PII tag.

The user will no longer have full read/write access to all metadata for Snowflake assets and a Looker project's assets.

The user can no longer remove the PII tag from any of these assets.

The combination of mechanisms in the example above shows their power. Through a small number of controls we can define wide-ranging but granular access permissions.

atlan

documentation

User roles

Connection admins

Access policies

Interactions
