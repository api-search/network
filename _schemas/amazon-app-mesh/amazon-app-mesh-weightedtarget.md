---
description: An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.
layout: schema
name: WeightedTarget
properties_list:
- description: ''
  name: port
  type: object
- description: ''
  name: virtualNode
  type: object
- description: ''
  name: weight
  type: object
provider_name: Amazon App Mesh
provider_slug: amazon-app-mesh
schema_file: json-schema/amazon-app-mesh-weightedtarget-schema.json
slug: amazon-app-mesh-weightedtarget
tags:
- AWS
- Microservices
- Networking
- Service Mesh
title: WeightedTarget
---
