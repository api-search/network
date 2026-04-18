---
class_count: 1
classes:
- id
context_file: json-ld/red-hat-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/red-hat/refs/heads/main/json-ld/red-hat-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Red Hat from Red Hat.
layout: jsonld
name: Red Hat Context
namespaces:
- prefix: redhat
  uri: https://developers.redhat.com/schemas/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: rdfs
  uri: http://www.w3.org/2000/01/rdf-schema#
properties:
- container: ''
  name: Cluster
  type: rdfs:Class
- container: ''
  name: Host
  type: rdfs:Class
- container: ''
  name: Advisory
  type: rdfs:Class
- container: ''
  name: JobTemplate
  type: rdfs:Class
- container: ''
  name: Job
  type: rdfs:Class
- container: ''
  name: Inventory
  type: rdfs:Class
- container: ''
  name: Repository
  type: rdfs:Class
- container: ''
  name: ContainerImage
  type: rdfs:Class
- container: ''
  name: Realm
  type: rdfs:Class
- container: ''
  name: ContentView
  type: rdfs:Class
- container: ''
  name: InsightsRule
  type: rdfs:Class
- container: ''
  name: NotificationEvent
  type: rdfs:Class
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: url
  type: reference
- container: ''
  name: email
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: cloudProvider
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: openshiftVersion
  type: string
- container: ''
  name: multiAz
  type: boolean
- container: ''
  name: nodeCount
  type: integer
- container: ''
  name: hostname
  type: string
- container: ''
  name: ipAddress
  type: string
- container: ''
  name: operatingSystem
  type: string
- container: ''
  name: rhelVersion
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: cveId
  type: string
- container: ''
  name: advisoryId
  type: string
- container: ''
  name: advisoryType
  type: string
- container: ''
  name: rebootRequired
  type: boolean
- container: ''
  name: playbook
  type: string
- container: ''
  name: inventory
  type: ''
- container: ''
  name: jobTemplate
  type: ''
- container: ''
  name: elapsed
  type: decimal
- container: ''
  name: namespace
  type: string
- container: ''
  name: manifestDigest
  type: string
- container: ''
  name: isPublic
  type: boolean
- container: ''
  name: tagCount
  type: integer
- container: ''
  name: realm
  type: string
- container: ''
  name: clientId
  type: string
- container: ''
  name: protocol
  type: string
- container: ''
  name: organizationId
  type: string
- container: ''
  name: eventType
  type: string
- container: ''
  name: bundle
  type: string
- container: ''
  name: application
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: publishedAt
  type: dateTime
- container: ''
  name: lastSeen
  type: dateTime
- container: ''
  name: timestamp
  type: dateTime
property_count: 55
provider_name: Red Hat
provider_slug: red-hat
slug: red-hat-context
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
- JSON-LD
- Linked Data
- Semantic Web
---
