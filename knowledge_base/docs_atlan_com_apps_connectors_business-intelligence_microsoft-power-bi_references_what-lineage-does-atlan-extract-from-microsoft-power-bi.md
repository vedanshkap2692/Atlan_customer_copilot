# What lineage does Atlan extract from Microsoft Power BI?
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-lineage-does-atlan-extract-from-microsoft-power-bi)

Microsoft Power BIGet StartedCrawl Power BI AssetsReferencesWhat does Atlan crawl from Microsoft Power BI?Preflight checks for Microsoft Power BIWhat lineage does Atlan extract from Microsoft Power BI?TroubleshootingFAQ

Get Started

Crawl Power BI Assets

ReferencesWhat does Atlan crawl from Microsoft Power BI?Preflight checks for Microsoft Power BIWhat lineage does Atlan extract from Microsoft Power BI?

What does Atlan crawl from Microsoft Power BI?

Preflight checks for Microsoft Power BI

What lineage does Atlan extract from Microsoft Power BI?

Troubleshooting

FAQ

Connect data

BI Tools

On-premises & Enterprise BI

Microsoft Power BI

References

What lineage does Atlan extract from Microsoft Power BI?

Atlan currently supports the following lineage forMicrosoft Power BI:

Lineage between Microsoft Power BI assets crawled in Atlan

Upstream lineage to SQL warehouse assets, includes table- and column-level lineage for the following supported SQL sources:Amazon RedshiftDatabricksGoogle BigQueryMicrosoft Azure Synapse AnalyticsMicrosoft SQL ServerMySQLOracle-  Atlan generates lineage for the following methods of Oracle connectivity:connection string   -  for example,<host_name>:<port>/<service_name>connect descriptor   -  for example,(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=<host_name>)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=<service_name>)))Lineage generation for TNS name connectivity is currently not supported.SAP HANASnowflakeTeradataSalesforce

Amazon Redshift

Databricks

Google BigQuery

Microsoft Azure Synapse Analytics

Microsoft SQL Server

MySQL

Oracle-  Atlan generates lineage for the following methods of Oracle connectivity:connection string   -  for example,<host_name>:<port>/<service_name>connect descriptor   -  for example,(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=<host_name>)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=<service_name>)))Lineage generation for TNS name connectivity is currently not supported.

connection string   -  for example,<host_name>:<port>/<service_name>

<host_name>:<port>/<service_name>

connect descriptor   -  for example,(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=<host_name>)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=<service_name>)))

(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=<host_name>)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=<service_name>)))

Lineage generation for TNS name connectivity is currently not supported.

SAP HANA

Snowflake

Teradata

Salesforce

This document helps you understand how Atlan generates lineage to upstream SQL sources for your Microsoft Power BI assets using a custom query parser, and the steps you can take while developing reports and dashboards in Microsoft Power BI to create seamless lineage generation.



## Lineage generationâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-lineage-does-atlan-extract-from-microsoft-power-bi)

Atlan generates lineage for your Microsoft Power BI assets as follows:

You connect to a SQL data source such as Snowflake and extract relevant SQL tables to create a table in Microsoft Power BI for analysis.

You connect to a SQL data source such as Snowflake and extract relevant SQL tables to create a table in Microsoft Power BI for analysis.

Once the data has been loaded, you can perform Microsoft Power BI native operations as required.

Once the data has been loaded, you can perform Microsoft Power BI native operations as required.

Each table created in Microsoft Power BI and part of a dataset has a Power Query expression associated with it. For example:letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),EXAMPLE_DB = Source{[Name="EXAMPLE_DATABASE_NAME",Kind="Database"]}[Data],EXAMPLE_Sch = EXAMPLE_DB{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="EXAMPLE_TABLE_NAME",Kind="Table"]}[Data]inEXAMPLE_Table_Var

Each table created in Microsoft Power BI and part of a dataset has a Power Query expression associated with it. For example:

letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),EXAMPLE_DB = Source{[Name="EXAMPLE_DATABASE_NAME",Kind="Database"]}[Data],EXAMPLE_Sch = EXAMPLE_DB{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="EXAMPLE_TABLE_NAME",Kind="Table"]}[Data]inEXAMPLE_Table_Var

letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),EXAMPLE_DB = Source{[Name="EXAMPLE_DATABASE_NAME",Kind="Database"]}[Data],EXAMPLE_Sch = EXAMPLE_DB{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="EXAMPLE_TABLE_NAME",Kind="Table"]}[Data]inEXAMPLE_Table_Var

Atlan retrieves the Power Query expression as a plain string from theMicrosoft Power BI APIresponse.

Atlan retrieves the Power Query expression as a plain string from theMicrosoft Power BI APIresponse.

Atlan's custom query parser then parses the Power Query expression to derive lineage between the upstream SQL tables and Microsoft Power BI table asset.

Atlan's custom query parser then parses the Power Query expression to derive lineage between the upstream SQL tables and Microsoft Power BI table asset.

However, note that the Power Query expression can be modified in the Power Query Editor of the Power BI Desktop application. These modifications may involve using parameter substitutes and variable naming patterns in the Power Query expression.

These modifications may lead to inconsistent behavior in Atlan's query parser. This is because the latter is built on the standard format of a Power Query expression, without any modifications.



## Limitations of query parserâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-lineage-does-atlan-extract-from-microsoft-power-bi)

To create seamless lineage generation, Atlan recommends the following when building tables in Microsoft Power BI.



### Using parametersâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-lineage-does-atlan-extract-from-microsoft-power-bi)

The Power Query expression associated with a table can be manually modified to serve different use cases. For example, if you're creating multiple tables using data from the same database and schema at source, you may want to usedynamic M query parametersto substitute common values in Power Query expressions.

Atlan recommends the following:

Avoid using the following words to define your parameter names:DatabaseSchemaTableViewWarehouseRole

Database

Database

Schema

Schema

Table

Table

View

View

Warehouse

Warehouse

Role

Role

Avoid including any spaces in your parameter names   -  for example,( Example : Example DB )

( Example : Example DB )

For example, Atlan's query parser doesn't support the following:

letSource = Snowflake.Databases("example.snowflakecomputing.com",WarehouseName,[Role="EXAMPLE_ROLE"]),DatabaseName = Source{[Name=DatabaseName,Kind="Database"]}[Data],EXAMPLE_Sch = DatabaseName{[Name=SchemaName,Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name=TableName,Kind="Table"]}[Data]inEXAMPLE_Table_Var

letSource = Snowflake.Databases("example.snowflakecomputing.com",WarehouseName,[Role="EXAMPLE_ROLE"]),DatabaseName = Source{[Name=DatabaseName,Kind="Database"]}[Data],EXAMPLE_Sch = DatabaseName{[Name=SchemaName,Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name=TableName,Kind="Table"]}[Data]inEXAMPLE_Table_Var

This example includesWarehouseName,DatabaseName,SchemaName, andTableNameas parameters, which aren't supported in the query parser.

WarehouseName

DatabaseName

SchemaName

TableName



### Parameter syntaxâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-lineage-does-atlan-extract-from-microsoft-power-bi)

There are different formats for the syntax used in parameter names for Power Query expressions. For example,param_name,#âparam_nameâ, or#"param nameâ.

param_name

#âparam_nameâ

#"param nameâ

Atlan recommends the following for parameter names:

Use plain text format

Avoid any special characters   -  for example,#,", and more

#

"

For example, Atlan's query parser doesn't support the following:

letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),DatabaseName = Source{[Name=#"DatabaseName",Kind="Database"]}[Data],EXAMPLE_Sch = DatabaseName{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="EXAMPLE_TABLE_NAME",Kind="Table"]}[Data]inEXAMPLE_Table_Var

letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),DatabaseName = Source{[Name=#"DatabaseName",Kind="Database"]}[Data],EXAMPLE_Sch = DatabaseName{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="EXAMPLE_TABLE_NAME",Kind="Table"]}[Data]inEXAMPLE_Table_Var

This example includes#"DatabaseName"as parameter name, which isn't supported in the query parser.

#"DatabaseName"



### Variable namesâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-lineage-does-atlan-extract-from-microsoft-power-bi)

While using parameters in Power Query expressions, make sure that the variable names don't match the parameter names. For example, Atlan's query parser doesn't support the following:

letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),DatabaseName = Source{[Name=DatabaseName,Kind="Database"]}[Data],EXAMPLE_Sch = DatabaseName{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="EXAMPLE_TABLE_NAME",Kind="Table"]}[Data]inEXAMPLE_Table_Var

letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),DatabaseName = Source{[Name=DatabaseName,Kind="Database"]}[Data],EXAMPLE_Sch = DatabaseName{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="EXAMPLE_TABLE_NAME",Kind="Table"]}[Data]inEXAMPLE_Table_Var

In this example,DatabaseNameis used as both a parameter name and variable name, which isn't supported in the query parser.

DatabaseName



### User-defined expressionsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-lineage-does-atlan-extract-from-microsoft-power-bi)

Parts of a Power Query expression can be parameterized and cross-referenced in other Power Query expressions. Atlan's query parser currently only parses standard forms of Power Query expressions, hence these user-defined expressions aren't supported.

Example of a supported Power Query expression:

letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),EXAMPLE_DB = Source{[Name="EXAMPLE_DATABASE_NAME",Kind="Database"]}[Data],EXAMPLE_Sch = EXAMPLE_DB{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="TBL_AGG_SALES_HT_POS_BEER",Kind="Table"]}[Data]inEXAMPLE_Table_Var

letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),EXAMPLE_DB = Source{[Name="EXAMPLE_DATABASE_NAME",Kind="Database"]}[Data],EXAMPLE_Sch = EXAMPLE_DB{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="TBL_AGG_SALES_HT_POS_BEER",Kind="Table"]}[Data]inEXAMPLE_Table_Var

Example of an unsupported Power Query expression:

letSource = db_source,EXAMPLE_Sch = db_source{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="EXAMPLE_TABLE_NAME",Kind="Table"]}[Data]inEXAMPLE_Table_Var

letSource = db_source,EXAMPLE_Sch = db_source{[Name="EXAMPLE_SCHEMA_NAME",Kind="Schema"]}[Data],EXAMPLE_Table_Var = EXAMPLE_Sch{[Name="EXAMPLE_TABLE_NAME",Kind="Table"]}[Data]inEXAMPLE_Table_Var

Example of a reference expression, parameterized asdb_source:

db_source

letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),EXAMPLE_DB = Source{[Name="EXAMPLE_DATABASE_NAME",Kind="Database"]}[Data]inEXAMPLE_DB

letSource = Snowflake.Databases("example.snowflakecomputing.com","EXAMPLE_WAREHOUSE",[Role="EXAMPLE_ROLE"]),EXAMPLE_DB = Source{[Name="EXAMPLE_DATABASE_NAME",Kind="Database"]}[Data]inEXAMPLE_DB



### Table functionsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-lineage-does-atlan-extract-from-microsoft-power-bi)

For column-level lineage generation, Atlan's custom query parser currently supports parsing expressions with the followingTable Functions:

Table.RenameColumns

Table.TransformColumnNames

Table.TransformColumns



### Power query functionsâ
(source: https://docs.atlan.com/apps/connectors/business-intelligence/microsoft-power-bi/references/what-lineage-does-atlan-extract-from-microsoft-power-bi)

Upstream lineage isn't supported when the data source expression involves the use of certain built-in Power Query functions. The following functions aren't supported:

Csv.Document

Csv.Document

DateTime.LocalNow

DateTime.LocalNow

Excel.Workbook

Excel.Workbook

Folder.Files

Folder.Files

Json.Document

Json.Document

List.Dates

List.Dates

SharePoint.Files

SharePoint.Files

SharePoint.Tables

SharePoint.Tables

UsageMetricsDataConnector.GetMetricsData

UsageMetricsDataConnector.GetMetricsData

Xml.Tables

Xml.Tables

connectors

data

crawl

Lineage generation

Limitations of query parser
