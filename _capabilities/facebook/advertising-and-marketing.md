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
- create a campaign.
- Ad Operations
- list custom audiences for targeting.
- Customer Support
- Marketing Manager
- advertising
- manages day-to-day ad campaign optimization.
- performance insights.
- direct messaging and customer communication.
- Conversational Commerce
- customer messaging across messenger and whatsapp.
- messaging
- performance tracking and insights.
- plans and executes advertising campaigns.
- create a new custom audience.
- get insights
- manages content and engagement across meta platforms.
- creates and publishes visual and text content.
- content publishing
- campaign management and audience targeting.
- list custom audiences.
- get advertising performance insights.
- manage advertising campaigns and performance.
- list campaigns
- social networking
- campaigns
- Content Creator
- list advertising campaigns.
- publishing and managing content across platforms.
- facebook
- list audiences
- list custom audiences
- audience management.
- marketing
- get ad insights
- social media
- Social Media Manager
- get advertising insights.
- create custom audience
- create a new advertising campaign.
- manage content across facebook, instagram, and threads.
- list all advertising campaigns.
- handles customer inquiries via messaging channels.
- create campaign
- campaign management.
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
