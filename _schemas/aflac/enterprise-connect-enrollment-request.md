---
description: Request payload for creating or updating an enrollment.
layout: schema
name: EnrollmentRequest
properties_list:
- description: Employee identifier.
  name: employee_id
  type: string
- description: Employer group identifier.
  name: group_id
  type: string
- description: Type of supplemental insurance product to enroll in.
  name: product_type
  type: string
- description: Coverage level for the enrollment.
  name: coverage_level
  type: string
- description: Requested effective date for coverage.
  name: effective_date
  type: string
- description: List of dependents to include in family coverage.
  name: dependents
  type: array
provider_name: aflac
provider_slug: aflac
schema_file: json-schema/enterprise-connect-enrollment-request-schema.json
slug: enterprise-connect-enrollment-request
tags: []
title: EnrollmentRequest
---
