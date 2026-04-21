---
consumed_apis:
- ssm-incidents
description: Unified capability for operations teams to manage incident response plans, respond to active incidents, update timelines, and coordinate responders.
layout: capability
name: Amazon Incident Manager - Incident Response
operations:
- description: List all response plans
  method: GET
  name: list-response-plans
  path: /v1/response-plans
- description: List active incidents
  method: GET
  name: list-incidents
  path: /v1/incidents
- description: Create a new incident
  method: POST
  name: create-incident
  path: /v1/incidents
personas: []
provider_name: Amazon Incident Manager
provider_slug: amazon-incident-manager
search_terms:
- create a new incident
- list all response plans
- manages incident response plans and responds to operational incidents
- monitors system reliability and coordinates incident resolution
- get details of a specific incident
- devops
- list active incidents
- automation
- get incident
- automated incident response plans and escalation
- manage incident response plans
- operations
- Operations Engineer
- start a new incident and trigger response plan
- create incident
- list all incident response plans
- Site Reliability Engineer
- list incidents
- update the summary or status of an active incident
- list timeline events for an incident
- creating, tracking, and resolving operational incidents
- list timeline events
- list response plans
- create response plan
- aws
- manage active incidents
- incident management
- create a new incident response plan with escalation contacts
- list active and recent incidents
- update incident
slug: incident-response
tags:
- AWS
- Incident Management
- DevOps
- Operations
- Automation
tools:
- description: List all incident response plans
  hints:
    openWorld: true
    readOnly: true
  name: list-response-plans
- description: Create a new incident response plan with escalation contacts
  hints:
    readOnly: false
  name: create-response-plan
- description: List active and recent incidents
  hints:
    openWorld: true
    readOnly: true
  name: list-incidents
- description: Start a new incident and trigger response plan
  hints:
    readOnly: false
  name: create-incident
- description: Update the summary or status of an active incident
  hints:
    readOnly: false
  name: update-incident
- description: Get details of a specific incident
  hints:
    readOnly: true
  name: get-incident
- description: List timeline events for an incident
  hints:
    openWorld: true
    readOnly: true
  name: list-timeline-events
---
