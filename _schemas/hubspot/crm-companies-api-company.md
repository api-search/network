---
description: A HubSpot company record.
layout: schema
name: Company
properties_list:
- description: The unique identifier for the company.
  name: id
  type: string
- description: The company's properties as key-value pairs.
  name: properties
  type: object
- description: The date and time the company was created.
  name: createdAt
  type: string
- description: The date and time the company was last updated.
  name: updatedAt
  type: string
- description: Whether the company has been archived.
  name: archived
  type: boolean
- description: The company's associations with other CRM objects.
  name: associations
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-companies-api-company-schema.json
slug: crm-companies-api-company
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
title: Company
---
