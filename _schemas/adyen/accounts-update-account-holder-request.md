---
description: UpdateAccountHolderRequest schema from Adyen API
layout: schema
name: UpdateAccountHolderRequest
properties_list:
- description: The code of the Account Holder to be updated.
  name: accountHolderCode
  type: string
- description: The details to which the Account Holder should be updated. Required if a processingTier is not provided.
  name: accountHolderDetails
  type: object
- description: A description of the account holder, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores `_`.
  name: description
  type: string
- description: 'The legal entity type of the account holder. This determines the information that should be provided in the request. Possible values: **Business**, **Individual**, or **NonProfit**. * If set to **Busi'
  name: legalEntity
  type: string
- description: The primary three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), to which the account holder should be updated.
  name: primaryCurrency
  type: string
- description: The processing tier to which the Account Holder should be updated. >The processing tier can not be lowered through this request. >Required if accountHolderDetails are not provided.
  name: processingTier
  type: integer
- description: The identifier of the profile that applies to this entity.
  name: verificationProfile
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-update-account-holder-request-schema.json
slug: accounts-update-account-holder-request
tags:
- Payments
- Financial Services
- Fintech
title: UpdateAccountHolderRequest
---
