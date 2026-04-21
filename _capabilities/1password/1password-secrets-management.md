---
consumed_apis:
- 1password-connect
- 1password-events
- 1password-partnership
description: Unified secrets management and security monitoring workflow for 1Password. Combines the Connect Server API (vault and item management), Events API (audit log and sign-in monitoring), and Partnership API (account provisioning) into a single workflow for DevOps engineers, security operations teams, and 1Password partners.
layout: capability
name: 1Password Secrets Management
operations:
- description: List all accessible vaults.
  method: GET
  name: list-vaults
  path: /v1/vaults
- description: List all items in a vault.
  method: GET
  name: list-items
  path: /v1/vaults/{vaultId}/items
- description: Create a new item in a vault.
  method: POST
  name: create-item
  path: /v1/vaults/{vaultId}/items
- description: Retrieve sign-in attempt events for security monitoring.
  method: POST
  name: get-sign-in-events
  path: /v1/events/sign-ins
- description: Retrieve item usage events for compliance and auditing.
  method: POST
  name: get-item-usage-events
  path: /v1/events/item-usage
- description: Provision a new 1Password account for a partner customer.
  method: POST
  name: create-account
  path: /v1/accounts
personas: []
provider_name: 1Password
provider_slug: 1password
search_terms:
- password manager
- manage items within a vault.
- update an existing item in a 1password vault.
- retrieve 1password sign-in attempt events for security monitoring.
- event streaming for sign-ins, item usage, and audit trails
- get a specific item from a 1password vault.
- retrieve 1password audit events for compliance reporting.
- retrieve sign-in attempt events for security monitoring.
- list vaults
- passwords
- provisions and manages 1password accounts for partner customers
- retrieve item usage events for compliance and auditing.
- devops
- monitors sign-in events, item usage, and audit logs for security compliance
- list all items stored in a specific 1password vault.
- list vault items
- get sign in events
- update item
- manages secrets injection into applications and infrastructure using connect server
- list api activity
- vault and item crud operations via connect server
- retrieve sign-in audit events.
- create a new item in a 1password vault.
- provision partner account
- list all accessible vaults.
- security
- 1Password Partner
- delete item
- Security Operations
- create a new item in a vault.
- DevOps Engineer
- list items
- retrieve 1password item usage events for compliance auditing.
- manage partner billing accounts.
- create account
- list all items in a vault.
- list all 1password vaults accessible to the connect server.
- retrieve item usage audit events.
- unified secrets management, security monitoring, and account provisioning
- account provisioning for 1password partners
- create item
- get audit events
- delete an item from a 1password vault.
- provision a new 1password account for a partner customer.
- get item usage events
- get item
- secrets
- manage 1password vaults.
- list all api requests made to the 1password connect server.
slug: 1password-secrets-management
tags:
- Security
- Passwords
- Secrets
- DevOps
tools:
- description: List all 1Password vaults accessible to the Connect Server.
  hints:
    openWorld: false
    readOnly: true
  name: list-vaults
- description: List all items stored in a specific 1Password vault.
  hints:
    openWorld: false
    readOnly: true
  name: list-vault-items
- description: Get a specific item from a 1Password vault.
  hints:
    openWorld: false
    readOnly: true
  name: get-item
- description: Create a new item in a 1Password vault.
  hints:
    destructive: false
    readOnly: false
  name: create-item
- description: Update an existing item in a 1Password vault.
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: update-item
- description: Delete an item from a 1Password vault.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-item
- description: Retrieve 1Password sign-in attempt events for security monitoring.
  hints:
    openWorld: false
    readOnly: true
  name: get-sign-in-events
- description: Retrieve 1Password item usage events for compliance auditing.
  hints:
    openWorld: false
    readOnly: true
  name: get-item-usage-events
- description: Retrieve 1Password audit events for compliance reporting.
  hints:
    openWorld: false
    readOnly: true
  name: get-audit-events
- description: List all API requests made to the 1Password Connect Server.
  hints:
    openWorld: false
    readOnly: true
  name: list-api-activity
- description: Provision a new 1Password account for a partner customer.
  hints:
    destructive: false
    readOnly: false
  name: provision-partner-account
---
