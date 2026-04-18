---
description: A paginated collection of groups.
layout: schema
name: GroupCollection
properties_list:
- description: Cursor for the next page of results.
  name: nextPageKey
  type: string
- description: The total number of groups in the account.
  name: totalCount
  type: integer
- description: The list of groups on this page.
  name: items
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/account-management-api-group-collection-schema.json
slug: account-management-api-group-collection
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
title: GroupCollection
---
