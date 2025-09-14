# Troubleshooting Snowflake connectivity
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/troubleshooting/troubleshooting-snowflake-connectivity)

SnowflakeGet StartedCrawl Snowflake AssetsManage Snowflake in AtlanReferencesTroubleshootingTroubleshooting Snowflake connectivityTroubleshooting Snowflake tag managementBest Practices

Get Started

Crawl Snowflake Assets

Manage Snowflake in Atlan

References

TroubleshootingTroubleshooting Snowflake connectivityTroubleshooting Snowflake tag management

Troubleshooting Snowflake connectivity

Troubleshooting Snowflake tag management

Best Practices

Connect data

Data Warehouses

Snowflake

Troubleshooting

Troubleshooting Snowflake connectivity



#### How to debug test authentication and preflight check errors?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/troubleshooting/troubleshooting-snowflake-connectivity)

Missing warehouse grants

The user doesnât have USAGE and OPERATE grants on a warehouse.

The user doesnât have USAGE and OPERATE grants on a warehouse.

Grant warehouse access to the role:GRANTOPERATE,USAGEONWAREHOUSE"<warehouse>"TOROLE atlan_user_role;

Grant warehouse access to the role:

GRANTOPERATE,USAGEONWAREHOUSE"<warehouse>"TOROLE atlan_user_role;

GRANTOPERATE,USAGEONWAREHOUSE"<warehouse>"TOROLE atlan_user_role;

Then, ensure that yougrant the role to the new user:GRANTROLE atlan_user_roleTOUSERatlan_user;

Then, ensure that yougrant the role to the new user:

GRANTROLE atlan_user_roleTOUSERatlan_user;

GRANTROLE atlan_user_roleTOUSERatlan_user;

Missing authorized access to SNOWFLAKE.ACCOUNT_USAGE schema

The user doesnât have authorized access to the SNOWFLAKE.ACCOUNT_USAGE database

The user doesnât have authorized access to the SNOWFLAKE.ACCOUNT_USAGE database

Reach out to your account admin togrant imported privilegeson theSnowflakedatabase to the role:USEROLE ACCOUNTADMIN;GRANTIMPORTEDPRIVILEGESONDATABASESNOWFLAKETOROLE atlan_user_role;

Reach out to your account admin togrant imported privilegeson theSnowflakedatabase to the role:

Snowflake

USEROLE ACCOUNTADMIN;GRANTIMPORTEDPRIVILEGESONDATABASESNOWFLAKETOROLE atlan_user_role;

USEROLE ACCOUNTADMIN;GRANTIMPORTEDPRIVILEGESONDATABASESNOWFLAKETOROLE atlan_user_role;

Ifusing a copied database, you'll need to grant the following permissions:GRANTUSAGEONDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTUSAGEONSCHEMA"<copied-schema>"INDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<copied-database>"TOROLE atlan_user_role;

Ifusing a copied database, you'll need to grant the following permissions:

GRANTUSAGEONDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTUSAGEONSCHEMA"<copied-schema>"INDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<copied-database>"TOROLE atlan_user_role;

GRANTUSAGEONDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTUSAGEONSCHEMA"<copied-schema>"INDATABASE"<copied-database>"TOROLE atlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<copied-database>"TOROLE atlan_user_role;

Missing usage grants on databases and/or schemas

The user doesn't have usage grants to the databases ` $missingDatabases ` and schemas ` $missingSchemas

The user doesn't have usage grants to the databases ` $missingDatabases ` and schemas ` $missingSchemas

Grantmissing permissions listed herefor information schema extraction method.

Atlan IP not allowlisted

Atlan's current location or network isn't recognized by Snowflake's security settings. This can happen if Atlan's IP address isn't on the list of allowed addresses in Snowflake's network policies.

Atlan's current location or network isn't recognized by Snowflake's security settings. This can happen if Atlan's IP address isn't on the list of allowed addresses in Snowflake's network policies.

If you are using the IP allowlist in your Snowflake instance, you must add theAtlan IP to the allowlist. ContactAtlan supportto obtain Atlan's IP addresses.

Incorrect credentials

The username or the password provided to connect to the Snowflake account is incorrect.

The username or the password provided to connect to the Snowflake account is incorrect.

Sign into the Snowflake account for the specified host and verify that the username and password are correct.

You can also create a new user, if required, by following the stepshere.

Missing or unauthorized role

The role specified in your connection configuration doesn't exist in Snowflake or your user account doesn't have grant to use this role.

The role specified in your connection configuration doesn't exist in Snowflake or your user account doesn't have grant to use this role.

If the role does not exist or is missing the required grants,create a roleand thengrant the role to the user.

User account locked

The user account you're using to connect to Snowflake has been locked temporarily because of multiple incorrect login attempts.

The user account you're using to connect to Snowflake has been locked temporarily because of multiple incorrect login attempts.

Wait for the user account to unlock or create a different user account to continue.

Missing or unauthorized warehouse

The warehouse specified in your connection configuration doesn't exist in Snowflake or your user account doesn't have grant to use this warehouse.

The warehouse specified in your connection configuration doesn't exist in Snowflake or your user account doesn't have grant to use this warehouse.

Ensure that the warehouse name is configured correctly.

Ensure that the warehouse name is configured correctly.

Update the warehouse name in the configuration if your account is using a different warehouse.Create a roleand thengrant the role to the userfor the updated warehouse.

Update the warehouse name in the configuration if your account is using a different warehouse.Create a roleand thengrant the role to the userfor the updated warehouse.

Missing access to non-system databases or schemas

The configured user doesn't have usage grants to any database or schema.orThe configured user doesn't have usage grants to any non-system database or schema.

The configured user doesn't have usage grants to any database or schema.

The configured user doesn't have usage grants to any non-system database or schema.

This pertains to the information schema method of fetching metadata. Ensure that the user has authorized access to the databases and schemas to be crawled.

Grant the requisite permissions as outlinedhere.



#### Why are some assets from a database or schema missing?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/troubleshooting/troubleshooting-snowflake-connectivity)

Check the grants on the role attached to the user defined for the crawler. Ensure the missing database or schema is present in these grants.SHOWGRANTSTOROLE atlan_user_role;

Check the grants on the role attached to the user defined for the crawler. Ensure the missing database or schema is present in these grants.

SHOWGRANTSTOROLE atlan_user_role;

SHOWGRANTSTOROLE atlan_user_role;



#### Why are new tables or views missing?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/troubleshooting/troubleshooting-snowflake-connectivity)

When using incremental extraction, consider running a one-time full extraction to capture any newly introduced metadata.

When using incremental extraction, consider running a one-time full extraction to capture any newly introduced metadata.

Make sure the role attached to the user defined for the crawler has grants for future tables and views being created in the database:GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE EXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;

Make sure the role attached to the user defined for the crawler has grants for future tables and views being created in the database:

GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE EXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;

GRANTUSAGEONFUTURE SCHEMASINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURETABLESINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE VIEWSINDATABASE"<database-name>"TOROLE atlan_user_role;GRANTREFERENCESONFUTURE EXTERNALTABLESINDATABASE"<database-name>"TOROLE atlan_user_role;

Make sure you run the below commands as well so that new tables and views you've created in-between are also visible to the user:GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOrole atlan_user_role;GRANTREFERENCESONALLTABLESINDATABASE"<database-name>"TOrole atlan_user_role;GRANTREFERENCESONALLEXTERNALTABLESINDATABASE"<database-name>"TOatlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<database-name>"TOrole atlan_user_role;

Make sure you run the below commands as well so that new tables and views you've created in-between are also visible to the user:

GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOrole atlan_user_role;GRANTREFERENCESONALLTABLESINDATABASE"<database-name>"TOrole atlan_user_role;GRANTREFERENCESONALLEXTERNALTABLESINDATABASE"<database-name>"TOatlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<database-name>"TOrole atlan_user_role;

GRANTUSAGEONALLSCHEMASINDATABASE"<database-name>"TOrole atlan_user_role;GRANTREFERENCESONALLTABLESINDATABASE"<database-name>"TOrole atlan_user_role;GRANTREFERENCESONALLEXTERNALTABLESINDATABASE"<database-name>"TOatlan_user_role;GRANTREFERENCESONALLVIEWSINDATABASE"<database-name>"TOrole atlan_user_role;



#### Why is some lineage missing?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/troubleshooting/troubleshooting-snowflake-connectivity)

The query miner only mines query history for up to the previous two weeks. The miner will not mine any queries that ran before that time window. If the queries that created your assets ran before that time window, lineage for those assets will not be present.

To mine more than the previous two weeks of query history, either useS3-based query miningorcontact Atlan support. Note that Snowflake itself only retains query history for so long as well, though. Once Snowflake itself no longer contains the query history we will be unable to mine it for lineage.

Lineage is unsupported for parameterized queries. Snowflake currentlydoes not resolve valuesfor parameterized queries before logging them in query history. This limits Atlan from generating lineage in such cases.



#### Missing attributes and lineageâ
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/troubleshooting/troubleshooting-snowflake-connectivity)

When using the account usage extraction method, there are currently some limitations. We are working with Snowflake to find workarounds for crawling the following:External table location dataProceduresPrimary key designation

External table location data

Procedures

Primary key designation

Furthermore, only database-level filtering is currently possible.



#### What views does Atlan require access to for the account usage method?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/troubleshooting/troubleshooting-snowflake-connectivity)

When using theaccount usage methodfor fetching metadata, Atlan requires access to the following views in Snowflake:

For the crawler:DATABASES,SCHEMATA,TABLES,VIEWS,COLUMNS, andPIPES

DATABASES

SCHEMATA

TABLES

VIEWS

COLUMNS

PIPES

For the miner andpopularity metrics:QUERY_HISTORY,ACCESS_HISTORY, andSESSIONS

QUERY_HISTORY

ACCESS_HISTORY

SESSIONS



#### Why am I getting a destination URL mismatch error when authenticating via Okta SSO?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/troubleshooting/troubleshooting-snowflake-connectivity)

This error can occur when you're connecting to Snowflake throughOkta SSOand enter the URL of your Snowflake instance in a format different from the one used in Okta.

Snowflake follows two URL formats:

Legacy format   - Â<AccountLocator>.<Region>.snowflakecomputing.comor<AccountLocator>.<Region>.<cloud>.snowflakecomputing.com

<AccountLocator>.<Region>.snowflakecomputing.com

<AccountLocator>.<Region>.<cloud>.snowflakecomputing.com

New URL format   -<Orgname>-<AccountName>.snowflakecomputing.com

<Orgname>-<AccountName>.snowflakecomputing.com

Ensure that you're using the same Snowflake URL format in Snowflake and Okta. Refer toSnowflake documentationto learn more.



#### Why am I getting a 'name or service not known' error when connecting via private link?â
(source: https://docs.atlan.com/apps/connectors/data-warehouses/snowflake/troubleshooting/troubleshooting-snowflake-connectivity)

If you're getting the following error messages   -java.net.UnknownHostExceptionandName or service not known-  this is a known error for users who have upgraded to the Snowflake JDBC driver version 3.13.25., have underscores in their account name, and connect to their Snowflake accounts overprivate link(for example,https://my_account.us-west-2.privatelink.snowflakecomputing.com).

java.net.UnknownHostException

Name or service not known

https://my_account.us-west-2.privatelink.snowflakecomputing.com

If your Snowflake account name has an underscore   -  for example,my_account- Â the updated JDBC driver will automatically convert underscores to dashes or hyphens-. This does not affect normal URLs because Snowflake accepts URLs with both hyphens and underscores.

my_account

-

For private link users, however, the JDBC driver will return an error if there are underscores present in the account name and the connection will fail. To troubleshoot further, refer toSnowflake documentation.

atlan

documentation
