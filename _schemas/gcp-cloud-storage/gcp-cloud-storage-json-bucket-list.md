---
description: A list of buckets.
layout: schema
name: BucketList
properties_list:
- description: The kind of item this is.
  name: kind
  type: string
- description: The continuation token. Provide this value as the pageToken in a subsequent request to return the next page of results.
  name: nextPageToken
  type: string
- description: The list of buckets.
  name: items
  type: array
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
schema_file: json-schema/gcp-cloud-storage-json-bucket-list-schema.json
slug: gcp-cloud-storage-json-bucket-list
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
title: BucketList
---
