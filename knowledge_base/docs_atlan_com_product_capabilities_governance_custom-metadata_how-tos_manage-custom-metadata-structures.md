# Manage custom metadata structures
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/manage-custom-metadata-structures)

Custom MetadataGet StartedAccess ManagementBadge ManagementStructure ManagementManage custom metadata structuresReferencesConceptsFAQ

Get Started

Access Management

Badge Management

Structure ManagementManage custom metadata structures

Manage custom metadata structures

References

Concepts

FAQ

Build governance

Custom Metadata

Structure Management

Manage custom metadata structures

You must be an admin user to manage custom metadata structures, including defining new ones.

Before users or integrations can enrich assets with custom metadata, you must first define its structure.



## Create custom metadata structureâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/manage-custom-metadata-structures)

To create a new custom metadata structure:

From the left menu of any screen, clickGovernance.

Under theMetadataheading, clickCustom Metadata.

Under theStart adding custom metadataheading, click the+Get startedto add a new structure:ForNameenter a name for the custom metadata structure. (Inour examples, this would beIPRorETL.)(Optional) To personalize your custom metadata, to the left of the name, click the image icon. From the upper right of the corresponding dialog:ClickIconsto add an icon to your custom metadata. Click the gray box to change the color of the icon to green, yellow, or red.ClickEmojito add an emoji to your custom metadata.ClickUpload Imageto upload an image for your custom metadata. The recommended size for image uploads is 24x24 pixels.(Optional) Add a description of the custom metadata below these.At the bottom right of the dialog, click theCreatebutton.

ForNameenter a name for the custom metadata structure. (Inour examples, this would beIPRorETL.)

(Optional) To personalize your custom metadata, to the left of the name, click the image icon. From the upper right of the corresponding dialog:ClickIconsto add an icon to your custom metadata. Click the gray box to change the color of the icon to green, yellow, or red.ClickEmojito add an emoji to your custom metadata.ClickUpload Imageto upload an image for your custom metadata. The recommended size for image uploads is 24x24 pixels.

ClickIconsto add an icon to your custom metadata. Click the gray box to change the color of the icon to green, yellow, or red.

ClickEmojito add an emoji to your custom metadata.

ClickUpload Imageto upload an image for your custom metadata. The recommended size for image uploads is 24x24 pixels.

(Optional) Add a description of the custom metadata below these.

At the bottom right of the dialog, click theCreatebutton.



## Create properties in the structureâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/manage-custom-metadata-structures)

To create custom metadata properties within a custom metadata structure:

From the left menu of any screen, clickGovernance.

Under theMetadataheading, clickCustom Metadata.

Under theCustom Metadataheading, select the custom metadata structure you want to change.

Click theNew propertybutton (no properties yet) orAdd propertybutton (to add more properties):ForName, enter a name for one property. (Inour examples, this would be one ofLicense type,Provider,Job link, and so on.)ForType, select the type of value you expect users to use for this property:TheTexttype allows free-form text values.TheIntegertype allows only whole numbers (no decimals).TheDecimaltype allows fractional numbers (those with decimal points).TheBooleantype allows only aYesor aNovalue.TheDatetype allows both date and time values in the following format   -  day, month, year, hours, minutes, and seconds.TheOptionstype allows you todefine your own set of predefined optionsfor values that are valid.TheUserstype allows only existing Atlan users as values.TheGroupstype allows only existing Atlan groups as values.TheURLtype allows only web links.TheSQLtype allows only SQL code.(Optional) ForDescription, enter an explanation for how you expect users to use this property.If you choseOptionsas the type, either:UnderSelect Options, select an existing set of options to reuse.Click theCreate Newlink to create a new set of options.UnderOption name, give the options a name.UnderValues, enter the list of values considered valid (separated by;).(Optional) UnderAssets, you can configure the connections and asset types on which this custom metadata should be visible to:ForConnections, select theconnectionto which you want to limit users to be able to enrich assets with this property. For example, you may want a property to only apply to a specific Snowflake connection.ForApplicable asset types, select the kinds of assets you want users to be able to enrich with this property. For example, you may want a property to only apply to SQL assets like tables and views, and not to BI assets.Â (Optional) UnderGlossary assets, you can configure the glossaries and glossary asset types on which this custom metadata should be visible to:ForGlossaries, select theglossariesto which you want to limit users to be able to enrich assets with this property.ForApplicable asset types, select theglossary assetsyou want users to be able to enrich with this property. For example, you may want a property to only apply to terms within a glossary, and not to categories.(Optional) UnderDomain assets, you can configure the data domains, subdomains, and products on which this custom metadata should be visible to:ForDomains, select thedomains or subdomainsto which you want to limit users to be able to enrich with this property.ForApplicable asset types, select thedomains, subdomains, orproductsyou want users to be able to enrich with this property. For example, you may want a property to only apply to products within a specific subdomain, and not to the parent domain.(Optional) UnderOther assets, forApplicable asset types, select assets that neither fall under the rubric of a connection or glossary   -  currently onlyfile assetsare supported.(Optional) UnderConfigurationstoggle any extra settings for the property:Allow multiple valuescontrols whether users can enter more than a single value for this property. (Note: this is only available for some types.)Show in filtercontrols whether users can filter on this property when doing asset discovery.Show in overviewcontrols whether the property will show up in theOverviewsidebar tab of assets. (All properties will show in the custom metadata's own tab, but those with thisShow in overviewenabled will also show in theOverviewtab.)

ForName, enter a name for one property. (Inour examples, this would be one ofLicense type,Provider,Job link, and so on.)

ForType, select the type of value you expect users to use for this property:TheTexttype allows free-form text values.TheIntegertype allows only whole numbers (no decimals).TheDecimaltype allows fractional numbers (those with decimal points).TheBooleantype allows only aYesor aNovalue.TheDatetype allows both date and time values in the following format   -  day, month, year, hours, minutes, and seconds.TheOptionstype allows you todefine your own set of predefined optionsfor values that are valid.TheUserstype allows only existing Atlan users as values.TheGroupstype allows only existing Atlan groups as values.TheURLtype allows only web links.TheSQLtype allows only SQL code.

TheTexttype allows free-form text values.

TheIntegertype allows only whole numbers (no decimals).

TheDecimaltype allows fractional numbers (those with decimal points).

TheBooleantype allows only aYesor aNovalue.

Yes

No

TheDatetype allows both date and time values in the following format   -  day, month, year, hours, minutes, and seconds.

TheOptionstype allows you todefine your own set of predefined optionsfor values that are valid.

TheUserstype allows only existing Atlan users as values.

TheGroupstype allows only existing Atlan groups as values.

TheURLtype allows only web links.

TheSQLtype allows only SQL code.

(Optional) ForDescription, enter an explanation for how you expect users to use this property.

If you choseOptionsas the type, either:UnderSelect Options, select an existing set of options to reuse.Click theCreate Newlink to create a new set of options.UnderOption name, give the options a name.UnderValues, enter the list of values considered valid (separated by;).

UnderSelect Options, select an existing set of options to reuse.

Click theCreate Newlink to create a new set of options.UnderOption name, give the options a name.UnderValues, enter the list of values considered valid (separated by;).

UnderOption name, give the options a name.

UnderValues, enter the list of values considered valid (separated by;).

;

(Optional) UnderAssets, you can configure the connections and asset types on which this custom metadata should be visible to:ForConnections, select theconnectionto which you want to limit users to be able to enrich assets with this property. For example, you may want a property to only apply to a specific Snowflake connection.ForApplicable asset types, select the kinds of assets you want users to be able to enrich with this property. For example, you may want a property to only apply to SQL assets like tables and views, and not to BI assets.

ForConnections, select theconnectionto which you want to limit users to be able to enrich assets with this property. For example, you may want a property to only apply to a specific Snowflake connection.

ForApplicable asset types, select the kinds of assets you want users to be able to enrich with this property. For example, you may want a property to only apply to SQL assets like tables and views, and not to BI assets.

Â (Optional) UnderGlossary assets, you can configure the glossaries and glossary asset types on which this custom metadata should be visible to:ForGlossaries, select theglossariesto which you want to limit users to be able to enrich assets with this property.ForApplicable asset types, select theglossary assetsyou want users to be able to enrich with this property. For example, you may want a property to only apply to terms within a glossary, and not to categories.

ForGlossaries, select theglossariesto which you want to limit users to be able to enrich assets with this property.

ForApplicable asset types, select theglossary assetsyou want users to be able to enrich with this property. For example, you may want a property to only apply to terms within a glossary, and not to categories.

(Optional) UnderDomain assets, you can configure the data domains, subdomains, and products on which this custom metadata should be visible to:ForDomains, select thedomains or subdomainsto which you want to limit users to be able to enrich with this property.ForApplicable asset types, select thedomains, subdomains, orproductsyou want users to be able to enrich with this property. For example, you may want a property to only apply to products within a specific subdomain, and not to the parent domain.

ForDomains, select thedomains or subdomainsto which you want to limit users to be able to enrich with this property.

ForApplicable asset types, select thedomains, subdomains, orproductsyou want users to be able to enrich with this property. For example, you may want a property to only apply to products within a specific subdomain, and not to the parent domain.

(Optional) UnderOther assets, forApplicable asset types, select assets that neither fall under the rubric of a connection or glossary   -  currently onlyfile assetsare supported.

(Optional) UnderConfigurationstoggle any extra settings for the property:Allow multiple valuescontrols whether users can enter more than a single value for this property. (Note: this is only available for some types.)Show in filtercontrols whether users can filter on this property when doing asset discovery.Show in overviewcontrols whether the property will show up in theOverviewsidebar tab of assets. (All properties will show in the custom metadata's own tab, but those with thisShow in overviewenabled will also show in theOverviewtab.)

Allow multiple valuescontrols whether users can enter more than a single value for this property. (Note: this is only available for some types.)

Show in filtercontrols whether users can filter on this property when doing asset discovery.

Show in overviewcontrols whether the property will show up in theOverviewsidebar tab of assets. (All properties will show in the custom metadata's own tab, but those with thisShow in overviewenabled will also show in theOverviewtab.)

That's it, your users can nowenrich assets with this custom metadata! ð



## Delete properties from a structureâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/manage-custom-metadata-structures)

Deleting a custom metadata property will remove the values for that property from any assets.

To delete custom metadata properties from a custom metadata structure:

From the left menu of any screen, clickGovernance.

Under theMetadataheading, clickCustom Metadata.

Under theCustom Metadataheading, select the custom metadata structure you want to change.

In the properties table on the right, click the delete icon on the far right of the row containing the property to delete the property.

When prompted for confirmation, click theConfirmbutton.



## Delete custom metadata structureâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/manage-custom-metadata-structures)

You can also delete an entire custom metadata structure.

Deleting a custom metadata structure will remove all its properties and all its custom metadata values from any assets. You might want to considerusing personas to hide the custom metadata, until you confirm it is no longer needed.

To delete a custom metadata structure:

From the left menu of any screen, clickGovernance.

Under theMetadataheading, clickCustom Metadata.

Under theCustom Metadataheading, select the custom metadata structure you want to delete.

In the upper right of the custom metadata structure, click the red delete icon.

When prompted for confirmation, click theDeletebutton.



## View linked assetsâ
(source: https://docs.atlan.com/product/capabilities/governance/custom-metadata/how-tos/manage-custom-metadata-structures)

Once users in your organization haveenriched their assets with custom metadata, you will be able to view the linked assets right from the governance center.

To view assets with custom metadata:

From the left menu of any screen, clickGovernance.

Under theMetadataheading, clickCustom Metadata.

Under theCustom Metadataheading, clickLinked Assetsto view all the assets linked to the custom metadata.

(Optional) Click any asset to open the asset sidebar for more details.

data

integration

Create custom metadata structure

Create properties in the structure

Delete properties from a structure

Delete custom metadata structure

View linked assets
