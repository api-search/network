---
description: Summary of an object in a bucket.
layout: schema
name: ObjectSummary
properties_list:
- description: The name of the object.
  name: name
  type: string
- description: Size of the object in bytes.
  name: size
  type: integer
- description: Base64-encoded MD5 hash.
  name: md5
  type: string
- description: The date and time the object was created.
  name: timeCreated
  type: string
- description: The date and time the object was last modified.
  name: timeModified
  type: string
- description: The storage tier of the object.
  name: storageTier
  type: string
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/object-storage-object-summary-schema.json
slug: object-storage-object-summary
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: ObjectSummary
---
