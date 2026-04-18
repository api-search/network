---
description: Details for creating a new bucket.
layout: schema
name: CreateBucketDetails
properties_list:
- description: The name of the bucket.
  name: name
  type: string
- description: The OCID of the compartment.
  name: compartmentId
  type: string
- description: The public access type.
  name: publicAccessType
  type: string
- description: The storage tier type.
  name: storageTier
  type: string
- description: Whether events are emitted for object state changes.
  name: objectEventsEnabled
  type: boolean
- description: The versioning status.
  name: versioning
  type: string
- description: ''
  name: freeformTags
  type: object
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/object-storage-create-bucket-details-schema.json
slug: object-storage-create-bucket-details
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: CreateBucketDetails
---
