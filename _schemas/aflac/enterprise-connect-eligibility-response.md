---
description: Result of an eligibility verification check.
layout: schema
name: EligibilityResponse
properties_list:
- description: Whether the employee is eligible for the product.
  name: eligible
  type: boolean
- description: Verified employee identifier.
  name: employee_id
  type: string
- description: Employer group identifier.
  name: group_id
  type: string
- description: Product type checked.
  name: product_type
  type: string
- description: Reason for ineligibility if not eligible.
  name: ineligibility_reason
  type: string
provider_name: aflac
provider_slug: aflac
schema_file: json-schema/enterprise-connect-eligibility-response-schema.json
slug: enterprise-connect-eligibility-response
tags: []
title: EligibilityResponse
---
