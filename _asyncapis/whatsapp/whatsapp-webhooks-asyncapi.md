---
channels:
- description: Receives all WhatsApp Business Platform webhook events. The field property in each change entry determines the event type.
  name: /webhook
  operation: publish
  operation_id: receiveWebhookEvent
  summary: Receive webhook events
description: WhatsApp Business Platform webhooks deliver real-time notifications for incoming messages, message status updates, template status changes, account updates, phone number quality changes, and security events. All webhook payloads are sent as HTTP POST requests signed with HMAC-SHA256 using the app secret via the X-Hub-Signature-256 header. Your endpoint must respond with HTTP 200 immediately and process events asynchronously.
layout: asyncapi
messages:
- description: ''
  name: IncomingMessage
  summary: A user sent a message to your WhatsApp Business number
  title: Incoming Message Notification
- description: ''
  name: MessageStatus
  summary: Status update for a sent message (sent, delivered, read, failed)
  title: Message Status Update
- description: ''
  name: TemplateStatusUpdate
  summary: A message template was approved, rejected, or had its status changed
  title: Message Template Status Change
- description: ''
  name: AccountUpdate
  summary: Policy enforcement or account restriction notification
  title: Account Policy Update
- description: ''
  name: PhoneNumberQualityUpdate
  summary: Phone number quality rating changed (flagged or unflagged)
  title: Phone Number Quality Rating Change
- description: ''
  name: SecurityEvent
  summary: Security-related event such as PIN change
  title: Security Alert
name: WhatsApp Webhooks
provider_name: WhatsApp
provider_slug: whatsapp
servers:
- description: Your HTTPS webhook endpoint configured in the Meta App Dashboard. Must respond to GET requests for verification and POST requests for event delivery.
  name: webhookEndpoint
  protocol: https
  url: '{webhookUrl}'
slug: whatsapp-webhooks-asyncapi
spec_file: asyncapi/whatsapp-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/whatsapp/refs/heads/main/asyncapi/whatsapp-webhooks-asyncapi.yml
tags:
- AsyncAPI
- Webhooks
- Events
version: '21.0'
---
