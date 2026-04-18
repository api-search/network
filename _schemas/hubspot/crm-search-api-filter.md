---
description: A single filter condition for a CRM object property.
layout: schema
name: Filter
properties_list:
- description: The name of the CRM property to filter on.
  name: propertyName
  type: string
- description: The comparison operator for the filter.
  name: operator
  type: string
- description: The value to compare against. Not required for HAS_PROPERTY and NOT_HAS_PROPERTY operators.
  name: value
  type: string
- description: The upper bound value for BETWEEN operator comparisons.
  name: highValue
  type: string
- description: An array of values for IN and NOT_IN operator comparisons.
  name: values
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-search-api-filter-schema.json
slug: crm-search-api-filter
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
