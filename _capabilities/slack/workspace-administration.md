---
consumed_apis:
- slack-admin
- slack-team
- slack-users
- slack-usergroups
- slack-migration
- slack-auth
- slack-oauth
- slack-openid
- slack-dnd
description: Unified workflow for workspace administration including admin controls, team settings, user management, user groups, authentication, and enterprise migration. Used by workspace administrators and IT teams.
layout: capability
name: Slack Workspace Administration
operations:
- description: List admin resources.
  method: GET
  name: list-admin
  path: /v1/admin
- description: List users.
  method: GET
  name: list-users
  path: /v1/users
- description: List user groups.
  method: GET
  name: list-groups
  path: /v1/user-groups
- description: Get team info.
  method: GET
  name: get-team
  path: /v1/team
personas: []
provider_name: Slack
provider_slug: slack
search_terms:
- migrate ids
- list admin
- list admin resources.
- list user groups
- test authentication.
- bots
- list groups
- list user groups.
- get workspace information.
- chat
- team information.
- team communication
- get do not disturb status.
- collaboration
- admin controls.
- list users.
- get team info.
- user management
- slack
- administration
- list users
- get team info
- messaging
- t1
- auth test
- get dnd status
- admin controls
- list workspace users.
- productivity
- enterprise
- user management.
- get team
- user group management.
- migrate enterprise ids.
- access admin controls.
slug: workspace-administration
tags:
- Slack
- Administration
- User Management
- Enterprise
tools:
- description: Access admin controls.
  hints:
    readOnly: true
  name: admin-controls
- description: Get workspace information.
  hints:
    readOnly: true
  name: get-team-info
- description: List workspace users.
  hints:
    readOnly: true
  name: list-users
- description: List user groups.
  hints:
    readOnly: true
  name: list-user-groups
- description: Migrate enterprise IDs.
  hints:
    readOnly: true
  name: migrate-ids
- description: Test authentication.
  hints:
    readOnly: true
  name: auth-test
- description: Get Do Not Disturb status.
  hints:
    readOnly: true
  name: get-dnd-status
---
