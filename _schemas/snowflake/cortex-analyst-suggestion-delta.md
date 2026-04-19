---
description: ''
layout: schema
name: SuggestionDelta
properties_list:
- description: The index of the suggestions array this delta object represents
  name: index
  type: integer
- description: The delta of a suggestion text, clients should concatenate all deltas for the same index
  name: suggestion_delta
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-analyst-suggestion-delta-schema.json
slug: cortex-analyst-suggestion-delta
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: SuggestionDelta
---
