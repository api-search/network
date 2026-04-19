---
consumed_apis:
- tag-manager
description: Workflow for managing tag deployment lifecycle including accounts, containers, workspaces, tags, triggers, variables, and version publishing. Used by marketing technologists and web analytics engineers.
layout: capability
name: Google Tag Manager Tag Deployment Management
operations:
- description: List all GTM accounts
  method: GET
  name: list-accounts
  path: /v1/accounts
- description: List containers in an account
  method: GET
  name: list-containers
  path: /v1/containers
- description: Create a container
  method: POST
  name: create-container
  path: /v1/containers
- description: List tags in a workspace
  method: GET
  name: list-tags
  path: /v1/tags
- description: Create a tag
  method: POST
  name: create-tag
  path: /v1/tags
- description: List triggers in a workspace
  method: GET
  name: list-triggers
  path: /v1/triggers
- description: List variables in a workspace
  method: GET
  name: list-variables
  path: /v1/variables
personas: []
provider_name: Google Tag Manager
provider_slug: google-tag-manager
search_terms:
- delete trigger
- list workspaces
- delete a tag
- list containers in an account
- create container
- delete container
- list variables
- analytics
- create a container
- create a tag
- create a new container
- publish a container version
- create workspace
- trigger management
- list workspaces in a container
- variable management
- delete variable
- delete tag
- delete a workspace
- create trigger
- create a new workspace
- list all gtm accounts
- delete a trigger
- list container version headers
- get account
- list triggers in a workspace
- create a new tag
- create a new trigger
- list tags
- tracking
- account management
- create variable
- list containers
- update account
- update account settings
- get container
- list tags in a workspace
- google tag manager
- marketing
- delete a container
- get tag
- conversion tracking
- list triggers
- get tag details
- list versions
- delete workspace
- get account details
- list accounts
- list variables in a workspace
- create a new variable
- list all google tag manager accounts
- delete a variable
- get container details
- container management
- publish version
- create tag
- tag management
slug: tag-deployment-management
tags:
- Google Tag Manager
- Tag Management
- Marketing
- Analytics
tools:
- description: List all Google Tag Manager accounts
  hints:
    idempotent: true
    readOnly: true
  name: list-accounts
- description: Get account details
  hints:
    idempotent: true
    readOnly: true
  name: get-account
- description: Update account settings
  hints:
    idempotent: true
    readOnly: false
  name: update-account
- description: List containers in an account
  hints:
    idempotent: true
    readOnly: true
  name: list-containers
- description: Create a new container
  hints:
    idempotent: false
    readOnly: false
  name: create-container
- description: Get container details
  hints:
    idempotent: true
    readOnly: true
  name: get-container
- description: Delete a container
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-container
- description: List workspaces in a container
  hints:
    idempotent: true
    readOnly: true
  name: list-workspaces
- description: Create a new workspace
  hints:
    idempotent: false
    readOnly: false
  name: create-workspace
- description: Delete a workspace
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-workspace
- description: List tags in a workspace
  hints:
    idempotent: true
    readOnly: true
  name: list-tags
- description: Create a new tag
  hints:
    idempotent: false
    readOnly: false
  name: create-tag
- description: Get tag details
  hints:
    idempotent: true
    readOnly: true
  name: get-tag
- description: Delete a tag
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-tag
- description: List triggers in a workspace
  hints:
    idempotent: true
    readOnly: true
  name: list-triggers
- description: Create a new trigger
  hints:
    idempotent: false
    readOnly: false
  name: create-trigger
- description: Delete a trigger
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-trigger
- description: List variables in a workspace
  hints:
    idempotent: true
    readOnly: true
  name: list-variables
- description: Create a new variable
  hints:
    idempotent: false
    readOnly: false
  name: create-variable
- description: Delete a variable
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-variable
- description: List container version headers
  hints:
    idempotent: true
    readOnly: true
  name: list-versions
- description: Publish a container version
  hints:
    idempotent: false
    readOnly: false
  name: publish-version
---
