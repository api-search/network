---
description: ''
layout: schema
name: DomainSearchResult
properties_list:
- description: The domain name searched.
  name: domain
  type: string
- description: Whether the domain is a disposable email service.
  name: disposable
  type: boolean
- description: Whether the domain is a webmail provider.
  name: webmail
  type: boolean
- description: Whether the mail server accepts all email addresses.
  name: accept_all
  type: boolean
- description: The email address pattern detected for the domain.
  name: pattern
  type: '[''string'', ''null'']'
- description: The name of the organization associated with the domain.
  name: organization
  type: string
- description: ''
  name: emails
  type: array
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-domain-search-result-schema.json
slug: hunter-domain-search-result
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: DomainSearchResult
---
