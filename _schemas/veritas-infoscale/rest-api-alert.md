---
description: Cluster alert schema from Veritas InfoScale REST API
layout: schema
name: Alert
properties_list:
- description: Alert unique identifier
  name: alertId
  type: string
- description: Alert severity
  name: severity
  type: string
- description: Alert message
  name: message
  type: string
- description: Alert source component
  name: source
  type: string
- description: Alert timestamp
  name: timestamp
  type: string
- description: Whether the alert has been acknowledged
  name: acknowledged
  type: boolean
- description: Related cluster identifier
  name: clusterId
  type: string
provider_name: Veritas InfoScale
provider_slug: veritas-infoscale
schema_file: json-schema/rest-api-alert-schema.json
slug: rest-api-alert
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
title: Alert
---
