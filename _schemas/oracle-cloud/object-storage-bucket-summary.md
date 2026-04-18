---
description: Summary information about a bucket.
layout: schema
name: BucketSummary
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
- description: The entity tag (ETag) for the bucket.
  name: etag
  type: string
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/object-storage-bucket-summary-schema.json
slug: object-storage-bucket-summary
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: BucketSummary
---
