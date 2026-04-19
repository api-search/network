---
description: ''
layout: schema
name: DataSource
properties_list:
- description: The Workday ID of the data source.
  name: id
  type: string
- description: A display descriptor for the data source.
  name: descriptor
  type: string
- description: The name of the data source used in WQL FROM clauses.
  name: name
  type: string
- description: The plural name of the data source.
  name: pluralName
  type: string
- description: The fields available in this data source.
  name: fields
  type: array
provider_name: Workday
provider_slug: workday
schema_file: json-schema/wql-data-source-schema.json
slug: wql-data-source
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: DataSource
---
