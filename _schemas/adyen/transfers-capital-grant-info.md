---
description: CapitalGrantInfo schema from Adyen API
layout: schema
name: CapitalGrantInfo
properties_list:
- description: An object containing the details of the receiving party of the grant. Setting either an `accountHolderId`, `balanceAccountId`, or both is required.
  name: counterparty
  type: object
- description: The identifier of the grant account used for the grant.
  name: grantAccountId
  type: string
- description: The identifier of the grant offer that has been selected and from which the grant details will be used.
  name: grantOfferId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-capital-grant-info-schema.json
slug: transfers-capital-grant-info
tags:
- Payments
- Financial Services
- Fintech
title: CapitalGrantInfo
---
