---
description: A single application container running within a pod.
layout: schema
name: Container
properties_list:
- description: Name of the container.
  name: name
  type: string
- description: Container image name.
  name: image
  type: string
- description: Entrypoint array.
  name: command
  type: array
- description: Arguments to the entrypoint.
  name: args
  type: array
- description: ''
  name: env
  type: array
- description: ''
  name: ports
  type: array
- description: ''
  name: volumeMounts
  type: array
- description: ''
  name: imagePullPolicy
  type: string
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-container-schema.json
slug: openshift-rest-container
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: Container
---
