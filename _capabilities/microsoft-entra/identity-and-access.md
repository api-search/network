---
consumed_apis:
- entra-graph
description: Unified workflow for managing identity and access including users, groups, applications, and service principals in Microsoft Entra ID. Used by IT administrators and identity engineers.
layout: capability
name: Microsoft Entra Identity and Access Management
operations:
- description: List all users in the directory.
  method: GET
  name: list-users
  path: /v1/users
- description: Create a new user.
  method: POST
  name: create-user
  path: /v1/users
- description: Get user details.
  method: GET
  name: get-user
  path: /v1/users/{id}
- description: Update user properties.
  method: PATCH
  name: update-user
  path: /v1/users/{id}
- description: Delete a user.
  method: DELETE
  name: delete-user
  path: /v1/users/{id}
- description: List user group memberships.
  method: GET
  name: list-user-memberships
  path: /v1/users/{id}/memberships
- description: List all groups.
  method: GET
  name: list-groups
  path: /v1/groups
- description: Create a new group.
  method: POST
  name: create-group
  path: /v1/groups
- description: Get group details.
  method: GET
  name: get-group
  path: /v1/groups/{id}
- description: Update group properties.
  method: PATCH
  name: update-group
  path: /v1/groups/{id}
- description: Delete a group.
  method: DELETE
  name: delete-group
  path: /v1/groups/{id}
- description: List group members.
  method: GET
  name: list-group-members
  path: /v1/groups/{id}/members
- description: Add a member to a group.
  method: POST
  name: add-group-member
  path: /v1/groups/{id}/members
- description: List all applications.
  method: GET
  name: list-applications
  path: /v1/applications
- description: Register a new application.
  method: POST
  name: create-application
  path: /v1/applications
- description: Get application details.
  method: GET
  name: get-application
  path: /v1/applications/{id}
- description: Update application properties.
  method: PATCH
  name: update-application
  path: /v1/applications/{id}
- description: Delete an application.
  method: DELETE
  name: delete-application
  path: /v1/applications/{id}
- description: List all service principals.
  method: GET
  name: list-service-principals
  path: /v1/service-principals
- description: Create a new service principal.
  method: POST
  name: create-service-principal
  path: /v1/service-principals
- description: Get service principal details.
  method: GET
  name: get-service-principal
  path: /v1/service-principals/{id}
- description: Update service principal.
  method: PATCH
  name: update-service-principal
  path: /v1/service-principals/{id}
- description: Delete a service principal.
  method: DELETE
  name: delete-service-principal
  path: /v1/service-principals/{id}
personas: []
provider_name: Microsoft Entra
provider_slug: microsoft-entra
search_terms:
- create a new user.
- zero trust
- list all application registrations.
- delete a user.
- microsoft
- update service principal
- list groups and roles a user belongs to.
- network security
- entra
- list group members.
- list all users in microsoft entra directory.
- get service principal
- register a new application.
- create a new user in the directory.
- individual application management.
- list all service principals.
- delete an application registration.
- delete application
- create application
- delete service principal
- list user memberships
- remove group member
- access management
- update group
- create a new service principal.
- authentication
- delete a group.
- list user group memberships.
- get user details.
- create user
- delete user
- list all applications.
- update user
- update service principal.
- list service principals
- remove a member from a group.
- get application details.
- list all groups in the directory.
- get group
- add group member
- user account management.
- directory management
- group membership management.
- individual service principal management.
- update service principal properties.
- individual group management.
- get group details.
- security
- delete group
- list users
- identity
- delete an application.
- delete a user from the directory.
- delete a service principal.
- update user properties.
- identity governance
- list all users in the directory.
- list members of a group.
- list all groups.
- update application properties.
- update application
- group management.
- individual user management.
- list group members
- list groups
- get application
- add a member to a group.
- azure ad
- create service principal
- create group
- service principal management.
- user group membership.
- get user
- update group properties.
- list applications
- get user properties by id.
- create a new group.
- get service principal details.
- microsoft entra
- application registration management.
slug: identity-and-access
tags:
- Microsoft Entra
- Identity
- Access Management
- Directory Management
tools:
- description: List all users in Microsoft Entra directory.
  hints:
    openWorld: true
    readOnly: true
  name: list-users
- description: Create a new user in the directory.
  hints:
    readOnly: false
  name: create-user
- description: Get user properties by ID.
  hints:
    readOnly: true
  name: get-user
- description: Update user properties.
  hints:
    idempotent: true
    readOnly: false
  name: update-user
- description: Delete a user from the directory.
  hints:
    destructive: true
    idempotent: true
  name: delete-user
- description: List groups and roles a user belongs to.
  hints:
    readOnly: true
  name: list-user-memberships
- description: List all groups in the directory.
  hints:
    openWorld: true
    readOnly: true
  name: list-groups
- description: Create a new group.
  hints:
    readOnly: false
  name: create-group
- description: Get group details.
  hints:
    readOnly: true
  name: get-group
- description: Update group properties.
  hints:
    idempotent: true
    readOnly: false
  name: update-group
- description: Delete a group.
  hints:
    destructive: true
    idempotent: true
  name: delete-group
- description: List members of a group.
  hints:
    readOnly: true
  name: list-group-members
- description: Add a member to a group.
  hints:
    readOnly: false
  name: add-group-member
- description: Remove a member from a group.
  hints:
    destructive: true
    idempotent: true
  name: remove-group-member
- description: List all application registrations.
  hints:
    openWorld: true
    readOnly: true
  name: list-applications
- description: Register a new application.
  hints:
    readOnly: false
  name: create-application
- description: Get application details.
  hints:
    readOnly: true
  name: get-application
- description: Update application properties.
  hints:
    idempotent: true
    readOnly: false
  name: update-application
- description: Delete an application registration.
  hints:
    destructive: true
    idempotent: true
  name: delete-application
- description: List all service principals.
  hints:
    openWorld: true
    readOnly: true
  name: list-service-principals
- description: Create a new service principal.
  hints:
    readOnly: false
  name: create-service-principal
- description: Get service principal details.
  hints:
    readOnly: true
  name: get-service-principal
- description: Update service principal properties.
  hints:
    idempotent: true
    readOnly: false
  name: update-service-principal
- description: Delete a service principal.
  hints:
    destructive: true
    idempotent: true
  name: delete-service-principal
---
