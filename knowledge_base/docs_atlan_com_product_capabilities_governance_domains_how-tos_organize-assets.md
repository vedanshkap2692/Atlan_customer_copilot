# Organize assets
(source: https://docs.atlan.com/product/capabilities/governance/domains/how-tos/organize-assets)

DomainsGet StartedAsset OrganizationHow to organize assets

Get Started

Asset OrganizationHow to organize assets

How to organize assets

Build governance

Domains

Asset Organization

How to organize assets

Anynon-guest user with edit access to an asset's metadatacan add assets to domains. This only includes admin and member users.Domain policiescurrently do not have any impact outside theproducts module.

You can map and organize your assets intodomains and subdomains. Domains provide you with a logical structure to group and govern your assets that aligns with business needs and ensures a curated discovery experience.

To add assets to a domain, note the following:

You can link assets to domains irrespective of whether or not you usedata products.

You can only add assets to any one specific domain or subdomain. Assets may be used across multiple domains, but can only belong to one domain or subdomain.

You can filter assets by a single domain, multiple domains, or no domains.

Atlan currently does not support adding glossaries, categories, and terms to domains.

Atlan currently does not supportraising a requestto add assets to domains.

Admin users can bulk add assets to domains usingplaybooks.



## Add an asset to a domainâ
(source: https://docs.atlan.com/product/capabilities/governance/domains/how-tos/organize-assets)

You can alsoset up playbooksto bulk add assets to your domains and subdomains. You will need to be an admin user in Atlan to create playbooks.

To add an asset to a domain, complete the following steps.

To add an asset to a domain:

From the left menu of any screen in Atlan, clickAssets.

On theAssetspage, click an asset to open the asset sidebar.

In theOverviewsidebar, underDomains, clickAdd to domain.

In the popup, check the boxes to select the domain or subdomain to which you want to add the asset. You can only select any one parent domain or nested subdomain.

(Optional) Hover over the linked domain or subdomain to view details in a popover, including the user that added the domain. You can also:ClickView domainto view the domain profile from the governance center.If theproducts module is turned off, you will need to be an admin user in Atlan to view the domain.If theproducts module is turned on,domain policieswill determine your ability to view the domain.Click the unlink icon to remove the asset from the linked domain.

ClickView domainto view the domain profile from the governance center.If theproducts module is turned off, you will need to be an admin user in Atlan to view the domain.If theproducts module is turned on,domain policieswill determine your ability to view the domain.

If theproducts module is turned off, you will need to be an admin user in Atlan to view the domain.

If theproducts module is turned on,domain policieswill determine your ability to view the domain.

Click the unlink icon to remove the asset from the linked domain.

(Optional) Click the pencil icon to change to a different domain or remove it from the asset.

(Optional) In theFiltersmenuon the left, clickDomainsto filter assets by domains:Check the boxes to select one or more domains or subdomains to filter your assets.ClickNo domainsto filter assets not mapped to any domain.

Check the boxes to select one or more domains or subdomains to filter your assets.

ClickNo domainsto filter assets not mapped to any domain.

To programmatically add assets to a domain or remove them from a linked domain, refer to ourdeveloper documentation.

atlan

documentation

Add an asset to a domain
