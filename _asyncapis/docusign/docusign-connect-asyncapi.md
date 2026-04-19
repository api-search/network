---
channels:
- description: Triggered when an envelope is sent to recipients for signing. The envelope transitions from draft to sent status.
  name: envelopeSent
- description: Triggered when an envelope is delivered to a recipient and they have viewed the documents.
  name: envelopeDelivered
- description: Triggered when all recipients have completed their required actions and the envelope is fully executed. This is the terminal success state for an envelope.
  name: envelopeCompleted
- description: Triggered when a recipient declines to sign the envelope. The envelope is moved to declined status and no further signing can occur unless the sender corrects and resends.
  name: envelopeDeclined
- description: Triggered when the sender voids an envelope, canceling the signing process. A voided envelope cannot be sent again.
  name: envelopeVoided
- description: Triggered when a signing invitation is sent to an individual recipient via email.
  name: recipientSent
- description: Triggered when a recipient opens the envelope and views the documents for the first time.
  name: recipientDelivered
- description: Triggered when a recipient completes their required actions such as signing, initialing, or approving the documents.
  name: recipientCompleted
- description: Triggered when a recipient declines to sign the envelope, providing a reason for the decline.
  name: recipientDeclined
- description: Triggered when a recipient fails identity verification or authentication during the signing process.
  name: recipientAuthenticationFailed
description: DocuSign Connect is a webhook notification service that sends real-time updates about envelope and recipient events to your application. Connect pushes notifications to your listener endpoint when envelope status changes, recipients complete actions, or other configured events occur. This enables event-driven integrations without the need to poll the eSignature REST API for status updates.
layout: asyncapi
messages:
- description: ''
  name: EnvelopeSentEvent
  summary: Notification sent when an envelope is dispatched to recipients.
  title: Envelope Sent
- description: ''
  name: EnvelopeDeliveredEvent
  summary: Notification sent when a recipient views the envelope documents.
  title: Envelope Delivered
- description: ''
  name: EnvelopeCompletedEvent
  summary: Notification sent when all recipients complete their actions and the envelope reaches terminal completed status.
  title: Envelope Completed
- description: ''
  name: EnvelopeDeclinedEvent
  summary: Notification sent when a recipient declines the envelope.
  title: Envelope Declined
- description: ''
  name: EnvelopeVoidedEvent
  summary: Notification sent when the sender voids the envelope.
  title: Envelope Voided
- description: ''
  name: RecipientSentEvent
  summary: Notification sent when a signing invitation is sent to a recipient.
  title: Recipient Sent
- description: ''
  name: RecipientDeliveredEvent
  summary: Notification sent when a recipient opens and views the documents.
  title: Recipient Delivered
- description: ''
  name: RecipientCompletedEvent
  summary: Notification sent when a recipient completes their signing or approval actions.
  title: Recipient Completed
- description: ''
  name: RecipientDeclinedEvent
  summary: Notification sent when a recipient declines to sign.
  title: Recipient Declined
- description: ''
  name: RecipientAuthenticationFailedEvent
  summary: Notification sent when a recipient fails identity verification.
  title: Recipient Authentication Failed
name: DocuSign Connect Webhooks
provider_name: Docusign
provider_slug: docusign
servers:
- description: Your application webhook listener endpoint. DocuSign Connect sends HTTP POST requests with JSON or XML payloads to this URL when configured events occur. The listener must respond with an HTTP 200 status to acknowledge receipt.
  name: production
  protocol: https
  url: ''
slug: docusign-connect-asyncapi
spec_file: asyncapi/docusign-connect-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/docusign/refs/heads/main/asyncapi/docusign-connect-asyncapi.yml
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
- AsyncAPI
- Webhooks
- Events
version: 2.0.0
---
