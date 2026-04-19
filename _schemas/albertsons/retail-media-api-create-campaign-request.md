---
description: Request body for creating a new advertising campaign.
layout: schema
name: Create Campaign Request
properties_list:
- description: Display name for the new campaign.
  name: name
  type: string
- description: Total budget allocated to the campaign in USD.
  name: budget
  type: number
- description: Campaign start date (ISO 8601).
  name: startDate
  type: string
- description: Campaign end date (ISO 8601).
  name: endDate
  type: string
- description: List of audience segment IDs for targeting.
  name: targetAudienceIds
  type: array
provider_name: albertsons
provider_slug: albertsons
schema_file: json-schema/retail-media-api-create-campaign-request-schema.json
slug: retail-media-api-create-campaign-request
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
title: Create Campaign Request
---
