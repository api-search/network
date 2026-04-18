---
description: A HubSpot deal record.
layout: schema
name: Deal
properties_list:
- description: The unique identifier for the deal.
  name: id
  type: string
- description: The deal's properties as key-value pairs.
  name: properties
  type: object
- description: The date and time the deal was created.
  name: createdAt
  type: string
- description: The date and time the deal was last updated.
  name: updatedAt
  type: string
- description: Whether the deal has been archived.
  name: archived
  type: boolean
- description: The deal's associations with other CRM objects.
  name: associations
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-crm-deals-deal-schema.json
slug: hubspot-crm-deals-deal
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
title: Deal
---
