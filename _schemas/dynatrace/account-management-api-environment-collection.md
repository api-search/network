---
description: A paginated collection of environments.
layout: schema
name: EnvironmentCollection
properties_list:
- description: Cursor for the next page of results.
  name: nextPageKey
  type: string
- description: The total number of environments in the account.
  name: totalCount
  type: integer
- description: The list of environments on this page.
  name: environments
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/account-management-api-environment-collection-schema.json
slug: account-management-api-environment-collection
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
title: EnvironmentCollection
---
