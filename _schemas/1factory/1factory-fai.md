---
description: Fai schema from 1Factory API
layout: schema
name: Fai
properties_list:
- description: ''
  name: ID
  type: object
- description: ''
  name: insp_ident_1
  type: object
- description: ''
  name: insp_ident_2
  type: object
- description: ''
  name: insp_ident_3
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
  name: customer_name
  type: object
- description: ''
  name: supplier_name
  type: object
- description: ''
  name: supplier_number
  type: object
- description: ''
  name: project_identifier
  type: object
- description: Location where inspection was performed, from your organization's Site LOV.
  name: site
  type: string
- description: ''
  name: created_by_name
  type: object
- description: ''
  name: created_on
  type: object
- description: Percentage of in-spec parts for this inspection.
  name: in_spec_pct
  type: number
- description: Current status of inspection.
  name: inspection_status
  type: string
- description: Name of user that last set inspection status.
  name: inspected_by_name
  type: string
- description: Date & time that inspection status set.
  name: inspected_on
  type: string
- description: Current review status of inspection.
  name: review_status
  type: string
- description: Name of user that set review status.
  name: reviewed_by_name
  type: string
- description: Date & time that review status was set.
  name: reviewed_on
  type: string
- description: Comments on this inspection
  name: notes
  type: string
- description: 'List of NCR #s associated with this inspection'
  name: ncrs
  type: array
- description: ''
  name: updated_on
  type: object
- description: ''
  name: closed_on
  type: object
- description: ''
  name: fai_type
  type: object
- description: ''
  name: number_of_parts
  type: object
provider_name: 1Factory
provider_slug: 1factory
schema_file: json-schema/1factory-fai-schema.json
slug: 1factory-fai
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
title: Fai
---
