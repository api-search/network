---
description: ''
layout: schema
name: ClientPreferences
properties_list:
- description: Indicates whether registered in 'DNCR' (Do Not Call Register) or not. Default false. <BR/> This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: registerForDNCR
  type: boolean
- description: Indicates whether registered for sms alert notification facility or not. Default false. <BR/> This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: smsAlert
  type: boolean
- description: Indicates whether registered for email alert notification facility or not. Default false. <BR/> This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: emailAlert
  type: boolean
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-client-preferences-schema.json
slug: mastercard-card-issuance-client-preferences
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: ClientPreferences
---
