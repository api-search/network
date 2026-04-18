---
description: ''
layout: schema
name: Kyc
properties_list:
- description: KYC status of the client. If the status is true it indicates that KYC data has been updated and KYC completed. <BR/>This field is required if configured as **Business Mandatory**<font color='red'>* </
  name: status
  type: boolean
- description: Remarks on the KYC status or documents. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - Required when KYC status is true.
  name: remark
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-kyc-schema.json
slug: mastercard-card-issuance-kyc
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Kyc
---
