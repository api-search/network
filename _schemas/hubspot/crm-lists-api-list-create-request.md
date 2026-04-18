---
description: Request body for creating a new CRM list.
layout: schema
name: ListCreateRequest
properties_list:
- description: The name of the list.
  name: name
  type: string
- description: The object type ID for the list (e.g., 0-1 for contacts).
  name: objectTypeId
  type: string
- description: The type of list processing.
  name: processingType
  type: string
- description: The filter branch definition for dynamic lists.
  name: filterBranch
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-lists-api-list-create-request-schema.json
slug: crm-lists-api-list-create-request
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
title: ListCreateRequest
---
