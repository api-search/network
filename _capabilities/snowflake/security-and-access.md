---
consumed_apis:
- snowflake-user
- snowflake-role
- snowflake-grant
- snowflake-database-role
- snowflake-network-policy
- snowflake-account
- snowflake-managed-account
description: Unified workflow for managing users, roles, grants, database roles, network policies, and account administration. Used by Platform Administrators and Security Engineers to govern access control and security posture.
layout: capability
name: Snowflake Security and Access
operations:
- description: List users
  method: GET
  name: list-users
  path: /v1/users
- description: Create a user
  method: POST
  name: create-user
  path: /v1/users
- description: List roles
  method: GET
  name: list-roles
  path: /v1/roles
- description: Create a role
  method: POST
  name: create-role
  path: /v1/roles
- description: Grant a privilege
  method: POST
  name: grant-privilege
  path: /v1/grants
- description: List grants
  method: GET
  name: list-grants
  path: /v1/grants
- description: List network policies
  method: GET
  name: list-network-policies
  path: /v1/network-policies
- description: Create a network policy
  method: POST
  name: create-network-policy
  path: /v1/network-policies
- description: List accounts
  method: GET
  name: list-accounts
  path: /v1/accounts
personas: []
provider_name: Snowflake
provider_slug: snowflake
search_terms:
- list all roles
- list all users
- list grants to a role
- data sharing
- delete a user
- data lakes
- administration
- list network policies
- list roles
- list managed accounts
- create a network policy
- fetch user
- list users
- grant management
- security
- access control
- network policy management
- grant a privilege to a role
- list grants
- data warehousing
- list accounts
- role management
- delete user
- revoke privilege
- create a user
- revoke a privilege from a role
- sql
- snowflake
- user management
- create a new role
- account management
- fetch user details
- grant a privilege
- create a role
- create network policy
- create user
- create role
- create database role
- create a database role
- database
- list database roles
- grant privilege
- create a new user
slug: security-and-access
tags:
- Snowflake
- Security
- Access Control
- Administration
tools:
- description: List all users
  hints:
    readOnly: true
  name: list-users
- description: Create a new user
  hints:
    readOnly: false
  name: create-user
- description: Fetch user details
  hints:
    readOnly: true
  name: fetch-user
- description: Delete a user
  hints:
    destructive: true
  name: delete-user
- description: List all roles
  hints:
    readOnly: true
  name: list-roles
- description: Create a new role
  hints:
    readOnly: false
  name: create-role
- description: Grant a privilege to a role
  hints:
    readOnly: false
  name: grant-privilege
- description: Revoke a privilege from a role
  hints:
    readOnly: false
  name: revoke-privilege
- description: List grants to a role
  hints:
    readOnly: true
  name: list-grants
- description: List database roles
  hints:
    readOnly: true
  name: list-database-roles
- description: Create a database role
  hints:
    readOnly: false
  name: create-database-role
- description: List network policies
  hints:
    readOnly: true
  name: list-network-policies
- description: Create a network policy
  hints:
    readOnly: false
  name: create-network-policy
- description: List accounts
  hints:
    readOnly: true
  name: list-accounts
- description: List managed accounts
  hints:
    readOnly: true
  name: list-managed-accounts
---
