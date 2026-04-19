---
description: An IAM policy for a Cloud Storage resource.
layout: schema
name: Policy
properties_list:
- description: The kind of item this is.
  name: kind
  type: string
- description: The ID of the resource to which this policy belongs.
  name: resourceId
  type: string
- description: The version of the policy. Valid values are 1 and 3. Any request that specifies conditional role bindings must specify version 3.
  name: version
  type: integer
- description: HTTP 1.1 Entity tag for the policy. Used for optimistic concurrency control.
  name: etag
  type: string
- description: A list of members bound to a role.
  name: bindings
  type: array
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
schema_file: json-schema/gcp-cloud-storage-json-policy-schema.json
slug: gcp-cloud-storage-json-policy
tags:
- Archival
- Backup
- Blob Storage
- Cloud Storage
- Data
- File Storage
- Google Cloud
- Object Storage
- Storage
title: Policy
---
