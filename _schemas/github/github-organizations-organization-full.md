---
description: Organization Full
layout: schema
name: organization-full
properties_list:
- description: ''
  name: login
  type: string
- description: ''
  name: id
  type: integer
- description: ''
  name: node_id
  type: string
- description: ''
  name: url
  type: string
- description: ''
  name: repos_url
  type: string
- description: ''
  name: events_url
  type: string
- description: ''
  name: hooks_url
  type: string
- description: ''
  name: issues_url
  type: string
- description: ''
  name: members_url
  type: string
- description: ''
  name: public_members_url
  type: string
- description: ''
  name: avatar_url
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: company
  type: string
- description: ''
  name: blog
  type: string
- description: ''
  name: location
  type: string
- description: ''
  name: email
  type: string
- description: ''
  name: twitter_username
  type: string
- description: ''
  name: is_verified
  type: boolean
- description: ''
  name: has_organization_projects
  type: boolean
- description: ''
  name: has_repository_projects
  type: boolean
- description: ''
  name: public_repos
  type: integer
- description: ''
  name: public_gists
  type: integer
- description: ''
  name: followers
  type: integer
- description: ''
  name: following
  type: integer
- description: ''
  name: html_url
  type: string
- description: ''
  name: type
  type: string
- description: ''
  name: total_private_repos
  type: integer
- description: ''
  name: owned_private_repos
  type: integer
- description: ''
  name: private_gists
  type: integer
- description: ''
  name: disk_usage
  type: integer
- description: ''
  name: collaborators
  type: integer
- description: ''
  name: billing_email
  type: string
- description: ''
  name: plan
  type: object
- description: ''
  name: default_repository_permission
  type: string
- description: ''
  name: members_can_create_repositories
  type: boolean
- description: ''
  name: two_factor_requirement_enabled
  type: boolean
- description: ''
  name: members_allowed_repository_creation_type
  type: string
- description: ''
  name: members_can_create_public_repositories
  type: boolean
- description: ''
  name: members_can_create_private_repositories
  type: boolean
- description: ''
  name: members_can_create_internal_repositories
  type: boolean
- description: ''
  name: members_can_create_pages
  type: boolean
- description: ''
  name: members_can_create_public_pages
  type: boolean
- description: ''
  name: members_can_create_private_pages
  type: boolean
- description: ''
  name: members_can_fork_private_repositories
  type: boolean
- description: ''
  name: web_commit_signoff_required
  type: boolean
- description: Whether GitHub Advanced Security is enabled for new repositories and repositories transferred to this organization. This field is only visible to organization owners or members of a team with the secu
  name: advanced_security_enabled_for_new_repositories
  type: boolean
- description: Whether GitHub Advanced Security is automatically enabled for new repositories and repositories transferred to this organization. This field is only visible to organization owners or members of a team
  name: dependabot_alerts_enabled_for_new_repositories
  type: boolean
- description: 'Whether dependabot security updates are automatically enabled for new repositories and repositories transferred to this organization. This field is only visible to organization owners or members of a '
  name: dependabot_security_updates_enabled_for_new_repositories
  type: boolean
- description: Whether dependency graph is automatically enabled for new repositories and repositories transferred to this organization. This field is only visible to organization owners or members of a team with th
  name: dependency_graph_enabled_for_new_repositories
  type: boolean
- description: Whether secret scanning is automatically enabled for new repositories and repositories transferred to this organization. This field is only visible to organization owners or members of a team with the
  name: secret_scanning_enabled_for_new_repositories
  type: boolean
- description: Whether secret scanning push protection is automatically enabled for new repositories and repositories transferred to this organization. This field is only visible to organization owners or members of
  name: secret_scanning_push_protection_enabled_for_new_repositories
  type: boolean
- description: Whether a custom link is shown to contributors who are blocked from pushing a secret by push protection.
  name: secret_scanning_push_protection_custom_link_enabled
  type: boolean
- description: An optional URL string to display to contributors who are blocked from pushing a secret.
  name: secret_scanning_push_protection_custom_link
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-organizations-organization-full-schema.json
slug: github-organizations-organization-full
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: organization-full
---
