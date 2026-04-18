---
description: Represents a user's permission settings for a Google Tag Manager Account and its Containers.
layout: schema
name: UserPermission
properties_list:
- description: GTM UserPermission's API relative path.
  name: path
  type: string
- description: The Account ID uniquely identifies the GTM Account.
  name: accountId
  type: string
- description: User's email address.
  name: emailAddress
  type: string
- description: GTM Container access permissions.
  name: containerAccess
  type: array
provider_name: Google Tag Manager
provider_slug: google-tag-manager
schema_file: json-schema/google-tag-manager-v2-user-permission-schema.json
slug: google-tag-manager-v2-user-permission
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
title: UserPermission
---
