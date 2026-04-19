---
consumed_apis:
- management-api
description: Workflow capability for managing Power Automate flows, environments, and connectors. Used by automation engineers and platform administrators.
layout: capability
name: Microsoft Power Automate Flow Automation
operations:
- description: List all environments
  method: GET
  name: list-environments
  path: /v1/environments
- description: List flows
  method: GET
  name: list-flows
  path: /v1/flows
- description: Create a flow
  method: POST
  name: create-flow
  path: /v1/flows
- description: Get flow details
  method: GET
  name: get-flow
  path: /v1/flows
- description: Update a flow
  method: PATCH
  name: update-flow
  path: /v1/flows
- description: Delete a flow
  method: DELETE
  name: delete-flow
  path: /v1/flows
- description: List connectors
  method: GET
  name: list-connectors
  path: /v1/connectors
personas: []
provider_name: Microsoft Power Automate
provider_slug: microsoft-power-automate
search_terms:
- turn off flow
- list flows in an environment
- connector management
- microsoft
- list flows
- turn on flow
- power platform
- stop/deactivate a flow
- get connector
- manages environments, connectors, and permissions
- rpa
- flow management
- list all environments
- delete flow
- flow lifecycle management
- get flow
- environment management
- get details of a specific flow
- start/activate a flow
- managing environments and available connectors
- integration
- delete a flow
- creating, running, and managing automation flows
- create a new automation flow
- update a flow's properties
- creates and manages automation flows
- list available connectors in an environment
- manage flows, environments, and connectors
- low-code
- get details of a specific connector
- update a flow
- Automation Engineer
- list all power automate environments
- list connectors
- create flow
- get flow details
- update flow
- microsoft power automate
- automation
- workflow
- list environments
- business process
- create a flow
- Platform Administrator
slug: flow-automation
tags:
- Microsoft Power Automate
- Automation
- Flow Management
- Low-Code
tools:
- description: List all Power Automate environments
  hints:
    openWorld: true
    readOnly: true
  name: list-environments
- description: List flows in an environment
  hints:
    openWorld: true
    readOnly: true
  name: list-flows
- description: Create a new automation flow
  hints:
    readOnly: false
  name: create-flow
- description: Get details of a specific flow
  hints:
    readOnly: true
  name: get-flow
- description: Update a flow's properties
  hints:
    readOnly: false
  name: update-flow
- description: Delete a flow
  hints:
    destructive: true
  name: delete-flow
- description: Start/activate a flow
  hints:
    readOnly: false
  name: turn-on-flow
- description: Stop/deactivate a flow
  hints:
    readOnly: false
  name: turn-off-flow
- description: List available connectors in an environment
  hints:
    readOnly: true
  name: list-connectors
- description: Get details of a specific connector
  hints:
    readOnly: true
  name: get-connector
---
