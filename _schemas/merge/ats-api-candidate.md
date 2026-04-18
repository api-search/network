---
description: A candidate in the recruiting pipeline from a connected ATS integration.
layout: schema
name: Candidate
properties_list:
- description: Unique Merge identifier.
  name: id
  type: string
- description: Third-party ID.
  name: remote_id
  type: string
- description: First name.
  name: first_name
  type: string
- description: Last name.
  name: last_name
  type: string
- description: Current or most recent company.
  name: company
  type: string
- description: Current or most recent title.
  name: title
  type: string
- description: Whether the candidate is private.
  name: is_private
  type: boolean
- description: Whether the candidate can be emailed.
  name: can_email
  type: boolean
- description: ''
  name: email_addresses
  type: array
- description: ''
  name: phone_numbers
  type: array
- description: ''
  name: tags
  type: array
- description: ''
  name: applications
  type: array
- description: ''
  name: attachments
  type: array
- description: ''
  name: remote_was_deleted
  type: boolean
- description: ''
  name: created_at
  type: string
- description: ''
  name: modified_at
  type: string
provider_name: Merge
provider_slug: merge
schema_file: json-schema/ats-api-candidate-schema.json
slug: ats-api-candidate
tags:
- Integrations
- Platform
- Unified API
title: Candidate
---
