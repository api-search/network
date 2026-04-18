---
description: An entry in the rejection blacklist.
layout: schema
name: RejectEntry
properties_list:
- description: The rejected email address.
  name: email
  type: string
- description: The reason the address is on the blacklist.
  name: reason
  type: string
- description: Extended details about the rejection.
  name: detail
  type: string
- description: When the entry was added to the blacklist.
  name: created_at
  type: string
- description: When the last event occurred for this address.
  name: last_event_at
  type: string
- description: When the rejection expires (if applicable).
  name: expires_at
  type: string
- description: Whether the rejection has expired.
  name: expired
  type: boolean
- description: The subaccount this rejection applies to, if any.
  name: subaccount
  type: string
- description: Sender statistics associated with the rejection.
  name: sender
  type: object
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-reject-entry-schema.json
slug: mailchimp-transactional-reject-entry
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: RejectEntry
---
