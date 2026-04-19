---
consumed_apis:
- crm
- chatbot
- notification-framework
description: Unified workflow for CRM users combining customer management, case management, sales, chatbot integration, and notifications across PeopleSoft CRM, Chatbot Integration, and Notification Framework APIs.
layout: capability
name: PeopleSoft Customer Engagement
operations:
- description: Retrieve customer records.
  method: GET
  name: list-customers
  path: /v1/customers
- description: Retrieve details for a specific customer.
  method: GET
  name: get-customer
  path: /v1/customers/{customerId}
- description: Retrieve support and service cases.
  method: GET
  name: list-cases
  path: /v1/cases
- description: Create a new support or service case.
  method: POST
  name: create-case
  path: /v1/cases
- description: Retrieve sales opportunities.
  method: GET
  name: list-opportunities
  path: /v1/opportunities
- description: Retrieve available chatbot intents.
  method: GET
  name: list-intents
  path: /v1/intents
- description: Process a chatbot intent fulfillment request.
  method: POST
  name: fulfill-intent
  path: /v1/intent-fulfillments
- description: Retrieve notifications for the current user.
  method: GET
  name: list-notifications
  path: /v1/notifications
- description: Send a notification via email, text, or in-app channels.
  method: POST
  name: send-notification
  path: /v1/notifications
personas: []
provider_name: PeopleSoft
provider_slug: peoplesoft
search_terms:
- chatbot
- enterprise software
- create case
- create a new support or service case.
- retrieve sales opportunities.
- financial and supply chain management.
- campus solutions.
- retrieve support and service cases.
- retrieve customer records.
- retrieve notifications for the current user.
- customer engagement
- campus solutions
- retrieve available chatbot intents.
- get customer
- chatbot intent fulfillments
- list customers
- human capital management.
- erp
- supply chain management
- support and service cases
- case management
- peopletools platform services.
- list cases
- process a chatbot intent fulfillment request.
- hcm
- crm
- fulfill intent
- notification management
- sales
- chatbot intents
- sales opportunities
- customer records
- retrieve details for a specific customer.
- send a notification via email, text, or in-app channels.
- send notification
- individual customer details
- list intents
- list notifications
- list opportunities
- financial management
- peoplesoft
slug: customer-engagement
tags:
- PeopleSoft
- CRM
- Customer Engagement
- Case Management
- Sales
- Chatbot
tools:
- description: Retrieve customer records.
  hints:
    openWorld: true
    readOnly: true
  name: list-customers
- description: Retrieve details for a specific customer.
  hints:
    openWorld: true
    readOnly: true
  name: get-customer
- description: Retrieve support and service cases.
  hints:
    openWorld: true
    readOnly: true
  name: list-cases
- description: Create a new support or service case.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-case
- description: Retrieve sales opportunities.
  hints:
    openWorld: true
    readOnly: true
  name: list-opportunities
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
---
