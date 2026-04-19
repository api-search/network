---
description: Email/password credentials for a user
layout: schema
name: CredentialsEmail
properties_list:
- description: Email address
  name: email
  type: string
- description: Whether these credentials are disabled
  name: is_disabled
  type: boolean
- description: Timestamp of last login with these credentials
  name: logged_in_at
  type: string
- description: Timestamp when these credentials were created
  name: created_at
  type: string
- description: Relative URL
  name: url
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-credentials-email-schema.json
slug: looker-credentials-email
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: CredentialsEmail
---
