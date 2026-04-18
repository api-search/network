---
description: A HubDB table.
layout: schema
name: HubDBTable
properties_list:
- description: The unique identifier for the table.
  name: id
  type: string
- description: The machine-readable name of the table.
  name: name
  type: string
- description: The human-readable label for the table.
  name: label
  type: string
- description: The column definitions for the table.
  name: columns
  type: array
- description: Whether the table has been published.
  name: published
  type: boolean
- description: The number of rows in the published table.
  name: rowCount
  type: integer
- description: The date and time the table was created.
  name: createdAt
  type: string
- description: The date and time the table was last updated.
  name: updatedAt
  type: string
- description: The date and time the table was last published.
  name: publishedAt
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-cms-hubdb-hub-db-table-schema.json
slug: hubspot-cms-hubdb-hub-db-table
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
title: HubDBTable
---
