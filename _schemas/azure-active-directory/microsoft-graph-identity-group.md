---
description: 'Represents an Azure AD group. Groups are collections of principals with shared access to resources. Microsoft Graph supports several types of groups: Microsoft 365 groups, security groups, and mail-enabled security groups.'
layout: schema
name: Group
properties_list:
- description: Classification for the group (e.g., low, medium, high business impact).
  name: classification
  type: '[''string'', ''null'']'
- description: Timestamp of when the group was created.
  name: createdDateTime
  type: string
- description: An optional description for the group.
  name: description
  type: '[''string'', ''null'']'
- description: The display name for the group. Required on creation.
  name: displayName
  type: string
- description: Timestamp of when the group is set to expire.
  name: expirationDateTime
  type: '[''string'', ''null'']'
- description: Specifies the group type. Include Unified for Microsoft 365 groups. Include DynamicMembership for dynamic groups.
  name: groupTypes
  type: array
- description: Indicates whether this group can be assigned to an Azure AD role. Can only be set at creation time.
  name: isAssignableToRole
  type: '[''boolean'', ''null'']'
- description: The SMTP address for the group.
  name: mail
  type: '[''string'', ''null'']'
- description: Specifies whether the group is mail-enabled. Required on creation.
  name: mailEnabled
  type: boolean
- description: The mail alias for the group, unique for Microsoft 365 groups. Required on creation.
  name: mailNickname
  type: string
- description: The rule that determines members for a dynamic group.
  name: membershipRule
  type: '[''string'', ''null'']'
- description: Indicates whether the dynamic membership processing is on or paused. On or Paused.
  name: membershipRuleProcessingState
  type: '[''string'', ''null'']'
- description: ''
  name: onPremisesDomainName
  type: '[''string'', ''null'']'
- description: ''
  name: onPremisesLastSyncDateTime
  type: '[''string'', ''null'']'
- description: ''
  name: onPremisesSyncEnabled
  type: '[''boolean'', ''null'']'
- description: The preferred language for a Microsoft 365 group in ISO 639-1 format.
  name: preferredLanguage
  type: '[''string'', ''null'']'
- description: ''
  name: proxyAddresses
  type: array
- description: Timestamp of when the group was last renewed.
  name: renewedDateTime
  type: string
- description: Specifies whether the group is a security group. Required on creation.
  name: securityEnabled
  type: boolean
- description: Security identifier (SID) of the group.
  name: securityIdentifier
  type: '[''string'', ''null'']'
- description: Specifies the group join policy and group content visibility. Public, Private, or HiddenMembership.
  name: visibility
  type: '[''string'', ''null'']'
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-group-schema.json
slug: microsoft-graph-identity-group
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
title: Group
---
