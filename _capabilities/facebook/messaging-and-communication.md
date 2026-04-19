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
- messaging
- list messenger conversations
- create whatsapp template
- social media
- Conversational Commerce
- Ad Operations
- advertising
- messenger messaging.
- whatsapp template management.
- manage content across facebook, instagram, and threads.
- social networking
- manages day-to-day ad campaign optimization.
- send whatsapp message
- customer communication
- handles customer inquiries via messaging channels.
- list templates
- Marketing Manager
- create a whatsapp message template.
- direct messaging and customer communication.
- Content Creator
- send a message via whatsapp business.
- send a messenger message.
- manage advertising campaigns and performance.
- creates and publishes visual and text content.
- whatsapp
- list messenger conversations.
- messenger
- publishing and managing content across platforms.
- campaign management and audience targeting.
- whatsapp messaging.
- send a whatsapp message.
- plans and executes advertising campaigns.
- performance tracking and insights.
- content publishing
- send messenger message
- facebook
- manages content and engagement across meta platforms.
- send a message via facebook messenger.
- Social Media Manager
- Customer Support
- list whatsapp templates
- conversation management.
- customer messaging across messenger and whatsapp.
- list whatsapp message templates.
- list conversations
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
