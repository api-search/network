---
description: ''
layout: schema
name: GitHook
properties_list:
- description: Whether to allow any Snowflake secret when accessing the Git repository. This setting is ignored if allowed_authentication_secrets is present.
  name: allow_any_secret
  type: boolean
- description: A comma-separated list of fully-qualified Snowflake secret names that UDF or procedure handler code can use when accessing the Git repository.
  name: allowed_authentication_secrets
  type: array
- description: A comma-separated list of Snowflake security integration names that UDF or procedure handler code can use when accessing the Git repository. If empty, allow no integrations.
  name: allowed_api_authentication_integrations
  type: array
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/api-integration-git-hook-schema.json
slug: api-integration-git-hook
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: GitHook
---
