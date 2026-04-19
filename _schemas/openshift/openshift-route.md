---
description: A Route resource exposes an OpenShift service at a hostname so that external clients can reach it by name. Routes support TLS termination strategies including edge, passthrough, and re-encrypt, as well as traffic splitting across multiple backends for A/B deployments.
layout: schema
name: OpenShift Route
properties_list:
- description: The API version for the Route resource.
  name: apiVersion
  type: string
- description: The resource kind, always Route.
  name: kind
  type: string
- description: ''
  name: metadata
  type: object
- description: ''
  name: spec
  type: object
- description: ''
  name: status
  type: object
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-route-schema.json
slug: openshift-route
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: OpenShift Route
---
