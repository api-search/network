---
description: Specification of the desired behavior of a pod.
layout: schema
name: PodSpec
properties_list:
- description: List of containers in the pod.
  name: containers
  type: array
- description: List of initialization containers.
  name: initContainers
  type: array
- description: ''
  name: restartPolicy
  type: string
- description: Name of the ServiceAccount to use for the pod.
  name: serviceAccountName
  type: string
- description: ''
  name: nodeSelector
  type: object
- description: ''
  name: volumes
  type: array
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-pod-spec-schema.json
slug: openshift-rest-pod-spec
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: PodSpec
---
