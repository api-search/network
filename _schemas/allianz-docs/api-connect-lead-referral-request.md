---
description: Request body for submitting an instant lead referral to Allianz
layout: schema
name: LeadReferralRequest
properties_list:
- description: Full name of the customer being referred
  name: customer_name
  type: string
- description: Email address of the customer being referred
  name: customer_email
  type: string
- description: Phone number of the customer being referred
  name: customer_phone
  type: string
- description: Insurance product the customer is interested in
  name: product_type
  type: string
- description: Additional notes about the customer's insurance needs
  name: notes
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-lead-referral-request-schema.json
slug: api-connect-lead-referral-request
tags:
- Financial Services
- Insurance
- Asset Management
title: LeadReferralRequest
---
