---
description: Details for updating a bucket.
layout: schema
name: UpdateBucketDetails
properties_list:
- description: The name of the bucket.
  name: name
  type: string
- description: The Object Storage namespace.
  name: namespace
  type: string
- description: The OCID of the compartment.
  name: compartmentId
  type: string
- description: ''
  name: publicAccessType
  type: string
- description: ''
  name: objectEventsEnabled
  type: boolean
- description: ''
  name: versioning
  type: string
- description: ''
  name: freeformTags
  type: object
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/object-storage-update-bucket-details-schema.json
slug: object-storage-update-bucket-details
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: UpdateBucketDetails
---
