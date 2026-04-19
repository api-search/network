---
class_count: 1
classes:
- id
context_file: json-ld/active-directory-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/active-directory/refs/heads/main/json-ld/active-directory-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Active Directory from Microsoft Active Directory.
layout: jsonld
name: Active Directory Context
namespaces:
- prefix: ad
  uri: https://learn.microsoft.com/en-us/graph/api/resources/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: User
  type: reference
- container: ''
  name: Group
  type: reference
- container: ''
  name: Application
  type: reference
- container: ''
  name: ServicePrincipal
  type: reference
- container: ''
  name: Device
  type: reference
- container: ''
  name: DirectoryRole
  type: reference
- container: ''
  name: AdministrativeUnit
  type: reference
- container: ''
  name: ConditionalAccessPolicy
  type: reference
- container: ''
  name: AppRoleAssignment
  type: reference
- container: ''
  name: PasswordProfile
  type: reference
- container: ''
  name: appId
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: userPrincipalName
  type: string
- container: ''
  name: mail
  type: string
- container: ''
  name: givenName
  type: string
- container: ''
  name: surname
  type: string
- container: ''
  name: jobTitle
  type: string
- container: ''
  name: department
  type: string
- container: ''
  name: officeLocation
  type: string
- container: ''
  name: mobilePhone
  type: string
- container: set
  name: businessPhones
  type: ''
- container: ''
  name: accountEnabled
  type: boolean
- container: ''
  name: usageLocation
  type: string
- container: ''
  name: preferredLanguage
  type: string
- container: ''
  name: createdDateTime
  type: dateTime
- container: ''
  name: lastPasswordChangeDateTime
  type: dateTime
- container: ''
  name: passwordPolicies
  type: string
- container: ''
  name: userType
  type: string
- container: ''
  name: onPremisesSyncEnabled
  type: boolean
- container: ''
  name: onPremisesDistinguishedName
  type: string
- container: ''
  name: externalUserState
  type: string
- container: set
  name: assignedLicenses
  type: ''
- container: ''
  name: mailNickname
  type: string
- container: ''
  name: mailEnabled
  type: boolean
- container: ''
  name: securityEnabled
  type: boolean
- container: set
  name: groupTypes
  type: ''
- container: ''
  name: visibility
  type: string
- container: ''
  name: membershipRule
  type: string
- container: ''
  name: membershipRuleProcessingState
  type: string
- container: ''
  name: renewedDateTime
  type: dateTime
- container: ''
  name: expirationDateTime
  type: dateTime
- container: ''
  name: preferredDataLocation
  type: string
- container: set
  name: resourceProvisioningOptions
  type: ''
- container: ''
  name: signInAudience
  type: string
- container: set
  name: identifierUris
  type: ''
- container: ''
  name: web
  type: ''
- container: set
  name: redirectUris
  type: ''
- container: ''
  name: logoutUrl
  type: anyURI
- container: set
  name: requiredResourceAccess
  type: ''
- container: set
  name: keyCredentials
  type: ''
- container: set
  name: passwordCredentials
  type: ''
- container: ''
  name: deletedDateTime
  type: dateTime
- container: ''
  name: servicePrincipalType
  type: string
- container: set
  name: appRoles
  type: ''
- container: set
  name: oauth2PermissionScopes
  type: ''
- container: ''
  name: homepage
  type: anyURI
- container: ''
  name: loginUrl
  type: anyURI
- container: set
  name: replyUrls
  type: ''
- container: set
  name: tags
  type: ''
- container: ''
  name: appRoleId
  type: string
- container: ''
  name: principalId
  type: string
- container: ''
  name: principalDisplayName
  type: string
- container: ''
  name: principalType
  type: string
- container: ''
  name: resourceId
  type: string
- container: ''
  name: resourceDisplayName
  type: string
- container: ''
  name: password
  type: string
- container: ''
  name: forceChangePasswordNextSignIn
  type: boolean
- container: ''
  name: forceChangePasswordNextSignInWithMfa
  type: boolean
property_count: 69
provider_name: Microsoft Active Directory
provider_slug: active-directory
slug: active-directory-context
tags:
- Active Directory
- Authentication
- Authorization
- Directory Services
- Identity Management
- Microsoft Entra
- Zero Trust
- JSON-LD
- Linked Data
- Semantic Web
---
