---
consumed_apis:
- account-management
description: Identity and access management workflow for platform admins managing Dynatrace users, groups, permissions, and environments across the account.
layout: capability
name: Dynatrace Identity And Access
operations:
- description: List all users in the account
  method: GET
  name: list-users
  path: /v1/users
- description: Create a new user
  method: POST
  name: create-user
  path: /v1/users
- description: Get user details
  method: GET
  name: get-user
  path: /v1/users/{userId}
- description: Update user profile and groups
  method: PUT
  name: update-user
  path: /v1/users/{userId}
- description: Delete a user
  method: DELETE
  name: delete-user
  path: /v1/users/{userId}
- description: List all groups
  method: GET
  name: list-groups
  path: /v1/groups
- description: Create a new group
  method: POST
  name: create-group
  path: /v1/groups
- description: Get group details
  method: GET
  name: get-group
  path: /v1/groups/{groupId}
- description: Update group name and description
  method: PUT
  name: update-group
  path: /v1/groups/{groupId}
- description: Delete a group
  method: DELETE
  name: delete-group
  path: /v1/groups/{groupId}
- description: List all permissions for the account
  method: GET
  name: list-permissions
  path: /v1/permissions
- description: List all environments
  method: GET
  name: list-environments
  path: /v1/environments
personas: []
provider_name: Dynatrace
provider_slug: dynatrace
search_terms:
- list permissions
- delete a group
- get user details
- get details of a specific group
- get details of a specific user
- application performance monitoring
- update a group's name and description
- list all users in the account
- analytics
- list all permissions for the account
- intelligence
- get, update, or delete a specific group
- delete user
- list environments
- create a new user
- create a new user and send an invitation email
- create group
- digital experience management
- get group
- list all environments associated with the account
- iam
- update a user's profile and group memberships
- permanently delete a group
- manage user groups
- list all permissions defined for the account
- ai operations
- list all users in the dynatrace account
- update group name and description
- update user profile and groups
- automation
- observability
- query permissions
- list users
- application security
- apm
- get, update, or delete a specific user
- create a new user group
- list groups
- delete a user
- platform administration
- access control
- get group details
- update user
- delete group
- get user
- cloud monitoring
- create user
- list all groups
- identity
- manage account users
- list all environments
- list all user groups in the account
- create a new group
- permanently remove a user from the account
- dynatrace
- update group
slug: identity-and-access
tags:
- Dynatrace
- Identity
- Access Control
- Platform Administration
- IAM
tools:
- description: List all users in the Dynatrace account
  hints:
    openWorld: true
    readOnly: true
  name: list-users
- description: Create a new user and send an invitation email
  hints:
    openWorld: true
    readOnly: false
  name: create-user
- description: Get details of a specific user
  hints:
    openWorld: true
    readOnly: true
  name: get-user
- description: Update a user's profile and group memberships
  hints:
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-user
- description: Permanently remove a user from the account
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-user
- description: List all user groups in the account
  hints:
    openWorld: true
    readOnly: true
  name: list-groups
- description: Create a new user group
  hints:
    openWorld: true
    readOnly: false
  name: create-group
- description: Get details of a specific group
  hints:
    openWorld: true
    readOnly: true
  name: get-group
- description: Update a group's name and description
  hints:
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-group
- description: Permanently delete a group
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-group
- description: List all permissions defined for the account
  hints:
    openWorld: true
    readOnly: true
  name: list-permissions
- description: List all environments associated with the account
  hints:
    openWorld: true
    readOnly: true
  name: list-environments
---
