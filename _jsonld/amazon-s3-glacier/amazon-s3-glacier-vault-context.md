---
class_count: 1
classes:
- Amazon S3 Glacier Vault
context_file: json-ld/amazon-s3-glacier-vault-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-s3-glacier/refs/heads/main/json-ld/amazon-s3-glacier-vault-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon S3 Glacier Vault from Amazon S3 Glacier.
layout: jsonld
name: Amazon S3 Glacier Vault Context
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
- container: ''
  name: VaultARN
  type: string
- container: ''
  name: VaultName
  type: string
- container: ''
  name: CreationDate
  type: dateTime
- container: ''
  name: LastInventoryDate
  type: dateTime
- container: ''
  name: NumberOfArchives
  type: integer
- container: ''
  name: SizeInBytes
  type: integer
- container: ''
  name: VaultAccessPolicy
  type: string
- container: ''
  name: VaultNotificationConfig
  type: string
- container: ''
  name: Tags
  type: string
property_count: 9
provider_name: Amazon S3 Glacier
provider_slug: amazon-s3-glacier
slug: amazon-s3-glacier-vault-context
tags:
- Archive
- AWS
- Backup
- Storage
- JSON-LD
- Linked Data
- Semantic Web
---
