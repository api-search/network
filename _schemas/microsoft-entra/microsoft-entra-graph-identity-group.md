---
description: Represents a Microsoft Entra group. Groups can be Microsoft 365 groups, security groups, mail-enabled security groups, or distribution groups.
layout: schema
name: Group
properties_list:
- description: Unique identifier for the group (GUID)
  name: id
  type: string
- description: The display name for the group. Required on create.
  name: displayName
  type: string
- description: An optional description for the group
  name: description
  type: '[''string'', ''null'']'
- description: Specifies whether the group is mail-enabled. Required on create. Set to true for Microsoft 365 groups.
  name: mailEnabled
  type: boolean
- description: The mail alias for the group, unique for Microsoft 365 groups. Required on create.
  name: mailNickname
  type: string
- description: Specifies whether the group is a security group. Required on create. Set to false for Microsoft 365 groups.
  name: securityEnabled
  type: boolean
- description: Specifies the group type. Set to ["Unified"] for Microsoft 365 groups. Empty array or ["DynamicMembership"] for other types.
  name: groupTypes
  type: array
- description: Specifies the group's join policy and content visibility for Microsoft 365 groups
  name: visibility
  type: '[''string'', ''null'']'
- description: 'The rule that determines members for this group if the group is a dynamic group. Example: user.department -eq "Marketing"'
  name: membershipRule
  type: '[''string'', ''null'']'
- description: Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused.
  name: membershipRuleProcessingState
  type: '[''string'', ''null'']'
- description: The SMTP address for the group
  name: mail
  type: '[''string'', ''null'']'
- description: Email addresses for the group that direct to the same inbox
  name: proxyAddresses
  type: array
- description: Indicates whether this group can be assigned to a Microsoft Entra role. Can only be set at group creation time.
  name: isAssignableToRole
  type: '[''boolean'', ''null'']'
- description: true if this group is synced from an on-premises directory
  name: onPremisesSyncEnabled
  type: '[''boolean'', ''null'']'
- description: Timestamp of when the group was created
  name: createdDateTime
  type: string
- description: Timestamp of when the group was last renewed (activity that extends expiration)
  name: renewedDateTime
  type: '[''string'', ''null'']'
- description: Direct members of this group. Returned only with $expand.
  name: members
  type: array
- description: Owners of the group. Returned only with $expand.
  name: owners
  type: array
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-group-schema.json
slug: microsoft-entra-graph-identity-group
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
title: Group
---
