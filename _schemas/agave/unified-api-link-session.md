---
description: An Agave Link session token.
layout: schema
name: LinkSession
properties_list:
- description: Token to initialize the Agave Link component for the user.
  name: link_token
  type: string
- description: The reference ID associated with this session.
  name: reference_id
  type: string
- description: Timestamp when the link token expires.
  name: expires_at
  type: string
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-link-session-schema.json
slug: unified-api-link-session
tags:
- Accounting
- Construction
- Integration
title: LinkSession
---
