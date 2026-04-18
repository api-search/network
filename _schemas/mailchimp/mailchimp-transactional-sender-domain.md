---
description: Information about a configured sender domain.
layout: schema
name: SenderDomain
properties_list:
- description: The domain name.
  name: domain
  type: string
- description: When the domain was added.
  name: created_at
  type: string
- description: When the domain settings were last tested.
  name: last_tested_at
  type: string
- description: SPF verification details.
  name: spf
  type: object
- description: DKIM verification details.
  name: dkim
  type: object
- description: When the domain ownership was verified.
  name: verified_at
  type: string
- description: Whether the domain can be used for DKIM signing.
  name: valid_signing
  type: boolean
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-sender-domain-schema.json
slug: mailchimp-transactional-sender-domain
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: SenderDomain
---
