---
class_count: 50
classes:
- AccountHolderCapability
- AccountHolderNotificationData
- AccountHolderNotificationRequest
- AccountHolder
- AccountSupportingEntityCapability
- Address
- Amount
- Authentication
- BalanceAccountNotificationData
- BalanceAccountNotificationRequest
- BalanceAccount
- BalancePlatformNotificationResponse
- Balance
- BulkAddress
- CapabilityProblemEntity-recursive
- CapabilityProblemEntity
- CapabilityProblem
- CapabilitySettings
- CardConfiguration
- CardOrderItemDeliveryStatus
- CardOrderItem
- CardOrderNotificationRequest
- Card
- ContactDetails
- Contact
- Expiry
- IbanAccountIdentification
- Name
- PaymentInstrumentNotificationData
- PaymentInstrumentReference
- PaymentInstrument
- PaymentNotificationRequest
- PersonalData
- PhoneNumber
- Phone
- PlatformPaymentConfiguration
- RemediatingAction
- Resource
- SweepConfigurationNotificationData
- SweepConfigurationNotificationRequest
- SweepConfigurationV2
- SweepCounterparty
- SweepSchedule
- USLocalAccountIdentification
- VerificationDeadline
- VerificationError-recursive
- VerificationError
- description
- email
- name
context_file: json-ld/adyen-configuration-webhooks-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-webhooks-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Webhooks from Adyen.
layout: jsonld
name: Adyen Configuration Webhooks Context
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
  name: allowedSettings
  type: string
- container: ''
  name: enabled
  type: boolean
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
  name: requestedSettings
  type: string
- container: set
  name: transferInstruments
  type: string
- container: ''
  name: verificationStatus
  type: string
- container: ''
  name: accountHolder
  type: string
- container: ''
  name: balancePlatform
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: environment
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: capabilities
  type: reference
- container: ''
  name: contactDetails
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: legalEntityId
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: migratedAccountHolderCode
  type: string
- container: ''
  name: primaryBalanceAccount
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: timeZone
  type: string
- container: set
  name: verificationDeadlines
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: houseNumberOrName
  type: string
- container: ''
  name: postalCode
  type: string
- container: ''
  name: stateOrProvince
  type: string
- container: ''
  name: street
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: value
  type: integer
- container: ''
  name: password
  type: string
- container: ''
  name: phone
  type: string
- container: ''
  name: balanceAccount
  type: string
- container: ''
  name: accountHolderId
  type: string
- container: set
  name: balances
  type: string
- container: ''
  name: defaultCurrencyCode
  type: string
- container: ''
  name: migratedAccountCode
  type: string
- container: set
  name: paymentInstruments
  type: string
- container: ''
  name: platformPaymentConfiguration
  type: string
- container: ''
  name: notificationResponse
  type: string
- container: ''
  name: available
  type: integer
- container: ''
  name: balance
  type: integer
- container: ''
  name: pending
  type: integer
- container: ''
  name: reserved
  type: integer
- container: ''
  name: company
  type: string
- container: ''
  name: mobile
  type: string
- container: set
  name: documents
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
  name: amountPerIndustry
  type: reference
- container: ''
  name: authorizedCardUsers
  type: boolean
- container: set
  name: fundingSource
  type: string
- container: ''
  name: interval
  type: string
- container: ''
  name: maxAmount
  type: string
- container: ''
  name: activation
  type: string
- container: ''
  name: activationUrl
  type: string
- container: ''
  name: bulkAddress
  type: string
- container: ''
  name: cardImageId
  type: string
- container: ''
  name: carrier
  type: string
- container: ''
  name: carrierImageId
  type: string
- container: ''
  name: configurationProfileId
  type: string
- container: ''
  name: envelope
  type: string
- container: ''
  name: insert
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: logoImageId
  type: string
- container: ''
  name: pinMailer
  type: string
- container: ''
  name: shipmentMethod
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: trackingNumber
  type: string
- container: ''
  name: card
  type: string
- container: ''
  name: cardOrderItemId
  type: string
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: paymentInstrumentId
  type: string
- container: ''
  name: pin
  type: string
- container: ''
  name: shippingMethod
  type: string
- container: ''
  name: authentication
  type: string
- container: ''
  name: bin
  type: string
- container: ''
  name: brand
  type: string
- container: ''
  name: brandVariant
  type: string
- container: ''
  name: cardholderName
  type: string
- container: ''
  name: configuration
  type: string
- container: ''
  name: cvc
  type: string
- container: ''
  name: deliveryContact
  type: string
- container: ''
  name: expiration
  type: string
- container: ''
  name: formFactor
  type: string
- container: ''
  name: lastFour
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: threeDSecure
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: webAddress
  type: string
- container: ''
  name: fullPhoneNumber
  type: string
- container: ''
  name: personalData
  type: string
- container: ''
  name: phoneNumber
  type: string
- container: ''
  name: month
  type: string
- container: ''
  name: year
  type: string
- container: ''
  name: iban
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: paymentInstrument
  type: string
- container: ''
  name: balanceAccountId
  type: string
- container: ''
  name: bankAccount
  type: string
- container: ''
  name: issuingCountryCode
  type: string
- container: ''
  name: paymentInstrumentGroupId
  type: string
- container: ''
  name: dateOfBirth
  type: string
- container: ''
  name: idNumber
  type: string
- container: ''
  name: nationality
  type: string
- container: ''
  name: phoneCountryCode
  type: string
- container: ''
  name: phoneType
  type: string
- container: ''
  name: salesDayClosingTime
  type: time
- container: ''
  name: settlementDelayDays
  type: integer
- container: ''
  name: code
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: accountId
  type: string
- container: ''
  name: sweep
  type: string
- container: ''
  name: counterparty
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: schedule
  type: string
- container: ''
  name: sweepAmount
  type: string
- container: ''
  name: targetAmount
  type: string
- container: ''
  name: triggerAmount
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: transferInstrumentId
  type: string
- container: ''
  name: cronExpression
  type: string
- container: ''
  name: accountNumber
  type: string
- container: ''
  name: accountType
  type: string
- container: ''
  name: routingNumber
  type: string
- container: set
  name: entityIds
  type: string
- container: ''
  name: expiresAt
  type: dateTime
- container: set
  name: remediatingActions
  type: string
- container: set
  name: subErrors
  type: string
property_count: 135
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-webhooks-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
