---
description: Docker build strategy that uses a Dockerfile to build images.
layout: schema
name: DockerBuildStrategy
properties_list:
- description: Path of the Dockerfile relative to the context directory.
  name: dockerfilePath
  type: string
- description: ''
  name: env
  type: array
- description: If true, Docker build caching is disabled.
  name: noCache
  type: boolean
- description: Forces a pull of the base image before the build.
  name: forcePull
  type: boolean
- description: Specifies build arguments to pass to Docker.
  name: buildArgs
  type: array
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-docker-build-strategy-schema.json
slug: openshift-rest-docker-build-strategy
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: DockerBuildStrategy
---
