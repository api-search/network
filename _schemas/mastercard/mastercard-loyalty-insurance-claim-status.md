---
description: ''
layout: schema
name: ClaimStatus
properties_list:
- description: Array of insurance claim features associated with the claim.
  name: features
  type: array
- description: URL to web page that facilitates uploading documents.
  name: uploadDocumentsUrl
  type: string
- description: Array of required documents for this claim.
  name: requiredDocuments
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-loyalty-insurance-claim-status-schema.json
slug: mastercard-loyalty-insurance-claim-status
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: ClaimStatus
---
