---
consumed_apis:
- activecampaign-v3
description: Unified workflow capability for marketing automation, contact management, campaign execution, and list segmentation. Used by marketing teams and growth engineers to orchestrate multi-channel customer journeys.
layout: capability
name: ActiveCampaign Marketing Automation
operations:
- description: List and search contacts
  method: GET
  name: list-contacts
  path: /v1/contacts
- description: Create a new contact
  method: POST
  name: create-contact
  path: /v1/contacts
- description: List all campaigns
  method: GET
  name: list-campaigns
  path: /v1/campaigns
- description: List all automations
  method: GET
  name: list-automations
  path: /v1/automations
- description: List all contact lists
  method: GET
  name: list-lists
  path: /v1/lists
- description: Create a new contact list
  method: POST
  name: create-list
  path: /v1/lists
- description: List all tags
  method: GET
  name: list-tags
  path: /v1/tags
personas: []
provider_name: ActiveCampaign
provider_slug: activecampaign
search_terms:
- marketing automation workflows
- list all email campaigns in activecampaign
- create a new contact tag in activecampaign
- list automations
- marketing automation
- list campaigns
- list all campaigns
- Marketing Manager
- campaigns
- list all contact lists in activecampaign
- email, sms, and multi-channel marketing automation
- create tag
- crm
- email marketing
- contacts
- customer experience
- list and search contacts
- create a new contact list
- contact lifecycle management
- create a new contact
- list and search activecampaign contacts by email, name, or other criteria
- Revenue Operations
- sales automation
- list tags
- list contact lists
- list contacts
- Growth Engineer
- cross-channel contact engagement and personalization
- email campaign management
- Sales Representative
- list all contact tags in activecampaign
- tracks deals, manages accounts, and uses crm features
- manages email campaigns, automations, and contact segmentation
- list all tags
- list all marketing automations in activecampaign
- activecampaign
- crm, pipeline management, and revenue operations
- create contact
- builds integrations, automation workflows, and uses the api directly
- create list
- list all contact lists
- sync a contact's data to activecampaign, creating or updating as needed
- contact tag management
- sync contact
- Email Marketer
- manage sales pipeline, deals, accounts, and tasks
- create a new contact in activecampaign
- list all automations
- orchestrate contact journeys, campaigns, automations, and list management
- contact list management
- Account Manager
- list lists
slug: marketing-automation
tags:
- ActiveCampaign
- Marketing Automation
- Email Marketing
- Contacts
- Campaigns
tools:
- description: List and search ActiveCampaign contacts by email, name, or other criteria
  hints:
    openWorld: true
    readOnly: true
  name: list-contacts
- description: Create a new contact in ActiveCampaign
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-contact
- description: Sync a contact's data to ActiveCampaign, creating or updating as needed
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: sync-contact
- description: List all email campaigns in ActiveCampaign
  hints:
    openWorld: true
    readOnly: true
  name: list-campaigns
- description: List all marketing automations in ActiveCampaign
  hints:
    openWorld: true
    readOnly: true
  name: list-automations
- description: List all contact lists in ActiveCampaign
  hints:
    openWorld: true
    readOnly: true
  name: list-contact-lists
- description: List all contact tags in ActiveCampaign
  hints:
    openWorld: true
    readOnly: true
  name: list-tags
- description: Create a new contact tag in ActiveCampaign
  hints:
    destructive: false
    readOnly: false
  name: create-tag
---
