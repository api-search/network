---
description: A customer journey definition in Adobe Journey Optimizer representing an orchestrated sequence of actions, conditions, and wait steps that guide individual profiles through personalized multi-channel experiences.
layout: schema
name: Adobe Experience Cloud Journey
properties_list:
- description: The unique identifier for the journey.
  name: journeyId
  type: string
- description: The human-readable name of the journey.
  name: name
  type: string
- description: A description of the journey purpose and flow.
  name: description
  type: string
- description: The current lifecycle status of the journey.
  name: status
  type: string
- description: The version identifier of the journey.
  name: version
  type: string
- description: The conditions under which profiles enter the journey.
  name: entryCondition
  type: object
- description: The ordered list of activities in the journey.
  name: activities
  type: array
- description: Execution metrics for the journey.
  name: metrics
  type: object
- description: When the journey was created.
  name: created
  type: string
- description: When the journey was last modified.
  name: lastModified
  type: string
- description: When the journey was last published.
  name: publishedAt
  type: string
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
schema_file: json-schema/adobe-experience-cloud-journey.json
slug: adobe-experience-cloud-journey
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
title: Adobe Experience Cloud Journey
---
