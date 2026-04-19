---
description: Custom build strategy that uses a custom builder image to execute an arbitrary build process.
layout: schema
name: CustomBuildStrategy
properties_list:
- description: ''
  name: env
  type: array
- description: If true, the Docker socket is exposed inside the build container.
  name: exposeDockerSocket
  type: boolean
- description: Forces a pull of the custom builder image before the build.
  name: forcePull
  type: boolean
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-custom-build-strategy-schema.json
slug: openshift-rest-custom-build-strategy
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: CustomBuildStrategy
---
