---
description: A supplemental insurance enrollment record for an employee.
layout: schema
name: Enrollment
properties_list:
- description: Unique enrollment identifier.
  name: enrollment_id
  type: string
- description: Employee identifier.
  name: employee_id
  type: string
- description: Employer group identifier.
  name: group_id
  type: string
- description: Associated policy identifier assigned upon enrollment.
  name: policy_id
  type: string
- description: Type of supplemental insurance product.
  name: product_type
  type: string
- description: Coverage level selected by the employee.
  name: coverage_level
  type: string
- description: Current enrollment status.
  name: status
  type: string
- description: Date the coverage became effective.
  name: effective_date
  type: string
- description: Date the coverage was terminated, if applicable.
  name: termination_date
  type: string
- description: Monthly premium amount in USD.
  name: monthly_premium
  type: number
- description: Timestamp when the enrollment was created.
  name: created_at
  type: string
- description: Timestamp when the enrollment was last updated.
  name: updated_at
  type: string
provider_name: aflac
provider_slug: aflac
schema_file: json-schema/enterprise-connect-enrollment-schema.json
slug: enterprise-connect-enrollment
tags: []
title: Enrollment
---
