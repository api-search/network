---
description: A single search filter
layout: schema
name: Filter
properties_list:
- description: The property to filter on
  name: propertyName
  type: string
- description: The filter operator
  name: operator
  type: string
- description: The value to filter by
  name: value
  type: string
- description: Values for IN/NOT_IN operators
  name: values
  type: array
- description: High value for BETWEEN operator
  name: highValue
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-engagement-notes-filter-schema.json
slug: hubspot-engagement-notes-filter
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
title: Filter
---
