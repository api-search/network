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
- oracle integration
- Integration Developer
- integration monitoring instances.
- get process instance details.
- list monitoring errors
- business process management with tasks and decision models.
- api management
- list tasks
- list errored integration instances.
- list all process definitions.
- list instances
- process instances.
- list all oracle integration connections.
- list all packages.
- b2b trading partner management and document exchange.
- ipaas
- builds and manages integration flows, connections, and adapters.
- designs and manages business process definitions and decision models.
- list all integrations.
- get task
- manages b2b trading partners, agreements, and document exchange.
- list dmn decision model spaces.
- real-time monitoring of integration instances and error handling.
- test connection
- Platform Administrator
- list all connections.
- integration flow design, deployment, and lifecycle management.
- get connection
- get task details.
- get process instance
- b2b
- list analytics queries
- get details of a specific connection.
- automation
- list all oracle integration flows.
- integration flows.
- list all trading partners.
- list errors
- test a connection for connectivity.
- list integration monitoring instances.
- integration
- integration management
- list packages
- list spaces
- b2b integration
- errored integration instances.
- cloud integration
- list process definitions
- list monitoring instances.
- process automation
- get integration
- list integrations
- list workspace spaces.
- enterprise integration
- list monitoring instances
- list all integration packages.
- list trading partners
- list connections
- list process instances.
- list all b2b trading partners.
- user tasks.
- list dmn spaces
- manages the oracle integration platform including monitoring, users, and configuration.
- list user tasks.
- integration connections.
- list process analytics queries.
- get details of a specific integration.
- list errored instances.
- list process instances
- integration packages.
- b2b trading partners.
- unified management of integrations, connections, monitoring, b2b, processes, and tasks.
- monitoring
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
