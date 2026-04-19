---
description: Parameters for a custom deployment strategy.
layout: schema
name: CustomDeploymentStrategyParams
properties_list:
- description: The container image that runs the custom deployment logic.
  name: image
  type: string
- description: ''
  name: environment
  type: array
- description: The command to execute in the custom deployer container.
  name: command
  type: array
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-custom-deployment-strategy-params-schema.json
slug: openshift-rest-custom-deployment-strategy-params
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: CustomDeploymentStrategyParams
---
