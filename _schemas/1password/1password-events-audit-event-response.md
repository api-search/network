---
description: The response containing audit event records and a cursor for pagination.
layout: schema
name: AuditEventResponse
properties_list:
- description: A cursor to use in the next request to continue fetching events.
  name: cursor
  type: string
- description: Whether there are more events available to fetch using the cursor.
  name: has_more
  type: boolean
- description: The list of audit event records.
  name: items
  type: array
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-events-audit-event-response-schema.json
slug: 1password-events-audit-event-response
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: AuditEventResponse
---
