---
consumed_apis:
- location-service
description: Unified workflow capability for Amazon Location Service combining resource management and operations.
layout: capability
name: Amazon Location Service Workflow
operations: []
personas: []
provider_name: Amazon Location Service
provider_slug: amazon-location-service
search_terms:
- map resources list maps
- integrates api into applications
- maps
- routing
- workflow
- geocoding
- location
- aws
- Administrator
- unified workflow for amazon location service resource management
- manages resources and configurations
- Developer
- retrieves the map resource details.
- geofencing
- map resources describe map
- amazon location service
- creates a map resource in your aws account.
- lists map resources in your aws account.
- map resources create map
slug: amazon-location-service-workflow
tags:
- Amazon Location Service
- AWS
- Workflow
tools:
- description: Creates a map resource in your AWS account.
  hints:
    idempotent: false
    readOnly: false
  name: map-resources-create-map
- description: Lists map resources in your AWS account.
  hints:
    idempotent: true
    readOnly: true
  name: map-resources-list-maps
- description: Retrieves the map resource details.
  hints:
    idempotent: true
    readOnly: true
  name: map-resources-describe-map
---
