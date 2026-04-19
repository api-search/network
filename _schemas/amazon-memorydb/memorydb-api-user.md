---
description: Represents a MemoryDB user.
layout: schema
name: User
properties_list:
- description: The names of the Access Control Lists to which the user belongs.
  name: ACLNames
  type: array
- description: The Amazon Resource Name (ARN) of the user.
  name: ARN
  type: string
- description: The name of the user.
  name: Name
  type: string
- description: Indicates the user status.
  name: Status
  type: string
provider_name: Amazon MemoryDB
provider_slug: amazon-memorydb
schema_file: json-schema/memorydb-api-user-schema.json
slug: memorydb-api-user
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: User
---
