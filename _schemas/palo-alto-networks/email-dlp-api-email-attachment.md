---
description: EmailAttachment schema from Palo Alto Networks Email DLP API
layout: schema
name: EmailAttachment
properties_list:
- description: Attachment filename.
  name: filename
  type: string
- description: MIME content type of the attachment.
  name: content_type
  type: string
- description: Attachment size in bytes.
  name: size
  type: integer
- description: Whether the attachment contained data pattern matches.
  name: has_matches
  type: boolean
- description: Number of data pattern matches in the attachment.
  name: match_count
  type: integer
- description: Names of data patterns that matched in the attachment.
  name: patterns_matched
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/email-dlp-api-email-attachment-schema.json
slug: email-dlp-api-email-attachment
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: EmailAttachment
---
