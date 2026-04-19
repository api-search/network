---
description: A GitHub user account.
layout: schema
name: SimpleUser
properties_list:
- description: The username of the user.
  name: login
  type: string
- description: The unique identifier of the user.
  name: id
  type: integer
- description: The GraphQL node ID of the user.
  name: node_id
  type: string
- description: URL to the user's avatar image.
  name: avatar_url
  type: string
- description: ''
  name: gravatar_id
  type: '[''string'', ''null'']'
- description: API URL for this user.
  name: url
  type: string
- description: URL to the user's GitHub profile.
  name: html_url
  type: string
- description: ''
  name: followers_url
  type: string
- description: ''
  name: following_url
  type: string
- description: ''
  name: gists_url
  type: string
- description: ''
  name: starred_url
  type: string
- description: ''
  name: subscriptions_url
  type: string
- description: ''
  name: organizations_url
  type: string
- description: ''
  name: repos_url
  type: string
- description: ''
  name: events_url
  type: string
- description: ''
  name: received_events_url
  type: string
- description: The type of account (User, Organization, Bot, etc.).
  name: type
  type: string
- description: Whether the user is a GitHub site administrator.
  name: site_admin
  type: boolean
provider_name: GitHub Copilot
provider_slug: github-copilot
schema_file: json-schema/github-copilot-simple-user-schema.json
slug: github-copilot-simple-user
tags:
- Agents
- AI
- Artificial Intelligence
- Code Generation
- Code Review
- Coding Agent
- Custom Instructions
- Developer Tools
- Extensions
- IDE
- Machine Learning
- MCP
- Metrics
- Model Context Protocol
- Productivity
title: SimpleUser
---
