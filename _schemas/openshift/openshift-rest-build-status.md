---
description: Status of the build execution.
layout: schema
name: BuildStatus
properties_list:
- description: The current phase of the build.
  name: phase
  type: string
- description: Whether the build was cancelled.
  name: cancelled
  type: boolean
- description: Human-readable message about the build status.
  name: message
  type: string
- description: Brief machine-readable reason for the build status.
  name: reason
  type: string
- description: Timestamp when the build started running.
  name: startTimestamp
  type: string
- description: Timestamp when the build completed.
  name: completionTimestamp
  type: string
- description: Duration of the build in nanoseconds.
  name: duration
  type: integer
- description: The Docker image reference of the built image.
  name: outputDockerImageReference
  type: string
- description: Build output details.
  name: output
  type: object
- description: The last few lines of the build log for failed builds.
  name: logSnippet
  type: string
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-build-status-schema.json
slug: openshift-rest-build-status
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: BuildStatus
---
