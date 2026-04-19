---
description: The response containing sign-in attempt records and a cursor for pagination.
layout: schema
name: SignInAttemptResponse
properties_list:
- description: A cursor to use in the next request to continue fetching events.
  name: cursor
  type: string
- description: Whether there are more events available to fetch using the cursor.
  name: has_more
  type: boolean
- description: The list of sign-in attempt records.
  name: items
  type: array
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-events-sign-in-attempt-response-schema.json
slug: 1password-events-sign-in-attempt-response
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: SignInAttemptResponse
---
