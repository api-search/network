---
description: Represents an error that occurred for a specific item in a batch operation
layout: schema
name: BatchError
properties_list:
- description: Error status code
  name: status
  type: string
- description: Error category
  name: category
  type: string
- description: Human-readable error message
  name: message
  type: string
- description: Additional context about the error
  name: context
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-crm-feature-flags-batch-error-schema.json
slug: hubspot-crm-feature-flags-batch-error
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
title: BatchError
---
