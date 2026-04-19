---
consumed_apis:
- tyk-gateway
- tyk-dashboard
description: Unified API management workflow combining Gateway and Dashboard APIs for API developers and platform engineers to manage API definitions, keys, policies, and portal configurations.
layout: capability
name: Tyk API Management
operations:
- description: List all API definitions from Dashboard
  method: GET
  name: list-apis
  path: /v1/apis
- description: Get a specific API definition
  method: GET
  name: get-api
  path: /v1/apis
- description: Create a new API definition
  method: POST
  name: create-api
  path: /v1/apis
- description: List all API keys
  method: GET
  name: list-keys
  path: /v1/keys
- description: List all policies
  method: GET
  name: list-policies
  path: /v1/policies
- description: List all dashboard users
  method: GET
  name: list-users
  path: /v1/users
- description: Check gateway health
  method: GET
  name: check-health
  path: /v1/health
- description: Get portal catalogue
  method: GET
  name: get-catalogue
  path: /v1/catalogue
personas: []
provider_name: Tyk
provider_slug: tyk
search_terms:
- list keys
- list policies
- check health
- get the developer portal catalogue
- api definitions
- graphql
- api keys
- list apis
- create a new api definition in the dashboard
- list all security policies
- check the gateway health status
- dashboard create policy
- dashboard get policy
- list users
- dashboard list apis
- create api
- gateway list apis
- open source
- gateway check health
- dashboard update api
- get api
- get a specific policy
- list all api definitions from the tyk dashboard
- dashboard create api
- create a new api definition
- check gateway health
- security policies
- list all dashboard users
- dashboard delete api
- dashboard list users
- api management
- dashboard get api
- list all certificates on the gateway
- hot reload the gateway configuration
- gateway
- create a new security policy
- create a new api key
- get a specific api definition from the dashboard
- list all api definitions from dashboard
- dashboard get catalogue
- gateway health
- dashboard list policies
- get portal catalogue
- update an api definition in the dashboard
- gateway list certificates
- dashboard create key
- api gateway
- delete an api definition from the dashboard
- get catalogue
- list all api definitions directly from the gateway
- list all api keys
- gateway hot reload
- get a specific api definition
- list all policies
- dashboard users
- portal catalogue
- tyk
- dashboard list keys
slug: api-management
tags:
- API Management
- Gateway
- Tyk
tools:
- description: List all API definitions from the Tyk Dashboard
  hints:
    openWorld: true
    readOnly: true
  name: dashboard-list-apis
- description: Get a specific API definition from the Dashboard
  hints:
    readOnly: true
  name: dashboard-get-api
- description: Create a new API definition in the Dashboard
  hints:
    readOnly: false
  name: dashboard-create-api
- description: Update an API definition in the Dashboard
  hints:
    idempotent: true
    readOnly: false
  name: dashboard-update-api
- description: Delete an API definition from the Dashboard
  hints:
    destructive: true
    idempotent: true
  name: dashboard-delete-api
- description: List all security policies
  hints:
    readOnly: true
  name: dashboard-list-policies
- description: Get a specific policy
  hints:
    readOnly: true
  name: dashboard-get-policy
- description: Create a new security policy
  hints:
    readOnly: false
  name: dashboard-create-policy
- description: List all API keys
  hints:
    readOnly: true
  name: dashboard-list-keys
- description: Create a new API key
  hints:
    readOnly: false
  name: dashboard-create-key
- description: List all dashboard users
  hints:
    readOnly: true
  name: dashboard-list-users
- description: Get the developer portal catalogue
  hints:
    readOnly: true
  name: dashboard-get-catalogue
- description: List all API definitions directly from the Gateway
  hints:
    readOnly: true
  name: gateway-list-apis
- description: Check the gateway health status
  hints:
    readOnly: true
  name: gateway-check-health
- description: Hot reload the gateway configuration
  hints:
    idempotent: true
    readOnly: false
  name: gateway-hot-reload
- description: List all certificates on the gateway
  hints:
    readOnly: true
  name: gateway-list-certificates
---
