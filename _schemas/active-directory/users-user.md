---
description: A Microsoft Entra ID user account managed via Microsoft Graph
layout: schema
name: User
properties_list:
- description: Unique identifier for the user (read-only)
  name: id
  type: string
- description: Name displayed in the address book for the user
  name: displayName
  type: string
- description: Principal name in UPN format (alias@domain)
  name: userPrincipalName
  type: string
- description: Primary SMTP address for the user
  name: mail
  type:
  - string
  - 'null'
- description: Given name (first name) of the user
  name: givenName
  type:
  - string
  - 'null'
- description: Surname (family name or last name) of the user
  name: surname
  type:
  - string
  - 'null'
- description: The user's job title
  name: jobTitle
  type:
  - string
  - 'null'
- description: Department name in which the user works
  name: department
  type:
  - string
  - 'null'
- description: Office location in the user's place of business
  name: officeLocation
  type:
  - string
  - 'null'
- description: Primary cellular telephone number for the user
  name: mobilePhone
  type:
  - string
  - 'null'
- description: Telephone numbers for the user
  name: businessPhones
  type: array
- description: True if the account is enabled; otherwise false
  name: accountEnabled
  type:
  - boolean
  - 'null'
- description: Two-letter country code (ISO 3166) required for license assignment
  name: usageLocation
  type:
  - string
  - 'null'
- description: Preferred language for the user (ISO 639-1 Code, e.g. en-US)
  name: preferredLanguage
  type:
  - string
  - 'null'
- description: Date and time the user was created
  name: createdDateTime
  type:
  - string
  - 'null'
- description: Timestamp of the last password change
  name: lastPasswordChangeDateTime
  type:
  - string
  - 'null'
- description: Password policies enforced for the user
  name: passwordPolicies
  type:
  - string
  - 'null'
- description: Whether the user is a member or guest in the tenant
  name: userType
  type:
  - string
  - 'null'
- description: Licenses assigned to the user
  name: assignedLicenses
  type: array
- description: True if the user is synchronized from on-premises Active Directory
  name: onPremisesSyncEnabled
  type:
  - boolean
  - 'null'
- description: Distinguished name from on-premises Active Directory
  name: onPremisesDistinguishedName
  type:
  - string
  - 'null'
- description: State of a guest/external user invited via Azure AD B2B
  name: externalUserState
  type:
  - string
  - 'null'
provider_name: Microsoft Active Directory
provider_slug: active-directory
schema_file: json-schema/users-user-schema.json
slug: users-user
tags:
- Active Directory
- Authentication
- Authorization
- Directory Services
- Identity Management
- Microsoft Entra
- Zero Trust
title: User
---
