---
class_count: 60
classes:
- PaginationInfo
- createdAt
- updatedAt
- APIKeyScope
- APIKey
- CreateAPIKeyRequest
- UpdateAPIKeyRequest
- PaginatedAPIKeysResponse
- DNSRecord
- Domain
- CreateDomainRequest
- UpdateDomainRequest
- PaginatedDomainsResponse
- email
- name
- Address
- Recipient
- Attachment
- Tracking
- Retention
- MessageSchedule
- CreateMessageRequest
- CreateConversationMessageRequest
- CreateSingleMessageResponse
- CreateMessageResponse
- DeliveryEvent
- MessageContentPart
- MessageAttachment
- MessageContentParsed
- MessageSummary
- PaginatedMessagesResponse
- Account
- UpdateAccountRequest
- UserAccount
- AccountMembersResponse
- AddMemberRequest
- Suppression
- CreateSuppressionResponse
- CreateSuppressionRequest
- PaginatedSuppressionsResponse
- url
- Route
- CreateRouteRequest
- UpdateRouteRequest
- PaginatedRoutesResponse
- Webhook
- CreateWebhookRequest
- UpdateWebhookRequest
- PaginatedWebhooksResponse
- SMTPCredential
- CreateSMTPCredentialRequest
- PaginatedSMTPCredentialsResponse
- DeliverabilityStatistics
- DeliverabilityStatisticsResponse
- Bounce
- BounceStatistics
- BounceStatisticsResponse
- DeliveryTimeStatistics
- DeliveryTime
- DeliveryTimeStatisticsResponse
context_file: json-ld/ahasend-openapi-v2-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/ahasend/refs/heads/main/json-ld/ahasend-openapi-v2-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Ahasend Openapi V2 from AhaSend.
layout: jsonld
name: Ahasend Openapi V2 Context
namespaces:
- prefix: ahasend
  uri: https://ahasend.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: hasMore
  type: boolean
- container: ''
  name: nextCursor
  type: string
- container: ''
  name: previousCursor
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: apiKeyId
  type: string
- container: ''
  name: scope
  type: string
- container: ''
  name: domainId
  type: string
- container: ''
  name: object
  type: string
- container: ''
  name: lastUsedAt
  type: dateTime
- container: ''
  name: accountId
  type: string
- container: ''
  name: label
  type: string
- container: ''
  name: publicKey
  type: string
- container: ''
  name: secretKey
  type: string
- container: set
  name: scopes
  type: string
- container: set
  name: data
  type: string
- container: ''
  name: pagination
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: host
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: required
  type: boolean
- container: ''
  name: propagated
  type: boolean
- container: ''
  name: domain
  type: string
- container: set
  name: dnsRecords
  type: string
- container: ''
  name: lastDnsCheckAt
  type: dateTime
- container: ''
  name: dnsValid
  type: boolean
- container: ''
  name: trackingSubdomain
  type: string
- container: ''
  name: returnPathSubdomain
  type: string
- container: ''
  name: subscriptionSubdomain
  type: string
- container: ''
  name: mediaSubdomain
  type: string
- container: ''
  name: dkimRotationIntervalDays
  type: integer
- container: ''
  name: rotationReady
  type: boolean
- container: ''
  name: dkimPrivateKey
  type: string
- container: ''
  name: substitutions
  type: reference
- container: ''
  name: base64
  type: boolean
- container: ''
  name: contentType
  type: string
- container: ''
  name: contentDisposition
  type: string
- container: ''
  name: contentId
  type: string
- container: ''
  name: fileName
  type: string
- container: ''
  name: open
  type: boolean
- container: ''
  name: click
  type: boolean
- container: ''
  name: metadata
  type: integer
- container: ''
  name: firstAttempt
  type: dateTime
- container: ''
  name: expires
  type: dateTime
- container: ''
  name: from
  type: string
- container: set
  name: recipients
  type: string
- container: ''
  name: replyTo
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: textContent
  type: string
- container: ''
  name: htmlContent
  type: string
- container: ''
  name: ampContent
  type: string
- container: set
  name: attachments
  type: string
- container: ''
  name: headers
  type: reference
- container: set
  name: tags
  type: string
- container: ''
  name: sandbox
  type: boolean
- container: ''
  name: sandboxResult
  type: string
- container: ''
  name: tracking
  type: string
- container: ''
  name: retention
  type: string
- container: ''
  name: schedule
  type: string
- container: set
  name: to
  type: string
- container: set
  name: cc
  type: string
- container: set
  name: bcc
  type: string
- container: ''
  name: recipient
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: error
  type: string
- container: ''
  name: time
  type: dateTime
- container: ''
  name: log
  type: string
- container: ''
  name: filename
  type: string
- container: set
  name: parts
  type: string
- container: ''
  name: sentAt
  type: dateTime
- container: ''
  name: deliveredAt
  type: dateTime
- container: ''
  name: retainUntil
  type: dateTime
- container: ''
  name: direction
  type: string
- container: ''
  name: isBounceNotification
  type: boolean
- container: ''
  name: bounceClassification
  type: string
- container: set
  name: deliveryAttempts
  type: string
- container: ''
  name: messageId
  type: string
- container: ''
  name: sender
  type: string
- container: ''
  name: numAttempts
  type: integer
- container: ''
  name: clickCount
  type: integer
- container: ''
  name: openCount
  type: integer
- container: ''
  name: referenceMessageId
  type: integer
- container: ''
  name: website
  type: reference
- container: ''
  name: about
  type: string
- container: ''
  name: trackOpens
  type: boolean
- container: ''
  name: trackClicks
  type: boolean
- container: ''
  name: rejectBadRecipients
  type: boolean
- container: ''
  name: rejectMistypedRecipients
  type: boolean
- container: ''
  name: messageMetadataRetention
  type: integer
- container: ''
  name: messageDataRetention
  type: integer
- container: ''
  name: userId
  type: string
- container: ''
  name: role
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: groupByMessageId
  type: boolean
- container: ''
  name: stripReplies
  type: boolean
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: successCount
  type: integer
- container: ''
  name: errorCount
  type: integer
- container: ''
  name: errorsSinceLastSuccess
  type: integer
- container: ''
  name: lastRequestAt
  type: dateTime
- container: ''
  name: onReception
  type: boolean
- container: ''
  name: onDelivered
  type: boolean
- container: ''
  name: onTransientError
  type: boolean
- container: ''
  name: onFailed
  type: boolean
- container: ''
  name: onBounced
  type: boolean
- container: ''
  name: onSuppressed
  type: boolean
- container: ''
  name: onOpened
  type: boolean
- container: ''
  name: onClicked
  type: boolean
- container: ''
  name: onSuppressionCreated
  type: boolean
- container: ''
  name: onDnsError
  type: boolean
- container: set
  name: domains
  type: string
- container: ''
  name: username
  type: string
- container: ''
  name: fromTimestamp
  type: dateTime
- container: ''
  name: toTimestamp
  type: dateTime
- container: ''
  name: receptionCount
  type: integer
- container: ''
  name: deliveredCount
  type: integer
- container: ''
  name: deferredCount
  type: integer
- container: ''
  name: bouncedCount
  type: integer
- container: ''
  name: failedCount
  type: integer
- container: ''
  name: suppressedCount
  type: integer
- container: ''
  name: openedCount
  type: integer
- container: ''
  name: clickedCount
  type: integer
- container: ''
  name: classification
  type: string
- container: ''
  name: count
  type: integer
- container: set
  name: bounces
  type: string
- container: ''
  name: avgDeliveryTime
  type: decimal
- container: set
  name: deliveryTimes
  type: string
- container: ''
  name: recipientDomain
  type: string
- container: ''
  name: deliveryTime
  type: decimal
property_count: 129
provider_name: AhaSend
provider_slug: ahasend
slug: ahasend-openapi-v2-context
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
- JSON-LD
- Linked Data
- Semantic Web
---
