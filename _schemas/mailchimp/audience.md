---
description: A Mailchimp audience (also known as a list). Audiences contain subscribers who have opted in to receive correspondence from you or your organization. They hold contact information, segmentation data, campaign defaults, and compliance settings.
layout: schema
name: Mailchimp Audience (List)
properties_list:
- description: A string that uniquely identifies this list.
  name: id
  type: string
- description: The ID used in the Mailchimp web application.
  name: web_id
  type: integer
- description: The name of the list/audience.
  name: name
  type: string
- description: Contact information displayed in campaign footers to comply with international spam laws.
  name: contact
  type: object
- description: The permission reminder for the list, reminding subscribers how they signed up.
  name: permission_reminder
  type: string
- description: Whether campaigns for this list use the Archive Bar in archives by default.
  name: use_archive_bar
  type: boolean
- description: Default values for campaigns created for this list.
  name: campaign_defaults
  type: object
- description: The email address to send subscribe notifications to. Set to empty string to disable.
  name: notify_on_subscribe
  type: string
- description: The email address to send unsubscribe notifications to. Set to empty string to disable.
  name: notify_on_unsubscribe
  type: string
- description: The date and time that this list was created in ISO 8601 format.
  name: date_created
  type: string
- description: An auto-generated activity score for the list (0-5).
  name: list_rating
  type: integer
- description: Whether the list supports multiple email formats (HTML and plain-text). When true, subscribers can choose their preferred format.
  name: email_type_option
  type: boolean
- description: The URL-shortened version of this list's subscribe form.
  name: subscribe_url_short
  type: string
- description: The full version of this list's subscribe form URL.
  name: subscribe_url_long
  type: string
- description: The list's Email Beamer address for creating campaigns via email.
  name: beamer_address
  type: string
- description: Legacy visibility setting. No longer used.
  name: visibility
  type: string
- description: Whether to require the subscriber to confirm subscription via email.
  name: double_optin
  type: boolean
- description: Whether this list has a welcome automation connected.
  name: has_welcome
  type: boolean
- description: Whether the list has marketing permissions (GDPR) enabled.
  name: marketing_permissions
  type: boolean
- description: Any list-specific modules installed for this list.
  name: modules
  type: array
- description: Stats for the list, including subscriber counts and campaign performance.
  name: stats
  type: object
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/audience.json
slug: audience
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: Mailchimp Audience (List)
---
