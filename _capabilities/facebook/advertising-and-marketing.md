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
- messaging
- social media
- get advertising insights.
- Conversational Commerce
- Ad Operations
- advertising
- list custom audiences for targeting.
- audience management.
- manage content across facebook, instagram, and threads.
- campaign management.
- social networking
- manages day-to-day ad campaign optimization.
- handles customer inquiries via messaging channels.
- campaigns
- Marketing Manager
- create a campaign.
- get insights
- direct messaging and customer communication.
- Content Creator
- create a new advertising campaign.
- manage advertising campaigns and performance.
- create campaign
- creates and publishes visual and text content.
- list custom audiences
- performance insights.
- campaign management and audience targeting.
- publishing and managing content across platforms.
- list custom audiences.
- performance tracking and insights.
- plans and executes advertising campaigns.
- content publishing
- list audiences
- list advertising campaigns.
- marketing
- facebook
- create custom audience
- manages content and engagement across meta platforms.
- get ad insights
- create a new custom audience.
- Social Media Manager
- Customer Support
- list all advertising campaigns.
- list campaigns
- get advertising performance insights.
- customer messaging across messenger and whatsapp.
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
