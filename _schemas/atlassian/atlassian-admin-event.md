---
description: Represents an audit event that occurred within the organization, capturing actions such as user changes, policy updates, and access modifications.
layout: schema
name: Event
properties_list:
- description: The unique identifier of the event.
  name: id
  type: string
- description: The resource type.
  name: type
  type: string
- description: The event attributes.
  name: attributes
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-admin-event-schema.json
slug: atlassian-admin-event
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: Event
---
