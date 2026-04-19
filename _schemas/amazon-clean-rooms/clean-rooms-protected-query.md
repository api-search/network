---
description: Represents a protected query executed within a Clean Rooms collaboration.
layout: schema
name: ProtectedQuery
properties_list:
- description: The unique ID of the protected query.
  name: id
  type: string
- description: The ID of the membership.
  name: membershipId
  type: string
- description: The ARN of the membership.
  name: membershipArn
  type: string
- description: The time when the query was created.
  name: createTime
  type: string
- description: The status of the protected query.
  name: status
  type: string
provider_name: Amazon Clean Rooms
provider_slug: amazon-clean-rooms
schema_file: json-schema/clean-rooms-protected-query-schema.json
slug: clean-rooms-protected-query
tags:
- AWS
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
title: ProtectedQuery
---
