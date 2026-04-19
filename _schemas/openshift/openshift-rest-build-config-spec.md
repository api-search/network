---
description: Specification of the desired BuildConfig behavior.
layout: schema
name: BuildConfigSpec
properties_list:
- description: Triggers that cause new builds to be created.
  name: triggers
  type: array
- description: Controls how builds from this config run concurrently.
  name: runPolicy
  type: string
- description: The ServiceAccount to run the build pod as.
  name: serviceAccount
  type: string
- description: Optional duration in seconds builds may be active before being terminated.
  name: completionDeadlineSeconds
  type: integer
- description: Number of successful builds to retain.
  name: successfulBuildsHistoryLimit
  type: integer
- description: Number of failed builds to retain.
  name: failedBuildsHistoryLimit
  type: integer
- description: ''
  name: nodeSelector
  type: object
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-build-config-spec-schema.json
slug: openshift-rest-build-config-spec
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: BuildConfigSpec
---
