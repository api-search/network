---
description: ''
layout: schema
name: OAuth
properties_list:
- description: The client ID of the OAuth2 credential associated with the Polaris service connection.
  name: oauth_client_id
  type: string
- description: The secret for the OAuth2 credential associated with the Polaris service connection.
  name: oauth_client_secret
  type: string
- description: The scope of the OAuth token. Only one scope is included in the Iceberg REST API specification, but catalogs can support more than one scope in their implementation.
  name: oauth_allowed_scopes
  type: array
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/catalog-integration-o-auth-schema.json
slug: catalog-integration-o-auth
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: OAuth
---
