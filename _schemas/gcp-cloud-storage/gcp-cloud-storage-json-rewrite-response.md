---
description: A rewrite response.
layout: schema
name: RewriteResponse
properties_list:
- description: The kind of item this is.
  name: kind
  type: string
- description: The total bytes rewritten so far.
  name: totalBytesRewritten
  type: string
- description: The total size of the object being copied.
  name: objectSize
  type: string
- description: Whether the rewrite is complete. If false, call the rewrite method again with the returned rewriteToken.
  name: done
  type: boolean
- description: A token to use in subsequent rewrite requests. Present only when the rewrite is not yet complete.
  name: rewriteToken
  type: string
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
schema_file: json-schema/gcp-cloud-storage-json-rewrite-response-schema.json
slug: gcp-cloud-storage-json-rewrite-response
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
title: RewriteResponse
---
