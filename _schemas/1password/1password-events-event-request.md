---
description: The request body for fetching events. Must include either a cursor string from a previous response to continue pagination, or a ResetCursor object to start fetching from a specific time.
layout: schema
name: EventRequest
properties_list:
- description: The maximum number of event records to return per page.
  name: limit
  type: integer
- description: A cursor from a previous response to continue fetching events from where the last request left off.
  name: cursor
  type: string
- description: An ISO 8601 timestamp to begin fetching events from a specific time. Used to create a new cursor starting from this point.
  name: start_time
  type: string
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-events-event-request-schema.json
slug: 1password-events-event-request
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: EventRequest
---
