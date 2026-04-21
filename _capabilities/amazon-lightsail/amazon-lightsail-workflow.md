---
consumed_apis:
- lightsail
description: Unified workflow capability for Amazon Lightsail combining resource management and operations.
layout: capability
name: Amazon Lightsail Workflow
operations: []
personas: []
provider_name: Amazon Lightsail
provider_slug: amazon-lightsail
search_terms:
- creates one or more amazon lightsail instances.
- aws
- unified workflow for amazon lightsail resource management
- Developer
- amazon lightsail
- workflow
- instances get instance
- Administrator
- instances create instances
- manages resources and configurations
- returns information about all amazon lightsail virtual private servers.
- instances get instances
- integrates api into applications
- returns information about a specific amazon lightsail instance.
slug: amazon-lightsail-workflow
tags:
- Amazon Lightsail
- AWS
- Workflow
tools:
- description: Creates one or more Amazon Lightsail instances.
  hints:
    idempotent: false
    readOnly: false
  name: instances-create-instances
- description: Returns information about all Amazon Lightsail virtual private servers.
  hints:
    idempotent: true
    readOnly: true
  name: instances-get-instances
- description: Returns information about a specific Amazon Lightsail instance.
  hints:
    idempotent: true
    readOnly: true
  name: instances-get-instance
---
