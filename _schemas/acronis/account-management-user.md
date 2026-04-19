---
description: Acronis platform user account
layout: schema
name: User
properties_list:
- description: User unique identifier
  name: id
  type: string
- description: Username/login for the user
  name: login
  type: string
- description: User email address
  name: email
  type: string
- description: ''
  name: firstname
  type: string
- description: ''
  name: lastname
  type: string
- description: Whether the user account is active
  name: enabled
  type: boolean
- description: Tenant the user belongs to
  name: tenant_id
  type: string
- description: ''
  name: created_at
  type: string
provider_name: Acronis
provider_slug: acronis
schema_file: json-schema/account-management-user-schema.json
slug: account-management-user
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
title: User
---
