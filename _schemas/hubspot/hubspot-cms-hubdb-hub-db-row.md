---
description: A row in a HubDB table.
layout: schema
name: HubDBRow
properties_list:
- description: The unique identifier for the row.
  name: id
  type: string
- description: The column values for the row as key-value pairs.
  name: values
  type: object
- description: The date and time the row was created.
  name: createdAt
  type: string
- description: The date and time the row was last updated.
  name: updatedAt
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-cms-hubdb-hub-db-row-schema.json
slug: hubspot-cms-hubdb-hub-db-row
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
title: HubDBRow
---
