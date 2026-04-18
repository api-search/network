---
description: A single filter criterion
layout: schema
name: Filter
properties_list:
- description: The property to filter on
  name: propertyName
  type: string
- description: The comparison operator
  name: operator
  type: string
- description: The value to compare against
  name: value
  type: string
- description: Values for IN/NOT_IN operators
  name: values
  type: array
- description: Upper bound for BETWEEN operator
  name: highValue
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/commerce-payments-api-filter-schema.json
slug: commerce-payments-api-filter
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
