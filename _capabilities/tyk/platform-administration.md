---
consumed_apis:
- tyk-dashboard-admin
- tyk-mdcb
description: Platform administration workflow combining Dashboard Admin and MDCB APIs for platform administrators to manage organizations, multi-data center deployments, and system diagnostics.
layout: capability
name: Tyk Platform Administration
operations:
- description: List all organizations
  method: GET
  name: list-organizations
  path: /v1/organizations
- description: Create a new organization
  method: POST
  name: create-organization
  path: /v1/organizations
- description: List admin users
  method: GET
  name: list-admin-users
  path: /v1/admin-users
- description: List all connected data planes
  method: GET
  name: list-dataplanes
  path: /v1/dataplanes
- description: Check MDCB health
  method: GET
  name: check-mdcb-health
  path: /v1/health
personas: []
provider_name: Tyk
provider_slug: tyk
search_terms:
- get diagnostics
- graphql
- administration
- platform
- list all tyk organizations
- update an organization
- api gateway
- organization management
- create an admin user
- list organizations
- open source
- delete organization
- get details for a specific data plane
- export system
- mdcb health
- mdcb
- create admin user
- export system configuration
- list all admin users
- list all connected data planes
- create organization
- list dataplanes
- data plane monitoring
- delete an organization
- tyk
- admin user management
- list admin users
- check mdcb health
- create a new organization
- update organization
- api management
- import system
- import system configuration
- list all connected data plane nodes
- get dataplane
- list all organizations
- get pprof diagnostic data from mdcb
slug: platform-administration
tags:
- Administration
- MDCB
- Platform
- Tyk
tools:
- description: List all Tyk organizations
  hints:
    openWorld: true
    readOnly: true
  name: list-organizations
- description: Create a new organization
  hints:
    readOnly: false
  name: create-organization
- description: Update an organization
  hints:
    idempotent: true
    readOnly: false
  name: update-organization
- description: Delete an organization
  hints:
    destructive: true
    idempotent: true
  name: delete-organization
- description: List all admin users
  hints:
    readOnly: true
  name: list-admin-users
- description: Create an admin user
  hints:
    readOnly: false
  name: create-admin-user
- description: Export system configuration
  hints:
    readOnly: true
  name: export-system
- description: Import system configuration
  hints:
    readOnly: false
  name: import-system
- description: List all connected data plane nodes
  hints:
    openWorld: true
    readOnly: true
  name: list-dataplanes
- description: Get details for a specific data plane
  hints:
    readOnly: true
  name: get-dataplane
- description: Check MDCB health
  hints:
    readOnly: true
  name: check-mdcb-health
- description: Get pprof diagnostic data from MDCB
  hints:
    readOnly: true
  name: get-diagnostics
---
