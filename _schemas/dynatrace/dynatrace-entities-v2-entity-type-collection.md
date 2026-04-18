---
description: A paginated collection of entity type definitions.
layout: schema
name: EntityTypeCollection
properties_list:
- description: Cursor for the next page of results.
  name: nextPageKey
  type: string
- description: The total number of entity types.
  name: totalCount
  type: integer
- description: The list of entity types on this page.
  name: types
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-entities-v2-entity-type-collection-schema.json
slug: dynatrace-entities-v2-entity-type-collection
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
title: EntityTypeCollection
---
