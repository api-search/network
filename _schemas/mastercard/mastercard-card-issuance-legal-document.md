---
description: Legal document that is required for KYC.
layout: schema
name: LegalDocument
properties_list:
- description: ID of legal document. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - Required when legal document type is provided.
  name: id
  type: string
- description: 'Place of issuance of legal document <BR/> **Conditional Mandatory**<font color=''red''>* </font> field - Required when legal document id is provided and configured in document checklist plan associated '
  name: placeOfIssuance
  type: string
- description: Date on which the legal document will expire. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - Required when legal document id is provided and configured in document checklist plan a
  name: expiryDate
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-legal-document-schema.json
slug: mastercard-card-issuance-legal-document
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: LegalDocument
---
