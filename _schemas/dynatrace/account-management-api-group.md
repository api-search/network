---
description: Represents a user group in the Dynatrace account.
layout: schema
name: Group
properties_list:
- description: The unique identifier of the group.
  name: groupId
  type: string
- description: The display name of the group.
  name: name
  type: string
- description: An optional description of the group's purpose or scope.
  name: description
  type: string
- description: The identifier of the group owner. LOCAL indicates the group is managed within Dynatrace; SSO indicates it is synced from an identity provider.
  name: owner
  type: string
- description: The date and time when the group was created.
  name: createdAt
  type: string
- description: The date and time when the group was last updated.
  name: updatedAt
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/account-management-api-group-schema.json
slug: account-management-api-group
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: Group
---
