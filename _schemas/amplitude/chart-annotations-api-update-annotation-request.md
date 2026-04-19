---
description: UpdateAnnotationRequest schema from Amplitude Chart Annotations API
layout: schema
name: UpdateAnnotationRequest
properties_list:
- description: The updated display label for the annotation.
  name: label
  type: string
- description: The updated date in YYYY-MM-DD format.
  name: date
  type: string
- description: The updated end date in YYYY-MM-DD format.
  name: end_date
  type: string
- description: Updated additional details or notes.
  name: details
  type: string
- description: The updated category.
  name: category
  type: string
- description: The updated chart ID.
  name: chart_id
  type: integer
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/chart-annotations-api-update-annotation-request-schema.json
slug: chart-annotations-api-update-annotation-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: UpdateAnnotationRequest
---
