---
description: BroadcastUpdateRequest schema from ActiveCampaign API
layout: schema
name: BroadcastUpdateRequest
properties_list:
- description: ''
  name: name
  type: string
- description: ''
  name: address_id
  type: integer
- description: ''
  name: body
  type: string
- description: ''
  name: media_urls
  type: array
- description: ''
  name: preview_url
  type: string
- description: ''
  name: shorten_track_links_enabled
  type: boolean
- description: Status of the broadcast. pending_review starts kicks off the broadcast to be sent
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
- description: custom run id generated from segmentMatchSome endpoint and passing a valid segment id
  name: custom_run_id
  type: string
- description: custom segment id generated from segmentsV2 endpoint and passing in a valid audience
  name: custom_segment_id
  type: string
- description: ''
  name: label_ids
  type: array
provider_name: ActiveCampaign
provider_slug: activecampaign
schema_file: json-schema/activecampaign-sms-broadcast-update-request-schema.json
slug: activecampaign-sms-broadcast-update-request
tags:
- Marketing Automation
- Email Marketing
- CRM
- Sales Automation
- Customer Experience
title: BroadcastUpdateRequest
---
