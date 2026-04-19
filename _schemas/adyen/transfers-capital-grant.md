---
description: CapitalGrant schema from Adyen API
layout: schema
name: CapitalGrant
properties_list:
- description: An object containing the amount of the grant, in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: amount
  type: object
- description: An object containing the details of the existing grant.
  name: balances
  type: object
- description: An object containing the details of the receiving party of the grant. Setting either an `accountHolderId`, `balanceAccountId`, or both is required.
  name: counterparty
  type: object
- description: An object containing the fee currency and value, in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: fee
  type: object
- description: The identifier of the grant account used for the grant.
  name: grantAccountId
  type: string
- description: The identifier of the grant offer that has been selected and from which the grant details will be used.
  name: grantOfferId
  type: string
- description: The identifier of the grant reference.
  name: id
  type: string
- description: An object containing the details of the 30-day repayment threshold.
  name: repayment
  type: object
- description: 'The current status of the grant. Possible values: **Pending**, **Active**, **Repaid**.'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-capital-grant-schema.json
slug: transfers-capital-grant
tags:
- Payments
- Financial Services
- Fintech
title: CapitalGrant
---
