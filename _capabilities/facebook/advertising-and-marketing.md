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
- get ad insights
- manage advertising campaigns and performance.
- performance tracking and insights.
- marketing
- create a campaign.
- Marketing Manager
- Content Creator
- customer messaging across messenger and whatsapp.
- list audiences
- audience management.
- campaigns
- Customer Support
- create campaign
- handles customer inquiries via messaging channels.
- manage content across facebook, instagram, and threads.
- direct messaging and customer communication.
- create a new custom audience.
- advertising
- manages content and engagement across meta platforms.
- messaging
- social networking
- list custom audiences.
- Ad Operations
- campaign management.
- facebook
- list campaigns
- create a new advertising campaign.
- creates and publishes visual and text content.
- content publishing
- social media
- publishing and managing content across platforms.
- Conversational Commerce
- create custom audience
- list custom audiences for targeting.
- get advertising insights.
- get insights
- list custom audiences
- list all advertising campaigns.
- get advertising performance insights.
- performance insights.
- list advertising campaigns.
- plans and executes advertising campaigns.
- campaign management and audience targeting.
- Social Media Manager
- manages day-to-day ad campaign optimization.
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
