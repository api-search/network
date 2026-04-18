---
description: A paginated collection of monitored entities.
layout: schema
name: EntityCollection
properties_list:
- description: Cursor for the next page of results. Null if no more pages.
  name: nextPageKey
  type: string
- description: The total number of entities matching the query.
  name: totalCount
  type: integer
- description: The number of results returned on this page.
  name: pageSize
  type: integer
- description: The list of entities on this page.
  name: entities
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/entities-api-v2-entity-collection-schema.json
slug: entities-api-v2-entity-collection
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
title: EntityCollection
---
