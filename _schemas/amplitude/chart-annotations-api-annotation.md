---
description: Annotation schema from Amplitude Chart Annotations API
layout: schema
name: Annotation
properties_list:
- description: The unique identifier of the annotation.
  name: id
  type: integer
- description: The display label for the annotation.
  name: label
  type: string
- description: The start date of the annotation in YYYY-MM-DD format.
  name: date
  type: string
- description: The end date of the annotation for date ranges. Null for point-in-time annotations.
  name: end_date
  type: string
- description: Additional details or notes for the annotation.
  name: details
  type: string
- description: The category of the annotation for organization purposes.
  name: category
  type: string
- description: The ID of the chart the annotation is associated with. Null for project-wide annotations.
  name: chart_id
  type: integer
- description: The timestamp when the annotation was created.
  name: created_at
  type: string
- description: The timestamp when the annotation was last updated.
  name: updated_at
  type: string
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/chart-annotations-api-annotation-schema.json
slug: chart-annotations-api-annotation
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Annotation
---
