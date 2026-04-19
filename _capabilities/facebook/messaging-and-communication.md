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
- manage advertising campaigns and performance.
- performance tracking and insights.
- send a whatsapp message.
- send a message via facebook messenger.
- messenger
- Marketing Manager
- Content Creator
- customer messaging across messenger and whatsapp.
- messenger messaging.
- Customer Support
- list messenger conversations
- handles customer inquiries via messaging channels.
- list whatsapp templates
- list conversations
- manage content across facebook, instagram, and threads.
- direct messaging and customer communication.
- advertising
- create a whatsapp message template.
- send a messenger message.
- list templates
- messaging
- manages content and engagement across meta platforms.
- social networking
- Ad Operations
- whatsapp template management.
- facebook
- list whatsapp message templates.
- send messenger message
- whatsapp
- conversation management.
- creates and publishes visual and text content.
- content publishing
- send whatsapp message
- social media
- customer communication
- Conversational Commerce
- publishing and managing content across platforms.
- list messenger conversations.
- create whatsapp template
- plans and executes advertising campaigns.
- campaign management and audience targeting.
- Social Media Manager
- whatsapp messaging.
- send a message via whatsapp business.
- manages day-to-day ad campaign optimization.
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
