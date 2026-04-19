---
description: Describes the state of a deployment at a point in time.
layout: schema
name: DeploymentCondition
properties_list:
- description: The type of condition.
  name: type
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: reason
  type: string
- description: ''
  name: message
  type: string
- description: ''
  name: lastUpdateTime
  type: string
- description: ''
  name: lastTransitionTime
  type: string
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-deployment-condition-schema.json
slug: openshift-rest-deployment-condition
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: DeploymentCondition
---
