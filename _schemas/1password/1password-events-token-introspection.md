---
description: Information about the bearer token used for authentication.
layout: schema
name: TokenIntrospection
properties_list:
- description: The unique identifier of the token.
  name: uuid
  type: string
- description: The features and permissions the token has access to.
  name: features
  type: array
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-events-token-introspection-schema.json
slug: 1password-events-token-introspection
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: TokenIntrospection
---
