---
consumed_apis:
- acquia-cloud
description: Unified workflow for managing Drupal applications on Acquia Cloud, including application discovery, environment management, organization administration, and account operations. Used by Drupal developers, DevOps engineers, and platform administrators to automate Acquia Cloud Platform workflows.
layout: capability
name: Acquia Drupal Application Management
operations:
- description: List all accessible Acquia Cloud applications
  method: GET
  name: list-applications
  path: /v1/applications
- description: Get application details
  method: GET
  name: get-application
  path: /v1/applications
- description: List environments for an application
  method: GET
  name: list-environments
  path: /v1/environments
- description: Get environment details
  method: GET
  name: get-environment
  path: /v1/environments
- description: List all organizations
  method: GET
  name: list-organizations
  path: /v1/organizations
- description: Get current user account details
  method: GET
  name: get-account
  path: /v1/account
personas: []
provider_name: Acquia
provider_slug: acquia
search_terms:
- devops
- list environments
- application discovery, environment management, and organization administration
- get application details
- Drupal Developer
- get application
- user, team, and organizational access control management
- experience
- drupal application hosting lifecycle on acquia cloud platform
- list all organizations
- get environment
- acquia
- list organizations
- acquia platform admin managing organizations, teams, and subscriptions
- get account
- get detailed information about a specific acquia cloud environment
- application environment operations
- get current user account details
- environments
- applications
- list all organizations the current acquia user belongs to
- Platform Administrator
- get the current acquia cloud user account profile and permissions
- DevOps Engineer
- current user account
- list all environments (dev, staging, prod) for an acquia cloud application
- developer building and deploying drupal applications on acquia cloud
- list all acquia cloud drupal applications the current user can access
- drupal application lifecycle management
- cloud ide environments and platform notification management
- cloud
- list environments for an application
- list applications
- list all accessible acquia cloud applications
- engineer managing ci/cd pipelines, deployments, and environment configuration
- content
- get detailed information about a specific acquia cloud application
- get environment details
- drupal
- organization management
slug: drupal-application-management
tags:
- Acquia
- Applications
- Cloud
- DevOps
- Drupal
- Environments
tools:
- description: List all Acquia Cloud Drupal applications the current user can access
  hints:
    openWorld: true
    readOnly: true
  name: list-applications
- description: Get detailed information about a specific Acquia Cloud application
  hints:
    idempotent: true
    readOnly: true
  name: get-application
- description: List all environments (dev, staging, prod) for an Acquia Cloud application
  hints:
    openWorld: true
    readOnly: true
  name: list-environments
- description: Get detailed information about a specific Acquia Cloud environment
  hints:
    idempotent: true
    readOnly: true
  name: get-environment
- description: List all organizations the current Acquia user belongs to
  hints:
    openWorld: true
    readOnly: true
  name: list-organizations
- description: Get the current Acquia Cloud user account profile and permissions
  hints:
    idempotent: true
    readOnly: true
  name: get-account
---
