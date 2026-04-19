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
- graphql
- administration
- update an organization
- mdcb
- get dataplane
- list all tyk organizations
- open source
- get details for a specific data plane
- data plane monitoring
- platform
- create an admin user
- api management
- list all connected data plane nodes
- export system
- list all organizations
- update organization
- list organizations
- list all admin users
- create admin user
- mdcb health
- api gateway
- create organization
- list admin users
- organization management
- delete an organization
- delete organization
- export system configuration
- import system
- import system configuration
- get pprof diagnostic data from mdcb
- admin user management
- list dataplanes
- get diagnostics
- check mdcb health
- tyk
- list all connected data planes
- create a new organization
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
