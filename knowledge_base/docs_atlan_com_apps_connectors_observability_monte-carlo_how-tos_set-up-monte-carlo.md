# Set up Monte Carlo
(source: https://docs.atlan.com/apps/connectors/observability/monte-carlo/how-tos/set-up-monte-carlo)

Monte CarloGet StartedSet up Monte CarloCrawl Monte Carlo AssetsReferences

Get StartedSet up Monte Carlo

Set up Monte Carlo

Crawl Monte Carlo Assets

References

Connect data

Data Quality & Observability

Monte Carlo

Get Started

Set up Monte Carlo

You will probably need your Monte Carloaccount ownerto complete these steps   -  you may not have access yourself.

Atlan supports the API authentication method for fetching metadata from Monte Carlo. This method uses an API key ID and secret to fetch metadata.



## Create an account-service API keyâ
(source: https://docs.atlan.com/apps/connectors/observability/monte-carlo/how-tos/set-up-monte-carlo)

Atlan doesnotmake any API requests or queries that will update the objects in your Monte Carlo environment.

You will need to create anaccount-service API keyin Monte Carlo for integration with Atlan.

To create an account-service API key forcrawling Monte Carlo:

Log in to your Monte Carlo instance.

Log in to your Monte Carlo instance.

In the top header of your Monte Carlo instance, clickSettings.

In the top header of your Monte Carlo instance, clickSettings.

In the left menu underSettings, clickAPI Accessand then clickAccount Service Keys.

In the left menu underSettings, clickAPI Accessand then clickAccount Service Keys.

From theAccount Service Keyspage, click theCreate Keybutton.

From theAccount Service Keyspage, click theCreate Keybutton.

In theCreate Account Service Keydialog, enter the following details:ForDescription, add a meaningful description for your API key   -  for example,Atlan connection.From theAuthorization Groupsdropdown, selectViewers (All)to provideminimum permissionsfor crawling Monte Carlo.(Optional) ForExpires After, keep the default selection or select a preferred option.ClickCreateto finish creating the account-service API key.

In theCreate Account Service Keydialog, enter the following details:

ForDescription, add a meaningful description for your API key   -  for example,Atlan connection.

Atlan connection

From theAuthorization Groupsdropdown, selectViewers (All)to provideminimum permissionsfor crawling Monte Carlo.

(Optional) ForExpires After, keep the default selection or select a preferred option.

ClickCreateto finish creating the account-service API key.

From the corresponding screen, copy theKey IDandSecretand store them in a secure location.dangerThe API secret cannot be retrieved later.

From the corresponding screen, copy theKey IDandSecretand store them in a secure location.

The API secret cannot be retrieved later.

connectors

data

integration

crawl

api

authentication

Create an account-service API key
