---
description: JSON Schema for a Microsoft Graph message resource representing an email message in a user's mailbox. Based on the microsoft.graph.message resource type from the Microsoft Graph v1.0 API.
layout: schema
name: Microsoft Outlook Message
properties_list:
- description: 'Unique identifier for the message. By default, this value changes when the item is moved from one container to another. Use the Prefer: IdType="ImmutableId" header for immutable identifiers.'
  name: id
  type: string
- description: The date and time the message was created. Uses ISO 8601 format in UTC time (e.g., 2014-01-01T00:00:00Z).
  name: createdDateTime
  type: string
- description: The date and time the message was last changed. Uses ISO 8601 format in UTC time.
  name: lastModifiedDateTime
  type: string
- description: The version of the message.
  name: changeKey
  type: string
- description: The categories associated with the message.
  name: categories
  type: array
- description: The date and time the message was received. Uses ISO 8601 format in UTC time.
  name: receivedDateTime
  type: string
- description: The date and time the message was sent. Uses ISO 8601 format in UTC time.
  name: sentDateTime
  type: string
- description: Indicates whether the message has attachments. This property does not include inline attachments. To verify inline attachments, parse the body property for a src attribute.
  name: hasAttachments
  type: boolean
- description: The message ID in the format specified by RFC 2822.
  name: internetMessageId
  type: string
- description: A collection of message headers defined by RFC 5322. Includes custom message headers starting with 'x-'. Returned only on applying a $select query option.
  name: internetMessageHeaders
  type: array
- description: The subject of the message.
  name: subject
  type: string
- description: The body of the message. Can be in HTML or text format.
  name: body
  type: object
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
- description: Indicates the position of the message within the conversation. Binary value encoded as base64.
  name: conversationIndex
  type: string
- description: Indicates whether a delivery receipt is requested for the message.
  name: isDeliveryReceiptRequested
  type:
  - boolean
  - 'null'
- description: Indicates whether a read receipt is requested for the message.
  name: isReadReceiptRequested
  type: boolean
- description: Indicates whether the message has been read.
  name: isRead
  type: boolean
- description: Indicates whether the message is a draft. A message is a draft if it has not been sent yet.
  name: isDraft
  type: boolean
- description: The URL to open the message in Outlook on the web. Append ispopout=0 to show in the review pane instead of a popout window.
  name: webLink
  type: string
- description: The classification of the message for the user, based on inferred relevance or importance, or on an explicit override.
  name: inferenceClassification
  type: string
- description: The follow-up flag value indicating the status, start date, due date, or completion date for the message.
  name: flag
  type: object
- description: The owner of the mailbox from which the message is sent. In most cases, this is the same as the sender property, except for sharing or delegation scenarios.
  name: from
  type: object
- description: The account that is used to generate the message. In most cases, this is the same as the from property. Can differ when sending from a shared mailbox or as a delegate.
  name: sender
  type: object
- description: 'The To: recipients for the message.'
  name: toRecipients
  type: array
- description: 'The Cc: recipients for the message.'
  name: ccRecipients
  type: array
- description: 'The Bcc: recipients for the message.'
  name: bccRecipients
  type: array
- description: The email addresses to use when replying.
  name: replyTo
  type: array
- description: The part of the body of the message that is unique to the current message. Not returned by default; use $select=uniqueBody.
  name: uniqueBody
  type: object
- description: The fileAttachment and itemAttachment attachments for the message.
  name: attachments
  type: array
provider_name: Microsoft Outlook
provider_slug: microsoft-outlook
schema_file: json-schema/microsoft-outlook-message-schema.json
slug: microsoft-outlook-message
tags:
- Calendar
- Contacts
- Email
- Enterprise
- Microsoft
- Office 365
- Productivity
title: Microsoft Outlook Message
---
