---
class_count: 18
classes:
- BroadcastListsResponse
- BroadcastUpdateRequest
- AIBroadcastRequest
- BroadcastMetrics
- BroadcastList
- BroadcastMessage
- SnapshotResponse
- BroadcastCreateRequest
- BroadcastMetricsResponse
- CreditsResponse
- RecipientsResponse
- FailureDetail
- AIBroadcastUpdateRequest
- AIBroadcastStatus
- BroadcastListResponse
- AIBroadcastResponse
- FailureDetailsResponse
- Recipient
context_file: json-ld/activecampaign-sms-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/json-ld/activecampaign-sms-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Activecampaign Sms from ActiveCampaign.
layout: jsonld
name: Activecampaign Sms Context
namespaces:
- prefix: activecampaign
  uri: https://developers.activecampaign.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: lists
  type: string
- container: ''
  name: meta
  type: reference
- container: ''
  name: name
  type: string
- container: ''
  name: addressId
  type: integer
- container: ''
  name: body
  type: string
- container: set
  name: mediaUrls
  type: reference
- container: ''
  name: previewUrl
  type: reference
- container: ''
  name: shortenTrackLinksEnabled
  type: boolean
- container: ''
  name: status
  type: string
- container: ''
  name: scheduledDate
  type: dateTime
- container: ''
  name: sentToCount
  type: integer
- container: set
  name: listIds
  type: integer
- container: ''
  name: segmentId
  type: string
- container: ''
  name: customRunId
  type: string
- container: ''
  name: customSegmentId
  type: string
- container: set
  name: labelIds
  type: integer
- container: ''
  name: source
  type: string
- container: ''
  name: prompt
  type: string
- container: ''
  name: tone
  type: string
- container: ''
  name: id
  type: integer
- container: ''
  name: sends
  type: integer
- container: ''
  name: deliveries
  type: integer
- container: ''
  name: replies
  type: integer
- container: ''
  name: failures
  type: integer
- container: ''
  name: optOuts
  type: integer
- container: ''
  name: clicks
  type: integer
- container: ''
  name: subscriberCount
  type: integer
- container: ''
  name: sentDate
  type: dateTime
- container: ''
  name: scheduledBy
  type: integer
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: createdBy
  type: integer
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: updatedBy
  type: integer
- container: ''
  name: deletedAt
  type: dateTime
- container: ''
  name: siftApproved
  type: integer
- container: ''
  name: arcApproved
  type: integer
- container: ''
  name: quietHoursEnabled
  type: integer
- container: ''
  name: snapshot
  type: reference
- container: set
  name: metrics
  type: string
- container: ''
  name: smsCredits
  type: reference
- container: set
  name: recipients
  type: string
- container: ''
  name: errorCode
  type: string
- container: ''
  name: errorSource
  type: string
- container: ''
  name: count
  type: integer
- container: ''
  name: broadcastId
  type: integer
- container: set
  name: broadcasts
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: phoneNumber
  type: string
- container: ''
  name: deliverability
  type: string
- container: ''
  name: optOut
  type: string
- container: ''
  name: details
  type: reference
property_count: 51
provider_name: ActiveCampaign
provider_slug: activecampaign
slug: activecampaign-sms-context
tags:
- Marketing Automation
- Email Marketing
- CRM
- Sales Automation
- Customer Experience
- JSON-LD
- Linked Data
- Semantic Web
---
