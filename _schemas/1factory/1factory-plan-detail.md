---
description: PlanDetail schema from 1Factory API
layout: schema
name: PlanDetail
properties_list:
- description: ''
  name: ID
  type: object
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
  name: operation
  type: object
- description: ''
  name: project_identifier
  type: object
- description: ''
  name: status
  type: object
- description: Version of the plan.
  name: version
  type: number
- description: ''
  name: version_status
  type: string
- description: The status of a plan that requires approval before releasing or closing. (Availability depends on Organization settings.)
  name: approval_status
  type: string
- description: ''
  name: customer_name
  type: object
- description: ''
  name: supplier_name
  type: object
- description: ''
  name: supplier_number
  type: object
- description: If the plan is for a tabulated part.
  name: is_tabulated
  type: boolean
- description: If the plan is a spec library
  name: is_spec_lib
  type: boolean
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
  name: specifications
  type: array
provider_name: 1Factory
provider_slug: 1factory
schema_file: json-schema/1factory-plan-detail-schema.json
slug: 1factory-plan-detail
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
title: PlanDetail
---
