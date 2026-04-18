---
aid: zendesk:comment-redactions
baseURL: https://{subdomain}.zendesk.com
description: The Zendesk Comment Redactions API lets you programmatically and permanently remove sensitive information from ticket conversations without deleting the entire message. By targeting a specific ticket comment and supplying the text to scrub (for example, credit card numbers, passwords, or PII), the API replaces the matching content in both the plain text and HTML versions with a redacted placeholder and records a redaction event in the tickets audit trail.
humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Zendesk Comment Redactions API
properties:
- type: Documentation
  url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/openapi/comment-redactions-openapi-original.yml
provider_name: Zendesk
provider_slug: zendesk
slug: comment-redactions
tags:
- Comments
- Redactions
---
