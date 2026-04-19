---
class_count: 9
classes:
- ResponseAdditionalDataBillingAddress
- ResponseAdditionalDataCard
- ResponseAdditionalDataCommon
- ResponseAdditionalDataDomesticError
- ResponseAdditionalDataInstallments
- ResponseAdditionalDataNetworkTokens
- ResponseAdditionalDataOpi
- ResponseAdditionalDataSepa
- ResponseAdditionalData3DSecure
context_file: json-ld/adyen-checkout-response-additional-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-response-additional-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Response Additional from Adyen.
layout: jsonld
name: Adyen Checkout Response Additional Context
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
  name: billingAddress.city
  type: string
- container: ''
  name: billingAddress.country
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
  name: cardBin
  type: string
- container: ''
  name: cardHolderName
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
  name: cardSummary
  type: string
- container: ''
  name: issuerBin
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
  name: alias
  type: string
- container: ''
  name: aliasType
  type: string
- container: ''
  name: authCode
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
  name: bic
  type: string
- container: ''
  name: coBrandedWith
  type: string
- container: ''
  name: cvcResult
  type: string
- container: ''
  name: cvcResultRaw
  type: string
- container: ''
  name: dsTransID
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
  name: fraudCheck[itemnr][fraudcheckname]
  type: string
- container: ''
  name: fraudManualReview
  type: string
- container: ''
  name: fraudResultType
  type: string
- container: ''
  name: fundingSource
  type: string
- container: ''
  name: fundsAvailability
  type: string
- container: ''
  name: inferredRefusalReason
  type: string
- container: ''
  name: isCardCommercial
  type: string
- container: ''
  name: issuerCountry
  type: string
- container: ''
  name: liabilityShift
  type: string
- container: ''
  name: mcBankNetReferenceNumber
  type: string
- container: ''
  name: merchantAdviceCode
  type: string
- container: ''
  name: merchantReference
  type: string
- container: ''
  name: networkTxReference
  type: string
- container: ''
  name: ownerName
  type: string
- container: ''
  name: paymentAccountReference
  type: string
- container: ''
  name: paymentMethod
  type: string
- container: ''
  name: paymentMethodVariant
  type: string
- container: ''
  name: payoutEligible
  type: string
- container: ''
  name: realtimeAccountUpdaterStatus
  type: string
- container: ''
  name: receiptFreeText
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
  name: recurring.shopperReference
  type: string
- container: ''
  name: recurringProcessingModel
  type: string
- container: ''
  name: referred
  type: string
- container: ''
  name: refusalReasonRaw
  type: string
- container: ''
  name: requestAmount
  type: string
- container: ''
  name: requestCurrencyCode
  type: string
- container: ''
  name: shopperInteraction
  type: string
- container: ''
  name: shopperReference
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
  name: visaTransactionId
  type: string
- container: ''
  name: xid
  type: string
- container: ''
  name: domesticRefusalReasonRaw
  type: string
- container: ''
  name: domesticShopperAdvice
  type: string
- container: ''
  name: installmentPaymentData.installmentType
  type: string
- container: ''
  name: installmentPaymentData.option[itemNr].annualPercentageRate
  type: string
- container: ''
  name: installmentPaymentData.option[itemNr].firstInstallmentAmount
  type: string
- container: ''
  name: installmentPaymentData.option[itemNr].installmentFee
  type: string
- container: ''
  name: installmentPaymentData.option[itemNr].interestRate
  type: string
- container: ''
  name: installmentPaymentData.option[itemNr].maximumNumberOfInstallments
  type: string
- container: ''
  name: installmentPaymentData.option[itemNr].minimumNumberOfInstallments
  type: string
- container: ''
  name: installmentPaymentData.option[itemNr].numberOfInstallments
  type: string
- container: ''
  name: installmentPaymentData.option[itemNr].subsequentInstallmentAmount
  type: string
- container: ''
  name: installmentPaymentData.option[itemNr].totalAmountDue
  type: string
- container: ''
  name: installmentPaymentData.paymentOptions
  type: string
- container: ''
  name: installments.value
  type: string
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
  name: opi.transToken
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
  name: cardHolderInfo
  type: string
- container: ''
  name: cavv
  type: string
- container: ''
  name: cavvAlgorithm
  type: string
- container: ''
  name: scaExemptionRequested
  type: string
- container: ''
  name: threeds2.cardEnrolled
  type: boolean
property_count: 99
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-response-additional-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
