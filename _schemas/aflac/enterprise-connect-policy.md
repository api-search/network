---
description: A supplemental insurance policy record.
layout: schema
name: Policy
properties_list:
- description: Unique policy identifier.
  name: policy_id
  type: string
- description: Associated enrollment identifier.
  name: enrollment_id
  type: string
- description: Policyholder employee identifier.
  name: employee_id
  type: string
- description: Employer group identifier.
  name: group_id
  type: string
- description: Type of supplemental insurance product.
  name: product_type
  type: string
- description: Policy status.
  name: status
  type: string
- description: Coverage face value amount in USD.
  name: face_value
  type: number
- description: Monthly premium amount in USD.
  name: monthly_premium
  type: number
- description: Policy effective date.
  name: effective_date
  type: string
provider_name: aflac
provider_slug: aflac
schema_file: json-schema/enterprise-connect-policy-schema.json
slug: enterprise-connect-policy
tags: []
title: Policy
---
