---
description: A Microsoft Entra security group or Microsoft 365 group managed via Microsoft Graph
layout: schema
name: Group
properties_list:
- description: Unique identifier for the group object (read-only)
  name: id
  type: string
- description: Display name for the group
  name: displayName
  type: string
- description: Optional description for the group
  name: description
  type:
  - string
  - 'null'
- description: SMTP address for the group
  name: mail
  type:
  - string
  - 'null'
- description: Mail alias for the group (without domain suffix)
  name: mailNickname
  type: string
- description: Specifies whether the group is mail-enabled
  name: mailEnabled
  type: boolean
- description: Specifies whether the group is a security group
  name: securityEnabled
  type: boolean
- description: Collection specifying the group type and dynamic membership. Unified = Microsoft 365 group.
  name: groupTypes
  type: array
- description: Visibility of a Microsoft 365 group content and members list
  name: visibility
  type:
  - string
  - 'null'
- description: Rule defining dynamic group membership (requires DynamicMembership in groupTypes)
  name: membershipRule
  type:
  - string
  - 'null'
- description: Indicates whether dynamic membership processing is on or paused
  name: membershipRuleProcessingState
  type:
  - string
  - 'null'
- description: True if the group is synced from on-premises Active Directory
  name: onPremisesSyncEnabled
  type:
  - boolean
  - 'null'
- description: Distinguished name from on-premises AD
  name: onPremisesDistinguishedName
  type:
  - string
  - 'null'
- description: Timestamp when the group was created
  name: createdDateTime
  type:
  - string
  - 'null'
- description: Timestamp when the Microsoft 365 group was last renewed
  name: renewedDateTime
  type:
  - string
  - 'null'
- description: Timestamp when the group expires (requires an expiration policy)
  name: expirationDateTime
  type:
  - string
  - 'null'
- description: Preferred data location for multi-geo tenant (e.g. CAN, EUR)
  name: preferredDataLocation
  type:
  - string
  - 'null'
- description: Resources provisioned (e.g. Team for Microsoft Teams-enabled groups)
  name: resourceProvisioningOptions
  type: array
provider_name: Microsoft Active Directory
provider_slug: active-directory
schema_file: json-schema/groups-group-schema.json
slug: groups-group
tags:
- Active Directory
- Authentication
- Authorization
- Directory Services
- Identity Management
- Microsoft Entra
- Zero Trust
title: Group
---
