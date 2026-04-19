---
description: JSON Schema for an ADP Worker object representing an employee or contractor in ADP HCM platforms.
layout: schema
name: ADP Worker
properties_list:
- description: ADP Associate Object Identifier - globally unique worker identifier
  name: associateOID
  type: string
- description: Client-assigned worker identification
  name: workerID
  type: object
- description: ''
  name: person
  type: object
- description: ''
  name: workerDates
  type: object
- description: Active and historical work assignments
  name: workAssignments
  type: array
- description: ''
  name: workerStatus
  type: object
provider_name: ADP
provider_slug: adp
schema_file: json-schema/adp-worker-schema.json
slug: adp-worker
tags:
- Benefits
- HCM
- HR
- Payroll
- Workforce
title: ADP Worker
---
