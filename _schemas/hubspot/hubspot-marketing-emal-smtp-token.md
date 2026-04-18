---
description: Represents an SMTP API token for transactional email sending
layout: schema
name: SmtpToken
properties_list:
- description: The unique identifier for the SMTP token
  name: id
  type: string
- description: The name of the email campaign associated with this token
  name: campaignName
  type: string
- description: The ID of the associated email campaign
  name: emailCampaignId
  type: string
- description: Whether sending an email creates a contact if one doesn't exist
  name: createContact
  type: boolean
- description: When the token was created
  name: createdAt
  type: string
- description: The user or application that created the token
  name: createdBy
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-marketing-emal-smtp-token-schema.json
slug: hubspot-marketing-emal-smtp-token
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
title: SmtpToken
---
