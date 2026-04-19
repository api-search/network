---
description: Parameters for a rolling deployment strategy.
layout: schema
name: RollingDeploymentStrategyParams
properties_list:
- description: The time to wait between individual pod updates.
  name: updatePeriodSeconds
  type: integer
- description: The time to wait between polling deployment status.
  name: intervalSeconds
  type: integer
- description: The time to wait for a scaling event before giving up.
  name: timeoutSeconds
  type: integer
- description: The maximum number of pods that can be unavailable during the update. Value can be an absolute number or a percentage.
  name: maxUnavailable
  type: string
- description: The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number or a percentage.
  name: maxSurge
  type: string
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-rolling-deployment-strategy-params-schema.json
slug: openshift-rest-rolling-deployment-strategy-params
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: RollingDeploymentStrategyParams
---
