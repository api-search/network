---
description: Entry trigger configuration for a journey. Defines how contacts enter the journey, such as via API event, scheduled automation, or audience.
layout: schema
name: JourneyTrigger
properties_list:
- description: Unique key for the trigger within the journey
  name: key
  type: string
- description: Display name of the trigger
  name: name
  type: string
- description: Type of trigger
  name: type
  type: string
- description: Key of the event definition associated with this trigger, used for API events
  name: eventDefinitionKey
  type: string
- description: Trigger-specific configuration
  name: configurationArguments
  type: object
provider_name: Salesforce Marketing Cloud
provider_slug: salesforce-marketing-cloud
schema_file: json-schema/salesforce-marketing-cloud-journey-trigger-schema.json
slug: salesforce-marketing-cloud-journey-trigger
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
title: JourneyTrigger
---
