---
description: BalanceAccountUpdateRequest schema from Adyen API
layout: schema
name: BalanceAccountUpdateRequest
properties_list:
- description: The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/accountHolders__resParam_id) associated with the balance account.
  name: accountHolderId
  type: string
- description: A human-readable description of the balance account, maximum 300 characters. You can use this parameter to distinguish between multiple balance accounts under an account holder.
  name: description
  type: string
- description: A set of key and value pairs for general use. The keys do not have specific names and may be used for storing miscellaneous data as desired. > Note that during an update of metadata, the omission of e
  name: metadata
  type: object
- description: Contains key-value pairs to the configure the settlement model in a balance account.
  name: platformPaymentConfiguration
  type: object
- description: Your reference to the balance account, maximum 150 characters.
  name: reference
  type: string
- description: 'The status of the balance account. Payment instruments linked to the balance account can only be used if the balance account status is **active**. Possible values: **active**, **inactive**, **closed**'
  name: status
  type: string
- description: The time zone of the balance account. For example, **Europe/Amsterdam**. Defaults to the time zone of the account holder if no time zone is set. For possible values, see the [list of time zone codes](
  name: timeZone
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-balance-account-update-request-schema.json
slug: configuration-balance-account-update-request
tags:
- Payments
- Financial Services
- Fintech
title: BalanceAccountUpdateRequest
---
