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
- campaigns
- get advertising insights.
- manages day-to-day ad campaign optimization.
- Customer Support
- customer messaging across messenger and whatsapp.
- get ad insights
- create custom audience
- get insights
- create a campaign.
- get advertising performance insights.
- create a new custom audience.
- Ad Operations
- create a new advertising campaign.
- list campaigns
- creates and publishes visual and text content.
- list custom audiences.
- social media
- marketing
- manages content and engagement across meta platforms.
- plans and executes advertising campaigns.
- manage advertising campaigns and performance.
- list all advertising campaigns.
- Conversational Commerce
- handles customer inquiries via messaging channels.
- social networking
- Marketing Manager
- content publishing
- performance insights.
- Content Creator
- messaging
- campaign management and audience targeting.
- list custom audiences
- Social Media Manager
- direct messaging and customer communication.
- campaign management.
- performance tracking and insights.
- list advertising campaigns.
- manage content across facebook, instagram, and threads.
- facebook
- advertising
- list custom audiences for targeting.
- audience management.
- publishing and managing content across platforms.
- create campaign
- list audiences
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
