---
consumed_apis:
- akamai-api-security
description: Unified workflow for managing Akamai API Security configurations, policies, and threat protection. Covers security posture management, API discovery, and configuration activation for security teams.
layout: capability
name: Akamai API Security Management
operations:
- description: List all API security configurations
  method: GET
  name: list-configurations
  path: /v1/configurations
- description: Create a new API security configuration
  method: POST
  name: create-configuration
  path: /v1/configurations
- description: List security policies
  method: GET
  name: list-policies
  path: /v1/policies
- description: Get API discovery results
  method: GET
  name: get-api-discovery
  path: /v1/api-discovery
- description: List configuration activations
  method: GET
  name: list-activations
  path: /v1/activations
personas: []
provider_name: Akamai API Security
provider_slug: akamai-api-security
search_terms:
- list policies
- api discovery
- list security configurations
- get api inventory including shadow and zombie api findings
- list configuration activations
- create a new akamai api security configuration
- check activation status
- list configurations
- list activations
- list all api security configurations
- create a new api security configuration
- list security policies
- Security Engineer
- api inventory and discovery
- api posture assessment and vulnerability management
- manages api security configurations and activations
- real-time api threat detection and blocking
- threat protection
- api security configuration and policy management
- runtime protection
- security automation
- security policy management
- create security configuration
- discover apis
- create configuration
- akamai
- list security policies within a configuration
- list and check status of security configuration activations
- get api discovery results
- manage api security configurations and posture
- API Security Analyst
- cloud security
- configuration activations
- api security configuration management
- get api discovery
- api security
- posture management
- list all akamai api security configurations
- monitors api discovery, threat detection, and posture findings
slug: api-security-management
tags:
- Akamai
- API Security
- Posture Management
- Runtime Protection
- Security Automation
tools:
- description: List all Akamai API Security configurations
  hints:
    openWorld: true
    readOnly: true
  name: list-security-configurations
- description: Create a new Akamai API Security configuration
  hints:
    destructive: false
    readOnly: false
  name: create-security-configuration
- description: List security policies within a configuration
  hints:
    openWorld: true
    readOnly: true
  name: list-security-policies
- description: Get API inventory including shadow and zombie API findings
  hints:
    openWorld: true
    readOnly: true
  name: discover-apis
- description: List and check status of security configuration activations
  hints:
    openWorld: true
    readOnly: true
  name: check-activation-status
---
