---
description: Schema for a request in progress response returned by the server.
layout: schema
name: SuccessAcceptedResponse
properties_list:
- description: Message code returned by the server.
  name: code
  type: string
- description: Message returned by the server
  name: message
  type: string
- description: Opaque result ID used for checking for request completion through one or more subsequent completion check operations.
  name: resultHandler
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/common-success-accepted-response-schema.json
slug: common-success-accepted-response
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: SuccessAcceptedResponse
---
