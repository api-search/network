---
description: A policy that triggers new deployments.
layout: schema
name: DeploymentTriggerPolicy
properties_list:
- description: The type of deployment trigger.
  name: type
  type: string
- description: Parameters for an ImageChange trigger.
  name: imageChangeParams
  type: object
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-deployment-trigger-policy-schema.json
slug: openshift-rest-deployment-trigger-policy
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: DeploymentTriggerPolicy
---
