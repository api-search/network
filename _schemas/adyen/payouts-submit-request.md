---
description: SubmitRequest schema from Adyen API
layout: schema
name: SubmitRequest
properties_list:
- description: This field contains additional data, which may be required for a particular request.
  name: additionalData
  type: object
- description: A container object for the payable amount information of the transaction.
  name: amount
  type: object
- description: 'The date of birth. Format: ISO-8601; example: YYYY-MM-DD For Paysafecard it must be the same as used when registering the Paysafecard account. > This field is mandatory for natural persons. > This fie'
  name: dateOfBirth
  type: string
- description: 'The type of the entity the payout is processed for. Allowed values: * NaturalPerson * Company > This field is required to update the existing `entityType` that is associated with this recurring contra'
  name: entityType
  type: string
- description: An integer value that is added to the normal fraud score. The value can be either positive or negative.
  name: fraudOffset
  type: integer
- description: The merchant account identifier you want to process the transaction request with.
  name: merchantAccount
  type: string
- description: The shopper's nationality. A valid value is an ISO 2-character country code (e.g. 'NL'). > This field is required to update the existing nationality that is associated with this recurring contract.
  name: nationality
  type: string
- description: A container for the type of recurring contract to be retrieved. The `recurring.contract` must be set to "PAYOUT".
  name: recurring
  type: object
- description: The merchant reference for this payout. This reference will be used in all communication to the merchant about the status of the payout. Although it is a good idea to make sure it is unique, this is n
  name: reference
  type: string
- description: This is the `recurringDetailReference` you want to use for this payout. You can use the value LATEST to select the most recently used recurring detail.
  name: selectedRecurringDetailReference
  type: string
- description: The shopper's email address.
  name: shopperEmail
  type: string
- description: The shopper's name. In case the `entityType` is `Company`, the `shopperName.lastName` must contain the company name. > This field is required to update the existing `shopperName` associated with a rec
  name: shopperName
  type: object
- description: The shopper's reference for the payout transaction.
  name: shopperReference
  type: string
- description: The description of this payout. This description is shown on the bank statement of the shopper (if this is supported by the chosen payment method).
  name: shopperStatement
  type: string
- description: The shopper's social security number.
  name: socialSecurityNumber
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-submit-request-schema.json
slug: payouts-submit-request
tags:
- Payments
- Financial Services
- Fintech
title: SubmitRequest
---
