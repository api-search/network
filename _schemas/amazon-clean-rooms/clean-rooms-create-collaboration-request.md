---
description: Request body for creating a collaboration.
layout: schema
name: CreateCollaborationRequest
properties_list:
- description: The display name for a collaboration.
  name: name
  type: string
- description: A description of the collaboration.
  name: description
  type: string
- description: A list of initial members for the collaboration.
  name: members
  type: array
- description: The display name of the collaboration creator.
  name: creatorDisplayName
  type: string
- description: The abilities granted to the collaboration creator.
  name: creatorMemberAbilities
  type: array
- description: An indicator as to whether query logging has been enabled or disabled.
  name: queryLogStatus
  type: string
provider_name: Amazon Clean Rooms
provider_slug: amazon-clean-rooms
schema_file: json-schema/clean-rooms-create-collaboration-request-schema.json
slug: clean-rooms-create-collaboration-request
tags:
- AWS
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
title: CreateCollaborationRequest
---
