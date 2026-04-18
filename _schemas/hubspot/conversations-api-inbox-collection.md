---
description: Paginated collection of inboxes
layout: schema
name: InboxCollection
properties_list:
- description: Array of inbox records
  name: results
  type: array
- description: Total number of inboxes available
  name: total
  type: integer
- description: Pagination information for list responses.
  name: paging
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/conversations-api-inbox-collection-schema.json
slug: conversations-api-inbox-collection
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
title: InboxCollection
---
