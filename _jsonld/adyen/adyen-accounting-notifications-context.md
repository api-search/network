---
class_count: 40
classes:
- AdditionalBankIdentification
- Address-2
- AmountAdjustment
- Amount
- AULocalAccountIdentification
- BalanceMutation
- BalancePlatformNotificationResponse
- BankAccountV3
- BRLocalAccountIdentification
- CALocalAccountIdentification
- CounterpartyV3
- CZLocalAccountIdentification
- DKLocalAccountIdentification
- HULocalAccountIdentification
- IbanAccountIdentification
- MerchantData
- NameLocation
- NOLocalAccountIdentification
- NumberAndBicAccountIdentification
- PartyIdentification-2
- PaymentInstrument
- PLLocalAccountIdentification
- RelayedAuthorisationData-2
- ResourceReference
- Resource
- SELocalAccountIdentification
- SGLocalAccountIdentification
- TransactionEventViolation
- TransactionRuleReference
- TransactionRuleSource
- TransactionRulesResult
- TransferEvent
- TransferNotificationData
- TransferNotificationRequest
- TransferNotificationTransferTracking
- TransferNotificationValidationFact
- UKLocalAccountIdentification
- USLocalAccountIdentification
- name
- description
context_file: json-ld/adyen-accounting-notifications-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounting-notifications-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounting Notifications from Adyen.
layout: jsonld
name: Adyen Accounting Notifications Context
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
  name: code
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: line1
  type: string
- container: ''
  name: line2
  type: string
- container: ''
  name: postalCode
  type: string
- container: ''
  name: stateOrProvince
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: amountAdjustmentType
  type: string
- container: ''
  name: basepoints
  type: integer
- container: ''
  name: currency
  type: string
- container: ''
  name: value
  type: integer
- container: ''
  name: accountNumber
  type: string
- container: ''
  name: bsbCode
  type: string
- container: ''
  name: balance
  type: integer
- container: ''
  name: received
  type: integer
- container: ''
  name: reserved
  type: integer
- container: ''
  name: notificationResponse
  type: string
- container: ''
  name: accountHolder
  type: string
- container: ''
  name: accountIdentification
  type: string
- container: ''
  name: bankCode
  type: string
- container: ''
  name: branchNumber
  type: string
- container: ''
  name: institutionNumber
  type: string
- container: ''
  name: transitNumber
  type: string
- container: ''
  name: balanceAccountId
  type: string
- container: ''
  name: bankAccount
  type: string
- container: ''
  name: merchant
  type: string
- container: ''
  name: transferInstrumentId
  type: string
- container: ''
  name: iban
  type: string
- container: ''
  name: mcc
  type: string
- container: ''
  name: merchantId
  type: string
- container: ''
  name: nameLocation
  type: string
- container: ''
  name: countryOfOrigin
  type: string
- container: ''
  name: rawData
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: additionalBankIdentification
  type: string
- container: ''
  name: bic
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: fullName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: tokenType
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: balancePlatform
  type: string
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: clearingNumber
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: transactionRule
  type: string
- container: ''
  name: transactionRuleSource
  type: string
- container: ''
  name: advice
  type: string
- container: ''
  name: allRulesPassed
  type: boolean
- container: set
  name: failedTransactionRules
  type: string
- container: ''
  name: score
  type: integer
- container: set
  name: amountAdjustments
  type: string
- container: ''
  name: bookingDate
  type: dateTime
- container: set
  name: mutations
  type: string
- container: ''
  name: originalAmount
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: transactionId
  type: string
- container: ''
  name: updateDate
  type: dateTime
- container: ''
  name: valueDate
  type: dateTime
- container: ''
  name: balanceAccount
  type: string
- container: set
  name: balances
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: counterparty
  type: string
- container: ''
  name: direction
  type: string
- container: set
  name: events
  type: string
- container: ''
  name: modificationMerchantReference
  type: string
- container: ''
  name: modificationPspReference
  type: string
- container: ''
  name: panEntryMode
  type: string
- container: ''
  name: paymentInstrument
  type: string
- container: ''
  name: paymentInstrumentId
  type: string
- container: ''
  name: paymentMerchantReference
  type: string
- container: ''
  name: priority
  type: string
- container: ''
  name: processingType
  type: string
- container: ''
  name: pspPaymentReference
  type: string
- container: ''
  name: referenceForBeneficiary
  type: string
- container: ''
  name: relayedAuthorisationData
  type: string
- container: ''
  name: sequenceNumber
  type: integer
- container: ''
  name: tracking
  type: string
- container: ''
  name: transactionRulesResult
  type: string
- container: set
  name: validationFacts
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: environment
  type: string
- container: ''
  name: result
  type: string
- container: ''
  name: sortCode
  type: string
- container: ''
  name: accountType
  type: string
- container: ''
  name: routingNumber
  type: string
property_count: 91
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounting-notifications-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
