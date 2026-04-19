---
description: Represents a worker in Workday, including employees and contingent workers. A worker has personal information, job data, compensation, and organizational relationships.
layout: schema
name: Worker
properties_list:
- description: The Workday ID of the worker.
  name: id
  type: string
- description: A display descriptor for the worker, typically the full name.
  name: descriptor
  type: string
- description: The employee ID or contingent worker ID.
  name: workerID
  type: string
- description: The type of worker (e.g., Employee, Contingent Worker).
  name: workerType
  type: object
- description: Personal information for the worker.
  name: personalInformation
  type: object
- description: Contact information for the worker.
  name: contactInformation
  type: object
- description: Primary job data for the worker.
  name: jobData
  type: object
- description: Organizational assignment data.
  name: organizationData
  type: object
- description: Management chain data.
  name: managementData
  type: object
- description: The original hire date.
  name: hireDate
  type: string
- description: The original hire date across all employments.
  name: originalHireDate
  type: string
- description: The termination date, if applicable.
  name: terminationDate
  type:
  - string
  - 'null'
- description: Whether the worker is currently active.
  name: isActive
  type: boolean
- description: An external system identifier for the worker.
  name: externalID
  type: string
- description: A link to the full worker resource.
  name: href
  type: string
provider_name: Workday
provider_slug: workday
schema_file: json-schema/worker.json
slug: worker
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: Worker
---
