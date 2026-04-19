---
description: GetAccountHolderResponse schema from Adyen API
layout: schema
name: GetAccountHolderResponse
properties_list:
- description: The code of the account holder.
  name: accountHolderCode
  type: string
- description: Details of the account holder.
  name: accountHolderDetails
  type: object
- description: The status of the account holder.
  name: accountHolderStatus
  type: object
- description: A list of the accounts under the account holder.
  name: accounts
  type: array
- description: The description of the account holder.
  name: description
  type: string
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: The legal entity of the account holder.
  name: legalEntity
  type: string
- description: Details of the account holder migrated to the balance platform.
  name: migrationData
  type: object
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals.
  name: primaryCurrency
  type: string
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
- description: The time that shows how up to date is the information in the response.
  name: systemUpToDateTime
  type: string
- description: The details of KYC Verification of the account holder.
  name: verification
  type: object
- description: The identifier of the profile that applies to this entity.
  name: verificationProfile
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-get-account-holder-response-schema.json
slug: accounts-get-account-holder-response
tags:
- Payments
- Financial Services
- Fintech
title: GetAccountHolderResponse
---
