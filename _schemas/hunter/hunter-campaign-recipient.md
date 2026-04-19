---
description: ''
layout: schema
name: CampaignRecipient
properties_list:
- description: Recipient email address.
  name: email
  type: string
- description: Associated lead identifier.
  name: lead_id
  type: '[''integer'', ''null'']'
- description: Current sending status for this recipient.
  name: sending_status
  type: string
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-campaign-recipient-schema.json
slug: hunter-campaign-recipient
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: CampaignRecipient
---
