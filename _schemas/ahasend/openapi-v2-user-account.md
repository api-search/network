---
description: UserAccount schema from AhaSend API
layout: schema
name: UserAccount
properties_list:
- description: Unique identifier for the user account relationship
  name: id
  type: string
- description: When the relationship was created
  name: created_at
  type: string
- description: When the relationship was last updated
  name: updated_at
  type: string
- description: User ID
  name: user_id
  type: string
- description: Account ID
  name: account_id
  type: string
- description: User role in the account
  name: role
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-user-account-schema.json
slug: openapi-v2-user-account
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: UserAccount
---
