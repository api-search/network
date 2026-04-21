---
consumed_apis:
- connect
description: Unified workflow capability for contact center operations combining instance management, agent management, queue management, contact handling, and real-time/historical metrics. Used by contact center administrators, supervisors, and operations teams to manage and monitor the Amazon Connect contact center platform.
layout: capability
name: Amazon Connect Contact Center Operations
operations:
- description: List all Amazon Connect instances
  method: GET
  name: list-instances
  path: /v1/instances
- description: Create a new Amazon Connect instance
  method: POST
  name: create-instance
  path: /v1/instances
- description: Get details of an Amazon Connect instance
  method: GET
  name: describe-instance
  path: /v1/instances/{instance-id}
- description: List agents in an Amazon Connect instance
  method: GET
  name: list-agents
  path: /v1/instances/{instance-id}/agents
- description: Create a new agent in an Amazon Connect instance
  method: POST
  name: create-agent
  path: /v1/instances/{instance-id}/agents
- description: Get details of a specific agent
  method: GET
  name: get-agent
  path: /v1/instances/{instance-id}/agents/{agent-id}
- description: List queues in an Amazon Connect instance
  method: GET
  name: list-queues
  path: /v1/instances/{instance-id}/queues
- description: Create a new queue in an Amazon Connect instance
  method: POST
  name: create-queue
  path: /v1/instances/{instance-id}/queues
- description: List routing profiles in an Amazon Connect instance
  method: GET
  name: list-routing-profiles
  path: /v1/instances/{instance-id}/routing-profiles
- description: List contact flows in an Amazon Connect instance
  method: GET
  name: list-contact-flows
  path: /v1/instances/{instance-id}/contact-flows
- description: Search contacts in an Amazon Connect instance
  method: POST
  name: search-contacts
  path: /v1/contacts/search
- description: Get real-time metrics for queues and agents
  method: POST
  name: get-current-metrics
  path: /v1/instances/{instance-id}/metrics/current
- description: Get historical metrics for an Amazon Connect instance
  method: POST
  name: get-historical-metrics
  path: /v1/instances/{instance-id}/metrics/historical
personas: []
provider_name: Amazon Connect
provider_slug: amazon-connect
search_terms:
- search for past contacts by time range, agent, queue, or channel
- get real-time metrics for queues and agents
- initiation, management, and search of contact interactions
- get details and status of a specific amazon connect instance
- routing profile management
- start outbound voice contact
- contact flow management
- create a new amazon connect instance
- create a new queue in an amazon connect instance
- amazon connect
- search contacts in an amazon connect instance
- get full details of a specific contact interaction
- get details of an amazon connect instance
- configuration and lifecycle management of amazon connect instances
- omnichannel
- list routing profiles
- get agent
- manages day-to-day contact center operations including agent status, contact handling, and performance reporting.
- get current metrics
- real-time and historical performance metrics and reporting
- initiate a chat contact session with a customer
- responsible for configuring and managing the amazon connect instance, including users, queues, routing profiles, and contact flows.
- monitors agent activity, queue health, and contact center performance using real-time and historical metrics dashboards.
- create agent
- list all amazon connect contact center instances in the aws account
- list all routing profiles configured in an amazon connect instance
- list all amazon connect instances
- list queues in an amazon connect instance
- ai
- list agents in an amazon connect instance
- user/agent account management and workforce administration
- create a new agent in an amazon connect instance
- describe instance
- real-time metrics
- create queue
- operations
- list contact flows in an amazon connect instance
- list all contact flows in an amazon connect instance
- contact center
- single instance operations
- list all agents/users in an amazon connect instance
- list routing profiles in an amazon connect instance
- start chat contact
- chat
- list contact flows
- metrics
- get historical metrics
- unified workflow for managing and monitoring the amazon connect contact center, combining instance administration, agent management, queue configuration, and real-time/historical metrics.
- queue management
- amazon connect instance management
- get historical metrics for an amazon connect instance
- describe contact
- get real-time metrics showing agents online, contacts in queue, and queue health
- Operations Team
- list instances
- agent/user management
- list queues
- voice
- get details of a specific agent
- Contact Center Supervisor
- Contact Center Administrator
- create instance
- customer service
- queue, routing profile, and contact flow configuration for intelligent routing
- aws
- list agents
- get historical metrics for contacts handled, handle time, abandon rate, and service level
- list all queues configured in an amazon connect instance
- historical metrics
- individual agent operations
- place an outbound call from the contact center to a customer phone number
- search contacts
- contact search
- get details of a specific agent including their routing profile and security profile
slug: contact-center-operations
tags:
- Amazon Connect
- Contact Center
- AWS
- Operations
- Metrics
tools:
- description: List all Amazon Connect contact center instances in the AWS account
  hints:
    openWorld: true
    readOnly: true
  name: list-instances
- description: Get details and status of a specific Amazon Connect instance
  hints:
    openWorld: true
    readOnly: true
  name: describe-instance
- description: List all agents/users in an Amazon Connect instance
  hints:
    openWorld: true
    readOnly: true
  name: list-agents
- description: Get details of a specific agent including their routing profile and security profile
  hints:
    openWorld: true
    readOnly: true
  name: get-agent
- description: List all queues configured in an Amazon Connect instance
  hints:
    openWorld: true
    readOnly: true
  name: list-queues
- description: List all routing profiles configured in an Amazon Connect instance
  hints:
    openWorld: true
    readOnly: true
  name: list-routing-profiles
- description: List all contact flows in an Amazon Connect instance
  hints:
    openWorld: true
    readOnly: true
  name: list-contact-flows
- description: Get real-time metrics showing agents online, contacts in queue, and queue health
  hints:
    openWorld: true
    readOnly: true
  name: get-current-metrics
- description: Get historical metrics for contacts handled, handle time, abandon rate, and service level
  hints:
    openWorld: true
    readOnly: true
  name: get-historical-metrics
- description: Search for past contacts by time range, agent, queue, or channel
  hints:
    openWorld: true
    readOnly: true
  name: search-contacts
- description: Get full details of a specific contact interaction
  hints:
    openWorld: true
    readOnly: true
  name: describe-contact
- description: Place an outbound call from the contact center to a customer phone number
  hints:
    openWorld: false
    readOnly: false
  name: start-outbound-voice-contact
- description: Initiate a chat contact session with a customer
  hints:
    openWorld: false
    readOnly: false
  name: start-chat-contact
---
