---
description: Describes a health check to be performed against a container.
layout: schema
name: Probe
properties_list:
- description: ''
  name: httpGet
  type: object
- description: ''
  name: tcpSocket
  type: object
- description: ''
  name: exec
  type: object
- description: ''
  name: initialDelaySeconds
  type: integer
- description: ''
  name: periodSeconds
  type: integer
- description: ''
  name: timeoutSeconds
  type: integer
- description: ''
  name: successThreshold
  type: integer
- description: ''
  name: failureThreshold
  type: integer
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-probe-schema.json
slug: openshift-rest-probe
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: Probe
---
