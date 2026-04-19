---
description: Describes the state of a route at a point in time.
layout: schema
name: RouteIngressCondition
properties_list:
- description: The type of the condition (e.g., Admitted).
  name: type
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: reason
  type: string
- description: ''
  name: message
  type: string
- description: ''
  name: lastTransitionTime
  type: string
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-route-ingress-condition-schema.json
slug: openshift-rest-route-ingress-condition
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: RouteIngressCondition
---
