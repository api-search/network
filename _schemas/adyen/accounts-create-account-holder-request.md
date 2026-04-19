---
description: CreateAccountHolderRequest schema from Adyen API
layout: schema
name: CreateAccountHolderRequest
properties_list:
- description: Your unique identifier for the prospective account holder. The length must be between three (3) and fifty (50) characters long. Only letters, digits, and hyphens (-) are allowed.
  name: accountHolderCode
  type: string
- description: The details of the prospective account holder.
  name: accountHolderDetails
  type: object
- description: If set to **true**, an account with the default options is automatically created for the account holder. By default, this field is set to **true**.
  name: createDefaultAccount
  type: boolean
- description: A description of the prospective account holder, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores `_`.
  name: description
  type: string
- description: 'The legal entity type of the account holder. This determines the information that should be provided in the request. Possible values: **Business**, **Individual**, or **NonProfit**. * If set to **Busi'
  name: legalEntity
  type: string
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals.
  name: primaryCurrency
  type: string
- description: The starting [processing tier](https://docs.adyen.com/marketplaces-and-platforms/classic/onboarding-and-verification/precheck-kyc-information) for the prospective account holder.
  name: processingTier
  type: integer
- description: The identifier of the profile that applies to this entity.
  name: verificationProfile
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-create-account-holder-request-schema.json
slug: accounts-create-account-holder-request
tags:
- Payments
- Financial Services
- Fintech
title: CreateAccountHolderRequest
---
