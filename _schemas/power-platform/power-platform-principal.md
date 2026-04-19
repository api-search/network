---
description: Represents a principal (user or service principal) that performed an action.
layout: schema
name: Principal
properties_list:
- description: The unique identifier of the principal.
  name: id
  type: string
- description: The display name of the principal.
  name: displayName
  type: '[''string'', ''null'']'
- description: The type of principal.
  name: type
  type: string
- description: The tenant ID of the principal.
  name: tenantId
  type: '[''string'', ''null'']'
provider_name: Microsoft Power Platform APIs
provider_slug: power-platform
schema_file: json-schema/power-platform-principal-schema.json
slug: power-platform-principal
tags:
- Business Applications
- Copilot Studio
- Dataverse
- Low-Code
- Microsoft
- No-Code
- Power Pages
- Power Platform
title: Principal
---
