---
description: A commerce payment object representing a payment transaction
layout: schema
name: CommercePayment
properties_list:
- description: The unique identifier of the commerce payment
  name: id
  type: string
- description: The properties of the commerce payment
  name: properties
  type: object
- description: When the commerce payment was created
  name: createdAt
  type: string
- description: When the commerce payment was last updated
  name: updatedAt
  type: string
- description: Whether the commerce payment is archived
  name: archived
  type: boolean
- description: When the commerce payment was archived
  name: archivedAt
  type: string
- description: Associated objects
  name: associations
  type: object
- description: Properties with their value history
  name: propertiesWithHistory
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/commerce-payments-api-commerce-payment-schema.json
slug: commerce-payments-api-commerce-payment
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
title: CommercePayment
---
