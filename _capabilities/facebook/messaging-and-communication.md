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
- whatsapp template management.
- social networking
- handles customer inquiries via messaging channels.
- customer messaging across messenger and whatsapp.
- customer communication
- whatsapp
- Marketing Manager
- list conversations
- send a message via facebook messenger.
- send a whatsapp message.
- campaign management and audience targeting.
- messenger messaging.
- manage advertising campaigns and performance.
- social media
- Social Media Manager
- messenger
- publishing and managing content across platforms.
- Conversational Commerce
- send a message via whatsapp business.
- plans and executes advertising campaigns.
- direct messaging and customer communication.
- send a messenger message.
- manages day-to-day ad campaign optimization.
- create a whatsapp message template.
- list whatsapp templates
- Ad Operations
- creates and publishes visual and text content.
- messaging
- list whatsapp message templates.
- manage content across facebook, instagram, and threads.
- Content Creator
- send messenger message
- manages content and engagement across meta platforms.
- list messenger conversations
- list templates
- Customer Support
- facebook
- send whatsapp message
- whatsapp messaging.
- advertising
- content publishing
- conversation management.
- performance tracking and insights.
- list messenger conversations.
- create whatsapp template
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
