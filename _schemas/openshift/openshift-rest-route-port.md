---
description: Route port configuration that specifies which service port the route points to.
layout: schema
name: RoutePort
properties_list:
- description: The target port on pods selected by the service this route points to. Can be a port name or number.
  name: targetPort
  type: string
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-route-port-schema.json
slug: openshift-rest-route-port
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: RoutePort
---
