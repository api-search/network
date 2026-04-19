---
description: Abortion insurance coverage restrictions covering Medicaid, private insurance, and ACA exchange plans for a US state.
layout: schema
name: InsuranceCoverage
properties_list:
- description: If true, state requires private health plans to cover abortion.
  name: requires_coverage
  type: boolean
- description: If true, private insurance may cover abortion without restrictions.
  name: private_coverage_no_restrictions
  type: boolean
- description: If true, private insurance coverage allowed when abortion is necessary to save pregnant person's life.
  name: private_exception_life
  type: boolean
- description: Private insurance coverage allowed for serious health conditions described by this field.
  name: private_exception_health
  type: string
- description: Private insurance coverage allowed for described fetal anomaly types.
  name: private_exception_fetal
  type: string
- description: If true, private insurance coverage allowed in cases of rape or incest.
  name: private_exception_rape_or_incest
  type: boolean
- description: If true, state has not restricted abortion coverage in ACA exchange plans.
  name: exchange_coverage_no_restrictions
  type: boolean
- description: If true, exchange plan coverage allowed when abortion is necessary to save pregnant person's life.
  name: exchange_exception_life
  type: boolean
- description: Exchange plan coverage allowed for health conditions described by this field.
  name: exchange_exception_health
  type: string
- description: Exchange plan coverage allowed for described fetal anomaly types.
  name: exchange_exception_fetal
  type: string
- description: If true, exchange plan coverage allowed in cases of rape or incest.
  name: exchange_exception_rape_or_incest
  type: boolean
- description: If true, state prohibits all exchange insurance coverage for abortion.
  name: exchange_forbids_coverage
  type: boolean
- description: If true, state uses Medicaid funds for medically necessary abortion determined by patient/provider.
  name: medicaid_coverage_provider_patient_decision
  type: boolean
- description: If true, Medicaid covers abortion necessary to save pregnant person's life (required by Hyde Amendment).
  name: medicaid_exception_life
  type: boolean
- description: Medicaid coverage for health conditions described by this field.
  name: medicaid_exception_health
  type: string
- description: Medicaid coverage for described fetal anomaly types.
  name: medicaid_exception_fetal
  type: string
- description: If true, Medicaid covers abortion in cases of rape or incest (required by Hyde Amendment).
  name: medicaid_exception_rape_or_incest
  type: boolean
- description: Date this policy record was last updated.
  name: Last Updated
  type: string
provider_name: Abortion Policy API
provider_slug: abortion-policy-api
schema_file: json-schema/insurance-coverage-schema.json
slug: insurance-coverage
tags:
- Abortion
- Policies
- Healthcare
- Government
title: InsuranceCoverage
---
