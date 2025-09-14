# Provide credentials to view sample data
(source: https://docs.atlan.com/product/capabilities/discovery/references/provide-credentials-to-view-sample-data)

DiscoveryGet StartedAsset ManagementConfigurationConceptsReferencesProvide credentials to view sample dataFAQ

Get Started

Asset Management

Configuration

Concepts

ReferencesProvide credentials to view sample data

Provide credentials to view sample data

FAQ

Use data

Discovery

References

Provide credentials to view sample data

Once your connection admins haveconfiguredbring your own credentials(BYOC)in Atlan, users will need to provide their own credentials before they can view the sample data in the asset profile. This will help you enforce better governance across your organization.

AnyAtlan userwithdata access to the assetand their own credentials for the data store. Atlan will display a100-row sample of the data.



## Use your own credentials to view sample dataâ
(source: https://docs.atlan.com/product/capabilities/discovery/references/provide-credentials-to-view-sample-data)

Atlan supports both basic username and password as well as key pair authentication of your credentials. Atlan also supportsSSO authentication.

To set up your own credentials for viewing sample data:

On theAssetspage, click on an asset to view its asset profile.

In the asset profile, clickSample Data.

To set up your credentials for viewing the sample data, clickGet Started.

In the popup window, clickGet Startedonce again to proceed.

In theUser credential setupdialog box,Basicis selected as the default authentication option. Enter the following:ForUsername, enter the username for the connection.ForPassword, enter the password for that connection.ForRole, enter your role for that connection.ForWarehouse, enter the name of the warehouse.

ForUsername, enter the username for the connection.

ForPassword, enter the password for that connection.

ForRole, enter your role for that connection.

ForWarehouse, enter the name of the warehouse.

Click theTest Authenticationbutton to confirm your credentials.

Once authentication is successful, clickDone.

You can now view sample data using your own credentials! ð

When using the key pair method, you'll need to enter your encrypted private key and the private key password to complete the authentication process.

Once you've set up your credentials for viewing sample data, you can alsomanage your credentials. If your admin has enabledsample data download, you can export sample data in a CSV file.

integration

connectors

Use your own credentials to view sample data
