---
description: BalanceAccount schema from Adyen API
layout: schema
name: BalanceAccount
properties_list:
- description: The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/accountHolders__resParam_id) associated with the balance account.
  name: accountHolderId
  type: string
- description: List of balances with the amount and currency.
  name: balances
  type: array
- description: The default three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance account. The default value is **EUR**. > After a balance account is created,
  name: defaultCurrencyCode
  type: string
- description: A human-readable description of the balance account, maximum 300 characters. You can use this parameter to distinguish between multiple balance accounts under an account holder.
  name: description
  type: string
- description: The unique identifier of the balance account.
  name: id
  type: string
- description: A set of key and value pairs for general use. The keys do not have specific names and may be used for storing miscellaneous data as desired. > Note that during an update of metadata, the omission of e
  name: metadata
  type: object
- description: The unique identifier of the account of the migrated account holder in the classic integration.
  name: migratedAccountCode
  type: string
- description: List of [payment instruments](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/paymentInstruments) associated with the balance account.
  name: paymentInstruments
  type: array
- description: Contains key-value pairs to the configure the settlement model in a balance account.
  name: platformPaymentConfiguration
  type: object
- description: Your reference for the balance account, maximum 150 characters.
  name: reference
  type: string
- description: The status of the balance account, set to **Active** by default.
  name: status
  type: string
- description: The time zone of the balance account. For example, **Europe/Amsterdam**. Defaults to the time zone of the account holder if no time zone is set. For possible values, see the [list of time zone codes](
  name: timeZone
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-balance-account-schema.json
slug: configuration-webhooks-balance-account
tags:
- Payments
- Financial Services
- Fintech
title: BalanceAccount
---
