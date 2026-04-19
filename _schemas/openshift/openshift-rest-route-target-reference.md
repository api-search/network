---
description: Specifies the target that traffic is routed to. Weight controls the proportion of traffic sent to this backend.
layout: schema
name: RouteTargetReference
properties_list:
- description: The kind of target, typically Service.
  name: kind
  type: string
- description: Name of the target service.
  name: name
  type: string
- description: Relative weight for traffic distribution (0-256). A zero weight causes no traffic to be sent to this backend.
  name: weight
  type: integer
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-route-target-reference-schema.json
slug: openshift-rest-route-target-reference
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: RouteTargetReference
---
