---
consumed_apis:
- workmail
description: Unified workflow for IT administrators and email operations teams to manage Amazon WorkMail organizations, users, groups, and mobile device access. Enables programmatic provisioning, deprovisioning, and governance of enterprise email infrastructure.
layout: capability
name: Amazon WorkMail Email Management
operations:
- description: List all WorkMail organizations.
  method: GET
  name: list-organizations
  path: /v1/organizations
- description: List users in an organization.
  method: GET
  name: list-users
  path: /v1/users
- description: Create a new email user.
  method: POST
  name: create-user
  path: /v1/users
- description: List email groups.
  method: GET
  name: list-groups
  path: /v1/groups
- description: List mobile device access rules.
  method: GET
  name: list-mobile-device-access-rules
  path: /v1/mobile-device-access
personas: []
provider_name: Amazon WorkMail
provider_slug: amazon-workmail
search_terms:
- IT Administrator
- Email Operations
- enterprise
- list email groups.
- create a new workmail user with mailbox.
- administration
- email
- create a new email user.
- calendar
- exchange
- list all workmail organizations.
- list users in an organization.
- enterprise email provisioning and management
- list organizations
- workmail organization management.
- list email distribution groups in an organization.
- list mobile device access control rules.
- it administration of email infrastructure
- list users
- mobile device access control.
- manages workmail infrastructure, user provisioning, and security policies.
- workflow for it administrators to manage workmail organizations, users, groups, and mobile device access policies.
- group management.
- business communication
- list groups
- handles day-to-day email user and group management.
- mobile device access control and compliance
- list users in a workmail organization.
- user provisioning and management.
- create user
- aws
- list mobile device access rules
- list mobile device access rules.
- list all amazon workmail organizations in the account.
slug: email-management
tags:
- AWS
- Email
- Calendar
- Business Communication
- Administration
tools:
- description: List all Amazon WorkMail organizations in the account.
  hints:
    openWorld: true
    readOnly: true
  name: list-organizations
- description: List users in a WorkMail organization.
  hints:
    openWorld: false
    readOnly: true
  name: list-users
- description: Create a new WorkMail user with mailbox.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-user
- description: List email distribution groups in an organization.
  hints:
    openWorld: false
    readOnly: true
  name: list-groups
- description: List mobile device access control rules.
  hints:
    openWorld: false
    readOnly: true
  name: list-mobile-device-access-rules
---
