---
consumed_apis:
- amazon-security-lake
description: Unified capability for managing a centralized security data lake including data lake configuration, log source ingestion, and subscriber access management. Used by Security Data Engineers and CISO teams.
layout: capability
name: Amazon Security Lake Security Data Lake
operations:
- description: List all security data lake configurations
  method: GET
  name: list-data-lakes
  path: /v1/data-lakes
- description: Create a new security data lake
  method: POST
  name: create-data-lake
  path: /v1/data-lakes
- description: List all configured log sources
  method: GET
  name: list-log-sources
  path: /v1/log-sources
- description: Add a native AWS log source
  method: POST
  name: add-aws-log-source
  path: /v1/log-sources
- description: List all data lake subscribers
  method: GET
  name: list-subscribers
  path: /v1/subscribers
- description: Create a new subscriber for data access
  method: POST
  name: create-subscriber
  path: /v1/subscribers
personas: []
provider_name: Amazon Security Lake
provider_slug: amazon-security-lake
search_terms:
- data lake
- ocsf
- add custom log source
- centralized security data lake lifecycle including data lake configuration, log source management, and subscriber access
- list data lakes
- create subscriber
- create a subscriber for security lake data access
- get data lake sources
- list log sources
- add a custom third-party log source to security lake
- get data lake source status across accounts and regions
- CISO
- list all data lake subscribers
- create a new subscriber for data access
- delete subscriber
- Security Data Engineer
- data subscriber access management
- create data lake
- add a native aws log source
- create a new security data lake
- get subscriber
- security data centralization and threat analysis
- security
- security leaders who consume security data for threat intelligence and compliance reporting
- list all amazon security lake data lake configurations
- list all configured log sources
- threat detection
- security data lake lifecycle management
- amazon security lake
- list all log sources configured in security lake
- data lake infrastructure management and subscriber access control
- list subscribers
- siem
- aws
- list all security lake data subscribers
- create a new amazon security lake data lake
- security log source management
- enable a native aws log source in security lake
- add aws log source
- engineers who configure and manage security data lakes, log sources, and subscriber access
- get details about a specific security lake subscriber
- list all security data lake configurations
- delete a security lake subscriber
slug: security-data-lake
tags:
- Amazon Security Lake
- Security
- Data Lake
- SIEM
- OCSF
tools:
- description: List all Amazon Security Lake data lake configurations
  hints:
    idempotent: true
    readOnly: true
  name: list-data-lakes
- description: Create a new Amazon Security Lake data lake
  hints:
    idempotent: false
    readOnly: false
  name: create-data-lake
- description: Get data lake source status across accounts and regions
  hints:
    idempotent: true
    readOnly: true
  name: get-data-lake-sources
- description: List all log sources configured in Security Lake
  hints:
    idempotent: true
    readOnly: true
  name: list-log-sources
- description: Enable a native AWS log source in Security Lake
  hints:
    idempotent: false
    readOnly: false
  name: add-aws-log-source
- description: Add a custom third-party log source to Security Lake
  hints:
    idempotent: false
    readOnly: false
  name: add-custom-log-source
- description: List all Security Lake data subscribers
  hints:
    idempotent: true
    readOnly: true
  name: list-subscribers
- description: Create a subscriber for Security Lake data access
  hints:
    idempotent: false
    readOnly: false
  name: create-subscriber
- description: Get details about a specific Security Lake subscriber
  hints:
    idempotent: true
    readOnly: true
  name: get-subscriber
- description: Delete a Security Lake subscriber
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-subscriber
---
