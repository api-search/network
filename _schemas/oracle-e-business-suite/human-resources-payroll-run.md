---
description: ''
layout: schema
name: PayrollRun
properties_list:
- description: Payroll action identifier
  name: payrollActionId
  type: integer
- description: Payroll identifier
  name: payrollId
  type: integer
- description: Action type (R=Run, Q=QuickPay, etc.)
  name: actionType
  type: string
- description: Action status
  name: actionStatus
  type: string
- description: ''
  name: effectiveDate
  type: string
- description: ''
  name: dateEarned
  type: string
- description: ''
  name: periodOfServiceId
  type: integer
- description: ''
  name: businessGroupId
  type: integer
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/human-resources-payroll-run-schema.json
slug: human-resources-payroll-run
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: PayrollRun
---
