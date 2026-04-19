---
description: A request to compose objects.
layout: schema
name: ComposeRequest
properties_list:
- description: The kind of item this is.
  name: kind
  type: string
- description: The list of source objects that will be concatenated into a single object. Maximum 32 objects.
  name: sourceObjects
  type: array
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
schema_file: json-schema/gcp-cloud-storage-json-compose-request-schema.json
slug: gcp-cloud-storage-json-compose-request
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
title: ComposeRequest
---
