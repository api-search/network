---
description: An entry in the sending allowlist.
layout: schema
name: AllowlistEntry
properties_list:
- description: The allowlisted email address.
  name: email
  type: string
- description: Details or comment about why the address is allowlisted.
  name: detail
  type: string
- description: When the entry was added to the allowlist.
  name: created_at
  type: string
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-allowlist-entry-schema.json
slug: mailchimp-transactional-allowlist-entry
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: AllowlistEntry
---
