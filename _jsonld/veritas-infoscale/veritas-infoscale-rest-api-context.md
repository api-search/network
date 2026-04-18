---
class_count: 10
classes:
- Cluster
- ServiceGroup
- Resource
- System
- DiskGroup
- Volume
- Disk
- Snapshot
- Alert
- Job
context_file: json-ld/veritas-infoscale-rest-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/veritas-infoscale/refs/heads/main/json-ld/veritas-infoscale-rest-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Veritas Infoscale Rest Api from Veritas InfoScale.
layout: jsonld
name: Veritas Infoscale Rest Api Context
namespaces:
- prefix: veritas
  uri: https://www.veritas.com/support/en_US/doc/infoscale/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: clusterId
  type: string
- container: ''
  name: clusterName
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: nodeCount
  type: integer
- container: ''
  name: clusterVersion
  type: string
- container: ''
  name: fencingMode
  type: string
- container: ''
  name: uptime
  type: string
- container: ''
  name: lastModified
  type: dateTime
- container: list
  name: systemList
  type: ''
- container: ''
  name: currentSystem
  type: string
- container: ''
  name: autoStart
  type: boolean
- container: ''
  name: parallel
  type: boolean
- container: ''
  name: resourceCount
  type: integer
- container: ''
  name: groupType
  type: string
- container: ''
  name: critical
  type: boolean
- container: ''
  name: totalSize
  type: string
- container: ''
  name: freeSize
  type: string
- container: ''
  name: diskCount
  type: integer
- container: ''
  name: volumeCount
  type: integer
- container: ''
  name: layout
  type: string
- container: ''
  name: size
  type: string
- container: ''
  name: plexCount
  type: integer
- container: ''
  name: readPolicy
  type: string
- container: ''
  name: usageType
  type: string
- container: ''
  name: diskGroup
  type: string
- container: ''
  name: frozen
  type: boolean
- container: ''
  name: cpuUsage
  type: double
- container: ''
  name: memoryUsage
  type: double
- container: ''
  name: platform
  type: string
- container: ''
  name: architecture
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: acknowledged
  type: boolean
- container: ''
  name: devicePath
  type: string
- container: ''
  name: mediaType
  type: string
property_count: 38
provider_name: Veritas InfoScale
provider_slug: veritas-infoscale
slug: veritas-infoscale-rest-api-context
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
- JSON-LD
- Linked Data
- Semantic Web
---
