---
consumed_apis:
- license-manager
description: Unified workflow capability for Amazon License Manager combining resource management and operations.
layout: capability
name: Amazon License Manager Workflow
operations: []
personas: []
provider_name: Amazon License Manager
provider_slug: amazon-license-manager
search_terms:
- aws
- gets detailed information about the specified license configuration.
- license management
- unified workflow for amazon license manager resource management
- compliance
- Developer
- license configurations create license configuratio
- workflow
- Administrator
- license configurations get license configuration
- license configurations list license configurations
- amazon license manager
- manages resources and configurations
- cost management
- software licensing
- integrates api into applications
- lists the license configurations for your account.
- creates a license configuration.
slug: amazon-license-manager-workflow
tags:
- Amazon License Manager
- AWS
- Workflow
tools:
- description: Creates a license configuration.
  hints:
    idempotent: false
    readOnly: false
  name: license-configurations-create-license-configuratio
- description: Lists the license configurations for your account.
  hints:
    idempotent: true
    readOnly: true
  name: license-configurations-list-license-configurations
- description: Gets detailed information about the specified license configuration.
  hints:
    idempotent: true
    readOnly: true
  name: license-configurations-get-license-configuration
---
