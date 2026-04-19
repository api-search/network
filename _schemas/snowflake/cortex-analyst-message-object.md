---
description: Represents a message within a chat.
layout: schema
name: MessageObject
properties_list:
- description: The entity that produced the message. One of `user` or `analyst`.
  name: role
  type: string
- description: The content of the message in array of text or SQL.
  name: content
  type: array
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-analyst-message-object-schema.json
slug: cortex-analyst-message-object
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: MessageObject
---
