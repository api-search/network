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
- list all api security configurations
- security automation
- threat protection
- Security Engineer
- manage api security configurations and posture
- check activation status
- create security configuration
- list security policies within a configuration
- list activations
- discover apis
- api posture assessment and vulnerability management
- monitors api discovery, threat detection, and posture findings
- api security configuration and policy management
- get api discovery
- api security configuration management
- api discovery
- create a new api security configuration
- create configuration
- runtime protection
- api security
- list configuration activations
- manages api security configurations and activations
- security policy management
- API Security Analyst
- get api inventory including shadow and zombie api findings
- akamai
- list policies
- cloud security
- list and check status of security configuration activations
- configuration activations
- posture management
- list security policies
- get api discovery results
- real-time api threat detection and blocking
- list all akamai api security configurations
- api inventory and discovery
- list security configurations
- create a new akamai api security configuration
- list configurations
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
