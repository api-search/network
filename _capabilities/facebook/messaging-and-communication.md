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
- send a message via whatsapp business.
- Conversational Commerce
- handles customer inquiries via messaging channels.
- plans and executes advertising campaigns.
- manages content and engagement across meta platforms.
- social networking
- campaign management and audience targeting.
- messenger
- manage advertising campaigns and performance.
- advertising
- messenger messaging.
- list messenger conversations
- Marketing Manager
- customer communication
- whatsapp messaging.
- Customer Support
- Ad Operations
- social media
- send a messenger message.
- list messenger conversations.
- list templates
- conversation management.
- messaging
- whatsapp
- send whatsapp message
- create a whatsapp message template.
- facebook
- create whatsapp template
- direct messaging and customer communication.
- list conversations
- list whatsapp templates
- performance tracking and insights.
- manage content across facebook, instagram, and threads.
- list whatsapp message templates.
- Content Creator
- creates and publishes visual and text content.
- send messenger message
- Social Media Manager
- customer messaging across messenger and whatsapp.
- whatsapp template management.
- publishing and managing content across platforms.
- content publishing
- send a message via facebook messenger.
- manages day-to-day ad campaign optimization.
- send a whatsapp message.
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
