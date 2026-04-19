---
description: CreateAccountHolderResponse schema from Adyen API
layout: schema
name: CreateAccountHolderResponse
properties_list:
- description: The code of a new account created for the account holder.
  name: accountCode
  type: string
- description: The code of the new account holder.
  name: accountHolderCode
  type: string
- description: Details of the new account holder.
  name: accountHolderDetails
  type: object
- description: The status of the new account holder.
  name: accountHolderStatus
  type: object
- description: The description of the new account holder.
  name: description
  type: string
- description: A list of fields that caused the `/createAccountHolder` request to fail.
  name: invalidFields
  type: array
- description: The type of legal entity of the new account holder.
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
schema_file: json-schema/notifications-create-account-holder-response-schema.json
slug: notifications-create-account-holder-response
tags:
- Payments
- Financial Services
- Fintech
title: CreateAccountHolderResponse
---
