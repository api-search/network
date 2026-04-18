---
description: An annotation marking a date range in reports
layout: schema
name: Annotation
properties_list:
- description: Unique annotation identifier
  name: id
  type: string
- description: Display name of the annotation
  name: name
  type: string
- description: Annotation text content
  name: description
  type: string
- description: ISO 8601 date range covered by this annotation
  name: dateRange
  type: string
- description: List of report suite IDs this annotation applies to
  name: rsids
  type: array
- description: Display color for the annotation in reports
  name: color
  type: string
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-annotation-schema.json
slug: adobe-analytics-annotation
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: Annotation
---
