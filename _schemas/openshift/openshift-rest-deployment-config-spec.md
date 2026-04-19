---
description: Specification for the desired deployment behavior.
layout: schema
name: DeploymentConfigSpec
properties_list:
- description: The desired number of pod replicas.
  name: replicas
  type: integer
- description: Label selector for pods managed by this deployment.
  name: selector
  type: object
- description: Triggers that cause new deployments to be created.
  name: triggers
  type: array
- description: Minimum number of seconds a newly created pod should be ready without any of its containers crashing before considered available.
  name: minReadySeconds
  type: integer
- description: Number of old ReplicationControllers to retain for rollback.
  name: revisionHistoryLimit
  type: integer
- description: Indicates that the deployment config is paused and new deployments will not be triggered.
  name: paused
  type: boolean
- description: If true, deployments are scaled down to zero after the deployment completes.
  name: test
  type: boolean
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-deployment-config-spec-schema.json
slug: openshift-rest-deployment-config-spec
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: DeploymentConfigSpec
---
