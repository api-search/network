---
description: DmpSegment from LinkedIn API
layout: schema
name: DmpSegment
properties_list:
- description: Unique identifier for the DMP segment
  name: id
  type: integer
- description: Display name of the segment
  name: name
  type: string
- description: URN of the sponsore account
  name: account
  type: string
- description: Access policy for the segment
  name: accessPolicy
  type: string
- description: Type of DMP segment
  name: type
  type: string
- description: Source platform for the segment data
  name: sourcePlatform
  type: string
- description: Current status of the segment
  name: status
  type: string
- description: Number of matched records
  name: matchedCount
  type: integer
- description: Total number of input records
  name: inputCount
  type: integer
- description: Size of the audience
  name: audienceSize
  type: integer
- description: ''
  name: destinations
  type: array
provider_name: LinkedIn
provider_slug: linkedin
schema_file: json-schema/linkedin-marketing-audience-dmp-segment-schema.json
slug: linkedin-marketing-audience-dmp-segment
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
title: DmpSegment
---
