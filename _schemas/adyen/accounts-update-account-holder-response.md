---
description: UpdateAccountHolderResponse schema from Adyen API
layout: schema
name: UpdateAccountHolderResponse
properties_list:
- description: The code of the account holder.
  name: accountHolderCode
  type: string
- description: Details of the account holder.
  name: accountHolderDetails
  type: object
- description: The new status of the account holder.
  name: accountHolderStatus
  type: object
- description: The description of the account holder.
  name: description
  type: string
- description: in case the account holder has not been updated, contains account holder fields, that did not pass the validation.
  name: invalidFields
  type: array
- description: The legal entity of the account holder.
  name: legalEntity
  type: string
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals.
  name: primaryCurrency
  type: string
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
- description: The details of KYC Verification of the account holder.
  name: verification
  type: object
- description: The identifier of the profile that applies to this entity.
  name: verificationProfile
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-update-account-holder-response-schema.json
slug: accounts-update-account-holder-response
tags:
- Payments
- Financial Services
- Fintech
title: UpdateAccountHolderResponse
---
