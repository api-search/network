---
description: ''
layout: schema
name: Source
properties_list:
- description: Domain where the email was found.
  name: domain
  type: string
- description: URL of the source page.
  name: uri
  type: string
- description: Date the email was extracted from the source.
  name: extracted_on
  type: string
- description: Date the email was last seen at the source.
  name: last_seen_on
  type: string
- description: Whether the email is still present on the source page.
  name: still_on_page
  type: boolean
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-source-schema.json
slug: hunter-source
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: Source
---
