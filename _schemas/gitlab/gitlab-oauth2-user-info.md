---
description: UserInfo from GitLab API
layout: schema
name: UserInfo
properties_list:
- description: Subject identifier. Unique to the user within the provider.
  name: sub
  type: string
- description: Full name of the user.
  name: name
  type: string
- description: The user's GitLab username.
  name: nickname
  type: string
- description: The user's email address. Requires the email scope.
  name: email
  type: string
- description: Whether the user's email address has been verified.
  name: email_verified
  type: boolean
- description: URL to the user's GitLab profile page.
  name: profile
  type: string
- description: URL to the user's avatar image.
  name: picture
  type: string
- description: List of groups the user belongs to.
  name: groups
  type: array
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-oauth2-user-info-schema.json
slug: gitlab-oauth2-user-info
tags:
- Code
- Platform
- Software Development
- Source Control
title: UserInfo
---
