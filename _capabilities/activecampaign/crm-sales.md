---
consumed_apis:
- activecampaign-v3
description: Workflow capability for CRM and sales pipeline management including deals, accounts, tasks, and pipeline stages. Used by sales teams and revenue operations to track and advance deals.
layout: capability
name: ActiveCampaign CRM and Sales
operations:
- description: List all deals
  method: GET
  name: list-deals
  path: /v1/deals
- description: Create a new deal
  method: POST
  name: create-deal
  path: /v1/deals
- description: List all accounts
  method: GET
  name: list-accounts
  path: /v1/accounts
- description: Create a new account
  method: POST
  name: create-account
  path: /v1/accounts
personas: []
provider_name: ActiveCampaign
provider_slug: activecampaign
search_terms:
- Revenue Operations
- manages email campaigns, automations, and contact segmentation
- Marketing Manager
- sales
- create a new deal
- accounts
- list all accounts
- create a new account
- list all deals
- crm
- deals
- list accounts
- company account management
- create a new sales deal in activecampaign crm
- retrieve a specific deal by id
- manage sales pipeline, deals, accounts, and tasks
- cross-channel contact engagement and personalization
- orchestrate contact journeys, campaigns, automations, and list management
- customer experience
- Growth Engineer
- Account Manager
- list all sales deals in activecampaign crm
- get deal
- list all company accounts in activecampaign crm
- sales deal management
- Email Marketer
- sales automation
- create a new company account in activecampaign crm
- create account
- email marketing
- tracks deals, manages accounts, and uses crm features
- list deals
- crm, pipeline management, and revenue operations
- Sales Representative
- marketing automation
- builds integrations, automation workflows, and uses the api directly
- email, sms, and multi-channel marketing automation
- create deal
- activecampaign
slug: crm-sales
tags:
- ActiveCampaign
- CRM
- Sales
- Deals
- Accounts
tools:
- description: List all sales deals in ActiveCampaign CRM
  hints:
    openWorld: true
    readOnly: true
  name: list-deals
- description: Create a new sales deal in ActiveCampaign CRM
  hints:
    destructive: false
    readOnly: false
  name: create-deal
- description: Retrieve a specific deal by ID
  hints:
    openWorld: false
    readOnly: true
  name: get-deal
- description: List all company accounts in ActiveCampaign CRM
  hints:
    openWorld: true
    readOnly: true
  name: list-accounts
- description: Create a new company account in ActiveCampaign CRM
  hints:
    destructive: false
    readOnly: false
  name: create-account
---
