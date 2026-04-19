---
description: CreateAnnotationRequest schema from Amplitude Chart Annotations API
layout: schema
name: CreateAnnotationRequest
properties_list:
- description: The display label for the annotation.
  name: label
  type: string
- description: The date of the annotation in YYYY-MM-DD format.
  name: date
  type: string
- description: The end date for date-range annotations in YYYY-MM-DD format.
  name: end_date
  type: string
- description: Additional details or notes for the annotation.
  name: details
  type: string
- description: The category to assign to the annotation.
  name: category
  type: string
- description: The ID of the chart to associate the annotation with. Omit for project-wide annotations.
  name: chart_id
  type: integer
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/chart-annotations-api-create-annotation-request-schema.json
slug: chart-annotations-api-create-annotation-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: CreateAnnotationRequest
---
