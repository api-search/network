---
consumed_apis:
- whatsapp-business-mgmt
description: Unified workflow for managing message templates and analyzing conversation and template performance. Combines Business Management API template CRUD and analytics capabilities used by marketing teams, content managers, and business analysts.
layout: capability
name: WhatsApp Templates And Analytics
operations:
- description: Lists all message templates for a WABA.
  method: GET
  name: list-message-templates
  path: /v1/message-templates
- description: Creates a new message template.
  method: POST
  name: create-message-template
  path: /v1/message-templates
- description: Deletes a message template.
  method: DELETE
  name: delete-message-template
  path: /v1/message-templates
- description: Updates an existing message template.
  method: POST
  name: update-message-template
  path: /v1/message-templates/{message_template_id}
- description: Retrieves conversation analytics.
  method: GET
  name: get-conversation-analytics
  path: /v1/conversation-analytics
- description: Retrieves template analytics.
  method: GET
  name: get-template-analytics
  path: /v1/template-analytics
personas: []
provider_name: WhatsApp
provider_slug: whatsapp
search_terms:
- updates an existing message template. only approved or paused templates can be edited. edits re-trigger the approval process.
- updates an existing message template.
- conversation analytics and reporting.
- analytics
- message template management.
- creates a new message template.
- create message template
- individual message template management.
- update message template
- get template analytics
- retrieves template analytics.
- lists all message templates for a waba.
- deletes a message template.
- whatsapp
- creates a new message template. templates must be approved by meta before use.
- retrieves analytics for specific message templates including sent, delivered, read, clicked, and cost metrics.
- retrieves conversation analytics for a waba with configurable time range, granularity, and dimensional breakdown.
- reporting
- retrieves conversation analytics.
- marketing
- lists all message templates for a whatsapp business account. supports filtering by name, language, status, and category.
- get conversation analytics
- message templates
- list message templates
- deletes a message template. deleting by name removes all language variants.
- delete message template
- template performance analytics.
slug: templates-and-analytics
tags:
- WhatsApp
- Message Templates
- Analytics
- Marketing
- Reporting
tools:
- description: Lists all message templates for a WhatsApp Business Account. Supports filtering by name, language, status, and category.
  hints:
    idempotent: true
    readOnly: true
  name: list-message-templates
- description: Creates a new message template. Templates must be approved by Meta before use.
  hints:
    destructive: false
    readOnly: false
  name: create-message-template
- description: Updates an existing message template. Only APPROVED or PAUSED templates can be edited. Edits re-trigger the approval process.
  hints:
    idempotent: true
    readOnly: false
  name: update-message-template
- description: Deletes a message template. Deleting by name removes all language variants.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-message-template
- description: Retrieves conversation analytics for a WABA with configurable time range, granularity, and dimensional breakdown.
  hints:
    idempotent: true
    readOnly: true
  name: get-conversation-analytics
- description: Retrieves analytics for specific message templates including sent, delivered, read, clicked, and cost metrics.
  hints:
    idempotent: true
    readOnly: true
  name: get-template-analytics
---
