---
consumed_apis:
- atlassian-admin
description: Platform administration workflow combining Admin Organizations, User Management, User Provisioning, and Jira Configuration APIs for IT administrators to manage users, groups, organizations, and platform settings.
layout: capability
name: Atlassian Platform Administration
operations:
- description: List Atlassian organizations
  method: GET
  name: list-organizations
  path: /v1/organizations
- description: List organization users
  method: GET
  name: list-users
  path: /v1/users
- description: List organization groups
  method: GET
  name: list-groups
  path: /v1/groups
- description: List organization domains
  method: GET
  name: list-domains
  path: /v1/domains
- description: List organization policies
  method: GET
  name: list-policies
  path: /v1/policies
- description: List audit events
  method: GET
  name: list-events
  path: /v1/events
personas: []
provider_name: Atlassian
provider_slug: atlassian
search_terms:
- list organization audit events
- list policies
- list all atlassian organizations
- list groups
- list domains in an organization
- list organization domains
- group management
- collaboration
- list organization groups
- audit events
- list organizations
- user management
- platform
- list users in an organization
- atlassian
- code
- get organization
- software development
- administration
- list users
- identity
- list events
- policy management
- list organization users
- domain management
- productivity
- list audit events
- list groups in an organization
- list atlassian organizations
- list organization policies
- get organization details
- organization management
- list domains
slug: platform-administration
tags:
- Administration
- Atlassian
- Identity
- Platform
tools:
- description: List all Atlassian organizations
  hints:
    openWorld: true
    readOnly: true
  name: list-organizations
- description: Get organization details
  hints:
    readOnly: true
  name: get-organization
- description: List users in an organization
  hints:
    readOnly: true
  name: list-users
- description: List groups in an organization
  hints:
    readOnly: true
  name: list-groups
- description: List domains in an organization
  hints:
    readOnly: true
  name: list-domains
- description: List organization policies
  hints:
    readOnly: true
  name: list-policies
- description: List organization audit events
  hints:
    readOnly: true
  name: list-events
---
