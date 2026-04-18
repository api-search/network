---
description: A GitHub organization that groups users and repositories together under shared ownership, permissions, and policies.
layout: schema
name: GitHub Organization
properties_list:
- description: The login name of the organization.
  name: login
  type: string
- description: The unique identifier of the organization.
  name: id
  type: integer
- description: The GraphQL node ID for the organization.
  name: node_id
  type: string
- description: The API URL for the organization.
  name: url
  type: string
- description: The URL of the organization on GitHub.
  name: html_url
  type: string
- description: API URL for the organization's repositories.
  name: repos_url
  type: string
- description: API URL for the organization's events.
  name: events_url
  type: string
- description: API URL for the organization's webhooks.
  name: hooks_url
  type: string
- description: API URL for the organization's issues.
  name: issues_url
  type: string
- description: API URL template for the organization's members.
  name: members_url
  type: string
- description: API URL template for the organization's public members.
  name: public_members_url
  type: string
- description: URL to the organization's avatar image.
  name: avatar_url
  type: string
- description: A description of the organization.
  name: description
  type:
  - string
  - 'null'
- description: The display name of the organization.
  name: name
  type:
  - string
  - 'null'
- description: The company name associated with the organization.
  name: company
  type:
  - string
  - 'null'
- description: The organization's blog or website URL.
  name: blog
  type:
  - string
  - 'null'
- description: The organization's location.
  name: location
  type:
  - string
  - 'null'
- description: The organization's publicly visible email address.
  name: email
  type:
  - string
  - 'null'
- description: The organization's Twitter/X username.
  name: twitter_username
  type:
  - string
  - 'null'
- description: Whether the organization has verified its domain.
  name: is_verified
  type: boolean
- description: Whether the organization has projects enabled.
  name: has_organization_projects
  type: boolean
- description: Whether repositories can have projects enabled.
  name: has_repository_projects
  type: boolean
- description: The number of public repositories.
  name: public_repos
  type: integer
- description: The number of public gists.
  name: public_gists
  type: integer
- description: The number of followers.
  name: followers
  type: integer
- description: The number of users the organization is following.
  name: following
  type: integer
- description: The account type.
  name: type
  type: string
- description: The date and time the organization was created.
  name: created_at
  type: string
- description: The date and time the organization was last updated.
  name: updated_at
  type: string
- description: ''
  name: plan
  type: object
- description: The default permission level for new repositories.
  name: default_repository_permission
  type: string
- description: Whether members can create repositories.
  name: members_can_create_repositories
  type: boolean
- description: Whether members can create public repositories.
  name: members_can_create_public_repositories
  type: boolean
- description: Whether members can create private repositories.
  name: members_can_create_private_repositories
  type: boolean
- description: Whether two-factor authentication is required for members.
  name: two_factor_requirement_enabled
  type: boolean
- description: The total number of private repositories.
  name: total_private_repos
  type: integer
- description: The number of private repositories owned by the organization.
  name: owned_private_repos
  type: integer
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-organization-schema.json
slug: github-organization
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: GitHub Organization
---
