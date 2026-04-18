---
description: Information about a Mandrill template.
layout: schema
name: TemplateInfo
properties_list:
- description: The URL-safe slug for the template.
  name: slug
  type: string
- description: The display name of the template.
  name: name
  type: string
- description: Labels applied to the template for organization.
  name: labels
  type: array
- description: The HTML code of the template.
  name: code
  type: string
- description: The default subject line.
  name: subject
  type: string
- description: The default from address.
  name: from_email
  type: string
- description: The default from name.
  name: from_name
  type: string
- description: The default text content.
  name: text
  type: string
- description: The name of the published version.
  name: publish_name
  type: string
- description: The HTML code of the published version.
  name: publish_code
  type: string
- description: The subject of the published version.
  name: publish_subject
  type: string
- description: The from address of the published version.
  name: publish_from_email
  type: string
- description: The from name of the published version.
  name: publish_from_name
  type: string
- description: The text content of the published version.
  name: publish_text
  type: string
- description: When the template was last published.
  name: published_at
  type: string
- description: When the template was created.
  name: created_at
  type: string
- description: When the template was last updated.
  name: updated_at
  type: string
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-template-info-schema.json
slug: mailchimp-transactional-template-info
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: TemplateInfo
---
