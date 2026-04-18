---
description: Repository invitations let you manage who you collaborate with.
layout: schema
name: repository-subscription
properties_list:
- description: Determines if notifications should be received from this repository.
  name: subscribed
  type: boolean
- description: Determines if all notifications should be blocked from this repository.
  name: ignored
  type: boolean
- description: ''
  name: reason
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: url
  type: string
- description: ''
  name: repository_url
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-repo-subscription-api-repository-subscription-schema.json
slug: github-repo-subscription-api-repository-subscription
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: repository-subscription
---
