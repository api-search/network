---
description: A column definition in a HubDB table.
layout: schema
name: HubDBColumn
properties_list:
- description: The unique identifier for the column.
  name: id
  type: string
- description: The machine-readable name of the column.
  name: name
  type: string
- description: The human-readable label for the column.
  name: label
  type: string
- description: The data type of the column.
  name: type
  type: string
- description: Available options for SELECT and MULTISELECT columns.
  name: options
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/cms-hubdb-api-hub-dbcolumn-schema.json
slug: cms-hubdb-api-hub-dbcolumn
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: HubDBColumn
---
