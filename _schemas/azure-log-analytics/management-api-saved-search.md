---
description: A saved search (KQL query) in a Log Analytics workspace.
layout: schema
name: SavedSearch
properties_list:
- description: Fully qualified resource ID.
  name: id
  type: string
- description: The name of the resource.
  name: name
  type: string
- description: The type of the resource.
  name: type
  type: string
- description: The ETag of the saved search.
  name: etag
  type: string
- description: Saved search properties.
  name: properties
  type: object
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
schema_file: json-schema/management-api-saved-search-schema.json
slug: management-api-saved-search
tags:
- Analytics
- Azure
- Cloud
- Logging
- Monitoring
title: SavedSearch
---
