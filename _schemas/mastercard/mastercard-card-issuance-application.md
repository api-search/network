---
description: ''
layout: schema
name: Application
properties_list:
- description: Client on-boarding application form number.
  name: formNumber
  type: string
- description: 'Indicates whether the application should go through the checker approval process prior to client on-boarding. Applicable only if not requested for ''instant card''. It will be always considered as true '
  name: makerChecker
  type: boolean
- description: Free text field that contains remarks entered while submitting the request. <BR/> This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: memo
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-application-schema.json
slug: mastercard-card-issuance-application
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Application
---
