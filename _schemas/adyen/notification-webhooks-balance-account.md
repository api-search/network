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
- description: The default three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance account. The default value is **EUR**.
  name: defaultCurrencyCode
  type: string
- description: A human-readable description of the balance account, maximum 300 characters. You can use this parameter to distinguish between multiple balance accounts under an account holder.
  name: description
  type: string
- description: The unique identifier of the balance account.
  name: id
  type: string
- description: List of [payment instruments](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/paymentInstruments) associated with the balance account.
  name: paymentInstruments
  type: array
- description: Your reference for the balance account, maximum 150 characters.
  name: reference
  type: string
- description: The status of the balance account, set to **Active** by default.
  name: status
  type: string
- description: Contains key-value pairs that specify configurations for balance sweeps per currency code. A sweep pulls in or pushes out funds based on a defined schedule, amount, and a source (for pulling funds) or
  name: sweepConfigurations
  type: object
- description: The [time zone](https://www.iana.org/time-zones) of the balance account. For example, **Europe/Amsterdam**. If not set, the time zone of the account holder will be used. For possible values, see the [
  name: timeZone
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-balance-account-schema.json
slug: notification-webhooks-balance-account
tags:
- Payments
- Financial Services
- Fintech
title: BalanceAccount
---
