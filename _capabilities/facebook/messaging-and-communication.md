---
consumed_apis:
- messenger-api
- whatsapp-api
description: Workflow capability for customer messaging across Messenger and WhatsApp. Combines Messenger Platform API for Facebook/Instagram messaging with WhatsApp Business API for business communication. Used by customer support teams and conversational commerce platforms.
layout: capability
name: Facebook Messaging and Communication
operations:
- description: Send a Messenger message.
  method: POST
  name: send-messenger-message
  path: /v1/messenger-messages
- description: Send a WhatsApp message.
  method: POST
  name: send-whatsapp-message
  path: /v1/whatsapp-messages
- description: List Messenger conversations.
  method: GET
  name: list-conversations
  path: /v1/conversations
- description: List WhatsApp message templates.
  method: GET
  name: list-templates
  path: /v1/templates
personas: []
provider_name: Facebook
provider_slug: facebook
search_terms:
- Ad Operations
- whatsapp template management.
- Customer Support
- Marketing Manager
- advertising
- manages day-to-day ad campaign optimization.
- list messenger conversations.
- direct messaging and customer communication.
- Conversational Commerce
- customer messaging across messenger and whatsapp.
- messaging
- performance tracking and insights.
- create whatsapp template
- list templates
- list whatsapp templates
- plans and executes advertising campaigns.
- whatsapp
- messenger messaging.
- conversation management.
- send messenger message
- manages content and engagement across meta platforms.
- creates and publishes visual and text content.
- send a message via facebook messenger.
- content publishing
- list whatsapp message templates.
- campaign management and audience targeting.
- manage advertising campaigns and performance.
- messenger
- social networking
- Content Creator
- customer communication
- send whatsapp message
- publishing and managing content across platforms.
- facebook
- list messenger conversations
- send a whatsapp message.
- social media
- whatsapp messaging.
- Social Media Manager
- list conversations
- manage content across facebook, instagram, and threads.
- send a message via whatsapp business.
- create a whatsapp message template.
- handles customer inquiries via messaging channels.
- send a messenger message.
slug: messaging-and-communication
tags:
- Facebook
- Messaging
- Customer Communication
- WhatsApp
- Messenger
tools:
- description: Send a message via Facebook Messenger.
  hints:
    readOnly: false
  name: send-messenger-message
- description: Send a message via WhatsApp Business.
  hints:
    readOnly: false
  name: send-whatsapp-message
- description: List Messenger conversations.
  hints:
    readOnly: true
  name: list-messenger-conversations
- description: List WhatsApp message templates.
  hints:
    readOnly: true
  name: list-whatsapp-templates
- description: Create a WhatsApp message template.
  hints:
    readOnly: false
  name: create-whatsapp-template
---
