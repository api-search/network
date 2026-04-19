---
class_count: 2
classes:
- ClusterMembers
- ClusterMember
context_file: json-ld/akka-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/akka/refs/heads/main/json-ld/akka-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Akka from Akka.
layout: jsonld
name: Akka Context
namespaces:
- prefix: akka
  uri: https://akka.io/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: members
  type: reference
- container: ''
  name: selfAddress
  type: string
- container: set
  name: unreachable
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: status
  type: string
- container: set
  name: roles
  type: string
- container: ''
  name: uid
  type: integer
property_count: 7
provider_name: Akka
provider_slug: akka
slug: akka-context
tags:
- Actor Model
- Distributed Systems
- Frameworks
- Java
- Microservices
- Reactive
- Scala
- JSON-LD
- Linked Data
- Semantic Web
---
