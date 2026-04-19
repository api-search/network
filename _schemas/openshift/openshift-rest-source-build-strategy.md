---
description: Source-to-Image (S2I) build strategy that combines application source with a builder image to produce a runnable image.
layout: schema
name: SourceBuildStrategy
properties_list:
- description: ''
  name: env
  type: array
- description: URL of S2I scripts to use instead of the ones in the builder image.
  name: scripts
  type: string
- description: Attempt to perform an incremental build reusing artifacts from a prior build.
  name: incremental
  type: boolean
- description: Overrides the default pull behavior and forces a pull of the builder image before the build.
  name: forcePull
  type: boolean
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-source-build-strategy-schema.json
slug: openshift-rest-source-build-strategy
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: SourceBuildStrategy
---
