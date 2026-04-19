---
description: An audience segment for targeting.
layout: schema
name: AudienceSegment
properties_list:
- description: ID of this audience segment.
  name: id
  type: string
- description: Name of this audience segment.
  name: name
  type: string
- description: Weight allocated to this segment. Must be between 1 and 1000.
  name: allocation
  type: integer
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-audience-segment-schema.json
slug: google-campaign-manager-audience-segment
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: AudienceSegment
---
