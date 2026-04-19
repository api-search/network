---
description: Configuration for envelope event notifications via DocuSign Connect webhooks.
layout: schema
name: EventNotification
properties_list:
- description: The webhook endpoint URL to receive notifications.
  name: url
  type: string
- description: When true, Connect logging is enabled.
  name: loggingEnabled
  type: string
- description: When true, requires HTTPS 200 acknowledgment.
  name: requireAcknowledgment
  type: string
- description: Envelope-level events to trigger notifications.
  name: envelopeEvents
  type: array
- description: Recipient-level events to trigger notifications.
  name: recipientEvents
  type: array
- description: When true, includes the certificate of completion.
  name: includeCertificateOfCompletion
  type: string
- description: When true, includes document PDFs in the notification.
  name: includeDocuments
  type: string
- description: When true, includes document custom fields.
  name: includeDocumentFields
  type: string
- description: When true, includes HMAC security headers.
  name: includeHMAC
  type: string
- description: ''
  name: includeSenderAccountAsCustomField
  type: string
- description: When true, includes time zone information.
  name: includeTimeZone
  type: string
- description: ''
  name: includeCertificateWithSoap
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-event-notification-schema.json
slug: docusign-esignature-event-notification
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: EventNotification
---
