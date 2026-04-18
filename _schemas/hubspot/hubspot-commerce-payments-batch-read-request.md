---
description: Request body for batch reading commerce payments
layout: schema
name: BatchReadRequest
properties_list:
- description: List of payment identifiers to read
  name: inputs
  type: array
- description: Properties to return for each payment
  name: properties
  type: array
- description: Properties to return with history
  name: propertiesWithHistory
  type: array
- description: The property to use as the identifier
  name: idProperty
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-commerce-payments-batch-read-request-schema.json
slug: hubspot-commerce-payments-batch-read-request
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
title: BatchReadRequest
---
