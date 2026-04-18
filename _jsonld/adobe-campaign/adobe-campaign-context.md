---
class_count: 29
classes:
- DeliveryRequest
- MarketingHistory
- OrgUnit
- PrivacyRequest
- PrivacyRequestResponse
- Profile
- ProfileCreate
- ProfileUpdate
- PushEventRequest
- PushEventResponse
- PushEventsRequest
- QueryDefinition
- QueryResult
- SOAPFault
- Service
- ServiceCreate
- ServiceUpdate
- SessionLogonRequest
- SessionLogonResponse
- SubscriptionRequest
- TransactionalEvent
- TransactionalEventResponse
- TransactionalEventStatus
- WorkflowCommand
- WorkflowPostEventRequest
- WorkflowRequest
- WriteCollectionRequest
- WriteRequest
- WriteResponse
context_file: json-ld/adobe-campaign-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/json-ld/adobe-campaign-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Campaign from Adobe Campaign.
layout: jsonld
name: Adobe Campaign Context
namespaces:
- prefix: ac
  uri: https://developer.adobe.com/campaign/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: PKey
  type: string
- container: ''
  name: activity
  type: string
- container: ''
  name: birthDate
  type: string
- container: ''
  name: blackList
  type: boolean
- container: ''
  name: blackListEmail
  type: boolean
- container: ''
  name: blackListMobile
  type: boolean
- container: ''
  name: collection
  type: reference
- container: ''
  name: create
  type: boolean
- container: ''
  name: created
  type: dateTime
- container: ''
  name: ctx
  type: reference
- container: ''
  name: deliveryId
  type: integer
- container: ''
  name: deliveryName
  type: string
- container: ''
  name: detail
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: end
  type: dateTime
- container: ''
  name: entity
  type: reference
- container: ''
  name: eventId
  type: integer
- container: set
  name: events
  type: string
- container: ''
  name: expiration
  type: dateTime
- container: ''
  name: faultcode
  type: string
- container: ''
  name: faultstring
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: gender
  type: string
- container: ''
  name: label
  type: string
- container: ''
  name: lastModified
  type: dateTime
- container: ''
  name: lastName
  type: string
- container: ''
  name: messageType
  type: string
- container: ''
  name: method
  type: string
- container: ''
  name: mobilePhone
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: namespaceName
  type: string
- container: ''
  name: parentTitle
  type: string
- container: ''
  name: phone
  type: string
- container: ''
  name: preferredLanguage
  type: string
- container: ''
  name: primaryKey
  type: string
- container: ''
  name: pushPlatform
  type: string
- container: ''
  name: queryDef
  type: reference
- container: ''
  name: reason
  type: string
- container: ''
  name: recipient
  type: reference
- container: ''
  name: reconciliationValue
  type: string
- container: ''
  name: regulation
  type: string
- container: ''
  name: resultSet
  type: reference
- container: ''
  name: rtEvent
  type: reference
- container: ''
  name: scheduled
  type: dateTime
- container: ''
  name: securityToken
  type: string
- container: ''
  name: service
  type: reference
- container: ''
  name: serviceName
  type: string
- container: ''
  name: sessionInfo
  type: reference
- container: ''
  name: sessionToken
  type: string
- container: ''
  name: start
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: strLogin
  type: string
- container: ''
  name: strPassword
  type: string
- container: ''
  name: subscriptions
  type: reference
- container: ''
  name: type
  type: string
- container: ''
  name: variables
  type: reference
- container: ''
  name: workflowId
  type: integer
property_count: 57
provider_name: Adobe Campaign
provider_slug: adobe-campaign
slug: adobe-campaign-context
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
- JSON-LD
- Linked Data
- Semantic Web
---
