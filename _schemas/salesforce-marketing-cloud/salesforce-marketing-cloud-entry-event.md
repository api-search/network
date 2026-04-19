---
description: Event payload used to inject a contact into a journey via the API event trigger.
layout: schema
name: EntryEvent
properties_list:
- description: Unique identifier for the contact entering the journey
  name: ContactKey
  type: string
- description: Key of the event definition matching the journey entry trigger
  name: EventDefinitionKey
  type: string
- description: Additional data to pass to the journey as key-value pairs. These values are available to activities within the journey.
  name: Data
  type: object
provider_name: Salesforce Marketing Cloud
provider_slug: salesforce-marketing-cloud
schema_file: json-schema/salesforce-marketing-cloud-entry-event-schema.json
slug: salesforce-marketing-cloud-entry-event
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
title: EntryEvent
---
