---
description: ''
layout: schema
name: EmailCountResult
properties_list:
- description: Total number of email addresses found.
  name: total
  type: integer
- description: Number of personal email addresses.
  name: personal_emails
  type: integer
- description: Number of generic email addresses.
  name: generic_emails
  type: integer
- description: Breakdown of email count by department.
  name: department
  type: object
- description: Breakdown of email count by seniority level.
  name: seniority
  type: object
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-email-count-result-schema.json
slug: hunter-email-count-result
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: EmailCountResult
---
