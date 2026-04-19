---
description: NotificationAdditionalData schema from Adyen API
layout: schema
name: NotificationAdditionalData
properties_list:
- description: Reference of the payment account.
  name: PaymentAccountReference
  type: string
- description: The acquirer account code.
  name: acquirerAccountCode
  type: string
- description: The acquirer code.
  name: acquirerCode
  type: string
- description: The acquirer reference.
  name: acquirerReference
  type: string
- description: ACS interface. Related to 3DS.
  name: acsRenderingType.acsInterface
  type: string
- description: ACS UI template.
  name: acsRenderingType.acsUiTemplate
  type: string
- description: Alias for this card.
  name: alias
  type: string
- description: Alias type.
  name: aliasType
  type: string
- description: Acquirer Reference Number of the dispute.
  name: arn
  type: string
- description: Authcode of the scheme.
  name: authCode
  type: string
- description: 3DS authentication type
  name: authenticationType
  type: string
- description: Authorisation MID of the acquirer.
  name: authorisationMid
  type: string
- description: The currency authorised for a dynamic zero auth request.
  name: authorisedAmountCurrency
  type: string
- description: The amount authorised for a dynamic zero auth request.
  name: authorisedAmountValue
  type: string
- description: Address Verification Service result.
  name: avsResult
  type: string
- description: Address Verification Service result raw.
  name: avsResultRaw
  type: string
- description: The bank account number.
  name: bankAccountNumber
  type: string
- description: The bank location.
  name: bankLocation
  type: string
- description: The bank location ID.
  name: bankLocationId
  type: string
- description: The bank name.
  name: bankName
  type: string
- description: The bank verificaiton result.
  name: bankVerificationResult
  type: string
- description: The bank verification result raw.
  name: bankVerificationResultRaw
  type: string
- description: Business Identifier Code.
  name: bic
  type: string
- description: 'BillingAddress: county.'
  name: billingAddress.city
  type: string
- description: 'BillingAddress: house number or name.'
  name: billingAddress.houseNumberOrName
  type: string
- description: 'BillingAddress: postal code.'
  name: billingAddress.postalCode
  type: string
- description: 'BillingAddress: state or province'
  name: billingAddress.stateOrProvince
  type: string
- description: 'BillingAddress: street'
  name: billingAddress.street
  type: string
- description: Browser code.
  name: browserCode
  type: string
- description: The amount of delay after authorisation.
  name: captureDelayHours
  type: string
- description: The merchant reference of the capture.
  name: captureMerchantReference
  type: string
- description: The PSP reference of the capture.
  name: capturePspReference
  type: string
- description: Card Bank Identification number.
  name: cardBin
  type: string
- description: Card issuing bank.
  name: cardIssuingBank
  type: string
- description: Card issuing country.
  name: cardIssuingCountry
  type: string
- description: Card issuing currency.
  name: cardIssuingCurrency
  type: string
- description: Card payment method.
  name: cardPaymentMethod
  type: string
- description: Card scheme enhanced data level.
  name: cardSchemeEnhancedDataLevel
  type: string
- description: Card summary
  name: cardSummary
  type: string
- description: Secure Cardholder Authentication Verification Value.
  name: cavv
  type: string
- description: CAVV algorithm.
  name: cavvAlgorithm
  type: string
- description: Information about the 3DS challenge being canceled.
  name: challengeCancel
  type: string
- description: ID of the Checkout Session.
  name: checkoutSessionId
  type: string
- description: Card Verification Code result.
  name: cvcResult
  type: string
- description: Card Verification Code result raw.
  name: cvcResultRaw
  type: string
- description: 'Delivery address: city.'
  name: deliveryAddress.city
  type: string
- description: 'Delivery address: country.'
  name: deliveryAddress.country
  type: string
- description: 'Delivery address: house number or name.'
  name: deliveryAddress.houseNumberOrName
  type: string
- description: 'Delivery address: postal code.'
  name: deliveryAddress.postalCode
  type: string
- description: 'Delivery address: state or province.'
  name: deliveryAddress.stateOrProvince
  type: string
- description: 'Delivery address: street.'
  name: deliveryAddress.street
  type: string
- description: Type of device the request was made from.
  name: deviceType
  type: string
- description: 'Direct debit GB: date of signature.'
  name: directdebit_GB.dateOfSignature
  type: string
- description: 'Direct debit GB: mandate ID.'
  name: directdebit_GB.mandateId
  type: string
- description: 'Direct debit GB: sequence type.'
  name: directdebit_GB.sequenceType
  type: string
- description: 'Direct debit GB: service user name.'
  name: directdebit_GB.serviceUserName
  type: string
- description: 'Direct debit GB: service user number.'
  name: directdebit_GB.serviceUserNumber
  type: string
- description: '3DS: Electronic Commerce Indicator.'
  name: eci
  type: string
- description: Expiry date of the card.
  name: expiryDate
  type: string
- description: Additional cost used in [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification).
  name: extraCostsCurrency
  type: string
- description: Related additional cost value.
  name: extraCostsValue
  type: string
- description: Gratuity related additional cost value.
  name: extraCostsValueGratuity
  type: string
- description: Surcharge related additional cost value.
  name: extraCostsValueSurcharge
  type: string
- description: Information on the fraud check in a dynamic format.
  name: fraudCheck-<check ID>-<name>
  type: string
- description: Indicates if the risk check was done manually.
  name: fraudManualReview
  type: string
- description: The fraud offset.
  name: fraudOffset
  type: string
- description: Result type of the fraud check.
  name: fraudResultType
  type: string
- description: Funding source.
  name: fundingSource
  type: string
- description: Chargeback gross currency.
  name: grossCurrency
  type: string
- description: Chargeback gross value.
  name: grossValue
  type: string
- description: International Bank Account Number.
  name: iban
  type: string
- description: 'The number of installments that the payment amount should be charged with. Example: 5 > Only relevant for card payments in countries that support installments.'
  name: installments.value
  type: string
- description: 3DS interaction counter.
  name: interactionCounter
  type: string
- description: Card holder name.
  name: issuerComments.cardholderName
  type: string
- description: Country of the card issuer.
  name: issuerCountry
  type: string
- description: 'Recurring: Latest card BIN.'
  name: latestCard.bin
  type: string
- description: 'Recurring: Latest card expiry date.'
  name: latestCard.expiryDate
  type: string
- description: 'Recurring: Latest card summary.'
  name: latestCard.summary
  type: string
- description: Risk liability shift.
  name: liabilityShift
  type: string
- description: 'A set of key-value pairs provided in the request, prefixed with ''metadata.''. For example, ''metadata.myField: myValue'''
  name: metadata
  type: object
- description: Recurring related.
  name: networkToken.available
  type: string
- description: Recurring related.
  name: networkToken.bin
  type: string
- description: Recurring related.
  name: networkToken.tokenSummary
  type: string
- description: NFC related.
  name: nfc.expire
  type: string
- description: NFC related.
  name: nfc.issue
  type: string
- description: NFC related.
  name: nfc.pin.provided
  type: string
- description: NFC related.
  name: nfc.uid
  type: string
- description: Trans token related to Oracle Opera.
  name: opi.transToken
  type: string
- description: Owner city.
  name: ownerCity
  type: string
- description: Owner name.
  name: ownerName
  type: string
- description: Related to PayU in LATAM.
  name: payULatamTrazabilityCode
  type: string
- description: ID of the Checkout payment link.
  name: paymentLinkId
  type: string
- description: Real time Account Update status.
  name: realtimeAccountUpdaterStatus
  type: string
- description: Recurring contract types.
  name: recurring.contractTypes
  type: string
- description: Recurring first PSP reference.
  name: recurring.firstPspReference
  type: string
- description: The [token for stored payment details](https://docs.adyen.com/online-payments/tokenization/create-and-use-tokens/) to make recurring payments.
  name: recurring.recurringDetailReference
  type: string
- description: 'If the payment is referred, this field is set to true. This field is unavailable if the payment is referred and is usually not returned with ecommerce transactions. Example: true'
  name: referred
  type: string
- description: 'Raw refusal reason received from the acquirer, where available. Example: AUTHORISED'
  name: refusalReasonRaw
  type: string
- description: Indicates if an auto rescue for a pyment is scheduled.
  name: retry.rescueScheduled
  type: string
- description: Related to Risk.
  name: riskProfile
  type: string
- description: Related to Risk.
  name: riskProfileReference
  type: string
- description: Country of the shopper.
  name: shopperCountry
  type: string
- description: Email of the shopper.
  name: shopperEmail
  type: string
- description: IP of the shopper.
  name: shopperIP
  type: string
- description: 'The shopper interaction type of the payment request. Example: Ecommerce'
  name: shopperInteraction
  type: string
- description: The locale of the shopper.
  name: shopperLocale
  type: string
- description: The social security number of the shopper.
  name: shopperSocialSecurityNumber
  type: string
- description: The text to be shown on the shopper's bank statement.
  name: shopperStatement
  type: string
- description: The telephone number of the shopper.
  name: shopperTelephone
  type: string
- description: Identifier of the store processing the transaction.
  name: store
  type: string
- description: Tender reference. For point-of-sale integrations only.
  name: tenderReference
  type: string
- description: Terminal ID. For point-of-sale integrations only.
  name: terminalId
  type: string
- description: 'A Boolean value indicating whether 3DS authentication was completed on this payment. Example: true'
  name: threeDAuthenticated
  type: string
- description: 'The raw 3DS authentication result from the card issuer. Example: N'
  name: threeDAuthenticatedResponse
  type: string
- description: 'A Boolean value indicating whether 3DS was offered for this payment. Example: true'
  name: threeDOffered
  type: string
- description: 'The raw enrollment result from the 3DS directory services of the card schemes. Example: Y'
  name: threeDOfferedResponse
  type: string
- description: The 3D Secure 2 version.
  name: threeDSVersion
  type: string
- description: Payment method variant of the token/wallet payment method.
  name: tokenTxVariant
  type: string
- description: Total fraud score from risk.
  name: totalFraudScore
  type: string
- description: Card summary without tokenization.
  name: untokenisedCardSummary
  type: string
- description: The 3DS transaction ID of the 3DS session sent in notifications. The value is Base64-encoded and is returned for transactions with directoryResponse 'N' or 'Y'. If you want to submit the xid in your 3
  name: xid
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/webhooks-notification-additional-data-schema.json
slug: webhooks-notification-additional-data
tags:
- Payments
- Financial Services
- Fintech
title: NotificationAdditionalData
---
