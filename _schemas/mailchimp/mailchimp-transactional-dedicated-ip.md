---
description: Information about a dedicated IP address.
layout: schema
name: DedicatedIP
properties_list:
- description: The dedicated IP address.
  name: ip
  type: string
- description: When the IP was provisioned.
  name: created_at
  type: string
- description: The IP pool this address belongs to.
  name: pool
  type: string
- description: The reverse DNS domain for the IP.
  name: domain
  type: string
- description: Custom DNS settings for the IP.
  name: custom_dns
  type: object
- description: IP warmup status.
  name: warmup
  type: object
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-dedicated-ip-schema.json
slug: mailchimp-transactional-dedicated-ip
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: DedicatedIP
---
