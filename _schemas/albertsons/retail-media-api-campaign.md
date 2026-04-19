---
description: An advertising campaign on the Albertsons Media Collective platform.
layout: schema
name: Campaign
properties_list:
- description: Unique identifier of the campaign.
  name: campaignId
  type: string
- description: Display name of the campaign.
  name: name
  type: string
- description: Current status of the campaign.
  name: status
  type: string
- description: Total budget allocated to the campaign in USD.
  name: budget
  type: number
- description: Campaign start date in ISO 8601 format.
  name: startDate
  type: string
- description: Campaign end date in ISO 8601 format.
  name: endDate
  type: string
- description: Total impressions delivered for the campaign.
  name: impressions
  type: integer
- description: Total clicks recorded for the campaign.
  name: clicks
  type: integer
provider_name: albertsons
provider_slug: albertsons
schema_file: json-schema/retail-media-api-campaign-schema.json
slug: retail-media-api-campaign
tags:
- Grocery
- Retail
- Retail Media
- Advertising
- Campaigns
- Analytics
- Consumer Goods
- Food
- Pharmacy
title: Campaign
---
