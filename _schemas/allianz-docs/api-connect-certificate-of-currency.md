---
description: Insurance Certificate of Currency confirming active coverage
layout: schema
name: CertificateOfCurrency
properties_list:
- description: Unique identifier for the certificate
  name: certificate_id
  type: string
- description: Policy number the certificate relates to
  name: policy_number
  type: string
- description: Name of the insured party
  name: insured_name
  type: string
- description: Insurance product type
  name: product_type
  type: string
- description: Coverage start date
  name: coverage_start
  type: string
- description: Coverage end date
  name: coverage_end
  type: string
- description: Total sum insured amount
  name: sum_insured
  type: number
- description: Currency code for the sum insured
  name: currency
  type: string
- description: Timestamp when the certificate was issued
  name: issued_at
  type: string
- description: URL to download the certificate as a PDF document
  name: download_url
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-certificate-of-currency-schema.json
slug: api-connect-certificate-of-currency
tags:
- Financial Services
- Insurance
- Asset Management
title: CertificateOfCurrency
---
