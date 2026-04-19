---
description: ResponseAdditionalDataCommon schema from Adyen API
layout: schema
name: ResponseAdditionalDataCommon
properties_list:
- description: 'The name of the Adyen acquirer account. Example: PayPalSandbox_TestAcquirer > Only relevant for PayPal transactions.'
  name: acquirerAccountCode
  type: string
- description: 'The name of the acquirer processing the payment request. Example: TestPmmAcquirer'
  name: acquirerCode
  type: string
- description: 'The reference number that can be used for reconciliation in case a non-Adyen acquirer is used for settlement. Example: 7C9N3FNBKT9'
  name: acquirerReference
  type: string
- description: 'The Adyen alias of the card. Example: H167852639363479'
  name: alias
  type: string
- description: 'The type of the card alias. Example: Default'
  name: aliasType
  type: string
- description: 'Authorisation code: * When the payment is authorised successfully, this field holds the authorisation code for the payment. * When the payment is not authorised, this field is empty. Example: 58747'
  name: authCode
  type: string
- description: Merchant ID known by the acquirer.
  name: authorisationMid
  type: string
- description: The currency of the authorised amount, as a three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes).
  name: authorisedAmountCurrency
  type: string
- description: Value of the amount authorised. This amount is represented in minor units according to the [following table](https://docs.adyen.com/development-resources/currency-codes).
  name: authorisedAmountValue
  type: string
- description: The AVS result code of the payment, which provides information about the outcome of the AVS check. For possible values, see [AVS](https://docs.adyen.com/risk-management/configure-standard-risk-rules/c
  name: avsResult
  type: string
- description: 'Raw AVS result received from the acquirer, where available. Example: D'
  name: avsResultRaw
  type: string
- description: 'BIC of a bank account. Example: TESTNL01 > Only relevant for SEPA Direct Debit transactions.'
  name: bic
  type: string
- description: Includes the co-branded card information.
  name: coBrandedWith
  type: string
- description: The result of CVC verification.
  name: cvcResult
  type: string
- description: The raw result of CVC verification.
  name: cvcResultRaw
  type: string
- description: Supported for 3D Secure 2. The unique transaction identifier assigned by the DS to identify a single transaction.
  name: dsTransID
  type: string
- description: 'The Electronic Commerce Indicator returned from the schemes for the 3DS payment session. Example: 02'
  name: eci
  type: string
- description: 'The expiry date on the card. Example: 6/2016 > Returned only in case of a card payment.'
  name: expiryDate
  type: string
- description: 'The currency of the extra amount charged due to additional amounts set in the skin used in the HPP payment request. Example: EUR'
  name: extraCostsCurrency
  type: string
- description: The value of the extra amount charged due to additional amounts set in the skin used in the HPP payment request. The amount is in minor units.
  name: extraCostsValue
  type: string
- description: The fraud score due to a particular fraud check. The fraud check name is found in the key of the key-value pair.
  name: fraudCheck-[itemNr]-[FraudCheckname]
  type: string
- description: Indicates if the payment is sent to manual review.
  name: fraudManualReview
  type: string
- description: The fraud result properties of the payment.
  name: fraudResultType
  type: string
- description: 'Information regarding the funding type of the card. The possible return values are: * CHARGE * CREDIT * DEBIT * PREPAID * PREPAID_RELOADABLE * PREPAID_NONRELOADABLE * DEFFERED_DEBIT > This functionali'
  name: fundingSource
  type: string
- description: 'Indicates availability of funds. Visa: * "I" (fast funds are supported) * "N" (otherwise) Mastercard: * "I" (product type is Prepaid or Debit, or issuing country is in CEE/HGEM list) * "N" (otherwise)'
  name: fundsAvailability
  type: string
- description: 'Provides the more granular indication of why a transaction was refused. When a transaction fails with either "Refused", "Restricted Card", "Transaction Not Permitted", "Not supported" or "DeclinedNon '
  name: inferredRefusalReason
  type: string
- description: Indicates if the card is used for business purposes only.
  name: isCardCommercial
  type: string
- description: 'The issuing country of the card based on the BIN list that Adyen maintains. Example: JP'
  name: issuerCountry
  type: string
- description: A Boolean value indicating whether a liability shift was offered for this payment.
  name: liabilityShift
  type: string
- description: The `mcBankNetReferenceNumber`, is a minimum of six characters and a maximum of nine characters long. > Contact Support Team to enable this field.
  name: mcBankNetReferenceNumber
  type: string
- description: The Merchant Advice Code (MAC) can be returned by Mastercard issuers for refused payments. If present, the MAC contains information about why the payment failed, and whether it can be retried. For mor
  name: merchantAdviceCode
  type: string
- description: The reference provided for the transaction.
  name: merchantReference
  type: string
- description: Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa. This contains either the Mastercard Trace ID or
  name: networkTxReference
  type: string
- description: The owner name of a bank account. Only relevant for SEPA Direct Debit transactions.
  name: ownerName
  type: string
- description: The Payment Account Reference (PAR) value links a network token with the underlying primary account number (PAN). The PAR value consists of 29 uppercase alphanumeric characters.
  name: paymentAccountReference
  type: string
- description: The payment method used in the transaction.
  name: paymentMethod
  type: string
- description: The Adyen sub-variant of the payment method used for the payment request. For more information, refer to [PaymentMethodVariant](https://docs.adyen.com/development-resources/paymentmethodvariant). Exam
  name: paymentMethodVariant
  type: string
- description: 'Indicates whether a payout is eligible or not for this card. Visa: * "Y" * "N" Mastercard: * "Y" (domestic and cross-border) * "D" (only domestic) * "N" (no MoneySend) * "U" (unknown)'
  name: payoutEligible
  type: string
- description: 'The response code from the Real Time Account Updater service. Possible return values are: * CardChanged * CardExpiryChanged * CloseAccount * ContactCardAccountHolder'
  name: realtimeAccountUpdaterStatus
  type: string
- description: Message to be displayed on the terminal.
  name: receiptFreeText
  type: string
- description: The recurring contract types applicable to the transaction.
  name: recurring.contractTypes
  type: string
- description: The `pspReference`, of the first recurring payment that created the recurring detail. This functionality requires additional configuration on Adyen's end. To enable it, contact the Support Team.
  name: recurring.firstPspReference
  type: string
- description: The reference that uniquely identifies the recurring transaction.
  name: recurring.recurringDetailReference
  type: string
- description: The provided reference of the shopper for a recurring transaction.
  name: recurring.shopperReference
  type: string
- description: The processing model used for the recurring transaction.
  name: recurringProcessingModel
  type: string
- description: 'If the payment is referred, this field is set to true. This field is unavailable if the payment is referred and is usually not returned with ecommerce transactions. Example: true'
  name: referred
  type: string
- description: 'Raw refusal reason received from the acquirer, where available. Example: AUTHORISED'
  name: refusalReasonRaw
  type: string
- description: The amount of the payment request.
  name: requestAmount
  type: string
- description: The currency of the payment request.
  name: requestCurrencyCode
  type: string
- description: 'The shopper interaction type of the payment request. Example: Ecommerce'
  name: shopperInteraction
  type: string
- description: 'The shopperReference passed in the payment request. Example: AdyenTestShopperXX'
  name: shopperReference
  type: string
- description: 'The terminal ID used in a point-of-sale payment. Example: 06022622'
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
- description: The `visaTransactionId`, has a fixed length of 15 numeric characters. > Contact Support Team to enable this field.
  name: visaTransactionId
  type: string
- description: The 3DS transaction ID of the 3DS session sent in notifications. The value is Base64-encoded and is returned for transactions with directoryResponse 'N' or 'Y'. If you want to submit the xid in your 3
  name: xid
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-response-additional-data-common-schema.json
slug: payouts-response-additional-data-common
tags:
- Payments
- Financial Services
- Fintech
title: ResponseAdditionalDataCommon
---
