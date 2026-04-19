---
class_count: 27
classes:
- AchNotificationOfChangeNotificationRequestDataNoc
- AchNotificationOfChangeNotificationRequestData
- AchNotificationOfChangeNotificationRequest
- Amount
- AuthorisationNotificationAdditionalData
- AuthorisationNotificationRequestItem
- AuthorisationNotificationRequestItemWrapper
- AuthorisationNotificationRequest
- ExpireNotificationRequestItem
- ExpireNotificationRequestItemWrapper
- ExpireNotificationRequest
- NotificationAdditionalData
- NotificationRequestItem
- NotificationRequestItemWrapper
- NotificationRequest
- NotificationResponse
- PaidoutReversedNotificationRequestItem
- PaidoutReversedNotificationRequestItemWrapper
- PaidoutReversedNotificationRequest
- RecurringContractNotificationAdditionalData
- RecurringContractNotificationRequestItem
- RecurringContractNotificationRequestItemWrapper
- RecurringContractNotificationRequest
- ReportAvailableNotificationRequestItem
- ReportAvailableNotificationRequestItemWrapper
- ReportAvailableNotificationRequest
- version
context_file: json-ld/adyen-webhooks-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-webhooks-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Webhooks from Adyen.
layout: jsonld
name: Adyen Webhooks Context
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
  name: newBankAccountNumber
  type: string
- container: ''
  name: newBankAccountType
  type: string
- container: ''
  name: newBranchCode
  type: string
- container: ''
  name: reasonCode
  type: string
- container: ''
  name: notificationOfChange
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: shopperReference
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
  name: type
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: value
  type: integer
- container: ''
  name: PaymentAccountReference
  type: string
- container: ''
  name: acquirerAccountCode
  type: string
- container: ''
  name: acquirerCode
  type: string
- container: ''
  name: acquirerReference
  type: string
- container: ''
  name: acsRenderingType.acsInterface
  type: string
- container: ''
  name: acsRenderingType.acsUiTemplate
  type: string
- container: ''
  name: alias
  type: string
- container: ''
  name: aliasType
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: authCode
  type: string
- container: ''
  name: authenticationType
  type: string
- container: ''
  name: authorisationMid
  type: string
- container: ''
  name: authorisedAmountCurrency
  type: string
- container: ''
  name: authorisedAmountValue
  type: string
- container: ''
  name: avsResult
  type: string
- container: ''
  name: avsResultRaw
  type: string
- container: ''
  name: bankAccountNumber
  type: string
- container: ''
  name: bankLocation
  type: string
- container: ''
  name: bankLocationId
  type: string
- container: ''
  name: bankName
  type: string
- container: ''
  name: bankVerificationResult
  type: string
- container: ''
  name: bankVerificationResultRaw
  type: string
- container: ''
  name: bic
  type: string
- container: ''
  name: billingAddress.city
  type: string
- container: ''
  name: billingAddress.houseNumberOrName
  type: string
- container: ''
  name: billingAddress.postalCode
  type: string
- container: ''
  name: billingAddress.stateOrProvince
  type: string
- container: ''
  name: billingAddress.street
  type: string
- container: ''
  name: browserCode
  type: string
- container: ''
  name: captureDelayHours
  type: string
- container: ''
  name: captureMerchantReference
  type: string
- container: ''
  name: capturePspReference
  type: string
- container: ''
  name: cardBin
  type: string
- container: ''
  name: cardIssuingBank
  type: string
- container: ''
  name: cardIssuingCountry
  type: string
- container: ''
  name: cardIssuingCurrency
  type: string
- container: ''
  name: cardPaymentMethod
  type: string
- container: ''
  name: cardSchemeEnhancedDataLevel
  type: string
- container: ''
  name: cardSummary
  type: string
- container: ''
  name: cavv
  type: string
- container: ''
  name: cavvAlgorithm
  type: string
- container: ''
  name: challengeCancel
  type: string
- container: ''
  name: checkoutSessionId
  type: string
- container: ''
  name: cvcResult
  type: string
- container: ''
  name: cvcResultRaw
  type: string
- container: ''
  name: deliveryAddress.city
  type: string
- container: ''
  name: deliveryAddress.country
  type: string
- container: ''
  name: deliveryAddress.houseNumberOrName
  type: string
- container: ''
  name: deliveryAddress.postalCode
  type: string
- container: ''
  name: deliveryAddress.stateOrProvince
  type: string
- container: ''
  name: deliveryAddress.street
  type: string
- container: ''
  name: deviceType
  type: string
- container: ''
  name: directdebitGb.dateofsignature
  type: string
- container: ''
  name: directdebitGb.mandateid
  type: string
- container: ''
  name: directdebitGb.sequencetype
  type: string
- container: ''
  name: directdebitGb.serviceusername
  type: string
- container: ''
  name: directdebitGb.serviceusernumber
  type: string
- container: ''
  name: eci
  type: string
- container: ''
  name: expiryDate
  type: string
- container: ''
  name: extraCostsCurrency
  type: string
- container: ''
  name: extraCostsValue
  type: string
- container: ''
  name: extraCostsValueGratuity
  type: string
- container: ''
  name: extraCostsValueSurcharge
  type: string
- container: ''
  name: fraudCheck<check id><name>
  type: string
- container: ''
  name: fraudManualReview
  type: string
- container: ''
  name: fraudOffset
  type: string
- container: ''
  name: fraudResultType
  type: string
- container: ''
  name: fundingSource
  type: string
- container: ''
  name: grossCurrency
  type: string
- container: ''
  name: grossValue
  type: string
- container: ''
  name: iDealConsumerAccountNumber
  type: string
- container: ''
  name: iDealConsumerBIC
  type: string
- container: ''
  name: iDealConsumerCity
  type: string
- container: ''
  name: iDealConsumerIBAN
  type: string
- container: ''
  name: iDealConsumerIban
  type: string
- container: ''
  name: iDealConsumerName
  type: string
- container: ''
  name: iDealTransactionId
  type: string
- container: ''
  name: iban
  type: string
- container: ''
  name: installments.value
  type: string
- container: ''
  name: interactionCounter
  type: string
- container: ''
  name: issuerComments.cardholderName
  type: string
- container: ''
  name: issuerCountry
  type: string
- container: ''
  name: latestCard.bin
  type: string
- container: ''
  name: latestCard.expiryDate
  type: string
- container: ''
  name: latestCard.summary
  type: string
- container: ''
  name: liabilityShift
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: networkToken.available
  type: string
- container: ''
  name: networkToken.bin
  type: string
- container: ''
  name: networkToken.tokenSummary
  type: string
- container: ''
  name: nfc.expire
  type: string
- container: ''
  name: nfc.issue
  type: string
- container: ''
  name: nfc.pin.provided
  type: string
- container: ''
  name: nfc.uid
  type: string
- container: ''
  name: opi.transToken
  type: string
- container: ''
  name: ownerCity
  type: string
- container: ''
  name: ownerName
  type: string
- container: ''
  name: payULatamTrazabilityCode
  type: string
- container: ''
  name: paymentLinkId
  type: string
- container: ''
  name: paypalAddressStatus
  type: string
- container: ''
  name: paypalBillingName
  type: string
- container: ''
  name: paypalEmail
  type: string
- container: ''
  name: paypalErrorCode
  type: string
- container: ''
  name: paypalErrorDescription
  type: string
- container: ''
  name: paypalPairingId
  type: string
- container: ''
  name: paypalPayerId
  type: string
- container: ''
  name: paypalPayerResidenceCountry
  type: string
- container: ''
  name: paypalPayerStatus
  type: string
- container: ''
  name: paypalPhone
  type: string
- container: ''
  name: paypalProtectionEligibility
  type: string
- container: ''
  name: paypalRisk
  type: string
- container: ''
  name: realtimeAccountUpdaterStatus
  type: string
- container: ''
  name: recurring.contractTypes
  type: string
- container: ''
  name: recurring.firstPspReference
  type: string
- container: ''
  name: recurring.recurringDetailReference
  type: string
- container: ''
  name: referred
  type: string
- container: ''
  name: refusalReasonRaw
  type: string
- container: ''
  name: retry.rescueScheduled
  type: string
- container: ''
  name: riskProfile
  type: string
- container: ''
  name: riskProfileReference
  type: string
- container: ''
  name: sepadirectdebit.dateOfSignature
  type: string
- container: ''
  name: sepadirectdebit.mandateId
  type: string
- container: ''
  name: sepadirectdebit.sequenceType
  type: string
- container: ''
  name: shopperCountry
  type: string
- container: ''
  name: shopperEmail
  type: string
- container: ''
  name: shopperIP
  type: string
- container: ''
  name: shopperInteraction
  type: string
- container: ''
  name: shopperLocale
  type: string
- container: ''
  name: shopperSocialSecurityNumber
  type: string
- container: ''
  name: shopperStatement
  type: string
- container: ''
  name: shopperTelephone
  type: string
- container: ''
  name: store
  type: string
- container: ''
  name: tenderReference
  type: string
- container: ''
  name: terminalId
  type: string
- container: ''
  name: threeDAuthenticated
  type: string
- container: ''
  name: threeDAuthenticatedResponse
  type: string
- container: ''
  name: threeDOffered
  type: string
- container: ''
  name: threeDOfferedResponse
  type: string
- container: ''
  name: threeDSVersion
  type: string
- container: ''
  name: tokenTxVariant
  type: string
- container: ''
  name: totalFraudScore
  type: string
- container: ''
  name: untokenisedCardSummary
  type: string
- container: ''
  name: xid
  type: string
- container: ''
  name: additionalData
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: eventCode
  type: string
- container: ''
  name: eventDate
  type: dateTime
- container: ''
  name: merchantAccountCode
  type: string
- container: ''
  name: merchantReference
  type: string
- container: set
  name: operations
  type: string
- container: ''
  name: paymentMethod
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: success
  type: string
- container: ''
  name: live
  type: string
- container: set
  name: notificationItems
  type: string
- container: ''
  name: originalReference
  type: string
- container: ''
  name: notificationResponse
  type: string
- container: ''
  name: originalPsp
  type: string
property_count: 171
provider_name: Adyen
provider_slug: adyen
slug: adyen-webhooks-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
