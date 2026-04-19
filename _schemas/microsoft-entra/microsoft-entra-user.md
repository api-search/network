---
description: Schema for a Microsoft Entra ID (formerly Azure AD) user resource as represented in the Microsoft Graph API. Contains identity, contact, organizational, and authentication profile properties.
layout: schema
name: Microsoft Entra User
properties_list:
- description: Unique identifier for the user (GUID). Assigned automatically by Microsoft Entra ID.
  name: id
  type: string
- description: The name displayed in the address book for the user. Maximum length is 256 characters.
  name: displayName
  type: string
- description: The given name (first name) of the user. Maximum length is 64 characters.
  name: givenName
  type:
  - string
  - 'null'
- description: The surname (family name or last name) of the user. Maximum length is 64 characters.
  name: surname
  type:
  - string
  - 'null'
- description: The user principal name (UPN) in the format alias@domain. The domain portion must be a verified domain in the tenant.
  name: userPrincipalName
  type: string
- description: The SMTP address of the user (e.g., jeff@contoso.com). Changes to this property also update the proxyAddresses collection.
  name: mail
  type:
  - string
  - 'null'
- description: The mail alias for the user. Must be specified when creating a new user. Maximum length is 64 characters.
  name: mailNickname
  type: string
- description: true if the account is enabled; otherwise, false. Must be specified when creating a new user.
  name: accountEnabled
  type: boolean
- description: ''
  name: passwordProfile
  type: object
- description: The user's job title. Maximum length is 128 characters.
  name: jobTitle
  type:
  - string
  - 'null'
- description: The name of the department in which the user works. Maximum length is 64 characters.
  name: department
  type:
  - string
  - 'null'
- description: The office location in the user's place of business.
  name: officeLocation
  type:
  - string
  - 'null'
- description: The company name associated with the user. Maximum length is 64 characters.
  name: companyName
  type:
  - string
  - 'null'
- description: The primary cellular telephone number for the user. Maximum length is 64 characters.
  name: mobilePhone
  type:
  - string
  - 'null'
- description: The telephone numbers for the user. Only one number can be set. Read-only for users synced from on-premises.
  name: businessPhones
  type: array
- description: The street address of the user's place of business. Maximum length is 1024 characters.
  name: streetAddress
  type:
  - string
  - 'null'
- description: The city in which the user is located. Maximum length is 128 characters.
  name: city
  type:
  - string
  - 'null'
- description: The state or province in the user's address. Maximum length is 128 characters.
  name: state
  type:
  - string
  - 'null'
- description: The postal code for the user's postal address. Maximum length is 40 characters.
  name: postalCode
  type:
  - string
  - 'null'
- description: The country or region in which the user is located. Use ISO 3166 two-letter country code (e.g., US, GB).
  name: country
  type:
  - string
  - 'null'
- description: A two-letter country code (ISO 3166). Required for users assigned licenses due to legal requirements.
  name: usageLocation
  type:
  - string
  - 'null'
- description: The preferred language for the user in ISO 639-1 code format (e.g., en-US).
  name: preferredLanguage
  type:
  - string
  - 'null'
- description: A string value that classifies the user type. Member users are internal to the tenant, Guest users are invited from outside.
  name: userType
  type: string
- description: The employee identifier assigned to the user by the organization. Maximum length is 16 characters.
  name: employeeId
  type:
  - string
  - 'null'
- description: Captures the enterprise worker type (e.g., Employee, Contractor, Consultant, Vendor).
  name: employeeType
  type:
  - string
  - 'null'
- description: The date and time when the user was hired or will start work in a future hire.
  name: employeeHireDate
  type:
  - string
  - 'null'
- description: true if synced from an on-premises directory; false if originally cloud-created; null if never synced.
  name: onPremisesSyncEnabled
  type:
  - boolean
  - 'null'
- description: The on-premises SAM account name synchronized from the on-premises directory.
  name: onPremisesSamAccountName
  type:
  - string
  - 'null'
- description: The on-premises distinguished name (DN) synchronized from Active Directory.
  name: onPremisesDistinguishedName
  type:
  - string
  - 'null'
- description: The on-premises domain name synchronized from Active Directory.
  name: onPremisesDomainName
  type:
  - string
  - 'null'
- description: Used to associate an on-premises Active Directory user account to their Entra user object. Must be specified if using a federated domain for the UPN.
  name: onPremisesImmutableId
  type:
  - string
  - 'null'
- description: The last time the object was synced with the on-premises directory.
  name: onPremisesLastSyncDateTime
  type:
  - string
  - 'null'
- description: List of proxy addresses (e.g., SMTP:jeff@contoso.com, smtp:jeff@contoso.onmicrosoft.com).
  name: proxyAddresses
  type: array
- description: The licenses assigned to the user including disabled service plans.
  name: assignedLicenses
  type: array
- description: The plans assigned to the user.
  name: assignedPlans
  type: array
- description: Identities associated with the user account including social identities for B2B/B2C scenarios.
  name: identities
  type: array
- description: The date and time the user was created.
  name: createdDateTime
  type: string
- description: The last interactive sign-in date and time for the user.
  name: lastSignInDateTime
  type:
  - string
  - 'null'
- description: The date and time the user was deleted. Only present for deleted users in the deletedItems container.
  name: deletedDateTime
  type:
  - string
  - 'null'
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-user-schema.json
slug: microsoft-entra-user
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
title: Microsoft Entra User
---
