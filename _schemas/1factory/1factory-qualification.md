---
description: Qualification schema from 1Factory API
layout: schema
name: Qualification
properties_list:
- description: Date and time when the qualification was assessed or updated.
  name: date
  type: string
- description: Current qualification status of the supplier.
  name: status
  type: string
- description: Review status of the qualification assessment.
  name: review_status
  type: string
- description: Review frequency in months for re-qualification.
  name: frequency
  type: integer
provider_name: 1Factory
provider_slug: 1factory
schema_file: json-schema/1factory-qualification-schema.json
slug: 1factory-qualification
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
title: Qualification
---
