---
description: A Mailchimp email marketing campaign. Represents a single email send or series of emails targeted at a list or segment of subscribers. Campaigns can be regular, plain-text, A/B split, RSS-driven, or multivariate.
layout: schema
name: Mailchimp Campaign
properties_list:
- description: A string that uniquely identifies this campaign.
  name: id
  type: string
- description: The ID used in the Mailchimp web application.
  name: web_id
  type: integer
- description: If this campaign is the child of another campaign, this identifies the parent campaign. For example, for RSS or Automation children.
  name: parent_campaign_id
  type: string
- description: The type of campaign.
  name: type
  type: string
- description: The date and time the campaign was created in ISO 8601 format.
  name: create_time
  type: string
- description: The link to the campaign's archive version.
  name: archive_url
  type: string
- description: The original link to the campaign's archive version.
  name: long_archive_url
  type: string
- description: The current status of the campaign.
  name: status
  type: string
- description: The total number of emails sent for this campaign.
  name: emails_sent
  type: integer
- description: The date and time a campaign was sent in ISO 8601 format.
  name: send_time
  type: string
- description: How the campaign's content is put together.
  name: content_type
  type: string
- description: Deprecated. Whether the campaign needs its blocks refreshed by opening the web-based campaign editor. Will always return false.
  name: needs_block_refresh
  type: boolean
- description: Whether the campaign qualifies to be resent to non-openers.
  name: resendable
  type: boolean
- description: List/audience settings for the campaign.
  name: recipients
  type: object
- description: The settings for the campaign, including subject line, from name, and reply-to address.
  name: settings
  type: object
- description: The tracking options for a campaign.
  name: tracking
  type: object
- description: For sent campaigns, a summary of opens, clicks, and e-commerce data.
  name: report_summary
  type: object
- description: Updates on campaigns in the process of sending.
  name: delivery_status
  type: object
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/campaign.json
slug: campaign
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: Mailchimp Campaign
---
