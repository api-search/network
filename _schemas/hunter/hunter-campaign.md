---
description: ''
layout: schema
name: Campaign
properties_list:
- description: Unique identifier for the campaign.
  name: id
  type: integer
- description: Name of the campaign.
  name: name
  type: string
- description: Number of recipients in the campaign.
  name: recipients_count
  type: integer
- description: Whether the campaign can be edited.
  name: editable
  type: boolean
- description: Whether the campaign has been started.
  name: started
  type: boolean
- description: Whether the campaign has been archived.
  name: archived
  type: boolean
- description: Whether the campaign is paused.
  name: paused
  type: boolean
- description: Current sending status of the campaign.
  name: sending_status
  type: '[''string'', ''null'']'
- description: Timestamp when the campaign was created.
  name: created_at
  type: string
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-campaign-schema.json
slug: hunter-campaign
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: Campaign
---
