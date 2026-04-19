---
description: OData collection response containing account records.
layout: schema
name: AccountCollection
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
- description: Array of account records.
  name: value
  type: array
provider_name: Microsoft Power Apps
provider_slug: microsoft-power-apps
schema_file: json-schema/microsoft-power-apps-dataverse-web-account-collection-schema.json
slug: microsoft-power-apps-dataverse-web-account-collection
tags:
- Business Applications
- Cloud
- Enterprise
- Low-Code
- Microsoft
- No-Code
- Power Platform
- SaaS
title: AccountCollection
---
