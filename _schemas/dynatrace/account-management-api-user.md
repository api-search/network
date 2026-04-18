---
description: Represents a user in the Dynatrace account.
layout: schema
name: User
properties_list:
- description: The unique identifier of the user.
  name: uid
  type: string
- description: The email address of the user, used as their login identifier.
  name: email
  type: string
- description: The first name of the user.
  name: firstName
  type: string
- description: The last name of the user.
  name: lastName
  type: string
- description: The list of group IDs that the user belongs to.
  name: groups
  type: array
- description: The current status of the user account.
  name: userStatus
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/account-management-api-user-schema.json
slug: account-management-api-user
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
title: User
---
