---
consumed_apis:
- amazon-pinpoint
description: Workflow capability for multi-channel customer engagement using Amazon Pinpoint. Combines campaign management, audience segmentation, customer journeys, and transactional messaging for marketing teams and growth engineers.
layout: capability
name: Amazon Pinpoint Customer Engagement
operations:
- description: List all Pinpoint applications
  method: GET
  name: list-apps
  path: /v1/apps
- description: Create a new Pinpoint application
  method: POST
  name: create-app
  path: /v1/apps
- description: List campaigns for an application
  method: GET
  name: list-campaigns
  path: /v1/campaigns
- description: Create a new marketing campaign
  method: POST
  name: create-campaign
  path: /v1/campaigns
- description: List audience segments
  method: GET
  name: list-segments
  path: /v1/audiences
- description: Create a new audience segment
  method: POST
  name: create-segment
  path: /v1/audiences
- description: List customer journeys
  method: GET
  name: list-journeys
  path: /v1/journeys
- description: Create a new customer journey
  method: POST
  name: create-journey
  path: /v1/journeys
- description: Send transactional messages to customer endpoints
  method: POST
  name: send-messages
  path: /v1/messages
personas: []
provider_name: Amazon Pinpoint
provider_slug: amazon-pinpoint
search_terms:
- create a new pinpoint application
- pinpoint application management
- create a new marketing campaign
- create a new pinpoint application for customer engagement
- customer journey workflow management
- list all pinpoint applications
- Marketing Manager
- sms
- analytics
- integrates messaging apis and manages endpoints
- push notifications
- create segment
- send transactional messages
- email
- send messages
- list audience segments for targeting campaigns and journeys
- messaging
- customer engagement
- marketing campaign management
- create journey
- send transactional messages (confirmations, alerts, notifications) to customer endpoints
- manages campaigns, segments, and journeys
- segmentation
- communications
- amazon
- create a new customer audience segment based on attributes or imported data
- list customer journeys
- Growth Engineer
- list marketing campaigns for a pinpoint application
- list campaigns
- create a new audience segment
- campaigns
- list automated customer journey workflows
- multi-channel customer engagement workflow
- list audience segments
- send transactional messages to customer endpoints
- journeys
- audience segment management
- list segments
- voice
- create audience segment
- list campaigns for an application
- aws
- marketing
- create app
- create a new customer journey
- list apps
- create a new multi-channel marketing campaign
- list journeys
- create campaign
- create a multi-step automated customer engagement journey
slug: customer-engagement
tags:
- Amazon
- AWS
- Marketing
- Customer Engagement
- Campaigns
- Journeys
- Segmentation
- Messaging
tools:
- description: List all Pinpoint applications
  hints:
    openWorld: true
    readOnly: true
  name: list-apps
- description: Create a new Pinpoint application for customer engagement
  hints:
    destructive: false
    readOnly: false
  name: create-app
- description: List marketing campaigns for a Pinpoint application
  hints:
    openWorld: true
    readOnly: true
  name: list-campaigns
- description: Create a new multi-channel marketing campaign
  hints:
    destructive: false
    readOnly: false
  name: create-campaign
- description: List audience segments for targeting campaigns and journeys
  hints:
    openWorld: true
    readOnly: true
  name: list-audience-segments
- description: Create a new customer audience segment based on attributes or imported data
  hints:
    destructive: false
    readOnly: false
  name: create-audience-segment
- description: List automated customer journey workflows
  hints:
    openWorld: true
    readOnly: true
  name: list-journeys
- description: Create a multi-step automated customer engagement journey
  hints:
    destructive: false
    readOnly: false
  name: create-journey
- description: Send transactional messages (confirmations, alerts, notifications) to customer endpoints
  hints:
    destructive: false
    readOnly: false
  name: send-transactional-messages
---
