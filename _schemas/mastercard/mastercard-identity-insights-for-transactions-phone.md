---
description: ''
layout: schema
name: Phone
properties_list:
- description: 'The match status between either of the input names (person or business) and the queried entity. Possible values are: * not-found * match * no-match'
  name: matchToName
  type: string
- description: The line type of the phone number. * landline - Traditional wired phone line. * fixed-voip - VOIP-based fixed line phones. * mobile - Wireless phone line. * voicemail - Voicemail-only service. * toll-
  name: lineType
  type: string
- description: True if the phone number is valid.
  name: valid
  type: boolean
- description: The company that provides voice and/or data services for the phone number. Carriers are returned at the MVNO level.
  name: phoneNumberCarrier
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-phone-schema.json
slug: mastercard-identity-insights-for-transactions-phone
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Phone
---
