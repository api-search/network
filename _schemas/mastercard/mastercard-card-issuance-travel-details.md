---
description: Travel Information, Applicable only if the client has a prepaid card.
layout: schema
name: TravelDetails
properties_list:
- description: Indicates the purpose of travel for which the client will be using the card. For example, medical reasons, cultural trip, and business trip and so on. <BR/> Valid values are as configured on portal in
  name: type
  type: string
- description: Start date of the planned travel. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - Required if travel type is provided. <br/> Format - It is expressed in ISO 8601 - `YYYY-MM-DD`
  name: startDate
  type: string
- description: End date of the planned travel. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - Required if travel type is provided. <br/> Format - It is expressed in ISO 8601 - `YYYY-MM-DD`
  name: endDate
  type: string
- description: Country Code where client is traveling to. <BR/> Expressed as a 2-letter (Alpha-2) country code as defined in ISO 3166. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - Required if t
  name: country
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-travel-details-schema.json
slug: mastercard-card-issuance-travel-details
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: TravelDetails
---
