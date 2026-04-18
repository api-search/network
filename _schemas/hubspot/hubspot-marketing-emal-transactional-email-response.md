---
description: Response after sending a transactional email
layout: schema
name: TransactionalEmailResponse
properties_list:
- description: The status of the email send
  name: status
  type: string
- description: A unique identifier for tracking the email status
  name: statusId
  type: string
- description: Additional details about the send result
  name: sendResult
  type: string
- description: When the send was requested
  name: requestedAt
  type: string
- description: When the send processing started
  name: startedAt
  type: string
- description: When the send processing completed
  name: completedAt
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-marketing-emal-transactional-email-response-schema.json
slug: hubspot-marketing-emal-transactional-email-response
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
title: TransactionalEmailResponse
---
