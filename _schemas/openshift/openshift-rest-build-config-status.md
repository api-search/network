---
description: Status of the BuildConfig.
layout: schema
name: BuildConfigStatus
properties_list:
- description: The version of the last build created from this config.
  name: lastVersion
  type: integer
- description: ''
  name: imageChangeTriggers
  type: array
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-build-config-status-schema.json
slug: openshift-rest-build-config-status
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: BuildConfigStatus
---
