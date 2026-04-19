---
description: Issue schema from 1Factory API
layout: schema
name: Issue
properties_list:
- description: ''
  name: ID
  type: object
- description: The reference number for the NCR, Complaint, or CAPA
  name: number
  type: number
- description: ''
  name: part_number
  type: object
- description: ''
  name: rev
  type: object
- description: ''
  name: part_description
  type: object
- description: ''
  name: customer_name
  type: object
- description: 'Your Organization''s custom identifier for customer NCRs (ex. Customer PO #)'
  name: customer_ident
  type: string
- description: ''
  name: supplier_name
  type: object
- description: 'Your Organization''s custom identifier for supplier NCRs (ex. Supplier Lot #)'
  name: supplier_ident
  type: string
- description: Type of NCR
  name: type
  type: string
- description: 'Your Organization''s custom primary identifier for manufacturing inspection identifiers. (ex. Job #)'
  name: mfg_insp_ident_1
  type: string
- description: 'Your Organization''s custom secondary identifier for manufacturing inspection identifiers. (ex. PO #)'
  name: mfg_insp_ident_2
  type: string
- description: 'Your Organization''s custom primary identifier for receiving inspection identifiers. (ex. Job #)'
  name: rec_insp_ident_1
  type: string
- description: 'Your Organization''s custom secondary identifier for receiving inspection identifiers. (ex. PO #)'
  name: rec_insp_ident_2
  type: string
- description: The number of parts in the lot of the NCR
  name: lot_quantity
  type: number
- description: The number of parts in the lot that were inspected as part of the NCR
  name: inspection_quantity
  type: number
- description: The number of parts rejected as part of the NCR
  name: defective_quantity
  type: number
- description: Business impact of the NCR
  name: impact
  type: string
- description: Where the problem for the NCR was detected.
  name: detected_at
  type: string
- description: A simple description of the problem.
  name: problem_type
  type: string
- description: The root cause of the problem.
  name: root_cause
  type: string
- description: The department or group that caused the problem.
  name: caused_by
  type: string
- description: Problem summary of the NCR.
  name: problem_summary
  type: string
- description: Cost of the NCR
  name: total_cost
  type: number
- description: Status of the NCR
  name: status
  type: string
- description: Status of all tasks on NCR.
  name: task_status
  type: string
- description: Number of tasks for the NCR.
  name: task_count
  type: number
- description: ''
  name: owner
  type: object
- description: ''
  name: created_by_name
  type: object
- description: ''
  name: created_on
  type: object
- description: ''
  name: updated_on
  type: object
- description: ''
  name: closed_on
  type: object
provider_name: 1Factory
provider_slug: 1factory
schema_file: json-schema/1factory-issue-schema.json
slug: 1factory-issue
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
title: Issue
---
