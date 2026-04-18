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
- send a messenger message.
- customer communication
- manages day-to-day ad campaign optimization.
- send messenger message
- Customer Support
- customer messaging across messenger and whatsapp.
- create whatsapp template
- whatsapp
- Ad Operations
- list whatsapp templates
- creates and publishes visual and text content.
- list whatsapp message templates.
- social media
- send a whatsapp message.
- send a message via facebook messenger.
- manages content and engagement across meta platforms.
- list conversations
- manage advertising campaigns and performance.
- plans and executes advertising campaigns.
- Conversational Commerce
- handles customer inquiries via messaging channels.
- messenger messaging.
- create a whatsapp message template.
- social networking
- Marketing Manager
- content publishing
- send whatsapp message
- whatsapp template management.
- messaging
- Content Creator
- send a message via whatsapp business.
- whatsapp messaging.
- Social Media Manager
- direct messaging and customer communication.
- performance tracking and insights.
- manage content across facebook, instagram, and threads.
- facebook
- advertising
- list templates
- list messenger conversations.
- publishing and managing content across platforms.
- list messenger conversations
- conversation management.
- campaign management and audience targeting.
- messenger
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
