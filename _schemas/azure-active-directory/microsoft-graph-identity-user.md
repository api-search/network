---
description: Represents an Azure AD user account. Inherits from directoryObject. Contains identity, profile, organizational, and authentication properties.
layout: schema
name: User
properties_list:
- description: True if the account is enabled; otherwise, false.
  name: accountEnabled
  type: boolean
- description: The licenses that are assigned to the user.
  name: assignedLicenses
  type: array
- description: The plans that are assigned to the user.
  name: assignedPlans
  type: array
- description: The telephone numbers for the user.
  name: businessPhones
  type: array
- description: The city where the user is located.
  name: city
  type: '[''string'', ''null'']'
- description: The company name associated with the user.
  name: companyName
  type: '[''string'', ''null'']'
- description: The country or region where the user is located.
  name: country
  type: '[''string'', ''null'']'
- description: The date and time the user was created.
  name: createdDateTime
  type: string
- description: The department in which the user works.
  name: department
  type: '[''string'', ''null'']'
- description: The name displayed in the address book for the user. Required on creation.
  name: displayName
  type: string
- description: The employee identifier assigned to the user by the organization.
  name: employeeId
  type: '[''string'', ''null'']'
- description: Captures the enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor.
  name: employeeType
  type: '[''string'', ''null'']'
- description: The given name (first name) of the user.
  name: givenName
  type: '[''string'', ''null'']'
- description: The user's job title.
  name: jobTitle
  type: '[''string'', ''null'']'
- description: The SMTP address for the user.
  name: mail
  type: '[''string'', ''null'']'
- description: The mail alias for the user. Required on creation.
  name: mailNickname
  type: string
- description: The primary cellular telephone number for the user.
  name: mobilePhone
  type: '[''string'', ''null'']'
- description: The office location in the user's place of business.
  name: officeLocation
  type: '[''string'', ''null'']'
- description: The on-premises Active Directory distinguished name.
  name: onPremisesDistinguishedName
  type: '[''string'', ''null'']'
- description: The on-premises domain name.
  name: onPremisesDomainName
  type: '[''string'', ''null'']'
- description: Used to associate an on-premises Active Directory user account to the Azure AD user object.
  name: onPremisesImmutableId
  type: '[''string'', ''null'']'
- description: The last time at which the object was synced with the on-premises directory.
  name: onPremisesLastSyncDateTime
  type: '[''string'', ''null'']'
- description: True if this user object is currently being synced from an on-premises Active Directory.
  name: onPremisesSyncEnabled
  type: '[''boolean'', ''null'']'
- description: Additional email addresses for the user.
  name: otherMails
  type: array
- description: Specifies password policies for the user. One of DisableStrongPassword and DisablePasswordExpiration, or both.
  name: passwordPolicies
  type: '[''string'', ''null'']'
- description: The postal code for the user's postal address.
  name: postalCode
  type: '[''string'', ''null'']'
- description: 'The preferred language for the user in ISO 639-1 code format. Example: en-US.'
  name: preferredLanguage
  type: '[''string'', ''null'']'
- description: 'The proxy addresses for the user. Example: SMTP:user@contoso.com, smtp:alias@contoso.com.'
  name: proxyAddresses
  type: array
- description: Any refresh tokens or session tokens issued before this time are invalid.
  name: signInSessionsValidFromDateTime
  type: string
- description: The state or province in the user's address.
  name: state
  type: '[''string'', ''null'']'
- description: The street address of the user's place of business.
  name: streetAddress
  type: '[''string'', ''null'']'
- description: The user's surname (family name or last name).
  name: surname
  type: '[''string'', ''null'']'
- description: A two-letter country code (ISO 3166). Required for users who will be assigned licenses.
  name: usageLocation
  type: '[''string'', ''null'']'
- description: 'The user principal name (UPN) of the user. Required on creation. Format: alias@domain.'
  name: userPrincipalName
  type: string
- description: A string value that classifies the user. Typically Member or Guest.
  name: userType
  type: '[''string'', ''null'']'
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-user-schema.json
slug: microsoft-graph-identity-user
tags:
- Authentication
- Authorization
- Identity
- Microsoft
- Microsoft Entra
- OAuth
- OpenID Connect
- SAML
- SCIM
- Single Sign-On
- Zero Trust
title: User
---
