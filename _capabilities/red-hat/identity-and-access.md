---
consumed_apis:
- keycloak-admin
description: Identity and access management workflow using Keycloak for managing realms, users, clients, roles, groups, and identity federation. Used by platform admins and security teams.
layout: capability
name: Red Hat Identity and Access
operations:
- description: List all realms.
  method: GET
  name: list-realms
  path: /v1/realms
- description: Get realm details.
  method: GET
  name: get-realm
  path: /v1/realms/{realm}
- description: List users.
  method: GET
  name: list-users
  path: /v1/realms/{realm}/users
- description: Create a user.
  method: POST
  name: create-user
  path: /v1/realms/{realm}/users
- description: List clients.
  method: GET
  name: list-clients
  path: /v1/realms/{realm}/clients
- description: List roles.
  method: GET
  name: list-roles
  path: /v1/realms/{realm}/roles
- description: List groups.
  method: GET
  name: list-groups
  path: /v1/realms/{realm}/groups
- description: List identity providers.
  method: GET
  name: list-identity-providers
  path: /v1/realms/{realm}/identity-providers
personas: []
provider_name: Red Hat
provider_slug: red-hat
search_terms:
- get realm configuration details.
- access management
- cloud
- list roles in a realm.
- list clients
- list groups.
- list realms
- delete a user from a realm.
- specific realm.
- open source
- list realm roles
- create user
- list client applications in a realm.
- containers
- list roles.
- list users
- list all keycloak realms.
- identity
- keycloak realms.
- list all realms.
- create a new user in a realm.
- list groups in a realm.
- linux
- list users in a realm.
- get realm
- keycloak
- get user details.
- register a new client application.
- red hat
- realm clients.
- get user
- realm users.
- list groups
- list identity providers.
- realm roles.
- enterprise
- list clients.
- get realm details.
- kubernetes
- terminate a user session.
- identity providers.
- create client
- list external identity providers.
- hybrid cloud
- realm groups.
- list roles
- list identity providers
- delete session
- create a user.
- delete user
- list users.
slug: identity-and-access
tags:
- Red Hat
- Keycloak
- Identity
- Access Management
tools:
- description: List all Keycloak realms.
  hints:
    readOnly: true
  name: list-realms
- description: Get realm configuration details.
  hints:
    idempotent: true
    readOnly: true
  name: get-realm
- description: List users in a realm.
  hints:
    readOnly: true
  name: list-users
- description: Create a new user in a realm.
  hints:
    readOnly: false
  name: create-user
- description: Get user details.
  hints:
    idempotent: true
    readOnly: true
  name: get-user
- description: Delete a user from a realm.
  hints:
    destructive: true
    readOnly: false
  name: delete-user
- description: List client applications in a realm.
  hints:
    readOnly: true
  name: list-clients
- description: Register a new client application.
  hints:
    readOnly: false
  name: create-client
- description: List roles in a realm.
  hints:
    readOnly: true
  name: list-realm-roles
- description: List groups in a realm.
  hints:
    readOnly: true
  name: list-groups
- description: List external identity providers.
  hints:
    readOnly: true
  name: list-identity-providers
- description: Terminate a user session.
  hints:
    destructive: true
    readOnly: false
  name: delete-session
---
