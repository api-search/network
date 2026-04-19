---
description: Request payload for creating an Agave Link session.
layout: schema
name: LinkSessionRequest
properties_list:
- description: Unique identifier for the user or entity linking their account.
  name: reference_id
  type: string
- description: URL to redirect the user to after completing the link flow.
  name: redirect_url
  type: string
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-link-session-request-schema.json
slug: unified-api-link-session-request
tags:
- Accounting
- Construction
- Integration
title: LinkSessionRequest
---
