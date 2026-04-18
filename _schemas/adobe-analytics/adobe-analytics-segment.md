---
description: An analytics segment definition
layout: schema
name: Segment
properties_list:
- description: Unique segment identifier
  name: id
  type: string
- description: Display name of the segment
  name: name
  type: string
- description: Description of the segment's purpose
  name: description
  type: string
- description: The report suite this segment is based on
  name: rsid
  type: string
- description: The owner of an Analytics component
  name: owner
  type: object
- description: The segment rule definition
  name: definition
  type: object
- description: Last modification timestamp
  name: modified
  type: string
- description: ''
  name: tags
  type: array
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-segment-schema.json
slug: adobe-analytics-segment
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: Segment
---
