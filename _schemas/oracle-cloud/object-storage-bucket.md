---
description: A bucket is a container for storing objects in Object Storage.
layout: schema
name: Bucket
properties_list:
- description: The Object Storage namespace.
  name: namespace
  type: string
- description: The name of the bucket.
  name: name
  type: string
- description: The OCID of the compartment.
  name: compartmentId
  type: string
- description: The OCID of the user who created the bucket.
  name: createdBy
  type: string
- description: The date and time the bucket was created.
  name: timeCreated
  type: string
- description: The type of public access enabled on this bucket.
  name: publicAccessType
  type: string
- description: The storage tier type.
  name: storageTier
  type: string
- description: Whether events are emitted for object state changes.
  name: objectEventsEnabled
  type: boolean
- description: ''
  name: freeformTags
  type: object
- description: ''
  name: definedTags
  type: object
- description: The entity tag for the object lifecycle policy.
  name: objectLifecyclePolicyEtag
  type: string
- description: Approximate number of objects in the bucket.
  name: approximateCount
  type: integer
- description: Approximate total size in bytes.
  name: approximateSize
  type: integer
- description: The versioning status of the bucket.
  name: versioning
  type: string
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/object-storage-bucket-schema.json
slug: object-storage-bucket
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: Bucket
---
