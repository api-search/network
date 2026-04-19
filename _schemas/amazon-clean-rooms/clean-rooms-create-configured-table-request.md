---
description: Request body for creating a configured table.
layout: schema
name: CreateConfiguredTableRequest
properties_list:
- description: The name of the configured table.
  name: name
  type: string
- description: A description for the configured table.
  name: description
  type: string
- description: A reference to the AWS Glue table being configured.
  name: tableReference
  type: object
- description: The columns of the underlying AWS Glue table that can be used by collaborators.
  name: allowedColumns
  type: array
- description: The analysis method for the configured table.
  name: analysisMethod
  type: string
provider_name: Amazon Clean Rooms
provider_slug: amazon-clean-rooms
schema_file: json-schema/clean-rooms-create-configured-table-request-schema.json
slug: clean-rooms-create-configured-table-request
tags:
- AWS
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
title: CreateConfiguredTableRequest
---
