---
description: Represents a single sign-in attempt to a 1Password account.
layout: schema
name: SignInAttempt
properties_list:
- description: The unique identifier for the sign-in attempt.
  name: uuid
  type: string
- description: The UUID of the session associated with the sign-in attempt.
  name: session_uuid
  type: string
- description: When the sign-in attempt occurred.
  name: timestamp
  type: string
- description: The category of the sign-in attempt.
  name: category
  type: string
- description: The type of sign-in method used.
  name: type
  type: string
- description: The two-letter ISO country code of the sign-in location.
  name: country
  type: string
- description: ''
  name: target_user
  type: object
- description: ''
  name: client
  type: object
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-events-sign-in-attempt-schema.json
slug: 1password-events-sign-in-attempt
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: SignInAttempt
---
