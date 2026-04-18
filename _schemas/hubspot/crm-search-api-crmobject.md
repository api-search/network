---
description: A CRM object record returned from a search.
layout: schema
name: CRMObject
properties_list:
- description: The unique identifier for the CRM record.
  name: id
  type: string
- description: The CRM record's properties as key-value pairs.
  name: properties
  type: object
- description: The date and time the record was created.
  name: createdAt
  type: string
- description: The date and time the record was last updated.
  name: updatedAt
  type: string
- description: Whether the record has been archived.
  name: archived
  type: boolean
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-search-api-crmobject-schema.json
slug: crm-search-api-crmobject
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
title: CRMObject
---
