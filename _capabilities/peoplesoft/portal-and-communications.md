---
consumed_apis:
- interaction-hub
- notification-framework
- chatbot
description: Unified workflow for content managers combining portal content management, branding, chatbot integration, and notification services across PeopleSoft Interaction Hub, Chatbot Integration, and Notification Framework APIs.
layout: capability
name: PeopleSoft Portal And Communications
operations:
- description: Retrieve portal content items.
  method: GET
  name: list-content
  path: /v1/content
- description: Create a new portal content item.
  method: POST
  name: create-content
  path: /v1/content
- description: Retrieve available branding themes.
  method: GET
  name: list-themes
  path: /v1/themes
- description: Retrieve notifications for the current user.
  method: GET
  name: list-notifications
  path: /v1/notifications
- description: Send a notification via email, text, or in-app channels.
  method: POST
  name: send-notification
  path: /v1/notifications
- description: Retrieve available chatbot intents.
  method: GET
  name: list-intents
  path: /v1/intents
- description: Process a chatbot intent fulfillment request.
  method: POST
  name: fulfill-intent
  path: /v1/intent-fulfillments
personas: []
provider_name: PeopleSoft
provider_slug: peoplesoft
search_terms:
- erp
- supply chain management
- content management
- peopletools platform services.
- create a new portal content item.
- list content
- retrieve notifications for the current user.
- retrieve available branding themes.
- notification management
- chatbot intents
- portal
- crm
- list themes
- peoplesoft
- notifications
- financial management
- create content
- communications
- branding themes
- process a chatbot intent fulfillment request.
- list notifications
- campus solutions.
- enterprise software
- campus solutions
- human capital management.
- chatbot
- retrieve portal content items.
- hcm
- retrieve available chatbot intents.
- portal content items
- send notification
- send a notification via email, text, or in-app channels.
- financial and supply chain management.
- fulfill intent
- chatbot intent fulfillments
- list intents
slug: portal-and-communications
tags:
- PeopleSoft
- Portal
- Content Management
- Communications
- Notifications
- Chatbot
tools:
- description: Retrieve portal content items.
  hints:
    openWorld: true
    readOnly: true
  name: list-content
- description: Create a new portal content item.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-content
- description: Retrieve available branding themes.
  hints:
    openWorld: true
    readOnly: true
  name: list-themes
- description: Retrieve notifications for the current user.
  hints:
    openWorld: true
    readOnly: true
  name: list-notifications
- description: Send a notification via email, text, or in-app channels.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: send-notification
- description: Retrieve available chatbot intents.
  hints:
    openWorld: true
    readOnly: true
  name: list-intents
- description: Process a chatbot intent fulfillment request.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: fulfill-intent
---
