---
description: Specification for creating or updating a journey
layout: schema
name: JourneyDefinition
properties_list:
- description: Customer-defined unique key for the journey
  name: key
  type: string
- description: Display name of the journey
  name: name
  type: string
- description: Description of the journey purpose
  name: description
  type: string
- description: Version of the Journey Builder API (e.g., 1.0)
  name: workflowApiVersion
  type: number
- description: ''
  name: triggers
  type: array
- description: ''
  name: activities
  type: array
- description: ''
  name: goals
  type: array
- description: ''
  name: exits
  type: array
provider_name: Salesforce Marketing Cloud
provider_slug: salesforce-marketing-cloud
schema_file: json-schema/salesforce-marketing-cloud-journey-definition-schema.json
slug: salesforce-marketing-cloud-journey-definition
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
title: JourneyDefinition
---
