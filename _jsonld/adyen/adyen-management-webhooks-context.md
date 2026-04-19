---
class_count: 17
classes:
- AccountCapabilityData
- AccountCreateNotificationData
- AccountNotificationResponse
- AccountUpdateNotificationData
- CapabilityProblemEntity-recursive
- CapabilityProblemEntity
- CapabilityProblem
- MerchantCreatedNotificationRequest
- MerchantUpdatedNotificationRequest
- MidServiceNotificationData
- PaymentMethodCreatedNotificationRequest
- PaymentMethodNotificationResponse
- PaymentMethodRequestRemovedNotificationRequest
- PaymentMethodScheduledForRemovalNotificationRequest
- RemediatingAction
- VerificationError-recursive
- VerificationError
context_file: json-ld/adyen-management-webhooks-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-webhooks-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Webhooks from Adyen.
layout: jsonld
name: Adyen Management Webhooks Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: allowed
  type: boolean
- container: ''
  name: allowedLevel
  type: string
- container: ''
  name: capability
  type: string
- container: set
  name: problems
  type: string
- container: ''
  name: requested
  type: boolean
- container: ''
  name: requestedLevel
  type: string
- container: ''
  name: verificationDeadline
  type: dateTime
- container: ''
  name: verificationStatus
  type: string
- container: ''
  name: capabilities
  type: reference
- container: ''
  name: companyId
  type: string
- container: ''
  name: legalEntityId
  type: string
- container: ''
  name: merchantId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: notificationResponse
  type: string
- container: set
  name: documents
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: owner
  type: string
- container: ''
  name: entity
  type: string
- container: set
  name: verificationErrors
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: data
  type: string
- container: ''
  name: environment
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: reference
  type: string
- container: ''
  name: storeId
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: message
  type: string
- container: set
  name: remediatingActions
  type: string
- container: set
  name: subErrors
  type: string
property_count: 30
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-webhooks-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
