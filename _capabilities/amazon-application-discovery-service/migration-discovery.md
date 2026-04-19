---
consumed_apis: []
description: Workflow capability for discovering on-premises infrastructure and preparing migration plans using AWS Application Discovery Service.
layout: capability
name: Migration Discovery Workflow
operations:
- description: List all discovery agents and their health status
  method: GET
  name: describe-agents
  path: /v1/agents
- description: Get count of discovered servers, agents, and applications
  method: GET
  name: get-discovery-summary
  path: /v1/summary
- description: List discovered servers, processes, and connections
  method: POST
  name: list-configurations
  path: /v1/configurations
- description: Export discovered data to S3
  method: POST
  name: start-export-task
  path: /v1/exports
- description: Check status of export tasks
  method: GET
  name: describe-export-tasks
  path: /v1/exports
personas: []
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
search_terms:
- migration
- list configurations
- infrastructure
- start import task
- get count of discovered servers, agents, and applications
- export all discovered server data to amazon s3 for detailed migration analysis and reporting.
- describe agents
- describe export tasks
- discovery
- list server neighbors
- list discovered servers, processes, and connections
- start export task
- list all aws application discovery service agents and their health status. use this to verify agents are running before starting discovery.
- asset discovery summary
- export discovered data to s3
- describe configurations
- list discovered configuration items such as servers, processes, connections, and applications for migration planning.
- data export tasks
- aws
- get detailed attributes for specific discovered configuration items to understand server specifications.
- check the status of discovery data export tasks to know when data is ready for analysis.
- create application groupings from discovered servers to organize migration waves.
- import on-premises server inventory from a csv file in amazon s3 when agents cannot be installed.
- check status of export tasks
- discovered configuration items
- start data collection
- find servers that communicate with a specific server to map application dependencies for migration grouping.
- amazon application discovery service
- start data collection on specified agents to begin discovering on-premises servers and processes.
- get a summary count of all discovered servers, applications, and agents to understand the scope of the environment.
- list all discovery agents and their health status
- get discovery summary
- discovery agents
- create application
slug: migration-discovery
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
tools:
- description: List all AWS Application Discovery Service agents and their health status. Use this to verify agents are running before starting discovery.
  hints:
    openWorld: true
    readOnly: true
  name: describe-agents
- description: Start data collection on specified agents to begin discovering on-premises servers and processes.
  hints:
    openWorld: false
    readOnly: false
  name: start-data-collection
- description: Get a summary count of all discovered servers, applications, and agents to understand the scope of the environment.
  hints:
    openWorld: true
    readOnly: true
  name: get-discovery-summary
- description: List discovered configuration items such as servers, processes, connections, and applications for migration planning.
  hints:
    openWorld: true
    readOnly: true
  name: list-configurations
- description: Get detailed attributes for specific discovered configuration items to understand server specifications.
  hints:
    openWorld: true
    readOnly: true
  name: describe-configurations
- description: Find servers that communicate with a specific server to map application dependencies for migration grouping.
  hints:
    openWorld: true
    readOnly: true
  name: list-server-neighbors
- description: Create application groupings from discovered servers to organize migration waves.
  hints:
    openWorld: false
    readOnly: false
  name: create-application
- description: Export all discovered server data to Amazon S3 for detailed migration analysis and reporting.
  hints:
    openWorld: false
    readOnly: false
  name: start-export-task
- description: Check the status of discovery data export tasks to know when data is ready for analysis.
  hints:
    openWorld: true
    readOnly: true
  name: describe-export-tasks
- description: Import on-premises server inventory from a CSV file in Amazon S3 when agents cannot be installed.
  hints:
    openWorld: false
    readOnly: false
  name: start-import-task
---
