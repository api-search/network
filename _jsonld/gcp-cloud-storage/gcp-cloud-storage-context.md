---
class_count: 0
classes: []
context_file: json-ld/gcp-cloud-storage-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/gcp-cloud-storage/refs/heads/main/json-ld/gcp-cloud-storage-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Gcp Cloud Storage from Google Cloud Storage.
layout: jsonld
name: Gcp Cloud Storage Context
namespaces:
- prefix: gcs
  uri: https://cloud.google.com/storage/docs/json_api/v1/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: rdf
  uri: http://www.w3.org/1999/02/22-rdf-syntax-ns#
properties:
- container: ''
  name: Bucket
  type: reference
- container: ''
  name: Object
  type: reference
- container: ''
  name: BucketAccessControl
  type: reference
- container: ''
  name: ObjectAccessControl
  type: reference
- container: ''
  name: Notification
  type: reference
- container: ''
  name: ServiceAccount
  type: reference
property_count: 6
provider_name: Google Cloud Storage
provider_slug: gcp-cloud-storage
slug: gcp-cloud-storage-context
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
- JSON-LD
- Linked Data
- Semantic Web
---
