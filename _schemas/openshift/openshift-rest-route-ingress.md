---
description: Holds information about the places where a route is exposed.
layout: schema
name: RouteIngress
properties_list:
- description: The hostname assigned to the route by the router.
  name: host
  type: string
- description: The name of the router that admitted this route.
  name: routerName
  type: string
- description: ''
  name: conditions
  type: array
- description: The wildcard policy applied by the router.
  name: wildcardPolicy
  type: string
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-route-ingress-schema.json
slug: openshift-rest-route-ingress
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: RouteIngress
---
