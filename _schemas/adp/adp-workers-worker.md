---
description: ADP Worker (employee or contractor)
layout: schema
name: Worker
properties_list:
- description: ADP Associate Object Identifier - unique worker identifier
  name: associateOID
  type: string
- description: ''
  name: workerID
  type: object
- description: ''
  name: workerDates
  type: object
- description: ''
  name: workAssignments
  type: array
- description: ''
  name: customFieldGroup
  type: object
provider_name: ADP
provider_slug: adp
schema_file: json-schema/adp-workers-worker-schema.json
slug: adp-workers-worker
tags:
- Benefits
- HCM
- HR
- Payroll
- Workforce
title: Worker
---
