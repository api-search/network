---
aid: zendesk:uploads
baseURL: https://{subdomain}.zendesk.com
description: The Zendesk Uploads API lets you upload files to Zendesk Support so they can be attached to tickets or embedded inline in ticket comments. When you POST a file, the API creates an upload and returns metadata plus a short-lived token. You then include one or more of these tokens when creating or updating a ticket to add the files as attachments. The API supports single-shot and chunked uploads (for large files), and provides endpoints to check an uploads details or delete it.
humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Zendesk Uploads API
properties:
- type: Documentation
  url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/openapi/uploads-openapi-original.yml
provider_name: Zendesk
provider_slug: zendesk
slug: uploads
tags:
- Uploads
---
