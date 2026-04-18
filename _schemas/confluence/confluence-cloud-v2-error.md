---
description: Error response from the Confluence API.
layout: schema
name: Error
properties_list:
- description: The HTTP status code.
  name: statusCode
  type: integer
- description: Details about the error.
  name: data
  type: object
- description: A human-readable error message.
  name: message
  type: string
provider_name: Confluence
provider_slug: confluence
schema_file: json-schema/confluence-cloud-v2-error-schema.json
slug: confluence-cloud-v2-error
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
title: Error
---
