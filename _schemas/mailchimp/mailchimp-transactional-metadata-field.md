---
description: A custom metadata field definition.
layout: schema
name: MetadataField
properties_list:
- description: The unique name of the metadata field.
  name: name
  type: string
- description: The current state of the field.
  name: state
  type: string
- description: The Mustache template for displaying the field in the UI.
  name: view_template
  type: string
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-metadata-field-schema.json
slug: mailchimp-transactional-metadata-field
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: MetadataField
---
