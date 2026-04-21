---
consumed_apis:
- workspaces-web
description: Unified workflow for IT administrators to manage Amazon WorkSpaces Web portals, user settings, browser policies, network configurations, and trust stores for enterprise secure browser deployments.
layout: capability
name: Amazon WorkSpaces Web Secure Browser Management
operations:
- description: List secure browser portals.
  method: GET
  name: list-portals
  path: /v1/portals
- description: Create a portal.
  method: POST
  name: create-portal
  path: /v1/portals
- description: List user settings.
  method: GET
  name: list-user-settings
  path: /v1/user-settings
- description: List browser settings.
  method: GET
  name: list-browser-settings
  path: /v1/browser-settings
- description: List network settings.
  method: GET
  name: list-network-settings
  path: /v1/network-settings
- description: List trust stores.
  method: GET
  name: list-trust-stores
  path: /v1/trust-stores
personas: []
provider_name: Amazon WorkSpaces Web
provider_slug: amazon-workspaces-web
search_terms:
- IT Administrator
- list secure browser portals.
- list network settings
- administration
- Security Engineer
- zero trust
- browser policy and access control enforcement
- user settings management.
- secure remote browser access infrastructure
- network configuration management.
- list browser policy settings for portals.
- create a new secure browser portal.
- workflow for it administrators to manage workspaces web portals and their associated security and network configurations.
- list trust stores.
- list browser settings.
- manages workspaces web portals and configurations.
- create a portal.
- list all workspaces web secure browser portals.
- portal management.
- create portal
- trust store management.
- list ssl certificate trust stores.
- list browser settings
- list network settings for portal connectivity.
- list user settings.
- list user settings configurations for portals.
- aws
- list portals
- configures browser policies and access controls.
- secure browser
- list user settings
- virtual desktop
- portal and resource provisioning
- end user computing
- list network settings.
- list trust stores
- browser policy management.
slug: secure-browser-management
tags:
- AWS
- Secure Browser
- End User Computing
- Administration
tools:
- description: List all WorkSpaces Web secure browser portals.
  hints:
    openWorld: true
    readOnly: true
  name: list-portals
- description: Create a new secure browser portal.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-portal
- description: List user settings configurations for portals.
  hints:
    openWorld: true
    readOnly: true
  name: list-user-settings
- description: List browser policy settings for portals.
  hints:
    openWorld: true
    readOnly: true
  name: list-browser-settings
- description: List network settings for portal connectivity.
  hints:
    openWorld: true
    readOnly: true
  name: list-network-settings
- description: List SSL certificate trust stores.
  hints:
    openWorld: true
    readOnly: true
  name: list-trust-stores
---
