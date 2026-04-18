---
description: User schema from Instagram Graph API
layout: schema
name: User
properties_list:
- description: App-scoped user ID.
  name: id
  type: string
- description: Instagram username.
  name: username
  type: string
- description: Profile name.
  name: name
  type: string
- description: Profile bio text.
  name: biography
  type: string
- description: Website URL from profile.
  name: website
  type: string
- description: Profile picture URL.
  name: profile_picture_url
  type: string
- description: Total followers.
  name: followers_count
  type: integer
- description: Total accounts followed.
  name: follows_count
  type: integer
- description: Total published media.
  name: media_count
  type: integer
provider_name: Instagram
provider_slug: instagram
schema_file: json-schema/instagram-graph-api-user-schema.json
slug: instagram-graph-api-user
tags:
- Instagram
- Meta
- Photos
- Social Media
- Videos
- Content Publishing
title: User
---
