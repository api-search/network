---
description: Base merchant model schema
layout: schema
name: BaseMerchant
properties_list:
- description: Name of the merchant that the item was purchased from.
  name: name
  type: string
- description: A four-digit number listed in ISO 18245 for retail financial services. MCC is used to classify the business by the type of goods or services it provides.
  name: categoryCode
  type: string
- description: The earliest date an Issuer can search for orders (i.e. the date an Issuer cannot search before). Date-Time must be in [ISO 8601 format](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6)
  name: orderAvailabilityDateTime
  type: string
- description: The number of months worth of data you have made available to search on.
  name: orderHistoryMonths
  type: integer
- description: The numbers of days that need to elapse between an authorization for a purchase and when the purchase can be searched on.
  name: orderLatencyDays
  type: integer
- description: Industry Code is used to classify the business by the type of industry.
  name: industryCode
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-ethoca-merchant-self-services-base-merchant-schema.json
slug: mastercard-ethoca-merchant-self-services-base-merchant
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: BaseMerchant
---
