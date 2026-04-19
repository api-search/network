---
description: ''
layout: schema
name: EmailVerifierResult
properties_list:
- description: The verification status of the email address.
  name: status
  type: string
- description: Deprecated. The deliverability result.
  name: result
  type: string
- description: Deliverability score.
  name: score
  type: integer
- description: The email address that was verified.
  name: email
  type: string
- description: Whether the email matches a valid format.
  name: regexp
  type: boolean
- description: Whether the email appears to be gibberish.
  name: gibberish
  type: boolean
- description: Whether the email uses a disposable provider.
  name: disposable
  type: boolean
- description: Whether the email is a webmail address.
  name: webmail
  type: boolean
- description: Whether MX records exist for the domain.
  name: mx_records
  type: boolean
- description: Whether an SMTP server was found.
  name: smtp_server
  type: boolean
- description: Whether the SMTP check passed.
  name: smtp_check
  type: boolean
- description: Whether the mail server accepts all addresses.
  name: accept_all
  type: boolean
- description: Whether the email is blocked.
  name: block
  type: boolean
- description: ''
  name: sources
  type: array
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-email-verifier-result-schema.json
slug: hunter-email-verifier-result
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: EmailVerifierResult
---
