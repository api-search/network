---
consumed_apis:
- amazon-ground-station
description: Workflow capability for satellite operators and mission control teams using Amazon Ground Station. Covers contact scheduling, mission profile management, satellite tracking, and dataflow configuration for satellite operations.
layout: capability
name: Amazon Ground Station Satellite Operations
operations:
- description: List all satellite contacts
  method: GET
  name: list-contacts
  path: /v1/contacts
- description: Schedule a satellite contact
  method: POST
  name: reserve-contact
  path: /v1/contacts
- description: List trackable satellites
  method: GET
  name: list-satellites
  path: /v1/satellites
- description: List available ground stations
  method: GET
  name: list-ground-stations
  path: /v1/ground-stations
- description: List all mission profiles
  method: GET
  name: list-mission-profiles
  path: /v1/mission-profiles
- description: Create a new mission profile
  method: POST
  name: create-mission-profile
  path: /v1/mission-profiles
personas: []
provider_name: Amazon Ground Station
provider_slug: amazon-ground-station
search_terms:
- get detailed information about a specific satellite contact
- satellite operations
- configures mission profiles and dataflow infrastructure
- schedule a new satellite contact window at an aws ground station
- schedule a satellite contact
- list all dataflow endpoint and antenna configurations
- list all configured satellite mission profiles
- create mission profile
- list satellites
- data processing
- create a dataflow endpoint group for satellite data delivery
- reserve contact
- iot
- list contacts
- list ground station locations
- list all available aws ground station antenna locations worldwide
- list ground stations
- reserve satellite contact
- satellite contact scheduling
- create a new mission profile defining satellite operations parameters
- list available ground stations
- cancel satellite contact
- list all satellites that can be tracked through aws ground station
- ground station locations
- amazon ground station
- describe contact
- list configs
- list satellite contacts
- list trackable satellites
- create dataflow endpoint group
- Mission Control Engineer
- space technology
- aws
- satellite mission profiles
- mission control
- satellite tracking information
- list mission profiles
- list all mission profiles
- cancel a previously scheduled satellite contact
- Satellite Operator
- schedules and manages satellite contacts and data downlinks
- list all scheduled and historical satellite contacts with status and timing
- satellite communications
- list all satellite contacts
- create a new mission profile
slug: amazon-ground-station-satellite-operations
tags:
- Amazon Ground Station
- Satellite Operations
- Mission Control
- Space Technology
- AWS
tools:
- description: List all scheduled and historical satellite contacts with status and timing
  hints:
    openWorld: true
    readOnly: true
  name: list-satellite-contacts
- description: Schedule a new satellite contact window at an AWS ground station
  hints:
    readOnly: false
  name: reserve-satellite-contact
- description: Cancel a previously scheduled satellite contact
  hints:
    destructive: true
    readOnly: false
  name: cancel-satellite-contact
- description: Get detailed information about a specific satellite contact
  hints:
    readOnly: true
  name: describe-contact
- description: List all satellites that can be tracked through AWS Ground Station
  hints:
    readOnly: true
  name: list-trackable-satellites
- description: List all available AWS Ground Station antenna locations worldwide
  hints:
    readOnly: true
  name: list-ground-station-locations
- description: List all configured satellite mission profiles
  hints:
    readOnly: true
  name: list-mission-profiles
- description: Create a new mission profile defining satellite operations parameters
  hints:
    readOnly: false
  name: create-mission-profile
- description: List all dataflow endpoint and antenna configurations
  hints:
    readOnly: true
  name: list-configs
- description: Create a dataflow endpoint group for satellite data delivery
  hints:
    readOnly: false
  name: create-dataflow-endpoint-group
---
