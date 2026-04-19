---
class_count: 11
classes:
- ParameterGroup
- Cluster
- Snapshot
- SubnetGroup
- ACL
- CreateClusterRequest
- User
- Tag
- DescribeClustersResponse
- description
- name
context_file: json-ld/amazon-memorydb-memorydb-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-memorydb/refs/heads/main/json-ld/amazon-memorydb-memorydb-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Memorydb Memorydb Api from Amazon MemoryDB.
layout: jsonld
name: Amazon Memorydb Memorydb Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: arn
  type: string
- container: ''
  name: family
  type: string
- container: ''
  name: availabilityMode
  type: string
- container: ''
  name: engineVersion
  type: string
- container: ''
  name: nodeType
  type: string
- container: ''
  name: numberOfShards
  type: integer
- container: ''
  name: status
  type: string
- container: ''
  name: tlsEnabled
  type: boolean
- container: ''
  name: clusterConfiguration
  type: reference
- container: ''
  name: kmsKeyId
  type: string
- container: ''
  name: vpcId
  type: string
- container: set
  name: userNames
  type: string
- container: ''
  name: aclName
  type: string
- container: ''
  name: clusterName
  type: string
- container: ''
  name: numReplicasPerShard
  type: integer
- container: ''
  name: numShards
  type: integer
- container: set
  name: aclNames
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: set
  name: clusters
  type: string
- container: ''
  name: nextToken
  type: string
property_count: 21
provider_name: Amazon MemoryDB
provider_slug: amazon-memorydb
slug: amazon-memorydb-memorydb-api-context
tags:
- AWS
- Broadcasting
- Media Processing
- Media
- JSON-LD
- Linked Data
- Semantic Web
---
