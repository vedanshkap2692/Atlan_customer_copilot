# Search and discover assets
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/search-and-discover-assets)

DiscoveryGet StartedSearch and discover assetsAsset ManagementConfigurationConceptsReferencesFAQ

Get StartedSearch and discover assets

Search and discover assets

Asset Management

Configuration

Concepts

References

FAQ

Use data

Discovery

Get Started

Search and discover assets

Atlan is a living catalog of all your data assets and knowledge. It lets you quickly discover and access your data, along with the tribal knowledge and business context.

Its Amazon-like search andfiltering experienceisn't just for data tables. It also extends to a variety of data assets, like columns, databases, SQL queries, BI dashboards, and much more.

To ensure a high-quality search experience, Atlan recommends the following:

Certify your assets

Link terms to your assetsto add business context

Enrich your assets with descriptions

Star your assetsfor easy access

You can bookmark yoursearch results with applied filtersor share them with other Atlan users in your organization for quick and easy access.



## Search superpowersâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/search-and-discover-assets)

Let's find out what makes Atlan's search intuitive and super quick.



### 
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/search-and-discover-assets)

Intelligent keyword recognition

Atlan supports powerful, intelligent search.Â When you search using keywords, the keywords in the matching search results will be highlighted for easy recognition. Even if your keyword contains an underscore_or a period.-  for example,instacart_order-  both keywords will be highlighted across all search results.

_

.

instacart_order

For keyword-based search:

If the keywords you're searching by is present in the asset name,description, orlinked term, only then will the asset appear in your search results.Â

Atlan displays search results based on asset names   -  technical name andalias-  that match your keyword(s).

If the keyword is aglossary term linked to assetsor present inasset descriptions, such assets will be boosted in search results.

Whether your search query is incomplete (insta) or misspelled (instacrt ordr), Atlan's powerful search can still help you discover exactly what you need.

insta

instacrt ordr



### Search from anywhereâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/search-and-discover-assets)

There are multiple ways to start your search:

Click theSearch assets across Atlanbar on the homepage.

ClickAssetsin the left-side panel.

UseCmd/Ctrl + Kto open the search page fromanywherein Atlan.



### Search using contextâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/search-and-discover-assets)

TheAssetssection offers avariety of filtersto narrow down your search. Here are the different types of filters that you can use:

Source: Search byconnectors, chosen from a list of connections within Atlan.

Domains: Filter assets bydomains, such as a single domain, multiple domains, or no domain.

Certificate: Search based on the certificate attached to data assets, such asVerified,Draft,Deprecated, andNo certificate.

Owners: Filter by selecting one or more users. You can also toggle betweenusersandgroupsÂ to filter based on a group of users.

Tags: Filter by user-generated tags, such aspublic,PII, and more.

public

PII

Terms: Filter by terms from your glossaries, such ascost,revenue, orP&L.

cost

revenue

P&L

Properties: Filter assets by other properties, like technical name oralias,description, last updated, and so on.

Atlan's search results include a quick count of all the resulting data assets grouped by type. As you apply the filters, you'll see these counts change in real time.

You can also enter a keyword in the search bar and filter your results by a specific type of data asset. For instance, enter the keywordorderin the search bar and then click theColumncheckbox to view column results for your searched keyword.

order



### Sort search resultsâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/search-and-discover-assets)

Atlan allows you to sort your search results in different ways. This helps you quickly find the assets you're interested in. Sorting options include:

Relevance: Sort by how closely the search results match your searched keywords.

Name: Sort by the asset name in an alphabetical or a reverse alphabetical order.

Updated on Atlan: Sort by the newest or oldest updated assets.

Star count: SortÂ assets bymost or fewest stars.

Order: Sort the search results in an ascending or descending order.

Popularity: Sort Snowflake and Google BigQuery assets by themost or least popular assets.

The sorting options may vary depending on the asset type selected. For example, if you are viewing the results while filtering by theTabletab, you'll also have the option of sorting by the most or fewest number of rows and columns.



### Search with patternsâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/search-and-discover-assets)

You can refine your search in Atlan with the following patterns:

Exact match search: Wrap the keywords within single''or double""quotation marks when typing them in the search bar   -  for example,"instacart_total_users". Only the asset names with case-insensitive exact match and following the order of the keywords will be boosted in the search results   -  for example,instacart_total_usersorInstacart_Total_Users. If the keywords are contained in theasset descriptionorlinked terms, such assets will show up next. Additionally, you can use exact match to search by thequalifiedNameor globally unique identifier (GUID) of an asset.

''

""

"instacart_total_users"

instacart_total_users

Instacart_Total_Users

qualifiedName

Combined string of database, schema, and table: For a more data-friendly search experience, copy the combined string ofdatabase.schema.table(orschema.table) from your SQL editor and paste it in the search bar   -  for example,atlan_db.public.instacart_total_orders.

database.schema.table

schema.table

atlan_db.public.instacart_total_orders

Multiple phrase match: When you enter two or more keywords, Atlan will find assets with asset names that partially match the keywords or a combination of them to narrow down the search results.



### See only what you want to seeâ
(source: https://docs.atlan.com/product/capabilities/discovery/how-tos/search-and-discover-assets)

Atlan gives you the option to customize your search. Want to show or hide certain fields in your search results? Click the3-doticon next to the search bar to set display preferences for each field:

Description

Terms

Tags

Connection

data

asset-profile

Search superpowers
