---
description: Standard Kubernetes object metadata
layout: schema
name: ObjectMeta
properties_list:
- description: Name of the resource, unique within a namespace
  name: name
  type: string
- description: Kubernetes namespace the resource belongs to
  name: namespace
  type: string
- description: Key-value pairs for organizing and selecting resources
  name: labels
  type: object
- description: Key-value pairs for storing arbitrary non-identifying metadata
  name: annotations
  type: object
- description: Timestamp when the resource was created
  name: creationTimestamp
  type: string
- description: Sequence number representing a specific generation of the resource
  name: generation
  type: integer
- description: Opaque value for optimistic concurrency control
  name: resourceVersion
  type: string
- description: Unique identifier for the resource
  name: uid
  type: string
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-object-meta-schema.json
slug: ambassador-object-meta
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: ObjectMeta
---
