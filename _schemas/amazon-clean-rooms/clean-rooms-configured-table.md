---
description: Represents a configured table in Clean Rooms.
layout: schema
name: ConfiguredTable
properties_list:
- description: The unique ID of the configured table.
  name: id
  type: string
- description: The ARN of the configured table.
  name: arn
  type: string
- description: A human-readable name for the configured table.
  name: name
  type: string
- description: A description of the configured table.
  name: description
  type: string
- description: The time when the configured table was created.
  name: createTime
  type: string
- description: The time when the configured table was last updated.
  name: updateTime
  type: string
- description: The analysis method for the configured table.
  name: analysisMethod
  type: string
provider_name: Amazon Clean Rooms
provider_slug: amazon-clean-rooms
schema_file: json-schema/clean-rooms-configured-table-schema.json
slug: clean-rooms-configured-table
tags:
- AWS
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
title: ConfiguredTable
---
