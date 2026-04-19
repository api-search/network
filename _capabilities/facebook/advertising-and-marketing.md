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
- social networking
- handles customer inquiries via messaging channels.
- create a new custom audience.
- customer messaging across messenger and whatsapp.
- list campaigns
- Marketing Manager
- list advertising campaigns.
- get insights
- campaigns
- audience management.
- campaign management and audience targeting.
- create a campaign.
- manage advertising campaigns and performance.
- social media
- Social Media Manager
- publishing and managing content across platforms.
- Conversational Commerce
- campaign management.
- get advertising performance insights.
- marketing
- plans and executes advertising campaigns.
- direct messaging and customer communication.
- list custom audiences for targeting.
- manages day-to-day ad campaign optimization.
- list all advertising campaigns.
- create a new advertising campaign.
- performance insights.
- list custom audiences
- Ad Operations
- creates and publishes visual and text content.
- get advertising insights.
- messaging
- Content Creator
- manages content and engagement across meta platforms.
- get ad insights
- create custom audience
- Customer Support
- facebook
- create campaign
- list audiences
- advertising
- content publishing
- performance tracking and insights.
- list custom audiences.
- manage content across facebook, instagram, and threads.
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
