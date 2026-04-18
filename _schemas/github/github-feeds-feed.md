---
description: Feed
layout: schema
name: feed
properties_list:
- description: ''
  name: timeline_url
  type: string
- description: ''
  name: user_url
  type: string
- description: ''
  name: current_user_public_url
  type: string
- description: ''
  name: current_user_url
  type: string
- description: ''
  name: current_user_actor_url
  type: string
- description: ''
  name: current_user_organization_url
  type: string
- description: ''
  name: current_user_organization_urls
  type: array
- description: ''
  name: security_advisories_url
  type: string
- description: A feed of discussions for a given repository.
  name: repository_discussions_url
  type: string
- description: A feed of discussions for a given repository and category.
  name: repository_discussions_category_url
  type: string
- description: ''
  name: _links
  type: object
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-feeds-feed-schema.json
slug: github-feeds-feed
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: feed
---
