# query data
(source: https://docs.atlan.com/product/capabilities/insights/how-tos/query-data#use-the-visual-query-builder)

InsightsGet StartedHow to query dataQuery ManagementCredentialsConceptsReferencesFAQTroubleshooting

Get StartedHow to query data

How to query data

Query Management

Credentials

Concepts

References

FAQ

Troubleshooting

Use data

Insights

Get Started

How to query data

There are two ways to query data in Atlan:

writing your own SQL

using the Visual Query Builder

Atlan pushes all queries to the source (no data is stored in Atlan). In addition, Atlan applies access policies to the results before displaying them.



## Write your own SQLâ
(source: https://docs.atlan.com/product/capabilities/insights/how-tos/query-data#use-the-visual-query-builder)

Anyone with the knowledge to write SQL. AnyAtlan userwithdata access to the assetcan query data.

To query an asset with your own SQL:

From the left menu of any screen, clickInsights.

Under theExplorertab, find the asset you want to query:Use theSelect databasedropdown to choose another database, if necessary.Search for the asset by name in the search bar, or browse for it in the tree structure.

Use theSelect databasedropdown to choose another database, if necessary.

Search for the asset by name in the search bar, or browse for it in the tree structure.

Hover over the table or view, and click the play icon. This writes and runs a basic preview query.(Optional) Click the open asset sidebar icon to view more details in the asset sidebar.(Optional) Click the eye icon to view a preview of the query results.(Optional) Click the 3-dot icon for more options:ClickSet editor contextto set the same connection, database, and schema name in the query editor as selected in theExplorertab.ClickPlace name in editorto view the asset name in the query editor.ClickCopy pathto copy the full path of the asset, including database and schema names.

(Optional) Click the open asset sidebar icon to view more details in the asset sidebar.

(Optional) Click the eye icon to view a preview of the query results.

(Optional) Click the 3-dot icon for more options:ClickSet editor contextto set the same connection, database, and schema name in the query editor as selected in theExplorertab.ClickPlace name in editorto view the asset name in the query editor.ClickCopy pathto copy the full path of the asset, including database and schema names.

ClickSet editor contextto set the same connection, database, and schema name in the query editor as selected in theExplorertab.

ClickPlace name in editorto view the asset name in the query editor.

ClickCopy pathto copy the full path of the asset, including database and schema names.

Under theUntitledtab on the right, change the sample query or write your own   -  separate multiple queries with a semicolon;. Click theRunbutton in the upper right to test your query as you write it.(Optional) Click the downward arrow next to theRunbutton toexport query results via emailorschedule the query.

;

(Optional) Click the downward arrow next to theRunbutton toexport query results via emailorschedule the query.

(Optional) If you have multiple tabs open in the query editor, right-click a tab to open the tabs menu. You can close a specific tab or all tabs, or duplicate the query.

(Optional) From the top right of the query editor, click the 3-dot icon for additional query editor actions or to customize it further:Click or hover overDuplicate queryto create a duplicate version of your query.Click or hover overOpen command paletteto view the actions you can run inside the query editor.Click or hover overThemesand then select your preferred theme for the query editor.Click or hover overTab spacingto change the tab spacing for your queries.Click or hover overFont sizeto change the font size for your queries.Click or hover overCursorto change the cursor position in the query editor.Click or hover overAutosuggestionsto turn off autosuggestions for assets in the query editor.

Click or hover overDuplicate queryto create a duplicate version of your query.

Click or hover overOpen command paletteto view the actions you can run inside the query editor.

Click or hover overThemesand then select your preferred theme for the query editor.

Click or hover overTab spacingto change the tab spacing for your queries.

Click or hover overFont sizeto change the font size for your queries.

Click or hover overCursorto change the cursor position in the query editor.

Click or hover overAutosuggestionsto turn off autosuggestions for assets in the query editor.

The editor supports all read-based SQL statements, includingJOIN. The editor will not run any write-based statements. The following SQL statements are not supported:

JOIN

UPDATE

UPDATE

DELETE

DELETE

CREATE

CREATE

ALTER

ALTER

DROP

DROP

TRUNCATE

TRUNCATE

INSERT INTO

INSERT INTO

You can select the context for your query to the left of theRunbutton. Then you won't need to fully qualify table names with schema and database names.



## Use the Visual Query Builderâ
(source: https://docs.atlan.com/product/capabilities/insights/how-tos/query-data#use-the-visual-query-builder)

AnyAtlan userwithdata access to the asset. No SQL knowledge required!

To query an asset using the Visual Query Builder:

From the left menu of any screen, clickInsights.

At the top of the screen, to the right of theUntitledtab, click the+button and selectNew visual query.

UnderSelect fromchoose the table or view you want to query.

(Optional) In the column selector to the right, select the column you want to query.

Then develop your query:Click theRunbutton to run the query and preview its results.Click the blue circular+button to add an action to the query.Repeat these steps until your query is complete.

Click theRunbutton to run the query and preview its results.

Click the blue circular+button to add an action to the query.

Repeat these steps until your query is complete.

(Optional) If there are any errors in your query, clickAuto fixfor Atlan to recommend a fix.Â

(Optional) In the query results set, clickCopyto copy the query results or clickDownloadto export them.

You can learn more about the query builder actions inthis example.

atlan

documentation

Write your own SQL

Use the Visual Query Builder
