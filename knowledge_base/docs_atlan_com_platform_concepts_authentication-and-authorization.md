# Authentication and authorization
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)

Get StartedWhat is Atlan?Quick Start GuidesCore ConceptsAuthentication and authorizationData and metadata persistenceEncryption and key managementHigh availability and disaster recovery (HA/DR)AdministrationSecurity & ComplianceReferencesFAQs

What is Atlan?

Quick Start Guides

Core ConceptsAuthentication and authorizationData and metadata persistenceEncryption and key managementHigh availability and disaster recovery (HA/DR)

Authentication and authorization

Data and metadata persistence

Encryption and key management

High availability and disaster recovery (HA/DR)

Administration

Security & Compliance

References

FAQs

Get Started

Core Concepts

Authentication and authorization

Atlan supports the following authentication methods:



## Basic authenticationâ
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)

Atlan initially comes with basic or username-password authentication. Admins caninvite new usersto log into Atlan. When a new user opens the invitation link, they will be able to set up their user profile, including username and password.

However, Atlan does not recommend using basic authentication. Instead, admins should configure and enforceSSO authentication.



## SSO authenticationâ
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)



### SSO using SAML 2.0â
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)

Atlan supports single sign-on (SSO), allowing admins to configure SSO authentication.

Atlan currently supports the following SSO providers:

Azure AD

Google

JumpCloud

Okta

OneLogin

Custom IdP



### SSO using SCIMâ
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)

System for Cross-domain Identity ManagementÂ (SCIM) provisioningworks in combination with SSO. Atlan currently supports SCIM provisioning for the following SSO providers:

Azure AD

Okta



## Authorizationâ
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)



### Role-based access control (RBAC)â
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)

Atlan implements role-based access control (RBAC) to ensure that users have the minimum level of access required to perform their tasks. Access rights are assigned based on roles, and users are granted permissions according to their responsibilities. A system owner or an authorized party must approve any additional permissions.

Atlan adheres to the principle of least privilege, ensuring that users are only granted the level of access necessary to perform their job functions.



### User access review (UAR)â
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)

Atlan recommends that admins performÂ access reviews of users, admins, and service accounts on a quarterly basis to ensure that appropriate access levels are maintained. Access reviews should also be documented.



## Identity and access managementâ
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)

For centralized management of groups and users, Atlan uses granularaccess policies.

Admins can define policies to control both which actions a user can take and against which assets. These can be as broad as entire databases down to individual columns. Organizations can even build policies based on asset classification. This opens up the ability to restrict access to sensitive data like Personally Identifiable Information (PII)   -  an essential feature in the GDPR era.

Atlandenies access by default, andexplicit denials override any grants. You can even deny admin users access to assets, if you want.



### Rolesâ
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)

You must assign every user in Atlan auser role. These control basic levels of access.



### Groupsâ
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)

You can also add users togroups. Groups provide a more maintainable mechanism for applying access controls.



### Policiesâ
(source: https://docs.atlan.com/platform/concepts/authentication-and-authorization)

You can defineaccess policiesfor both users and groups.

Through these policies you can restrict which users can take which actions on which assets.

For example, you can set uptagssuch as PII and apply this to data assets like tables. You can also configure the tag to propagate downstream to any columns or tables created from them.

You can then defineaccess controls based on these tagsto restrict access to tagged assets. If Atlan propagates tags for you to derived assets, the access control is automatically applied to those derived assets as well.

atlan

documentation

Basic authentication

SSO authentication

Authorization

Identity and access management
