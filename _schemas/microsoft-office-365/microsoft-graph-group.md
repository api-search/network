---
description: Represents an Azure Active Directory group. Can be a Microsoft 365 group, a security group, a mail-enabled security group, or a distribution group.
layout: schema
name: Group
properties_list:
- description: The unique identifier for the group.
  name: id
  type: string
- description: The display name for the group.
  name: displayName
  type: string
- description: An optional description for the group.
  name: description
  type: string
- description: The SMTP address for the group.
  name: mail
  type: string
- description: Specifies whether the group is mail-enabled.
  name: mailEnabled
  type: boolean
- description: The mail alias for the group, unique for Microsoft 365 groups in the organization.
  name: mailNickname
  type: string
- description: Specifies whether the group is a security group.
  name: securityEnabled
  type: boolean
- description: Specifies the group type and its membership. If the collection includes "Unified", the group is a Microsoft 365 group.
  name: groupTypes
  type: array
- description: Specifies the visibility of a Microsoft 365 group. Default value is Public.
  name: visibility
  type: string
- description: Timestamp of when the group was created.
  name: createdDateTime
  type: string
- description: Timestamp of when the group was last renewed.
  name: renewedDateTime
  type: string
- description: Describes a classification for the group (such as low, medium, or high business impact).
  name: classification
  type: string
- description: The rule that determines members for this group if the group is a dynamic group.
  name: membershipRule
  type: string
- description: Whether dynamic membership processing is on or paused.
  name: membershipRuleProcessingState
  type: string
- description: Specifies the group resources provisioned as part of Microsoft 365 group creation (e.g., Team).
  name: resourceProvisioningOptions
  type: array
- description: Direct members of this group.
  name: members
  type: array
- description: The owners of the group.
  name: owners
  type: array
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-graph-group-schema.json
slug: microsoft-graph-group
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: Group
---
