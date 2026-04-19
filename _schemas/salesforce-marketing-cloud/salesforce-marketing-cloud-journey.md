---
description: Represents a customer journey in Marketing Cloud. A journey defines an automated workflow that guides contacts through a series of marketing interactions across channels.
layout: schema
name: Journey
properties_list:
- description: System-generated unique identifier for the journey
  name: id
  type: string
- description: Customer-defined unique key for the journey
  name: key
  type: string
- description: Display name of the journey
  name: name
  type: string
- description: Description of the journey purpose
  name: description
  type: string
- description: Current version number of the journey
  name: version
  type: integer
- description: Current status of the journey
  name: status
  type: string
- description: ''
  name: createdDate
  type: string
- description: ''
  name: modifiedDate
  type: string
- description: Version of the Journey Builder API used
  name: workflowApiVersion
  type: number
- description: Entry triggers that inject contacts into the journey
  name: triggers
  type: array
- description: Activities that contacts pass through in the journey
  name: activities
  type: array
- description: Goal criteria that measure journey success
  name: goals
  type: array
- description: Exit criteria that remove contacts from the journey
  name: exits
  type: array
- description: Runtime statistics for the journey
  name: stats
  type: object
provider_name: Salesforce Marketing Cloud
provider_slug: salesforce-marketing-cloud
schema_file: json-schema/salesforce-marketing-cloud-journey-schema.json
slug: salesforce-marketing-cloud-journey
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
title: Journey
---
