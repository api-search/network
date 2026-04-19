---
description: An audience segment definition used across Adobe Experience Cloud products to target groups of profiles based on shared attributes, behaviors, or engagement patterns.
layout: schema
name: Adobe Experience Cloud Segment
properties_list:
- description: The unique identifier for the segment.
  name: segmentId
  type: string
- description: The human-readable name of the segment.
  name: name
  type: string
- description: A detailed description of what the segment represents.
  name: description
  type: string
- description: The segment definition expression.
  name: expression
  type: object
- description: How the segment is evaluated against profiles.
  name: evaluationType
  type: string
- description: The merge policy used when evaluating this segment.
  name: mergePolicyId
  type: string
- description: The XDM schema this segment is based on.
  name: schema
  type: object
- description: The current status of the segment.
  name: status
  type: string
- description: The estimated number of profiles in this segment.
  name: profileCount
  type: integer
- description: The user who created the segment.
  name: owner
  type: object
- description: Tags for organizing and categorizing segments.
  name: tags
  type: array
- description: When the segment was created.
  name: created
  type: string
- description: When the segment was last modified.
  name: lastModified
  type: string
- description: When the segment was last evaluated.
  name: lastEvaluated
  type: string
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
schema_file: json-schema/adobe-experience-cloud-segment.json
slug: adobe-experience-cloud-segment
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
title: Adobe Experience Cloud Segment
---
