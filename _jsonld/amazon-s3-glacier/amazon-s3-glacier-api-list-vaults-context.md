---
class_count: 1
classes:
- ListVaultsOutput
context_file: json-ld/amazon-s3-glacier-api-list-vaults-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-s3-glacier/refs/heads/main/json-ld/amazon-s3-glacier-api-list-vaults-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon S3 Glacier Api List Vaults from Amazon S3 Glacier.
layout: jsonld
name: Amazon S3 Glacier Api List Vaults Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: VaultList
  type: string
- container: ''
  name: Marker
  type: string
property_count: 2
provider_name: Amazon S3 Glacier
provider_slug: amazon-s3-glacier
slug: amazon-s3-glacier-api-list-vaults-context
tags:
- Archive
- AWS
- Backup
- Storage
- JSON-LD
- Linked Data
- Semantic Web
---
