---
description: ''
layout: schema
name: EmailFinderResult
properties_list:
- description: First name of the person.
  name: first_name
  type: string
- description: Last name of the person.
  name: last_name
  type: string
- description: The found email address.
  name: email
  type: string
- description: Confidence score for the email.
  name: score
  type: integer
- description: The domain name used for the search.
  name: domain
  type: string
- description: Job position or title.
  name: position
  type: '[''string'', ''null'']'
- description: Company name.
  name: company
  type: '[''string'', ''null'']'
- description: Twitter handle.
  name: twitter
  type: '[''string'', ''null'']'
- description: LinkedIn profile URL.
  name: linkedin_url
  type: '[''string'', ''null'']'
- description: Phone number.
  name: phone_number
  type: '[''string'', ''null'']'
- description: ''
  name: sources
  type: array
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-email-finder-result-schema.json
slug: hunter-email-finder-result
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: EmailFinderResult
---
