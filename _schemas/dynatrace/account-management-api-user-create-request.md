---
description: Request body for creating or updating a user.
layout: schema
name: UserCreateRequest
properties_list:
- description: The email address of the user. Used as the login identifier.
  name: email
  type: string
- description: The first name of the user.
  name: firstName
  type: string
- description: The last name of the user.
  name: lastName
  type: string
- description: The list of group IDs to assign the user to. The user gains all permissions associated with these groups.
  name: groups
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/account-management-api-user-create-request-schema.json
slug: account-management-api-user-create-request
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
title: UserCreateRequest
---
