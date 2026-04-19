---
description: SpecInspectionType schema from 1Factory API
layout: schema
name: SpecInspectionType
properties_list:
- description: ''
  name: inspection_type
  type: object
- description: How the feature should be inspected.
  name: inspection_method
  type: string
- description: How frequently should the feature be checked.
  name: sampling_rule
  type: string
- description: How the data for this specification is recorded - numerically, as a pass/fail, or calculated from other features.
  name: data_type
  type: string
provider_name: 1Factory
provider_slug: 1factory
schema_file: json-schema/1factory-spec-inspection-type-schema.json
slug: 1factory-spec-inspection-type
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
title: SpecInspectionType
---
