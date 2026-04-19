---
description: A list of objects.
layout: schema
name: ObjectList
properties_list:
- description: The kind of item this is.
  name: kind
  type: string
- description: The continuation token. Provide this value as the pageToken in a subsequent request to return the next page of results.
  name: nextPageToken
  type: string
- description: The list of prefixes of objects matching-but-not-listed up to and including the requested delimiter.
  name: prefixes
  type: array
- description: The list of objects.
  name: items
  type: array
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
schema_file: json-schema/gcp-cloud-storage-json-object-list-schema.json
slug: gcp-cloud-storage-json-object-list
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
title: ObjectList
---
