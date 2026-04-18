---
description: Result of an association query
layout: schema
name: AssociationResult
properties_list:
- description: Reference to a CRM object by ID
  name: from
  type: object
- description: Associated objects
  name: to
  type: array
- description: Pagination information
  name: paging
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-associations-api-association-result-schema.json
slug: crm-associations-api-association-result
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
title: AssociationResult
---
