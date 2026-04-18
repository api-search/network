---
description: Schema for a Hugging Face user account including profile information, organizations, and subscription details.
layout: schema
name: Hugging Face User
properties_list:
- description: Account type
  name: type
  type: string
- description: Unique user identifier
  name: id
  type: string
- description: Username (handle)
  name: name
  type: string
- description: Full display name
  name: fullname
  type: string
- description: Email address
  name: email
  type: string
- description: Whether the email has been verified
  name: emailVerified
  type: boolean
- description: Subscription plan
  name: plan
  type: string
- description: Whether the user is on a Pro plan
  name: isPro
  type: boolean
- description: Whether the user has a payment method configured
  name: canPay
  type: boolean
- description: URL to the user's avatar image
  name: avatarUrl
  type: string
- description: Organizations the user belongs to
  name: orgs
  type: array
- description: Authentication information
  name: auth
  type: object
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-user-schema.json
slug: hugging-face-user
tags: []
title: Hugging Face User
---
