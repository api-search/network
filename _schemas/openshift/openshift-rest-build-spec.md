---
description: Specification of the desired build behavior.
layout: schema
name: BuildSpec
properties_list:
- description: The name of the ServiceAccount to use to run the build pod.
  name: serviceAccount
  type: string
- description: Optional duration in seconds the build may run before the system terminates it. The countdown starts from the time the build pod is scheduled.
  name: completionDeadlineSeconds
  type: integer
- description: Selector which must match a node's labels for the build pod to be scheduled on that node.
  name: nodeSelector
  type: object
- description: Describes which triggers started the most recent build.
  name: triggeredBy
  type: array
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-build-spec-schema.json
slug: openshift-rest-build-spec
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: BuildSpec
---
