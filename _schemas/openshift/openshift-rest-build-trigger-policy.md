---
description: A policy that causes a new build to be created.
layout: schema
name: BuildTriggerPolicy
properties_list:
- description: The type of build trigger.
  name: type
  type: string
- description: ''
  name: github
  type: object
- description: ''
  name: generic
  type: object
- description: ''
  name: imageChange
  type: object
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-build-trigger-policy-schema.json
slug: openshift-rest-build-trigger-policy
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: BuildTriggerPolicy
---
