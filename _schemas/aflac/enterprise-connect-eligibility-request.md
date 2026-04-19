---
description: Request payload for eligibility verification.
layout: schema
name: EligibilityRequest
properties_list:
- description: Employee identifier to verify.
  name: employee_id
  type: string
- description: Employer group identifier.
  name: group_id
  type: string
- description: Supplemental insurance product to check eligibility for.
  name: product_type
  type: string
provider_name: aflac
provider_slug: aflac
schema_file: json-schema/enterprise-connect-eligibility-request-schema.json
slug: enterprise-connect-eligibility-request
tags: []
title: EligibilityRequest
---
