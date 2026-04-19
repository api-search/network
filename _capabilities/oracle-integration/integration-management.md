---
consumed_apis:
- oracle-developer-api
- oracle-process-api
description: Unified workflow for managing Oracle Integration lifecycle including integrations, connections, packages, monitoring, B2B trading partners, process automation, tasks, and decision models. Used by integration developers and platform administrators.
layout: capability
name: Oracle Integration Management
operations:
- description: List all connections.
  method: GET
  name: list-connections
  path: /v1/connections
- description: List all integrations.
  method: GET
  name: list-integrations
  path: /v1/integrations
- description: List monitoring instances.
  method: GET
  name: list-instances
  path: /v1/monitoring/instances
- description: List errored instances.
  method: GET
  name: list-errors
  path: /v1/monitoring/errors
- description: List all packages.
  method: GET
  name: list-packages
  path: /v1/packages
- description: List all trading partners.
  method: GET
  name: list-trading-partners
  path: /v1/trading-partners
- description: List process instances.
  method: GET
  name: list-process-instances
  path: /v1/processes
- description: List user tasks.
  method: GET
  name: list-tasks
  path: /v1/tasks
personas: []
provider_name: Oracle Integration
provider_slug: oracle-integration
search_terms:
- list spaces
- integration flow design, deployment, and lifecycle management.
- errored integration instances.
- list process definitions
- b2b
- integration monitoring instances.
- list user tasks.
- list all b2b trading partners.
- list errors
- list all oracle integration connections.
- monitoring
- list packages
- integration management
- process instances.
- integration
- get details of a specific integration.
- list all process definitions.
- list dmn decision model spaces.
- list connections
- list workspace spaces.
- manages the oracle integration platform including monitoring, users, and configuration.
- Platform Administrator
- test a connection for connectivity.
- list dmn spaces
- integration connections.
- enterprise integration
- list tasks
- test connection
- get task details.
- api management
- get details of a specific connection.
- list process instances
- get connection
- get task
- user tasks.
- cloud integration
- designs and manages business process definitions and decision models.
- list all packages.
- list all integrations.
- list monitoring instances.
- list analytics queries
- process automation
- list integrations
- integration packages.
- list integration monitoring instances.
- b2b trading partners.
- list trading partners
- list all trading partners.
- get integration
- list all integration packages.
- list process analytics queries.
- Integration Developer
- get process instance details.
- manages b2b trading partners, agreements, and document exchange.
- list instances
- list all oracle integration flows.
- get process instance
- list errored integration instances.
- automation
- list errored instances.
- ipaas
- list monitoring errors
- builds and manages integration flows, connections, and adapters.
- list process instances.
- list monitoring instances
- b2b integration
- real-time monitoring of integration instances and error handling.
- b2b trading partner management and document exchange.
- unified management of integrations, connections, monitoring, b2b, processes, and tasks.
- oracle integration
- list all connections.
- business process management with tasks and decision models.
- integration flows.
slug: integration-management
tags:
- Oracle Integration
- Integration Management
- Process Automation
- B2B
- Monitoring
tools:
- description: List all Oracle Integration connections.
  hints:
    openWorld: true
    readOnly: true
  name: list-connections
- description: Get details of a specific connection.
  hints:
    readOnly: true
  name: get-connection
- description: Test a connection for connectivity.
  hints:
    readOnly: true
  name: test-connection
- description: List all Oracle Integration flows.
  hints:
    openWorld: true
    readOnly: true
  name: list-integrations
- description: Get details of a specific integration.
  hints:
    readOnly: true
  name: get-integration
- description: List integration monitoring instances.
  hints:
    openWorld: true
    readOnly: true
  name: list-monitoring-instances
- description: List errored integration instances.
  hints:
    readOnly: true
  name: list-monitoring-errors
- description: List all integration packages.
  hints:
    readOnly: true
  name: list-packages
- description: List all B2B trading partners.
  hints:
    openWorld: true
    readOnly: true
  name: list-trading-partners
- description: List all process definitions.
  hints:
    readOnly: true
  name: list-process-definitions
- description: List process instances.
  hints:
    openWorld: true
    readOnly: true
  name: list-process-instances
- description: Get process instance details.
  hints:
    readOnly: true
  name: get-process-instance
- description: List user tasks.
  hints:
    openWorld: true
    readOnly: true
  name: list-tasks
- description: Get task details.
  hints:
    readOnly: true
  name: get-task
- description: List DMN decision model spaces.
  hints:
    readOnly: true
  name: list-dmn-spaces
- description: List workspace spaces.
  hints:
    readOnly: true
  name: list-spaces
- description: List process analytics queries.
  hints:
    readOnly: true
  name: list-analytics-queries
---
