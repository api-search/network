---
consumed_apis:
- graph-identity
description: Unified identity and access management workflow combining user lifecycle, group management, application registration, and service principal operations. Used by IT administrators and identity engineers to manage enterprise identity infrastructure.
layout: capability
name: Azure AD Identity and Access Management
operations:
- description: List directory users.
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
  path: /v1/users/{userId}
- description: Update user properties.
  method: PATCH
  name: update-user
  path: /v1/users/{userId}
- description: Delete a user.
  method: DELETE
  name: delete-user
  path: /v1/users/{userId}
- description: List groups.
  method: GET
  name: list-groups
  path: /v1/groups
- description: Create a group.
  method: POST
  name: create-group
  path: /v1/groups
- description: Get group details.
  method: GET
  name: get-group
  path: /v1/groups/{groupId}
- description: List group members.
  method: GET
  name: list-group-members
  path: /v1/groups/{groupId}/members
- description: Add a group member.
  method: POST
  name: add-group-member
  path: /v1/groups/{groupId}/members
- description: List app registrations.
  method: GET
  name: list-applications
  path: /v1/applications
- description: List service principals.
  method: GET
  name: list-service-principals
  path: /v1/service-principals
personas: []
provider_name: Azure Active Directory
provider_slug: azure-active-directory
search_terms:
- microsoft
- update user properties.
- access management
- register a new application in azure ad.
- list azure ad users with optional filtering.
- delete an azure ad group.
- add a member to an azure ad group.
- list groups and roles a user belongs to.
- list groups.
- zero trust
- get group details.
- microsoft entra
- get azure ad user details by id or upn.
- list group members
- single group operations.
- add a group member.
- delete group
- list members of an azure ad group.
- oauth
- get a service principal by id.
- create user
- create a new user.
- group membership.
- azure active directory
- update azure ad user properties.
- list users
- list service principals
- identity
- list azure ad service principals.
- list applications
- service principal management.
- create a new azure ad group.
- openid connect
- list app registrations.
- authorization
- delete a user.
- group management.
- get user details.
- list service principals.
- get service principal
- create application
- get user
- get an application registration by id.
- create a group.
- list groups
- list user memberships
- list group members.
- list azure ad application registrations.
- list directory users.
- scim
- app registration management.
- create a new azure ad user account.
- get azure ad group details.
- create group
- user lifecycle management.
- single user operations.
- get group
- list azure ad groups with optional filtering.
- get application
- saml
- authentication
- single sign-on
- delete an azure ad user account.
- delete user
- update user
- add group member
slug: identity-and-access
tags:
- Microsoft Entra
- Identity
- Access Management
- Azure Active Directory
tools:
- description: List Azure AD users with optional filtering.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-users
- description: Create a new Azure AD user account.
  hints:
    readOnly: false
  name: create-user
- description: Get Azure AD user details by ID or UPN.
  hints:
    idempotent: true
    readOnly: true
  name: get-user
- description: Update Azure AD user properties.
  hints:
    idempotent: true
    readOnly: false
  name: update-user
- description: Delete an Azure AD user account.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-user
- description: List groups and roles a user belongs to.
  hints:
    idempotent: true
    readOnly: true
  name: list-user-memberships
- description: List Azure AD groups with optional filtering.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-groups
- description: Create a new Azure AD group.
  hints:
    readOnly: false
  name: create-group
- description: Get Azure AD group details.
  hints:
    idempotent: true
    readOnly: true
  name: get-group
- description: Delete an Azure AD group.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-group
- description: List members of an Azure AD group.
  hints:
    idempotent: true
    readOnly: true
  name: list-group-members
- description: Add a member to an Azure AD group.
  hints:
    readOnly: false
  name: add-group-member
- description: List Azure AD application registrations.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-applications
- description: Register a new application in Azure AD.
  hints:
    readOnly: false
  name: create-application
- description: Get an application registration by ID.
  hints:
    idempotent: true
    readOnly: true
  name: get-application
- description: List Azure AD service principals.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-service-principals
- description: Get a service principal by ID.
  hints:
    idempotent: true
    readOnly: true
  name: get-service-principal
---
