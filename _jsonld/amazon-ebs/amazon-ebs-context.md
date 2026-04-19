---
class_count: 3
classes:
- Amazon EBS Volume
- DescribeVolumesResult
- Volume
context_file: json-ld/amazon-ebs-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-ebs/refs/heads/main/json-ld/amazon-ebs-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Ebs from Amazon EBS.
layout: jsonld
name: Amazon Ebs Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: pan
  uri: https://aws.amazon.com/schema/
properties:
- container: ''
  name: volumeId
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: volumeType
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: availabilityZone
  type: string
- container: ''
  name: createTime
  type: dateTime
- container: ''
  name: encrypted
  type: boolean
- container: ''
  name: kmsKeyId
  type: string
- container: ''
  name: iops
  type: integer
- container: ''
  name: throughput
  type: integer
- container: ''
  name: snapshotId
  type: string
- container: ''
  name: multiAttachEnabled
  type: boolean
- container: set
  name: attachments
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: instanceId
  type: string
- container: ''
  name: device
  type: string
- container: ''
  name: attachTime
  type: dateTime
- container: ''
  name: deleteOnTermination
  type: boolean
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: set
  name: volumeSet
  type: string
- container: ''
  name: nextToken
  type: string
property_count: 24
provider_name: Amazon EBS
provider_slug: amazon-ebs
slug: amazon-ebs-context
tags:
- Amazon Web Services
- AWS
- Block Storage
- EBS
- EC2
- Snapshots
- Storage
- Volumes
- JSON-LD
- Linked Data
- Semantic Web
---
