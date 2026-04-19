---
description: A request to roll back a deployment to a previous version.
layout: schema
name: DeploymentConfigRollback
properties_list:
- description: ''
  name: apiVersion
  type: string
- description: ''
  name: kind
  type: string
- description: Name of the deployment config to roll back.
  name: name
  type: string
- description: ''
  name: spec
  type: object
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-deployment-config-rollback-schema.json
slug: openshift-rest-deployment-config-rollback
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: DeploymentConfigRollback
---
