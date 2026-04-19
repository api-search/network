---
description: Describes how to perform a deployment.
layout: schema
name: DeploymentStrategy
properties_list:
- description: The deployment strategy type.
  name: type
  type: string
- description: Duration in seconds that the deployer pods may be active before the system retries the deployment.
  name: activeDeadlineSeconds
  type: integer
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-deployment-strategy-schema.json
slug: openshift-rest-deployment-strategy
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: DeploymentStrategy
---
