# Data Products
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

Data ProductsGet StartedStakeholder ManagementProduct ManagementDomain ManagementConceptsWhat is business lineage?What is a product score?What are data products?

Get Started

Stakeholder Management

Product Management

Domain Management

ConceptsWhat is business lineage?What is a product score?What are data products?

What is business lineage?

What is a product score?

What are data products?

Configure Atlan

Data Products

Concepts

What are data products?

âAvailable via the Data Marketplace package

From a single data table to a collection of data assets, anything can be a data product in Atlan. Data products provide a framework for your teams to curate assets specific to a domain, business unit, region of operation, brand, and more. These curated data products then empower your data consumers to easily discover data assets, quickly get the context they need, and collaborate more efficiently.

As organizations shift from centralized data architectures, build a new paradigm of governance with data products in Atlan.



## Enable products moduleâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

You will need to be anadmin userin Atlan to enable the products module for your organization.

To enable data products for your Atlan users:

From the left menu of any screen in Atlan, clickAdmin.

Under theWorkspaceheading, clickLabs.

On theLabspage, turn onProducts moduleto enable your users to create and managedata domainsandproducts.

In theWho can access Products moduledialog, you can configure access to the module for the following sets of users:ClickOnly adminsto enable the products module for admin users only.ClickSelected personasto enable the products module for specificpersonaswithdomain policies. Select the persona(s) to which you want to limit usage of the products module.If there are no personas with domain policies, you can either create anew persona with a domain policyoradd a domain policyto an existing persona.Include all adminsis selected by default. This allows any admin user to access and manage the module irrespective of whether they belong to the specified personas. (Optional) Uncheck theInclude all adminscheckbox to remove the default selection.ClickAll users and personasto enable the products module for all your Atlan users and personas.

ClickOnly adminsto enable the products module for admin users only.

ClickSelected personasto enable the products module for specificpersonaswithdomain policies. Select the persona(s) to which you want to limit usage of the products module.If there are no personas with domain policies, you can either create anew persona with a domain policyoradd a domain policyto an existing persona.Include all adminsis selected by default. This allows any admin user to access and manage the module irrespective of whether they belong to the specified personas. (Optional) Uncheck theInclude all adminscheckbox to remove the default selection.

If there are no personas with domain policies, you can either create anew persona with a domain policyoradd a domain policyto an existing persona.

Include all adminsis selected by default. This allows any admin user to access and manage the module irrespective of whether they belong to the specified personas. (Optional) Uncheck theInclude all adminscheckbox to remove the default selection.

ClickAll users and personasto enable the products module for all your Atlan users and personas.

(Optional) ClickConfigureto update your user selections for access to the module.

(Optional) To hide theproduct scorecardon your data products, turn offProduct score.

(Optional) To enable your users to search for data products fromasset discovery, turn onShow products in asset discovery.

If you'd like to disable theProductsmodule from your organization's Atlan workspace, follow the steps above to turn it off.

Once enabled, you can also temporarily disable the module and turn it on again as needed. For any domains and products you may have created, this will not result in any data loss.



## Order of operationsâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

To start using data products, you will need to:

Create a data domain

(Optional)Add data subdomains

Create domain policies

Create data productswithin the data domain

Discover and collaborate on data products

Track and monitor domain usage



## Stakeholdersâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

Atlan currently supports addingpredefined stakeholders and creating custom onesfor your data domains and subdomains. These are responsibilities you can assign to your users based on their function within a specific domain or subdomain. Stakeholders do not enforce access control, but are meant to help your data consumers understand the organizational structure and responsibilities.

Atlan provides the following options:

Domain owner-  overall domain management and reporting.

Architect-  design and deployment of domains and subdomains.

Data product owner-  creation, management, and documentation of data products.

Data engineer-  creation and management of data pipelines.

Create new stakeholdersthat better reflect your organizational structure and functions.



## Components of a data productâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

To search for a data product:

From the left menu of any screen in Atlan, you can either:ClickProductsto search for data products from the products homepage:From the left navigation menu, use the search bar or select the relevant domain and then select a data product.In theData productssection, select a trending or recently viewed data product. The list ofTrending productsis sorted by the total count of views on each product, with the most viewed product listed at the top.From the top right of any screen in Atlan, click thestar icon. From theStarred assetspopup, select a starred data product.If your Atlan admin has enabled theShow products in asset discoverytoggle, clickAssetsto search for data products fromasset discovery:Click theAsset typedropdown and then selectProductto filter for data products.Use theFiltersmenuon the left to further refine your search.Click any data product to view the product sidebar or open the product profile. In addition to the factors documentedhere, Atlan usesproduct scoreto determine the most relevant results for your product search.Use the search bar to search for products using keyword-based search.

ClickProductsto search for data products from the products homepage:From the left navigation menu, use the search bar or select the relevant domain and then select a data product.In theData productssection, select a trending or recently viewed data product. The list ofTrending productsis sorted by the total count of views on each product, with the most viewed product listed at the top.From the top right of any screen in Atlan, click thestar icon. From theStarred assetspopup, select a starred data product.

From the left navigation menu, use the search bar or select the relevant domain and then select a data product.

In theData productssection, select a trending or recently viewed data product. The list ofTrending productsis sorted by the total count of views on each product, with the most viewed product listed at the top.

From the top right of any screen in Atlan, click thestar icon. From theStarred assetspopup, select a starred data product.

If your Atlan admin has enabled theShow products in asset discoverytoggle, clickAssetsto search for data products fromasset discovery:Click theAsset typedropdown and then selectProductto filter for data products.Use theFiltersmenuon the left to further refine your search.Click any data product to view the product sidebar or open the product profile. In addition to the factors documentedhere, Atlan usesproduct scoreto determine the most relevant results for your product search.Use the search bar to search for products using keyword-based search.

Click theAsset typedropdown and then selectProductto filter for data products.

Use theFiltersmenuon the left to further refine your search.

Click any data product to view the product sidebar or open the product profile. In addition to the factors documentedhere, Atlan usesproduct scoreto determine the most relevant results for your product search.

Use the search bar to search for products using keyword-based search.



### Overviewâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

This section displays important details about the data product:

Data product status   -  current status of the data product:Draft-  data product is in draft state and only visible to product ownersPublished-  data product is active for consumptionSunset-  data product is planned for retirementArchived-  data product is archived and will be no longer available to users

Draft-  data product is in draft state and only visible to product owners

Published-  data product is active for consumption

Sunset-  data product is planned for retirement

Archived-  data product is archived and will be no longer available to users

Domain name   -  view and navigate to the data domain that the data product belongs to

Criticality   -  view business criticality rating:High-  high business impact_Medium   - _ moderate business impactLow-  internal or non-business impact

High-  high business impact

_Medium   - _ moderate business impact

Low-  internal or non-business impact

Sensitivity   -  view sensitivity score for data product classification:Public-  may be freely accessibleInternal-  may only be distributed within the organizationConfidential-  may only be limited to a specific domain or team within an organization

Public-  may be freely accessible

Internal-  may only be distributed within the organization

Confidential-  may only be limited to a specific domain or team within an organization

Freshness   -  timestamp for when the data product was last updated in Atlan. This only includes metadata updates made on the data product and not on any underlying assets.

Description of the data product

Linked assets at a glance

List of assets designated as output ports



### Output portsâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

This section displays a list of assets that allow users to consume the data product across multiple domains. A data product can have multiple output ports. Click the output port asset to open the asset sidebar and view more details.



### README and resourcesâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

This section allows you to add aREADMEandresourcesto your data product. READMEs can help you provide detailed documentation about the product to your data consumers. Resources enable you to add links to internal or external URLs for more context.



### Product scoreâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

Based on the principles of data as a product,product scorescan help you signal the accuracy and completeness of your data products, helping build trust in them. Atlan calculates and assigns a product score to your data products based on a preset criteria of metadata completeness.



### Details sidebarâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

The sidebar to the right of the product profile allows you to view and add metadata, depending on yourdomain permissions:

Visibilityhelps you determine who can access and monitor the data product throughout its entire lifecycle:Private to members of this domain-  only members of a specific domain can access the data product.Private to selected members-  only members of a specific domain and other selected users or groups can access the data product.Public-  everyone in the organization can access the data product.

Private to members of this domain-  only members of a specific domain can access the data product.

Private to selected members-  only members of a specific domain and other selected users or groups can access the data product.

Public-  everyone in the organization can access the data product.

UnderTerms, click+to addtermsand offer contextual information for your data product.Â

UnderOwners, click+to assignownersto the data product.

UnderTags, click+toattach a tagand configuretag propagationfor all assets in the data product.

UnderCertificate, click+to update the certification status. Choose fromfour certificateÂ options-Draft,Verified,Deprecated, andNo certificate.



### Product profile headerâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

This section helps you perform quick actions. From the top right of the product profile:

Click the user avatars to view a list of recently visited users, total views on your product, total number of unique visitors, and total views by user.Use the days filter to filter product views and user activity in the last 7, 30, and 90 days.This feature is turned on by default   -  admins canturn off user activity.

Use the days filter to filter product views and user activity in the last 7, 30, and 90 days.

This feature is turned on by default   -  admins canturn off user activity.

Click the star button tostar your productand bookmark it for easy access.

Click theSlackorTeamsicon to post on aSlackorMicrosoft Teamschannel.

Click the 3-dot icon toadd an announcementto your product.



### Assetsâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

TheAssetstab provides a comprehensive list of assets included in the data product:

Search for specific assets in the sidebar

Filter assets by input and output ports

Select an asset to view more details in the asset sidebar

View queried at source information for all assets



### Lineageâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

TheLineagetab provides avisual representationof the provenance of and relationships between your data products in Atlan.



### Activity logâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

TheActivitytab provides achangelogfor your data product.

Activity-  view details about changes made to the data product andfilter for specific types of metadata changes

Views-  view top and recent users of the data product

Producers-  view information about when the data product was created and last updated and by whom



### Contractsâ
(source: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products)

TheContractstab displays anylinked contractsfor the output ports in your data product. You can view contract specifications, track the evolution of your contract over time, and compare and contrast multiple versions.

atlan

documentation

Enable products module

Order of operations

Stakeholders

Components of a data product
