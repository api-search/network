---
description: A paginated collection of users.
layout: schema
name: UserCollection
properties_list:
- description: Cursor for the next page of results.
  name: nextPageKey
  type: string
- description: The total number of users in the account.
  name: totalCount
  type: integer
- description: The list of users on this page.
  name: items
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-account-management-user-collection-schema.json
slug: dynatrace-account-management-user-collection
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
title: UserCollection
---
