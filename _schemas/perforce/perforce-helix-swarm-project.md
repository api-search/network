---
description: A project in Helix Swarm, grouping branches, members, and review settings.
layout: schema
name: Project
properties_list:
- description: The project identifier.
  name: id
  type: string
- description: The project display name.
  name: name
  type: string
- description: The project description.
  name: description
  type: string
- description: List of project member usernames.
  name: members
  type: array
- description: List of project owner usernames.
  name: owners
  type: array
- description: List of associated Perforce groups.
  name: subgroups
  type: array
- description: Branch definitions for the project.
  name: branches
  type: array
- description: Whether the project has been deleted.
  name: deleted
  type: boolean
- description: Deploy configuration for the project.
  name: deploy
  type: object
- description: Email notification settings.
  name: emailFlags
  type: object
- description: A Perforce jobview expression for the project.
  name: jobview
  type: string
- description: Minimum number of up votes required for approval.
  name: minimumUpVotes
  type: integer
- description: Whether the project is private.
  name: private
  type: boolean
- description: Whether to retain default reviewers on review updates.
  name: retainDefaultReviewers
  type: boolean
- description: Test configuration for the project.
  name: tests
  type: object
- description: The workflow identifier associated with the project.
  name: workflow
  type: string
- description: Default settings for the project.
  name: defaults
  type: object
- description: The project readme content.
  name: readme
  type: string
provider_name: Perforce
provider_slug: perforce
schema_file: json-schema/perforce-helix-swarm-project-schema.json
slug: perforce-helix-swarm-project
tags: []
title: Project
---
