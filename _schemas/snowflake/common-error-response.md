---
description: ''
layout: schema
name: ErrorResponse
properties_list:
- description: Error message returned by the server
  name: message
  type: string
- description: Error code.
  name: code
  type: string
- description: Error code, same as `code` above. This property has been deprecated and will be removed in a future release, but is temporarily supported for for short-term backward compatibility.
  name: error_code
  type: string
- description: Unique request ID.
  name: request_id
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/common-error-response-schema.json
slug: common-error-response
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ErrorResponse
---
