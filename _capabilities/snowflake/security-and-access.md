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
- create a database role
- revoke privilege
- fetch user details
- grant a privilege
- list grants to a role
- list network policies
- administration
- role management
- user management
- delete user
- account management
- create a new user
- list all roles
- sql
- list accounts
- grant privilege
- data sharing
- create database role
- data warehousing
- create network policy
- list users
- create a role
- security
- fetch user
- grant management
- delete a user
- access control
- network policy management
- data lakes
- list roles
- create user
- list grants
- create a new role
- grant a privilege to a role
- create a network policy
- database
- list database roles
- revoke a privilege from a role
- list managed accounts
- create a user
- list all users
- create role
- snowflake
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
