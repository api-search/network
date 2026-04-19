---
description: An Access Control List.
layout: schema
name: ACL
properties_list:
- description: The Amazon Resource Name (ARN) of the ACL.
  name: ARN
  type: string
- description: The name of the Access Control List.
  name: Name
  type: string
- description: Indicates the current status of the ACL.
  name: Status
  type: string
- description: The list of user names that belong to the ACL.
  name: UserNames
  type: array
provider_name: Amazon MemoryDB
provider_slug: amazon-memorydb
schema_file: json-schema/memorydb-api-acl-schema.json
slug: memorydb-api-acl
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: ACL
---
