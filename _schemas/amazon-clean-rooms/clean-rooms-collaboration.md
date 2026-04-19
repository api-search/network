---
description: Represents an AWS Clean Rooms collaboration workspace.
layout: schema
name: Collaboration
properties_list:
- description: The unique ID of the collaboration.
  name: id
  type: string
- description: The ARN of the collaboration.
  name: arn
  type: string
- description: A human-readable identifier for the collaboration.
  name: name
  type: string
- description: A description of the collaboration.
  name: description
  type: string
- description: The account ID of the creator.
  name: creatorAccountId
  type: string
- description: The display name of the collaboration creator.
  name: creatorDisplayName
  type: string
- description: The time when the collaboration was created.
  name: createTime
  type: string
- description: The time when the collaboration was last updated.
  name: updateTime
  type: string
- description: Whether query logs are enabled.
  name: queryLogStatus
  type: string
provider_name: Amazon Clean Rooms
provider_slug: amazon-clean-rooms
schema_file: json-schema/clean-rooms-collaboration-schema.json
slug: clean-rooms-collaboration
tags:
- AWS
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
title: Collaboration
---
