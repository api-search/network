---
description: Represents an Azure Active Directory user account. Inherits from directoryObject. Contains the user's profile information, organizational hierarchy, assigned licenses, and managed resources.
layout: schema
name: User
properties_list:
- description: The unique identifier for the user. Inherited from directoryObject. GUID format.
  name: id
  type: string
- description: The name displayed in the address book for the user.
  name: displayName
  type: string
- description: The given name (first name) of the user.
  name: givenName
  type: string
- description: The user's surname (family name or last name).
  name: surname
  type: string
- description: The SMTP address for the user. This property cannot contain accent characters.
  name: mail
  type: string
- description: The user principal name (UPN) of the user. The UPN is an Internet-style login name based on RFC 822. By convention, this should map to the user's email name.
  name: userPrincipalName
  type: string
- description: The user's job title.
  name: jobTitle
  type: string
- description: The name of the department in which the user works.
  name: department
  type: string
- description: The office location in the user's place of business.
  name: officeLocation
  type: string
- description: The company name associated with the user.
  name: companyName
  type: string
- description: The telephone numbers for the user.
  name: businessPhones
  type: array
- description: The primary cellular telephone number for the user.
  name: mobilePhone
  type: string
- description: The street address of the user's place of business.
  name: streetAddress
  type: string
- description: The city in which the user is located.
  name: city
  type: string
- description: The state or province in the user's address.
  name: state
  type: string
- description: The postal code for the user's postal address.
  name: postalCode
  type: string
- description: The country or region in which the user is located; for example, US or UK.
  name: country
  type: string
- description: The preferred language for the user. Should follow ISO 639-1 Code; for example en-US.
  name: preferredLanguage
  type: string
- description: True if the account is enabled; otherwise, false. Required when creating a user.
  name: accountEnabled
  type: boolean
- description: The date and time the user was created in ISO 8601 format.
  name: createdDateTime
  type: string
- description: The date and time of the user's most recent interactive or non-interactive sign-in.
  name: lastSignInDateTime
  type: string
- description: A two-letter country code (ISO 3166) required for users who will be assigned licenses. Not nullable.
  name: usageLocation
  type: string
- description: Represents the identities that can be used to sign in to this user account.
  name: identities
  type: array
- description: The licenses assigned to the user.
  name: assignedLicenses
  type: array
- description: The groups, directory roles, and administrative units the user is a member of.
  name: memberOf
  type: array
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-graph-user-schema.json
slug: microsoft-graph-user
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: User
---
