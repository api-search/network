---
description: An affiliate referral event tracking a publisher's referral of a customer to acehardware.com via the Impact affiliate network.
layout: schema
name: AceHardwareAffiliateReferral
properties_list:
- description: Unique identifier for this referral event
  name: referralId
  type: string
- description: Impact affiliate account identifier
  name: affiliateId
  type: string
- description: Name of the affiliate publisher
  name: affiliateName
  type: string
- description: URL of the affiliate's referring page
  name: referralUrl
  type: string
- description: Ace Hardware product page the customer was referred to
  name: destinationUrl
  type: string
- description: Date and time the affiliate link was clicked
  name: clickDate
  type: string
- description: Date and time the purchase was completed
  name: conversionDate
  type: string
- description: Ace Hardware order identifier from the converted sale
  name: orderId
  type: string
- description: Total order value in USD
  name: orderValue
  type: number
- description: Commission percentage earned by the affiliate
  name: commissionRate
  type: number
- description: Commission amount earned in USD
  name: commissionAmount
  type: number
- description: Status of the commission
  name: status
  type: string
provider_name: Ace Hardware
provider_slug: ace-hardware
schema_file: json-schema/ace-hardware-affiliate-referral-schema.json
slug: ace-hardware-affiliate-referral
tags:
- Retail
- Hardware
- Home Improvement
- Tools
- Paint
- Cooperative
- EDI
- Affiliate
title: AceHardwareAffiliateReferral
---
