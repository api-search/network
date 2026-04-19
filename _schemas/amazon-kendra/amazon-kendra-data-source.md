---
description: A data source connector for an Amazon Kendra index.
layout: schema
name: DataSource
properties_list:
- description: The identifier of the data source.
  name: Id
  type: string
- description: The name of the data source.
  name: Name
  type: string
- description: The type of the data source.
  name: Type
  type: string
- description: The status of the data source.
  name: Status
  type: string
- description: The cron schedule for sync.
  name: Schedule
  type: string
- description: The ID of the index this data source belongs to.
  name: IndexId
  type: string
provider_name: Amazon Kendra
provider_slug: amazon-kendra
schema_file: json-schema/amazon-kendra-data-source-schema.json
slug: amazon-kendra-data-source
tags:
- AI
- AWS
- Enterprise Search
- Knowledge Management
- Machine Learning
- Natural Language
title: DataSource
---
