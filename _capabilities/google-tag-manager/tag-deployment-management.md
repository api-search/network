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
- create a new variable
- update account settings
- list triggers
- list versions
- get tag details
- google tag manager
- list variables
- analytics
- get container details
- delete a trigger
- list tags in a workspace
- list tags
- trigger management
- get container
- delete a container
- list triggers in a workspace
- create a new workspace
- create workspace
- container management
- list workspaces
- delete workspace
- create a new tag
- list all google tag manager accounts
- delete a variable
- get account
- delete a tag
- create a new trigger
- update account
- list container version headers
- marketing
- create a new container
- create variable
- list containers in an account
- create a container
- delete container
- list all gtm accounts
- create container
- delete trigger
- create tag
- tracking
- tag management
- get account details
- delete tag
- create a tag
- variable management
- conversion tracking
- publish a container version
- list containers
- delete a workspace
- list accounts
- list variables in a workspace
- delete variable
- account management
- create trigger
- list workspaces in a container
- get tag
- publish version
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
