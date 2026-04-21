---
consumed_apis:
- cloud-ops
description: Unified workflow for platform administrators to manage Temporal Cloud infrastructure including namespaces, users, service accounts, API keys, and regions.
layout: capability
name: Temporal Cloud Operations
operations:
- description: List all namespaces
  method: GET
  name: list-namespaces
  path: /v1/namespaces
- description: Create a namespace
  method: POST
  name: create-namespace
  path: /v1/namespaces
- description: Get namespace details
  method: GET
  name: get-namespace
  path: /v1/namespaces/{namespace}
- description: Delete a namespace
  method: DELETE
  name: delete-namespace
  path: /v1/namespaces/{namespace}
- description: List all users
  method: GET
  name: list-users
  path: /v1/users
- description: Create a user
  method: POST
  name: create-user
  path: /v1/users
- description: List all service accounts
  method: GET
  name: list-service-accounts
  path: /v1/service-accounts
- description: Create a service account
  method: POST
  name: create-service-account
  path: /v1/service-accounts
- description: List all API keys
  method: GET
  name: list-api-keys
  path: /v1/api-keys
- description: Create an API key
  method: POST
  name: create-api-key
  path: /v1/api-keys
- description: List available regions
  method: GET
  name: list-regions
  path: /v1/regions
personas: []
provider_name: Temporal
provider_slug: temporal
search_terms:
- get namespace details
- create a new temporal cloud namespace
- service account management
- get user details
- delete api key
- create an api key
- temporal
- list regions
- list all users in the account
- get service account details
- user management
- delete user
- create a new user
- workflow infrastructure
- list all namespaces
- update namespace
- workflows
- create namespace
- create a namespace
- list all available temporal cloud regions
- get async operation
- delete a namespace
- create a new api key for authentication
- list users
- list all api keys in the account
- list all service accounts
- get namespace
- update namespace configuration
- platform administration
- delete a user
- get details for a specific namespace
- delete namespace
- list all temporal cloud namespaces
- create a service account for api access
- get service account
- delete a service account
- create a service account
- list namespaces
- delete a temporal cloud namespace
- get api key
- cloud operations
- get user
- check the status of an asynchronous operation
- delete service account
- create user
- api key management
- list all api keys
- list service accounts
- namespace management
- list available regions
- region information
- create service account
- delete an api key
- create a user
- get api key details
- list all users
- create api key
- single namespace operations
- procode_api_composition
- list api keys
slug: cloud-operations
tags:
- Temporal
- Cloud Operations
- Platform Administration
- Workflow Infrastructure
tools:
- description: List all Temporal Cloud namespaces
  hints:
    openWorld: true
    readOnly: true
  name: list-namespaces
- description: Create a new Temporal Cloud namespace
  hints:
    readOnly: false
  name: create-namespace
- description: Get details for a specific namespace
  hints:
    readOnly: true
  name: get-namespace
- description: Update namespace configuration
  hints:
    idempotent: true
    readOnly: false
  name: update-namespace
- description: Delete a Temporal Cloud namespace
  hints:
    destructive: true
  name: delete-namespace
- description: List all users in the account
  hints:
    readOnly: true
  name: list-users
- description: Create a new user
  hints:
    readOnly: false
  name: create-user
- description: Get user details
  hints:
    readOnly: true
  name: get-user
- description: Delete a user
  hints:
    destructive: true
  name: delete-user
- description: List all service accounts
  hints:
    readOnly: true
  name: list-service-accounts
- description: Create a service account for API access
  hints:
    readOnly: false
  name: create-service-account
- description: Get service account details
  hints:
    readOnly: true
  name: get-service-account
- description: Delete a service account
  hints:
    destructive: true
  name: delete-service-account
- description: List all API keys in the account
  hints:
    readOnly: true
  name: list-api-keys
- description: Create a new API key for authentication
  hints:
    readOnly: false
  name: create-api-key
- description: Get API key details
  hints:
    readOnly: true
  name: get-api-key
- description: Delete an API key
  hints:
    destructive: true
  name: delete-api-key
- description: List all available Temporal Cloud regions
  hints:
    readOnly: true
  name: list-regions
- description: Check the status of an asynchronous operation
  hints:
    readOnly: true
  name: get-async-operation
---
