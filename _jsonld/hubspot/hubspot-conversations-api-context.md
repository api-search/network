---
class_count: 17
classes:
- Inbox
- InboxCollection
- Thread
- ThreadCollection
- Message
- MessageStatus
- MessageCollection
- Actor
- ActorCollection
- Attachment
- Channel
- ChannelCollection
- SendMessageRequest
- MessageRecipient
- UpdateThreadRequest
- Paging
- PagingNext
context_file: json-ld/hubspot-conversations-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-conversations-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Conversations Api from HubSpot.
layout: jsonld
name: Hubspot Conversations Api Context
namespaces:
- prefix: hubspot
  uri: https://developers.hubspot.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: name
  type: ''
- container: ''
  name: type
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: archived
  type: boolean
- container: set
  name: results
  type: reference
- container: ''
  name: total
  type: integer
- container: ''
  name: paging
  type: reference
- container: ''
  name: inboxId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: spam
  type: boolean
- container: ''
  name: associatedContactId
  type: string
- container: ''
  name: assignedTo
  type: string
- container: ''
  name: originalChannelId
  type: string
- container: ''
  name: originalChannelAccountId
  type: string
- container: ''
  name: latestMessageTimestamp
  type: dateTime
- container: ''
  name: latestMessageSentTimestamp
  type: dateTime
- container: ''
  name: latestMessageReceivedTimestamp
  type: dateTime
- container: ''
  name: closedAt
  type: dateTime
- container: ''
  name: text
  type: string
- container: ''
  name: richText
  type: string
- container: ''
  name: direction
  type: string
- container: ''
  name: channelId
  type: string
- container: ''
  name: channelAccountId
  type: string
- container: set
  name: senders
  type: reference
- container: set
  name: recipients
  type: reference
- container: ''
  name: truncationStatus
  type: string
- container: set
  name: attachments
  type: reference
- container: ''
  name: statusType
  type: string
- container: ''
  name: actorId
  type: string
- container: ''
  name: email
  type: ''
- container: ''
  name: url
  type: ''
- container: ''
  name: filename
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: accountId
  type: string
- container: ''
  name: senderActorId
  type: string
- container: ''
  name: next
  type: reference
- container: ''
  name: after
  type: string
- container: ''
  name: link
  type: string
property_count: 40
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-conversations-api-context
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
- JSON-LD
- Linked Data
- Semantic Web
---
