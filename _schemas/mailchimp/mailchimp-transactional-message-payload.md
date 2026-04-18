---
description: The message object containing all parameters for a transactional email, including recipients, content, attachments, and tracking options.
layout: schema
name: MessagePayload
properties_list:
- description: The full HTML content of the message.
  name: html
  type: string
- description: The full plain-text content of the message.
  name: text
  type: string
- description: The message subject line.
  name: subject
  type: string
- description: The sender email address.
  name: from_email
  type: string
- description: The sender display name.
  name: from_name
  type: string
- description: An array of recipient objects.
  name: to
  type: array
- description: Optional extra headers to add to the message (e.g., Reply-To).
  name: headers
  type: object
- description: Whether this message is important and should be delivered ahead of non-important messages.
  name: important
  type: boolean
- description: Whether to enable open tracking for this message.
  name: track_opens
  type: boolean
- description: Whether to enable click tracking for this message.
  name: track_clicks
  type: boolean
- description: Whether to automatically generate a plain-text version from the HTML content.
  name: auto_text
  type: boolean
- description: Whether to automatically generate HTML from the plain-text content.
  name: auto_html
  type: boolean
- description: Whether to automatically inline all CSS styles from style blocks in the HTML content.
  name: inline_css
  type: boolean
- description: Whether to strip query strings from URLs when aggregating tracked click data.
  name: url_strip_qs
  type: boolean
- description: Whether to show all recipients in the To header of each email.
  name: preserve_recipients
  type: boolean
- description: Whether to include a View Content Link in the Mandrill dashboard for this message.
  name: view_content_link
  type: boolean
- description: An optional address to BCC on the message.
  name: bcc_address
  type: string
- description: A custom domain to use for tracking opens and clicks.
  name: tracking_domain
  type: string
- description: A custom domain to use for DKIM signing instead of the default.
  name: signing_domain
  type: string
- description: A custom domain to use for the return-path header.
  name: return_path_domain
  type: string
- description: Whether to evaluate merge tags in the message.
  name: merge
  type: boolean
- description: The merge tag language to use (Mailchimp or Handlebars).
  name: merge_language
  type: string
- description: Global merge variables applied to all recipients.
  name: global_merge_vars
  type: array
- description: Per-recipient merge variables.
  name: merge_vars
  type: array
- description: An array of string tags to apply to this message for analytics.
  name: tags
  type: array
- description: The unique ID of a subaccount for this message.
  name: subaccount
  type: string
- description: An array of domains for which Google Analytics tracking parameters will be appended.
  name: google_analytics_domains
  type: array
- description: The utm_campaign tracking parameter for Google Analytics.
  name: google_analytics_campaign
  type: string
- description: Key-value metadata to associate with the message.
  name: metadata
  type: object
- description: Per-recipient metadata.
  name: recipient_metadata
  type: array
- description: An array of file attachments.
  name: attachments
  type: array
- description: An array of inline images referenced with "cid:" in the HTML content.
  name: images
  type: array
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-message-payload-schema.json
slug: mailchimp-transactional-message-payload
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: MessagePayload
---
