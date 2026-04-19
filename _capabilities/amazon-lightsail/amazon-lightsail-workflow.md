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
- returns information about all amazon lightsail virtual private servers.
- instances get instance
- instances get instances
- integrates api into applications
- manages resources and configurations
- instances create instances
- returns information about a specific amazon lightsail instance.
- aws
- creates one or more amazon lightsail instances.
- amazon lightsail
- unified workflow for amazon lightsail resource management
- Administrator
- workflow
- Developer
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
