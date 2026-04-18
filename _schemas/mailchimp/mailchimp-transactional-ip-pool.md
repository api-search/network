---
description: An IP pool grouping dedicated IPs.
layout: schema
name: IPPool
properties_list:
- description: The pool name.
  name: name
  type: string
- description: When the pool was created.
  name: created_at
  type: string
- description: The dedicated IPs in this pool.
  name: ips
  type: array
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-ip-pool-schema.json
slug: mailchimp-transactional-ip-pool
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: IPPool
---
