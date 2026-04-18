---
description: A HubSpot contact record.
layout: schema
name: Contact
properties_list:
- description: The unique identifier for the contact.
  name: id
  type: string
- description: The contact's properties as key-value pairs.
  name: properties
  type: object
- description: The date and time the contact was created.
  name: createdAt
  type: string
- description: The date and time the contact was last updated.
  name: updatedAt
  type: string
- description: Whether the contact has been archived.
  name: archived
  type: boolean
- description: The contact's associations with other CRM objects.
  name: associations
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-contacts-api-contact-schema.json
slug: crm-contacts-api-contact
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
title: Contact
---
