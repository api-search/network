---
description: Payload for creating or updating a segment
layout: schema
name: SegmentCreate
properties_list:
- description: Display name of the segment
  name: name
  type: string
- description: Description of the segment's purpose
  name: description
  type: string
- description: Report suite ID this segment is based on
  name: rsid
  type: string
- description: The segment rule definition in Analytics query format
  name: definition
  type: object
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-segment-create-schema.json
slug: adobe-analytics-segment-create
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: SegmentCreate
---
