---
class_count: 10
classes:
- name
- description
- identifier
- url
- dateCreated
- dateModified
- contentType
- contentSize
- owner
- version
context_file: json-ld/amazon-s3-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-s3/refs/heads/main/json-ld/amazon-s3-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon S3 from Amazon S3.
layout: jsonld
name: Amazon S3 Context
namespaces:
- prefix: s3
  uri: https://docs.aws.amazon.com/AmazonS3/latest/API/
- prefix: aws
  uri: https://aws.amazon.com/
- prefix: iam
  uri: https://docs.aws.amazon.com/IAM/latest/UserGuide/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: schema
  uri: https://schema.org/
properties:
- container: ''
  name: Bucket
  type: ''
- container: ''
  name: S3Object
  type: ''
- container: ''
  name: Owner
  type: ''
- container: ''
  name: AccessPoint
  type: ''
- container: ''
  name: BatchJob
  type: ''
- container: ''
  name: TableBucket
  type: ''
- container: ''
  name: Table
  type: ''
- container: ''
  name: Tag
  type: ''
- container: ''
  name: Grant
  type: ''
- container: ''
  name: StorageLensConfiguration
  type: ''
- container: ''
  name: MultiRegionAccessPoint
  type: ''
property_count: 11
provider_name: Amazon S3
provider_slug: amazon-s3
slug: amazon-s3-context
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
- JSON-LD
- Linked Data
- Semantic Web
---
