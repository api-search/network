---
description: NewPartMaster schema from 1Factory API
layout: schema
name: NewPartMaster
properties_list:
- description: ''
  name: part_number
  type: object
- description: ''
  name: rev
  type: object
- description: Description of the part. (Optional).
  name: description
  type: string
- description: Status of Part Master entry.
  name: status
  type: string
- description: 'An alternative identifier used to identify a part, such as Drawing #, or customer / supplier part number.'
  name: alt_part_number
  type: string
- description: An alternate part revision, such as a drawing revision, or customer / supplier part revision.
  name: alt_rev
  type: string
- description: 'A second alternative identifier used to identify a part, such as Drawing #, or customer / supplier part number.'
  name: alt_part_number2
  type: string
- description: A second alternate part revision, such as a drawing revision, or customer / supplier part revision.
  name: alt_rev2
  type: string
- description: ''
  name: project_identifier
  type: object
- description: Cost of the part. (Optional).
  name: cost
  type: number
- description: Unit used for determine part cost. (Optional)
  name: unit
  type: string
- description: If true, indicates part is an assembly. (Optional)
  name: is_assembly
  type: boolean
- description: If true, indicates part is an ITAR part with additional controls. (Optional)
  name: is_itar
  type: boolean
- description: If true, indicates part is bought, rather than made. (Optional)
  name: is_buy
  type: boolean
- description: Detailed comments regarding the part. (Optional)
  name: comments
  type: string
provider_name: 1Factory
provider_slug: 1factory
schema_file: json-schema/1factory-new-part-master-schema.json
slug: 1factory-new-part-master
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
title: NewPartMaster
---
