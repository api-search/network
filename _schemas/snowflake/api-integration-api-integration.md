---
description: A Snowflake API integration object.
layout: schema
name: ApiIntegration
properties_list:
- description: Name of the API integration.
  name: name
  type: string
- description: A comma-separated list of endpoints and resources that Snowflake can access.
  name: api_allowed_prefixes
  type: array
- description: A comma-separated list of endpoints and resources that are not allowed to be called from Snowflake.
  name: api_blocked_prefixes
  type: array
- description: Whether the API integration is enabled.
  name: enabled
  type: boolean
- description: Comment for the API integration.
  name: comment
  type: string
- description: Date and time when the API integration was created.
  name: created_on
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/api-integration-api-integration-schema.json
slug: api-integration-api-integration
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ApiIntegration
---
