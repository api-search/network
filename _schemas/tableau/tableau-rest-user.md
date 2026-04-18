---
description: ''
layout: schema
name: User
properties_list:
- description: The unique identifier for the user.
  name: id
  type: string
- description: The name (user name) of the user.
  name: name
  type: string
- description: The display name of the user.
  name: fullName
  type: string
- description: The email address of the user.
  name: email
  type: string
- description: The role of the user on the site.
  name: siteRole
  type: string
- description: The authentication type for the user.
  name: authSetting
  type: string
- description: The date and time of the user's last login.
  name: lastLogin
  type: string
- description: The external authentication user ID.
  name: externalAuthUserId
  type: string
- description: The user's locale setting.
  name: locale
  type: string
- description: The user's language setting.
  name: language
  type: string
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-user-schema.json
slug: tableau-rest-user
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: User
---
