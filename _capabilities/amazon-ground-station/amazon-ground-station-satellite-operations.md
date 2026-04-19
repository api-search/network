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
- reserve contact
- schedules and manages satellite contacts and data downlinks
- create dataflow endpoint group
- schedule a satellite contact
- list ground stations
- Satellite Operator
- list trackable satellites
- iot
- list satellite contacts
- space technology
- configures mission profiles and dataflow infrastructure
- create a dataflow endpoint group for satellite data delivery
- list all satellite contacts
- satellite operations
- list available ground stations
- satellite tracking information
- list all scheduled and historical satellite contacts with status and timing
- describe contact
- data processing
- list configs
- get detailed information about a specific satellite contact
- Mission Control Engineer
- schedule a new satellite contact window at an aws ground station
- ground station locations
- list contacts
- create mission profile
- list satellites
- list all dataflow endpoint and antenna configurations
- list ground station locations
- aws
- create a new mission profile defining satellite operations parameters
- list all satellites that can be tracked through aws ground station
- list mission profiles
- list all available aws ground station antenna locations worldwide
- amazon ground station
- satellite communications
- cancel a previously scheduled satellite contact
- satellite mission profiles
- cancel satellite contact
- mission control
- list all mission profiles
- list all configured satellite mission profiles
- reserve satellite contact
- satellite contact scheduling
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
