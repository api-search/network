---
description: BusinessDetails schema from Adyen API
layout: schema
name: BusinessDetails
properties_list:
- description: The registered name of the company (if it differs from the legal name of the company).
  name: doingBusinessAs
  type: string
- description: The legal name of the company.
  name: legalBusinessName
  type: string
- description: Information about the parent public company. Required if the account holder is 100% owned by a publicly listed company.
  name: listedUltimateParentCompany
  type: array
- description: The registration number of the company.
  name: registrationNumber
  type: string
- description: Array containing information about individuals associated with the account holder either through ownership or control. For details about how you can identify them, refer to [our verification guide](ht
  name: shareholders
  type: array
- description: Signatories associated with the company. Each array entry should represent one signatory.
  name: signatories
  type: array
- description: Market Identifier Code (MIC).
  name: stockExchange
  type: string
- description: International Securities Identification Number (ISIN).
  name: stockNumber
  type: string
- description: Stock Ticker symbol.
  name: stockTicker
  type: string
- description: The tax ID of the company.
  name: taxId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-business-details-schema.json
slug: notifications-business-details
tags:
- Payments
- Financial Services
- Fintech
title: BusinessDetails
---
