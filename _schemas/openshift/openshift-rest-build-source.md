---
description: Specifies the source code location and type for the build input.
layout: schema
name: BuildSource
properties_list:
- description: The type of source input.
  name: type
  type: string
- description: Git source location.
  name: git
  type: object
- description: The Dockerfile content used as build input.
  name: dockerfile
  type: string
- description: The subdirectory within the source repository used as the context for the build.
  name: contextDir
  type: string
- description: Secret holding credentials for accessing the source repository.
  name: sourceSecret
  type: object
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-build-source-schema.json
slug: openshift-rest-build-source
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: BuildSource
---
