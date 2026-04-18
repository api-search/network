---
description: A message in a mailFolder.
layout: schema
name: Message
properties_list:
- description: Unique identifier for the message. Read-only.
  name: id
  type: string
- description: The date and time the message was created in UTC (ISO 8601).
  name: createdDateTime
  type: string
- description: The date and time the message was last changed in UTC (ISO 8601).
  name: lastModifiedDateTime
  type: string
- description: The version of the message.
  name: changeKey
  type: string
- description: The categories associated with the message.
  name: categories
  type: array
- description: The date and time the message was received in UTC (ISO 8601).
  name: receivedDateTime
  type: string
- description: The date and time the message was sent in UTC (ISO 8601).
  name: sentDateTime
  type: string
- description: Indicates whether the message has attachments. Does not include inline attachments.
  name: hasAttachments
  type: boolean
- description: The message ID in the format specified by RFC 2822.
  name: internetMessageId
  type: string
- description: Collection of message headers defined by RFC 5322. Returned only on applying a $select query option.
  name: internetMessageHeaders
  type: array
- description: The subject of the message.
  name: subject
  type: string
- description: The first 255 characters of the message body in text format.
  name: bodyPreview
  type: string
- description: The importance of the message.
  name: importance
  type: string
- description: The unique identifier for the message's parent mailFolder.
  name: parentFolderId
  type: string
- description: The ID of the conversation the email belongs to.
  name: conversationId
  type: string
- description: Indicates the position of the message within the conversation.
  name: conversationIndex
  type: string
- description: Indicates whether a delivery receipt is requested.
  name: isDeliveryReceiptRequested
  type: boolean
- description: Indicates whether a read receipt is requested.
  name: isReadReceiptRequested
  type: boolean
- description: Indicates whether the message has been read.
  name: isRead
  type: boolean
- description: Indicates whether the message is a draft.
  name: isDraft
  type: boolean
- description: The URL to open the message in Outlook on the web.
  name: webLink
  type: string
- description: The classification of the message based on inferred relevance or importance, or on an explicit override.
  name: inferenceClassification
  type: string
- description: The To recipients for the message.
  name: toRecipients
  type: array
- description: The Cc recipients for the message.
  name: ccRecipients
  type: array
- description: The Bcc recipients for the message.
  name: bccRecipients
  type: array
- description: The email addresses to use when replying.
  name: replyTo
  type: array
- description: The fileAttachment and itemAttachment attachments for the message.
  name: attachments
  type: array
provider_name: Microsoft Outlook
provider_slug: microsoft-outlook
schema_file: json-schema/microsoft-graph-mail-message-schema.json
slug: microsoft-graph-mail-message
tags:
- Calendar
- Contacts
- Email
- Enterprise
- Microsoft
- Office 365
- Productivity
title: Message
---
