---
description: A resource message representing a Google Analytics account.
layout: schema
name: Account
properties_list:
- description: Output only. Time when this account was originally created.
  name: createTime
  type: string
- description: Output only. Indicates whether this Account is soft-deleted or not. Deleted accounts are excluded from List results unless specifically requested.
  name: deleted
  type: boolean
- description: Required. Human-readable display name for this account.
  name: displayName
  type: string
- description: 'Output only. Resource name of this account. Format: accounts/{account} Example: "accounts/100"'
  name: name
  type: string
- description: Country of business. Must be a Unicode CLDR region code.
  name: regionCode
  type: string
- description: Output only. Time when account payload fields were last updated.
  name: updateTime
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/admin-api-account-schema.json
slug: admin-api-account
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: Account
---
