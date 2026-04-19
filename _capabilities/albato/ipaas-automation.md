---
consumed_apis:
- albato-automations
- albato-embedded
description: Workflow capability for managing no-code automation and embedded iPaaS functionality in Albato. Combines automation workflow management and embedded team management to support operations teams and SaaS developers.
layout: capability
name: Albato iPaaS Automation
operations:
- description: List all automation workflows
  method: GET
  name: list-automations
  path: /v1/automations
- description: List embedded teams
  method: GET
  name: list-teams
  path: /v1/teams
- description: List available connectors
  method: GET
  name: list-connectors
  path: /v1/connectors
personas: []
provider_name: Albato
provider_slug: albato
search_terms:
- list automations
- Automation Builder
- automation workflows
- workflow automation
- creates no-code automation workflows in albato connecting apps without writing code, configuring triggers, actions, conditions, and delays.
- list connectors
- list albato automations
- list all automation workflows
- webhooks
- browse 1,000+ available app connectors for albato embedded. search by name or filter to find specific integrations.
- embedded integration
- list teams
- albato
- app integration
- manage no-code automations and embedded ipaas customer teams
- list all albato automation workflows with their status, trigger counts, and success/error rates.
- integrates albato embedded ipaas into saas products to offer white-label automation capabilities to customers. manages teams and connectors.
- ipaas
- app connectors
- workflow
- Operations Manager
- list automation templates available for albato embedded use.
- list albato embedded teams
- get albato automation
- list albato connectors
- white-label
- monitors automation health, reviews execution rates and errors, and ensures business processes run reliably across integrated apps.
- embedded teams
- embedded ipaas
- list embedded teams
- SaaS Developer
- create and monitor automation workflows
- list available connectors
- get execution history for an albato automation including success/error rates and step completion details.
- get details and configuration for a specific albato automation.
- saas
- integrations
- list albato templates
- list all embedded teams (customer accounts) in albato embedded ipaas with active automation and transaction counts.
- list albato executions
- manage embedded ipaas customer accounts
- no-code automation
slug: ipaas-automation
tags:
- Albato
- iPaaS
- No-Code Automation
- Workflow
- Embedded Integration
- SaaS
tools:
- description: List all Albato automation workflows with their status, trigger counts, and success/error rates.
  hints:
    openWorld: false
    readOnly: true
  name: list-albato-automations
- description: Get details and configuration for a specific Albato automation.
  hints:
    openWorld: false
    readOnly: true
  name: get-albato-automation
- description: Get execution history for an Albato automation including success/error rates and step completion details.
  hints:
    openWorld: false
    readOnly: true
  name: list-albato-executions
- description: List all embedded teams (customer accounts) in Albato Embedded iPaaS with active automation and transaction counts.
  hints:
    openWorld: false
    readOnly: true
  name: list-albato-embedded-teams
- description: Browse 1,000+ available app connectors for Albato Embedded. Search by name or filter to find specific integrations.
  hints:
    openWorld: false
    readOnly: true
  name: list-albato-connectors
- description: List automation templates available for Albato Embedded use.
  hints:
    openWorld: false
    readOnly: true
  name: list-albato-templates
---
