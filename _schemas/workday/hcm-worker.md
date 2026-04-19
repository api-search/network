---
description: ''
layout: schema
name: Worker
properties_list:
- description: The Workday ID of the worker.
  name: id
  type: string
- description: A display descriptor for the worker.
  name: descriptor
  type: string
- description: The employee or contingent worker ID.
  name: workerID
  type: string
- description: ''
  name: primaryWorkEmail
  type: string
- description: ''
  name: primaryWorkPhone
  type: string
- description: ''
  name: businessTitle
  type: string
- description: The hire date for the worker.
  name: hireDate
  type: string
- description: The termination date, if applicable.
  name: terminationDate
  type: string
- description: Whether the worker is a manager.
  name: isManager
  type: boolean
- description: The external ID for the worker.
  name: externalID
  type: string
provider_name: Workday
provider_slug: workday
schema_file: json-schema/hcm-worker-schema.json
slug: hcm-worker
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: Worker
---
