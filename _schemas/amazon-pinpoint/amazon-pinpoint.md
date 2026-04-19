---
description: Schema defining the structure of an Amazon Pinpoint application resource, including campaigns, segments, channels, and messaging configuration for multi-channel marketing communications.
layout: schema
name: Amazon Pinpoint Application Definition
properties_list:
- description: The unique identifier for the application.
  name: Id
  type: string
- description: The Amazon Resource Name of the application.
  name: Arn
  type: string
- description: The display name of the application.
  name: Name
  type: string
- description: Tags associated with the application.
  name: tags
  type: object
- description: The date and time when the application was created.
  name: CreationDate
  type: string
- description: The campaigns for the application.
  name: Campaigns
  type: array
- description: The audience segments for the application.
  name: Segments
  type: array
- description: ''
  name: Channels
  type: object
provider_name: Amazon Pinpoint
provider_slug: amazon-pinpoint
schema_file: json-schema/amazon-pinpoint-schema.json
slug: amazon-pinpoint
tags:
- AWS
- Campaigns
- Communications
- Email
- Marketing
- Messaging
- Push Notifications
- SMS
- Voice
- Customer Engagement
- Segmentation
- Journeys
- Analytics
title: Amazon Pinpoint Application Definition
---
