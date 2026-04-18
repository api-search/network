---
description: EmailDLPIncident schema from Palo Alto Networks Email DLP API
layout: schema
name: EmailDLPIncident
properties_list:
- description: Unique incident identifier.
  name: id
  type: string
- description: Email address of the message sender.
  name: sender
  type: string
- description: Email message subject line.
  name: subject
  type: string
- description: Current status or verdict for the email message.
  name: status
  type: string
- description: Incident severity based on data pattern sensitivity.
  name: severity
  type: string
- description: Data patterns that matched in the email content.
  name: data_patterns
  type: array
- description: Total number of data pattern matches across all patterns.
  name: match_count
  type: integer
- description: Timestamp when the incident was detected.
  name: timestamp
  type: string
- description: Whether the email contained attachments.
  name: has_attachments
  type: boolean
- description: Number of attachments in the email.
  name: attachment_count
  type: integer
- description: Direction of the email message.
  name: direction
  type: string
- description: Automated action taken on the message.
  name: action_taken
  type: string
- description: Email address of the analyst who reviewed the incident.
  name: reviewed_by
  type: string
- description: Timestamp when the incident was last reviewed.
  name: reviewed_at
  type: string
- description: Comment added during verdict review.
  name: comment
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/email-dlp-api-email-dlp-incident-schema.json
slug: email-dlp-api-email-dlp-incident
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: EmailDLPIncident
---
