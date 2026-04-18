---
description: ''
layout: schema
name: UserInfo
properties_list:
- description: Account type (user or organization)
  name: type
  type: string
- description: ''
  name: id
  type: string
- description: Username
  name: name
  type: string
- description: Full display name
  name: fullname
  type: string
- description: ''
  name: email
  type: string
- description: ''
  name: emailVerified
  type: boolean
- description: Subscription plan
  name: plan
  type: string
- description: ''
  name: canPay
  type: boolean
- description: ''
  name: avatarUrl
  type: string
- description: ''
  name: orgs
  type: array
- description: ''
  name: auth
  type: object
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-hub-user-info-schema.json
slug: hugging-face-hub-user-info
tags: []
title: UserInfo
---
