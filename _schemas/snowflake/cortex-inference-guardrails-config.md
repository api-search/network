---
description: Guardrails configuration
layout: schema
name: GuardrailsConfig
properties_list:
- description: Controls whether guardrails are enabled
  name: enabled
  type: boolean
- description: The response when the guardrails model marks the completion as unsafe
  name: response_when_unsafe
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-inference-guardrails-config-schema.json
slug: cortex-inference-guardrails-config
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: GuardrailsConfig
---
