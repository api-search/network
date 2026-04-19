---
description: BroadcastCreateRequest schema from ActiveCampaign API
layout: schema
name: BroadcastCreateRequest
properties_list:
- description: Name of the broadcast
  name: name
  type: string
- description: ID for sender name
  name: address_id
  type: integer
- description: SMS message content
  name: body
  type: string
- description: Media URLs for MMS
  name: media_urls
  type: array
- description: ''
  name: preview_url
  type: string
- description: ''
  name: shorten_track_links_enabled
  type: boolean
- description: ''
  name: status
  type: string
- description: ''
  name: scheduled_date
  type: string
- description: ''
  name: sent_to_count
  type: integer
- description: ''
  name: list_ids
  type: array
- description: ''
  name: segment_id
  type: string
- description: custom segment id generated from segmentsV2 endpoint and passing in a valid audience
  name: custom_segment_id
  type: string
- description: ''
  name: label_ids
  type: array
provider_name: ActiveCampaign
provider_slug: activecampaign
schema_file: json-schema/activecampaign-sms-broadcast-create-request-schema.json
slug: activecampaign-sms-broadcast-create-request
tags:
- Marketing Automation
- Email Marketing
- CRM
- Sales Automation
- Customer Experience
title: BroadcastCreateRequest
---
