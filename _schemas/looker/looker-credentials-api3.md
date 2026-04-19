---
description: API3 client credentials for a user
layout: schema
name: CredentialsApi3
properties_list:
- description: Unique identifier
  name: id
  type: integer
- description: API3 client ID
  name: client_id
  type: string
- description: Timestamp when these credentials were created
  name: created_at
  type: string
- description: Whether these credentials are disabled
  name: is_disabled
  type: boolean
- description: Credential type
  name: type
  type: string
- description: Relative URL
  name: url
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-credentials-api3-schema.json
slug: looker-credentials-api3
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: CredentialsApi3
---
