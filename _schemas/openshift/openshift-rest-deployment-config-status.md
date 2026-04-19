---
description: Status of the DeploymentConfig.
layout: schema
name: DeploymentConfigStatus
properties_list:
- description: The version of the most recent deployment.
  name: latestVersion
  type: integer
- description: The most recent generation observed by the deployment controller.
  name: observedGeneration
  type: integer
- description: Total number of non-terminated pods targeted by this deployment.
  name: replicas
  type: integer
- description: Total number of non-terminated pods that have the desired template spec.
  name: updatedReplicas
  type: integer
- description: Total number of available pods targeted by this deployment.
  name: availableReplicas
  type: integer
- description: Total number of unavailable pods targeted by this deployment.
  name: unavailableReplicas
  type: integer
- description: Total number of ready pods targeted by this deployment.
  name: readyReplicas
  type: integer
- description: ''
  name: conditions
  type: array
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-deployment-config-status-schema.json
slug: openshift-rest-deployment-config-status
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: DeploymentConfigStatus
---
