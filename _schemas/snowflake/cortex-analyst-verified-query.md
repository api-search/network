---
description: VerifiedQuery represents a (question, sql) pair that has been manually verified (e.g. by an analyst) to be correct.
layout: schema
name: VerifiedQuery
properties_list:
- description: A name for this verified query. Mainly used for display purposes.
  name: name
  type: string
- description: The question being answered.
  name: question
  type: string
- description: The correct SQL query for answering the question.
  name: sql
  type: string
- description: Timestamp at which the query was last verified - measures in seconds since epoch, in UTC.
  name: verified_at
  type: integer
- description: Name of the person who verified this query.
  name: verified_by
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-analyst-verified-query-schema.json
slug: cortex-analyst-verified-query
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: VerifiedQuery
---
