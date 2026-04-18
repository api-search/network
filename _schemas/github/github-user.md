---
description: A GitHub user account representing an individual, organization, or bot that interacts with repositories, issues, and other resources.
layout: schema
name: GitHub User
properties_list:
- description: The username of the user.
  name: login
  type: string
- description: The unique identifier for the user.
  name: id
  type: integer
- description: The GraphQL node ID for the user.
  name: node_id
  type: string
- description: URL to the user's avatar image.
  name: avatar_url
  type: string
- description: The Gravatar ID associated with the user's email.
  name: gravatar_id
  type:
  - string
  - 'null'
- description: The API URL for the user.
  name: url
  type: string
- description: URL to the user's GitHub profile.
  name: html_url
  type: string
- description: API URL for the user's followers.
  name: followers_url
  type: string
- description: API URL template for who the user is following.
  name: following_url
  type: string
- description: API URL template for the user's gists.
  name: gists_url
  type: string
- description: API URL for the user's repositories.
  name: repos_url
  type: string
- description: The type of GitHub account.
  name: type
  type: string
- description: Whether the user is a GitHub site administrator.
  name: site_admin
  type: boolean
- description: The display name of the user.
  name: name
  type:
  - string
  - 'null'
- description: The company the user is associated with.
  name: company
  type:
  - string
  - 'null'
- description: The user's blog or website URL.
  name: blog
  type:
  - string
  - 'null'
- description: The user's location.
  name: location
  type:
  - string
  - 'null'
- description: The user's publicly visible email address.
  name: email
  type:
  - string
  - 'null'
- description: Whether the user has indicated they are available for hire.
  name: hireable
  type:
  - boolean
  - 'null'
- description: The user's biography.
  name: bio
  type:
  - string
  - 'null'
- description: The user's Twitter/X username.
  name: twitter_username
  type:
  - string
  - 'null'
- description: The number of public repositories the user owns.
  name: public_repos
  type: integer
- description: The number of public gists the user has created.
  name: public_gists
  type: integer
- description: The number of followers the user has.
  name: followers
  type: integer
- description: The number of users the user is following.
  name: following
  type: integer
- description: The date and time the user account was created.
  name: created_at
  type: string
- description: The date and time the user account was last updated.
  name: updated_at
  type: string
- description: Whether the user has two-factor authentication enabled. Only visible for the authenticated user.
  name: two_factor_authentication
  type: boolean
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-user-schema.json
slug: github-user
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: GitHub User
---
