---
description: Represents a user account in Azure Active Directory (Microsoft Entra ID). A user is a core identity object in the Microsoft identity platform, containing profile information, authentication credentials, organizational relationships, and license assignments. This schema is based on the Microsoft Graph v1.0 user resource type as documented at https://learn.microsoft.com/en-us/graph/api/resources/user.
layout: schema
name: Azure Active Directory User
properties_list:
- description: The OData type annotation for the user resource.
  name: '@odata.type'
  type: string
- description: The unique identifier for the user. This is a GUID assigned by Azure AD when the user object is created. Read-only.
  name: id
  type: string
- description: The date and time the user was deleted. Null if the user has not been deleted. Read-only.
  name: deletedDateTime
  type:
  - string
  - 'null'
- description: True if the account is enabled; otherwise, false. This property is required when creating a user. A disabled account cannot authenticate.
  name: accountEnabled
  type: boolean
- description: 'Sets the age group of the user. Allowed values: null, Minor, NotAdult, Adult.'
  name: ageGroup
  type:
  - string
  - 'null'
- description: The licenses assigned to the user, including specific disabled service plans. Read-only. Not nullable.
  name: assignedLicenses
  type: array
- description: The plans assigned to the user from subscriptions. Read-only. Not nullable.
  name: assignedPlans
  type: array
- description: The telephone numbers for the user. Only one number can be set for this property. Read-only for users synced from on-premises directory.
  name: businessPhones
  type: array
- description: The city where the user is located. Maximum length is 128 characters.
  name: city
  type:
  - string
  - 'null'
- description: The name of the company associated with the user. This property can be useful for describing the company that an external user comes from. Maximum length is 64 characters.
  name: companyName
  type:
  - string
  - 'null'
- description: 'Sets whether consent was obtained for minors. Allowed values: null, Granted, Denied, NotRequired.'
  name: consentProvidedForMinor
  type:
  - string
  - 'null'
- description: The country or region where the user is located. Use the ISO 3166 two-letter country code format (e.g., US, GB, DE). Maximum length is 128 characters.
  name: country
  type:
  - string
  - 'null'
- description: The date and time the user was created in ISO 8601 format and UTC time. Read-only.
  name: createdDateTime
  type:
  - string
  - 'null'
- description: 'Indicates whether the user account was created through one of the following methods: as a regular school or work account (null), as an external account (Invitation), as a local account for an Azure Ac'
  name: creationType
  type:
  - string
  - 'null'
- description: The name of the department in which the user works. Maximum length is 64 characters.
  name: department
  type:
  - string
  - 'null'
- description: The name displayed in the address book for the user. This is usually the combination of the first name, middle initial, and last name. This property is required when a user is created and cannot be cl
  name: displayName
  type: string
- description: The date and time when the user was hired or will start work in case of a future hire.
  name: employeeHireDate
  type:
  - string
  - 'null'
- description: The employee identifier assigned to the user by the organization. The maximum length is 16 characters.
  name: employeeId
  type:
  - string
  - 'null'
- description: The date and time when the user left or will leave the organization.
  name: employeeLeaveDateTime
  type:
  - string
  - 'null'
- description: Represents organization data (e.g., division and costCenter) associated with a user.
  name: employeeOrgData
  type: object
- description: Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor.
  name: employeeType
  type:
  - string
  - 'null'
- description: 'For an external user invited to the tenant, this property represents the invited user''s invitation status. Possible values: PendingAcceptance, Accepted, null. Read-only.'
  name: externalUserState
  type:
  - string
  - 'null'
- description: Shows the timestamp for the latest change to the externalUserState property. Read-only.
  name: externalUserStateChangeDateTime
  type:
  - string
  - 'null'
- description: The fax number of the user.
  name: faxNumber
  type:
  - string
  - 'null'
- description: The given name (first name) of the user. Maximum length is 64 characters.
  name: givenName
  type:
  - string
  - 'null'
- description: Represents the identities that can be used to sign in to this user account. An identity can be provided by Microsoft, by organizations, or by social identity providers. May contain multiple items with
  name: identities
  type: array
- description: The instant message voice-over-IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only.
  name: imAddresses
  type: array
- description: Do not use. Reserved for future use.
  name: isResourceAccount
  type:
  - boolean
  - 'null'
- description: The user's job title. Maximum length is 128 characters.
  name: jobTitle
  type:
  - string
  - 'null'
- description: The time when this Azure AD user last changed their password or when their password was created. Read-only.
  name: lastPasswordChangeDateTime
  type:
  - string
  - 'null'
- description: Used by enterprise applications to determine the legal age group of the user. Read-only.
  name: legalAgeGroupClassification
  type:
  - string
  - 'null'
- description: State of license assignments for this user. Read-only.
  name: licenseAssignmentStates
  type: array
- description: The SMTP address for the user (e.g., admin@contoso.com). Changes to this property also update the user's proxyAddresses collection to include the value as an SMTP address. This property cannot contain
  name: mail
  type:
  - string
  - 'null'
- description: The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters.
  name: mailNickname
  type: string
- description: The primary cellular telephone number for the user. Read-only for users synced from on-premises directory.
  name: mobilePhone
  type:
  - string
  - 'null'
- description: The office location in the user's place of business.
  name: officeLocation
  type:
  - string
  - 'null'
- description: Contains the on-premises Active Directory distinguished name or DN. Read-only.
  name: onPremisesDistinguishedName
  type:
  - string
  - 'null'
- description: Contains the on-premises domainFQDN, also called dnsDomainName, synced from the on-premises directory. Read-only.
  name: onPremisesDomainName
  type:
  - string
  - 'null'
- description: Contains extensionAttributes1-15 for the user. These extension attributes are also known as Exchange custom attributes. Read-only for cloud-only users.
  name: onPremisesExtensionAttributes
  type: object
- description: This property is used to associate an on-premises Active Directory user account to their Azure AD user object. This property must be specified when creating a new user if you are using a federated dom
  name: onPremisesImmutableId
  type:
  - string
  - 'null'
- description: Indicates the last time at which the object was synced with the on-premises directory. Read-only.
  name: onPremisesLastSyncDateTime
  type:
  - string
  - 'null'
- description: Errors when using Microsoft synchronization product during provisioning. Read-only.
  name: onPremisesProvisioningErrors
  type: array
- description: Contains the on-premises samAccountName synced from the on-premises directory. Read-only.
  name: onPremisesSamAccountName
  type:
  - string
  - 'null'
- description: Contains the on-premises security identifier (SID) for the user that was synced from on-premises to the cloud. Read-only.
  name: onPremisesSecurityIdentifier
  type:
  - string
  - 'null'
- description: True if this user object is currently being synced from an on-premises Active Directory (AD); otherwise, the user isn't being synced and can be managed in Azure Active Directory. Read-only.
  name: onPremisesSyncEnabled
  type:
  - boolean
  - 'null'
- description: Contains the on-premises userPrincipalName synced from the on-premises directory. Read-only.
  name: onPremisesUserPrincipalName
  type:
  - string
  - 'null'
- description: A list of additional email addresses for the user (e.g., ["bob@contoso.com", "Robert@fabrikam.com"]).
  name: otherMails
  type: array
- description: Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. Disab
  name: passwordPolicies
  type:
  - string
  - 'null'
- description: Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created.
  name: passwordProfile
  type: object
- description: The postal code for the user's postal address. The postal code is specific to the user's country/region. Maximum length is 40 characters.
  name: postalCode
  type:
  - string
  - 'null'
- description: The preferred language for the user, expressed in ISO 639-1 code format (e.g., en-US).
  name: preferredLanguage
  type:
  - string
  - 'null'
- description: The preferred data location for the user, indicating the geographic region for their data.
  name: preferredDataLocation
  type:
  - string
  - 'null'
- description: The plans that are provisioned for the user. Read-only. Not nullable.
  name: provisionedPlans
  type: array
- description: 'A list that includes the user''s SMTP and SIP proxy addresses. For example: ["SMTP:bob@contoso.com", "smtp:bob@sales.contoso.com"]. The address prefixed with SMTP (uppercase) is the primary. Read-only.'
  name: proxyAddresses
  type: array
- description: Security identifier (SID) of the user, used in Windows scenarios. Read-only.
  name: securityIdentifier
  type:
  - string
  - 'null'
- description: Do not use in Microsoft Graph. Manage this property through the Microsoft 365 admin center instead.
  name: showInAddressList
  type:
  - boolean
  - 'null'
- description: Get the last signed-in date and request ID of the sign-in for a given user. Read-only. Requires Azure AD Premium P1 or P2 license.
  name: signInActivity
  type: object
- description: Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated a
  name: signInSessionsValidFromDateTime
  type:
  - string
  - 'null'
- description: The state or province in the user's address. Maximum length is 128 characters.
  name: state
  type:
  - string
  - 'null'
- description: The street address of the user's place of business. Maximum length is 1024 characters.
  name: streetAddress
  type:
  - string
  - 'null'
- description: The user's surname (family name or last name). Maximum length is 64 characters.
  name: surname
  type:
  - string
  - 'null'
- description: 'A two-letter country code (ISO standard 3166). Required for users that will be assigned licenses due to legal requirements to check for availability of services in countries/regions. Examples include '
  name: usageLocation
  type:
  - string
  - 'null'
- description: The user principal name (UPN) of the user. The UPN is an Internet-style sign-in name based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format
  name: userPrincipalName
  type: string
- description: A string value that can be used to classify user types in your directory, such as Member and Guest.
  name: userType
  type:
  - string
  - 'null'
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/azure-active-directory-user-schema.json
slug: azure-active-directory-user
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
title: Azure Active Directory User
---
