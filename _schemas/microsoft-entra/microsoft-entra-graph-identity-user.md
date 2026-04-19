---
description: Represents a Microsoft Entra ID user account. Contains identity, contact, organizational, and authentication properties.
layout: schema
name: User
properties_list:
- description: Unique identifier for the user (GUID). Assigned automatically by the directory.
  name: id
  type: string
- description: The name displayed in the address book for the user
  name: displayName
  type: string
- description: The given name (first name) of the user
  name: givenName
  type: '[''string'', ''null'']'
- description: The surname (family name) of the user
  name: surname
  type: '[''string'', ''null'']'
- description: The SMTP address of the user. This property cannot be set during creation for cloud-only users.
  name: mail
  type: '[''string'', ''null'']'
- description: The user principal name (UPN) of the user in the format alias@domain. The domain must be present in the tenant's verified domains collection.
  name: userPrincipalName
  type: string
- description: The mail alias for the user. Must be specified when creating a new user.
  name: mailNickname
  type: string
- description: true if the account is enabled; otherwise, false. Must be specified when creating a new user.
  name: accountEnabled
  type: boolean
- description: The user's job title
  name: jobTitle
  type: '[''string'', ''null'']'
- description: The department in which the user works
  name: department
  type: '[''string'', ''null'']'
- description: The office location in the user's place of business
  name: officeLocation
  type: '[''string'', ''null'']'
- description: The company name associated with the user
  name: companyName
  type: '[''string'', ''null'']'
- description: The primary cellular telephone number for the user
  name: mobilePhone
  type: '[''string'', ''null'']'
- description: The telephone numbers for the user's business
  name: businessPhones
  type: array
- description: The street address of the user's place of business
  name: streetAddress
  type: '[''string'', ''null'']'
- description: The city in which the user is located
  name: city
  type: '[''string'', ''null'']'
- description: The state or province in the user's address
  name: state
  type: '[''string'', ''null'']'
- description: The postal code for the user's postal address
  name: postalCode
  type: '[''string'', ''null'']'
- description: The country or region in which the user is located (ISO 3166 two-letter code)
  name: country
  type: '[''string'', ''null'']'
- description: Two-letter country code (ISO 3166). Required for users assigned licenses due to legal requirements for checking service availability.
  name: usageLocation
  type: '[''string'', ''null'']'
- description: The preferred language for the user in ISO 639-1 code format (e.g., en-US)
  name: preferredLanguage
  type: '[''string'', ''null'']'
- description: Classification of the user type relative to the tenant
  name: userType
  type: string
- description: The employee identifier assigned by the organization
  name: employeeId
  type: '[''string'', ''null'']'
- description: Captures the type of worker (e.g., Employee, Contractor, Consultant, Vendor)
  name: employeeType
  type: '[''string'', ''null'']'
- description: The date and time when the user was hired
  name: employeeHireDate
  type: '[''string'', ''null'']'
- description: true if this user is synced from an on-premises directory; false if originally created in Azure AD; null if never synced
  name: onPremisesSyncEnabled
  type: '[''boolean'', ''null'']'
- description: The on-premises SAM account name synchronized from the on-premises directory
  name: onPremisesSamAccountName
  type: '[''string'', ''null'']'
- description: List of proxy addresses for the user including SMTP and smtp prefixed addresses
  name: proxyAddresses
  type: array
- description: Licenses assigned to the user
  name: assignedLicenses
  type: array
- description: The date and time the user was created
  name: createdDateTime
  type: string
- description: The date and time of the user's most recent interactive sign-in activity
  name: lastSignInDateTime
  type: '[''string'', ''null'']'
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-user-schema.json
slug: microsoft-entra-graph-identity-user
tags:
- Access Management
- Authentication
- Azure AD
- Entra
- Identity
- Identity Governance
- Microsoft
- Network Security
- Security
- Zero Trust
title: User
---
