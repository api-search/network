---
description: ''
layout: schema
name: CustomField
properties_list:
- description: 'Custom field name like: `clientDateField1`, `clientDataField1`, `clientNumberField1`, `cardDateField1`, `cardDataField1`, `cardNumberField1`, `accountDateField1`, `accountDataField1`, `accountNumberFi'
  name: name
  type: string
- description: Custom field value. * In case of date value, it must be expressed in ISO 8601 format - YYYY-MM-DD. For example, 2022-01-16 * In case of data, it could be a free text that may contain alphanumeric lett
  name: value
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-custom-field-schema.json
slug: mastercard-card-issuance-custom-field
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: CustomField
---
