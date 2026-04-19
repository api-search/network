---
description: ''
layout: schema
name: DomainEmail
properties_list:
- description: The email address.
  name: value
  type: string
- description: Whether the email is personal or generic.
  name: type
  type: string
- description: Confidence score for the email address.
  name: confidence
  type: integer
- description: First name of the person.
  name: first_name
  type: '[''string'', ''null'']'
- description: Last name of the person.
  name: last_name
  type: '[''string'', ''null'']'
- description: Job position or title.
  name: position
  type: '[''string'', ''null'']'
- description: Seniority level.
  name: seniority
  type: '[''string'', ''null'']'
- description: Department within the organization.
  name: department
  type: '[''string'', ''null'']'
- description: LinkedIn profile URL.
  name: linkedin
  type: '[''string'', ''null'']'
- description: Twitter handle.
  name: twitter
  type: '[''string'', ''null'']'
- description: Phone number.
  name: phone_number
  type: '[''string'', ''null'']'
- description: ''
  name: sources
  type: array
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-domain-email-schema.json
slug: hunter-domain-email
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: DomainEmail
---
