---
description: Request body for staff-assisted policy details completion
layout: schema
name: PolicyDetailsAssistedRequest
properties_list:
- description: Unique identifier of the price estimate to convert
  name: estimate_id
  type: string
- description: Unique identifier of the customer
  name: customer_id
  type: string
- description: Preferred payment frequency for the policy
  name: payment_frequency
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-policy-details-assisted-request-schema.json
slug: api-connect-policy-details-assisted-request
tags:
- Financial Services
- Insurance
- Asset Management
title: PolicyDetailsAssistedRequest
---
