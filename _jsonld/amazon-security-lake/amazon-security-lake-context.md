---
class_count: 3
classes:
- DataLake
- LogSource
- Subscriber
context_file: json-ld/amazon-security-lake-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-security-lake/refs/heads/main/json-ld/amazon-security-lake-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Security Lake from Amazon Security Lake.
layout: jsonld
name: Amazon Security Lake Context
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
  name: dataLakeArn
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: encryptionConfiguration
  type: string
- container: ''
  name: lifecycleConfiguration
  type: string
- container: ''
  name: s3BucketArn
  type: string
- container: ''
  name: sourceName
  type: string
- container: ''
  name: sourceVersion
  type: string
- container: ''
  name: sourceStatus
  type: string
- container: ''
  name: subscriberId
  type: string
- container: ''
  name: subscriberArn
  type: string
- container: ''
  name: subscriberName
  type: string
- container: ''
  name: subscriberDescription
  type: string
- container: ''
  name: subscriberStatus
  type: string
- container: set
  name: accessTypes
  type: string
- container: ''
  name: resourceShareArn
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
property_count: 18
provider_name: Amazon Security Lake
provider_slug: amazon-security-lake
slug: amazon-security-lake-context
tags:
- AWS
- Data Lake
- Security
- SIEM
- Threat Detection
- JSON-LD
- Linked Data
- Semantic Web
---
