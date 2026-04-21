---
consumed_apis:
- pluralsight-user-management
- pluralsight-teams
- pluralsight-licensing-rest
- pluralsight-plan-info
- pluralsight-flow-users
- pluralsight-flow-teams
- pluralsight-flow-integrations
- pluralsight-flow-repos
description: Unified workflow for platform administrators to manage users, teams, licensing, plan configuration, and Flow workspace settings. Combines user management, teams, licensing, plan info, Flow users, Flow teams, Flow integrations, and Flow repos APIs.
layout: capability
name: Pluralsight User And Team Administration
operations:
- description: Query and manage users via GraphQL
  method: POST
  name: manage-users
  path: /v1/users
- description: Query and manage teams via GraphQL
  method: POST
  name: manage-teams
  path: /v1/teams
- description: List pending user invitations
  method: GET
  name: list-invitations
  path: /v1/invitations
- description: Create a new user invitation
  method: POST
  name: create-invitation
  path: /v1/invitations
- description: List users in the plan
  method: GET
  name: list-license-users
  path: /v1/license-users
- description: List teams in the plan
  method: GET
  name: list-license-teams
  path: /v1/license-teams
- description: Retrieve account and plan details
  method: POST
  name: query-plan-info
  path: /v1/plan-info
- description: List Flow workspace users
  method: GET
  name: list-flow-users
  path: /v1/flow-users
- description: Update Flow user accounts
  method: PUT
  name: update-flow-users
  path: /v1/flow-users
- description: List Flow engineering teams
  method: GET
  name: list-flow-teams
  path: /v1/flow-teams
- description: List Flow integrations and connection status
  method: GET
  name: list-integrations
  path: /v1/integrations
- description: Retrieve repository data and metadata
  method: GET
  name: get-repos
  path: /v1/repositories
personas: []
provider_name: Pluralsight
provider_slug: pluralsight
search_terms:
- flow engineering team management
- manage teams
- query and manage teams including creating teams, managing membership, assigning managers, and configuring team permissions.
- list flow integrations and check connection status with external tools and services.
- skills assessment
- technology
- get repos
- list license teams
- update flow user accounts
- send a new user invitation. deprecated - migrate to graphql user management api.
- courses
- list teams in the plan. deprecated - migrate to graphql teams api.
- list flow integrations and connection status
- list flow workspace users
- engineering metrics
- user management
- retrieve account and plan details including subscription tier and configuration.
- account and plan details including subscription tier
- query and manage users via graphql
- team management including creating teams, managing membership, and permissions
- list invitations
- retrieve repository data and metadata across connected source control systems.
- user management including listing, inviting, editing, and removing users
- list flow teams
- list pending user invitations
- licensing
- query plan info
- create a new user invitation
- list users in the plan. deprecated - migrate to graphql user management api.
- list users in the plan
- platform administration
- list teams in the plan
- list pending user invitations. deprecated - migrate to graphql user management api.
- list flow users
- pluralsight
- video training
- create invitation
- flow workspace user management
- team administration
- list flow users in the workspace.
- learning
- list flow engineering teams and team membership data.
- manage users
- query and manage users including listing users, inviting members, editing user details, removing users, and canceling invitations.
- plan team listing (legacy rest, deprecated)
- list integrations
- update flow users
- plan user listing (legacy rest, deprecated)
- list license users
- list flow engineering teams
- education
- query and manage teams via graphql
- flow integration management and connection status
- user invitation management (legacy rest, deprecated)
- connected repository data and metadata
- update, merge, hide, or perform bulk operations on flow user accounts.
- retrieve repository data and metadata
- retrieve account and plan details
slug: user-and-team-administration
tags:
- Pluralsight
- User Management
- Team Administration
- Platform Administration
- Licensing
tools:
- description: Query and manage users including listing users, inviting members, editing user details, removing users, and canceling invitations.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: manage-users
- description: Query and manage teams including creating teams, managing membership, assigning managers, and configuring team permissions.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: manage-teams
- description: List pending user invitations. Deprecated - migrate to GraphQL User Management API.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-invitations
- description: Send a new user invitation. Deprecated - migrate to GraphQL User Management API.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-invitation
- description: List users in the plan. Deprecated - migrate to GraphQL User Management API.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-license-users
- description: List teams in the plan. Deprecated - migrate to GraphQL Teams API.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-license-teams
- description: Retrieve account and plan details including subscription tier and configuration.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-plan-info
- description: List Flow users in the workspace.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-flow-users
- description: Update, merge, hide, or perform bulk operations on Flow user accounts.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-flow-users
- description: List Flow engineering teams and team membership data.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-flow-teams
- description: List Flow integrations and check connection status with external tools and services.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-integrations
- description: Retrieve repository data and metadata across connected source control systems.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-repos
---
