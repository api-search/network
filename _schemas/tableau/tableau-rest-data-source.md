---
description: ''
layout: schema
name: DataSource
properties_list:
- description: The unique identifier for the data source.
  name: id
  type: string
- description: The name of the data source.
  name: name
  type: string
- description: A description of the data source.
  name: description
  type: string
- description: The URL name of the data source.
  name: contentUrl
  type: string
- description: The type of data source (e.g., sqlserver, postgres, excel, hyper, etc.).
  name: type
  type: string
- description: The date and time the data source was created.
  name: createdAt
  type: string
- description: The date and time the data source was last updated.
  name: updatedAt
  type: string
- description: Whether the data source is certified.
  name: isCertified
  type: boolean
- description: The certification note for the data source.
  name: certificationNote
  type: string
- description: Whether the data source uses a remote query agent.
  name: useRemoteQueryAgent
  type: boolean
- description: Whether the data source has extracts.
  name: hasExtracts
  type: boolean
- description: Whether the data source extracts are encrypted.
  name: encryptExtracts
  type: string
- description: ''
  name: project
  type: object
- description: ''
  name: owner
  type: object
- description: ''
  name: tags
  type: object
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-data-source-schema.json
slug: tableau-rest-data-source
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: DataSource
---
