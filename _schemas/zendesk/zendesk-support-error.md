---
description: An error response from the Zendesk API.
layout: schema
name: Error
properties_list:
- description: The error type identifier.
  name: error
  type: string
- description: A human-readable description of the error.
  name: description
  type: string
- description: Additional details about the error.
  name: details
  type: object
provider_name: Zendesk
provider_slug: zendesk
schema_file: json-schema/zendesk-support-error-schema.json
slug: zendesk-support-error
tags:
- Chat
- CRM
- Help Center
- Sell
- Support
- T1
- Talk
- Ticketing
- Tickets
title: Error
---
