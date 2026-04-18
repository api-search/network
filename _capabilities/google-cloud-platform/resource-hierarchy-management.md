---
consumed_apis:
- cloud-resource-manager
description: Workflow for managing the Google Cloud resource hierarchy including projects, folders, organizations, and tags. Used by cloud administrators and platform engineers.
layout: capability
name: Google Cloud Platform Resource Hierarchy Management
operations:
- description: List projects
  method: GET
  name: list-projects
  path: /v1/projects
- description: Create a project
  method: POST
  name: create-project
  path: /v1/projects
- description: Get project details
  method: GET
  name: get-project
  path: /v1/projects/{name}
- description: Update a project
  method: PATCH
  name: update-project
  path: /v1/projects/{name}
- description: Delete a project
  method: DELETE
  name: delete-project
  path: /v1/projects/{name}
- description: List folders
  method: GET
  name: list-folders
  path: /v1/folders
- description: Create a folder
  method: POST
  name: create-folder
  path: /v1/folders
- description: Get organization details
  method: GET
  name: get-organization
  path: /v1/organizations/{name}
personas: []
provider_name: Google Cloud Platform
provider_slug: google-cloud-platform
search_terms:
- get folder
- single project operations
- delete a project
- delete a google cloud project
- search for projects matching a query
- project management
- create a folder
- create folder
- organization operations
- create a new tag key
- platform as a service
- resource management
- create a project
- list folders
- get folder details
- list tag keys
- search projects
- infrastructure
- create project
- delete folder
- governance
- search organizations
- delete a folder
- list google cloud projects under a parent
- get project
- list projects
- update project
- get organization
- list tag keys for resource tagging
- get project details
- search for organizations
- update a project
- create tag key
- cloud computing
- api management
- create a new google cloud project
- delete project
- google cloud
- list folders under a parent
- get organization details
- folder management
slug: resource-hierarchy-management
tags:
- Google Cloud
- Resource Management
- Governance
- Infrastructure
tools:
- description: List Google Cloud projects under a parent
  hints:
    idempotent: true
    readOnly: true
  name: list-projects
- description: Create a new Google Cloud project
  hints:
    idempotent: false
    readOnly: false
  name: create-project
- description: Get project details
  hints:
    idempotent: true
    readOnly: true
  name: get-project
- description: Update a project
  hints:
    idempotent: true
    readOnly: false
  name: update-project
- description: Delete a Google Cloud project
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-project
- description: Search for projects matching a query
  hints:
    idempotent: true
    readOnly: true
  name: search-projects
- description: List folders under a parent
  hints:
    idempotent: true
    readOnly: true
  name: list-folders
- description: Create a folder
  hints:
    idempotent: false
    readOnly: false
  name: create-folder
- description: Get folder details
  hints:
    idempotent: true
    readOnly: true
  name: get-folder
- description: Delete a folder
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-folder
- description: Get organization details
  hints:
    idempotent: true
    readOnly: true
  name: get-organization
- description: Search for organizations
  hints:
    idempotent: true
    readOnly: true
  name: search-organizations
- description: List tag keys for resource tagging
  hints:
    idempotent: true
    readOnly: true
  name: list-tag-keys
- description: Create a new tag key
  hints:
    idempotent: false
    readOnly: false
  name: create-tag-key
---
