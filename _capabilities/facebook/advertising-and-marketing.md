---
consumed_apis:
- marketing-api
- graph-api
- instagram-api
description: Workflow capability for managing advertising campaigns across Facebook and Instagram. Combines Marketing API for campaign management with Graph API for content insights and Instagram API for visual ad performance. Used by marketing managers and ad operations teams.
layout: capability
name: Facebook Advertising and Marketing
operations:
- description: List advertising campaigns.
  method: GET
  name: list-campaigns
  path: /v1/campaigns
- description: Create a campaign.
  method: POST
  name: create-campaign
  path: /v1/campaigns
- description: Get advertising insights.
  method: GET
  name: get-insights
  path: /v1/insights
- description: List custom audiences.
  method: GET
  name: list-audiences
  path: /v1/audiences
personas: []
provider_name: Facebook
provider_slug: facebook
search_terms:
- create custom audience
- Conversational Commerce
- campaigns
- handles customer inquiries via messaging channels.
- plans and executes advertising campaigns.
- get insights
- manages content and engagement across meta platforms.
- social networking
- campaign management and audience targeting.
- create a campaign.
- manage advertising campaigns and performance.
- advertising
- create a new advertising campaign.
- Marketing Manager
- Customer Support
- Ad Operations
- social media
- list advertising campaigns.
- list custom audiences.
- create a new custom audience.
- marketing
- campaign management.
- get advertising insights.
- messaging
- create campaign
- direct messaging and customer communication.
- facebook
- list all advertising campaigns.
- list custom audiences
- get advertising performance insights.
- performance insights.
- list audiences
- performance tracking and insights.
- manage content across facebook, instagram, and threads.
- Content Creator
- creates and publishes visual and text content.
- audience management.
- Social Media Manager
- get ad insights
- customer messaging across messenger and whatsapp.
- publishing and managing content across platforms.
- content publishing
- list campaigns
- manages day-to-day ad campaign optimization.
- list custom audiences for targeting.
slug: advertising-and-marketing
tags:
- Facebook
- Advertising
- Marketing
- Campaigns
tools:
- description: List all advertising campaigns.
  hints:
    readOnly: true
  name: list-campaigns
- description: Create a new advertising campaign.
  hints:
    readOnly: false
  name: create-campaign
- description: Get advertising performance insights.
  hints:
    readOnly: true
  name: get-ad-insights
- description: List custom audiences for targeting.
  hints:
    readOnly: true
  name: list-custom-audiences
- description: Create a new custom audience.
  hints:
    readOnly: false
  name: create-custom-audience
---
