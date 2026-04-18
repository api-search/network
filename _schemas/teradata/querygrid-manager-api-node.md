---
description: A node in the QueryGrid environment.
layout: schema
name: Node
properties_list:
- description: Unique node identifier.
  name: id
  type: string
- description: Node name.
  name: name
  type: string
- description: Node hostname.
  name: hostname
  type: string
- description: Parent system identifier.
  name: systemId
  type: string
- description: Node status.
  name: status
  type: string
- description: Installed software version.
  name: softwareVersion
  type: string
provider_name: Teradata
provider_slug: teradata
schema_file: json-schema/querygrid-manager-api-node-schema.json
slug: querygrid-manager-api-node
tags:
- Analytics
- Cloud
- Data Management
- Data Warehousing
- Database
- Enterprise
- Machine Learning
- SQL
title: Node
---
