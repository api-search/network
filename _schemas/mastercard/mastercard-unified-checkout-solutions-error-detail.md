---
description: Error associated with a failed Digital Payment Application (DPA) item action.
layout: schema
name: ErrorDetail
properties_list:
- description: Reason for receiving an error for the Digital Payment Application (DPA) item.
  name: reason
  type: string
- description: Indicates the source type of the Digital Payment Application (DPA) item error.
  name: sourceType
  type: string
- description: Additional details on the Digital Payment Application (DPA) item error.
  name: message
  type: string
- description: Indicates the field name for the cause of the Digital Payment Application (DPA) item error.
  name: source
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-unified-checkout-solutions-error-detail-schema.json
slug: mastercard-unified-checkout-solutions-error-detail
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: ErrorDetail
---
