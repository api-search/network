---
description: Represents an Azure Active Directory (Entra ID) user account accessed through the Microsoft Graph API. A user resource contains profile information, organizational hierarchy, contact details, assigned licenses, and managed resources. This schema models the user resource as documented at https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0
layout: schema
name: Microsoft Office 365 User
properties_list:
- description: The unique identifier for the user. Inherited from directoryObject. A GUID value assigned by Azure AD and immutable once set.
  name: id
  type: string
- description: The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. Maximum length is 256 characters.
  name: displayName
  type:
  - string
  - 'null'
- description: The given name (first name) of the user. Maximum length is 64 characters.
  name: givenName
  type:
  - string
  - 'null'
- description: The user's surname (family name or last name). Maximum length is 64 characters.
  name: surname
  type:
  - string
  - 'null'
- description: The SMTP address for the user, for example, admin@contoso.com. Changes to this property also update the user's proxyAddresses collection to include the value as an SMTP address. This property cannot c
  name: mail
  type:
  - string
  - 'null'
- description: The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The gen
  name: userPrincipalName
  type: string
- description: The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters.
  name: mailNickname
  type:
  - string
  - 'null'
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
- description: The office location in the user's place of business. Maximum length is 128 characters.
  name: officeLocation
  type:
  - string
  - 'null'
- description: The company name which the user is associated with. This property can be useful for describing the company that an external user comes from. Maximum length is 64 characters.
  name: companyName
  type:
  - string
  - 'null'
- description: The telephone numbers for the user. Only one number can be set for this property. Read-only for users synced from on-premises directory.
  name: businessPhones
  type: array
- description: The primary cellular telephone number for the user. Read-only for users synced from on-premises directory.
  name: mobilePhone
  type:
  - string
  - 'null'
- description: The fax number of the user.
  name: faxNumber
  type:
  - string
  - 'null'
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
- description: The postal code for the user's postal address. The postal code is specific to the user's country/region. Maximum length is 40 characters.
  name: postalCode
  type:
  - string
  - 'null'
- description: The country or region in which the user is located; for example, US or UK. Maximum length is 128 characters.
  name: country
  type:
  - string
  - 'null'
- description: 'A two-letter country code (ISO standard 3166). Required for users that are assigned licenses due to legal requirements to check for availability of services in countries. Examples include: US, JP, and'
  name: usageLocation
  type:
  - string
  - 'null'
- description: The preferred language for the user. Should follow ISO 639-1 Code; for example en-US.
  name: preferredLanguage
  type:
  - string
  - 'null'
- description: The preferred data location for the user, used in multi-geo environments.
  name: preferredDataLocation
  type:
  - string
  - 'null'
- description: true if the account is enabled; otherwise, false. This property is required when a user is created.
  name: accountEnabled
  type:
  - boolean
  - 'null'
- description: Sets the age group of the user.
  name: ageGroup
  type:
  - string
  - 'null'
- description: Sets whether consent has been obtained for minors.
  name: consentProvidedForMinor
  type:
  - string
  - 'null'
- description: Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties.
  name: legalAgeGroupClassification
  type:
  - string
  - 'null'
- description: The employee identifier assigned to the user by the organization. Maximum length is 16 characters.
  name: employeeId
  type:
  - string
  - 'null'
- description: Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor.
  name: employeeType
  type:
  - string
  - 'null'
- description: The date and time when the user was hired or will start work in a future hire.
  name: employeeHireDate
  type:
  - string
  - 'null'
- description: Represents organization data (e.g., division and costCenter) associated with a user.
  name: employeeOrgData
  type:
  - object
  - 'null'
- description: A string value that can be used to classify user types in your directory, such as Member and Guest.
  name: userType
  type:
  - string
  - 'null'
- description: For an external user invited to the tenant, this property represents the invited user's invitation status.
  name: externalUserState
  type:
  - string
  - 'null'
- description: Shows the timestamp for the latest change to the externalUserState property.
  name: externalUserStateChangeDateTime
  type:
  - string
  - 'null'
- description: The date and time the user was created, in ISO 8601 format and UTC time.
  name: createdDateTime
  type:
  - string
  - 'null'
- description: The date and time of the user's most recent interactive or non-interactive sign-in activity. Read-only and returned only on $select.
  name: lastSignInDateTime
  type:
  - string
  - 'null'
- description: The date and time the user was deleted. Returned only on $select.
  name: deletedDateTime
  type:
  - string
  - 'null'
- description: This property is used to associate an on-premises Active Directory user account to their Azure AD user object. Must be specified when creating a new user account if using a federated domain for the us
  name: onPremisesImmutableId
  type:
  - string
  - 'null'
- description: Indicates the last time at which the object was synced with the on-premises directory.
  name: onPremisesLastSyncDateTime
  type:
  - string
  - 'null'
- description: true if this user object is currently being synced from an on-premises Active Directory; otherwise the user isn't being synced and can be managed in Azure Active Directory.
  name: onPremisesSyncEnabled
  type:
  - boolean
  - 'null'
- description: Contains the on-premises samAccountName synchronized from the on-premises directory.
  name: onPremisesSamAccountName
  type:
  - string
  - 'null'
- description: Contains the on-premises domainFQDN (also called dnsDomainName) synchronized from the on-premises directory.
  name: onPremisesDomainName
  type:
  - string
  - 'null'
- description: Contains the on-premises Active Directory distinguished name or DN.
  name: onPremisesDistinguishedName
  type:
  - string
  - 'null'
- description: Contains the on-premises security identifier (SID) for the user.
  name: onPremisesSecurityIdentifier
  type:
  - string
  - 'null'
- description: Contains the on-premises userPrincipalName synchronized from the on-premises directory.
  name: onPremisesUserPrincipalName
  type:
  - string
  - 'null'
- description: 'For example: ["SMTP: bob@contoso.com", "smtp: bob@sales.contoso.com"]. Changes to the mail property also update this collection to include the value as an SMTP address.'
  name: proxyAddresses
  type: array
- description: 'A list of additional email addresses for the user; for example: ["bob@contoso.com", "Robert@fabrikam.com"].'
  name: otherMails
  type: array
- description: The instant message voice-over IP (VOIP) session initiation protocol (SIP) addresses for the user.
  name: imAddresses
  type: array
- description: true if the Outlook global address list should contain this user; otherwise, false.
  name: showInAddressList
  type:
  - boolean
  - 'null'
- description: Specifies the password profile for the user. The profile contains the user's password. Required when creating a user.
  name: passwordProfile
  type:
  - object
  - 'null'
- description: Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. Disab
  name: passwordPolicies
  type:
  - string
  - 'null'
- description: 'Represents the identities that can be used to sign in to this user account. An identity can be provided by Microsoft (also known as a local account), by organizations, or by social identity providers '
  name: identities
  type: array
- description: The licenses that are assigned to the user, including inherited (group-based) licenses.
  name: assignedLicenses
  type: array
- description: The plans that are assigned to the user.
  name: assignedPlans
  type: array
- description: The plans that are provisioned for the user.
  name: provisionedPlans
  type: array
- description: A freeform text entry field for the user to describe themselves. Returned only on $select.
  name: aboutMe
  type:
  - string
  - 'null'
- description: The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. Returned only on $select.
  name: birthday
  type:
  - string
  - 'null'
- description: The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. Returned only on $select.
  name: hireDate
  type:
  - string
  - 'null'
- description: A list for the user to describe their interests. Returned only on $select.
  name: interests
  type: array
- description: The URL for the user's personal site. Returned only on $select.
  name: mySite
  type:
  - string
  - 'null'
- description: A list for the user to enumerate their past projects. Returned only on $select.
  name: pastProjects
  type: array
- description: A list for the user to enumerate their responsibilities. Returned only on $select.
  name: responsibilities
  type: array
- description: A list for the user to enumerate the schools they have attended. Returned only on $select.
  name: schools
  type: array
- description: A list for the user to enumerate their skills. Returned only on $select.
  name: skills
  type: array
- description: Get the last signed-in date and request ID of the sign-in for a given user. Read-only. Returned only on $select.
  name: signInActivity
  type:
  - object
  - 'null'
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-office-365-user-schema.json
slug: microsoft-office-365-user
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: Microsoft Office 365 User
---
