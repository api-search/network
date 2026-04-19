---
description: OData collection response containing entity definition records.
layout: schema
name: EntityCollection
properties_list:
- description: OData context URL describing the collection.
  name: '@odata.context'
  type: string
- description: Total count of matching records (when $count=true).
  name: '@odata.count'
  type: integer
- description: URL to retrieve the next page of results.
  name: '@odata.nextLink'
  type: string
- description: Array of entity definition records.
  name: value
  type: array
provider_name: Microsoft Power Apps
provider_slug: microsoft-power-apps
schema_file: json-schema/microsoft-power-apps-dataverse-web-entity-collection-schema.json
slug: microsoft-power-apps-dataverse-web-entity-collection
tags:
- Business Applications
- Cloud
- Enterprise
- Low-Code
- Microsoft
- No-Code
- Power Platform
- SaaS
title: EntityCollection
---
