---
description: Payload for creating an annotation
layout: schema
name: AnnotationCreate
properties_list:
- description: Display name
  name: name
  type: string
- description: Annotation notes
  name: description
  type: string
- description: ISO 8601 date range
  name: dateRange
  type: string
- description: Report suite IDs to apply to
  name: rsids
  type: array
- description: Hex color code
  name: color
  type: string
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-annotation-create-schema.json
slug: adobe-analytics-annotation-create
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: AnnotationCreate
---
