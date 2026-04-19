---
description: BroadcastMessage schema from ActiveCampaign API
layout: schema
name: BroadcastMessage
properties_list:
- description: Unique identifier for the broadcast
  name: id
  type: integer
- description: Name of the broadcast
  name: name
  type: string
- description: ID used to get sender name
  name: address_id
  type: integer
- description: SMS message content
  name: body
  type: string
- description: Media URLs for MMS messages
  name: media_urls
  type: array
- description: URL for message preview
  name: preview_url
  type: string
- description: Whether link shortening is enabled
  name: shorten_track_links_enabled
  type: boolean
- description: Current status of the broadcast
  name: status
  type: string
- description: Date when broadcast was sent
  name: sent_date
  type: string
- description: Scheduled send date (UTC)
  name: scheduled_date
  type: string
- description: custom run id generated from segmentMatchSome endpoint
  name: custom_run_id
  type: string
- description: custom segment id generated from segmentsV2 endpoint and passing in a valid audience
  name: custom_segment_id
  type: string
- description: User ID who scheduled the broadcast
  name: scheduled_by
  type: integer
- description: Number of recipients
  name: sent_to_count
  type: integer
- description: Creation timestamp
  name: created_at
  type: string
- description: User ID who created the broadcast
  name: created_by
  type: integer
- description: Last update timestamp
  name: updated_at
  type: string
- description: User ID who last updated
  name: updated_by
  type: integer
- description: Deletion timestamp (for soft deletes)
  name: deleted_at
  type: string
- description: Sift approval status
  name: sift_approved
  type: integer
- description: ARC approval status
  name: arc_approved
  type: integer
- description: Whether quiet hours are enabled
  name: quiet_hours_enabled
  type: integer
- description: Associated list IDs
  name: list_ids
  type: array
- description: Segment ID (can be UUID or integer string)
  name: segment_id
  type: string
- description: Associated label IDs
  name: label_ids
  type: array
provider_name: ActiveCampaign
provider_slug: activecampaign
schema_file: json-schema/activecampaign-sms-broadcast-message-schema.json
slug: activecampaign-sms-broadcast-message
tags:
- Marketing Automation
- Email Marketing
- CRM
- Sales Automation
- Customer Experience
title: BroadcastMessage
---
