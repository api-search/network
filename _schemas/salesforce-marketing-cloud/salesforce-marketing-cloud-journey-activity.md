---
description: An activity within a journey. Activities represent the actions performed on contacts, such as sending emails, waiting, or making decisions.
layout: schema
name: JourneyActivity
properties_list:
- description: Unique key for the activity within the journey
  name: key
  type: string
- description: Display name of the activity
  name: name
  type: string
- description: Type of activity
  name: type
  type: string
- description: Activity-specific configuration
  name: configurationArguments
  type: object
- description: Possible outcomes of the activity leading to next steps
  name: outcomes
  type: array
provider_name: Salesforce Marketing Cloud
provider_slug: salesforce-marketing-cloud
schema_file: json-schema/salesforce-marketing-cloud-journey-activity-schema.json
slug: salesforce-marketing-cloud-journey-activity
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
title: JourneyActivity
---
