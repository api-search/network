---
description: Represents a member's participation in a Clean Rooms collaboration.
layout: schema
name: Membership
properties_list:
- description: The unique ID of the membership.
  name: id
  type: string
- description: The ARN of the membership.
  name: arn
  type: string
- description: The ARN of the collaboration.
  name: collaborationArn
  type: string
- description: The ID of the collaboration.
  name: collaborationId
  type: string
- description: The account ID of the collaboration creator.
  name: collaborationCreatorAccountId
  type: string
- description: The name of the collaboration.
  name: collaborationName
  type: string
- description: The status of the membership.
  name: status
  type: string
provider_name: Amazon Clean Rooms
provider_slug: amazon-clean-rooms
schema_file: json-schema/clean-rooms-membership-schema.json
slug: clean-rooms-membership
tags:
- AWS
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
title: Membership
---
