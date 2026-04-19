---
description: ''
layout: schema
name: WorkerSummary
properties_list:
- description: The Workday ID of the worker.
  name: id
  type: string
- description: A display descriptor for the worker (typically full name).
  name: descriptor
  type: string
- description: A link to the full worker resource.
  name: href
  type: string
- description: The primary work email address.
  name: primaryWorkEmail
  type: string
- description: The primary work phone number.
  name: primaryWorkPhone
  type: string
- description: Whether this is the primary job for the worker.
  name: isPrimaryJob
  type: boolean
- description: The business title for the worker.
  name: businessTitle
  type: string
provider_name: Workday
provider_slug: workday
schema_file: json-schema/hcm-worker-summary-schema.json
slug: hcm-worker-summary
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: WorkerSummary
---
