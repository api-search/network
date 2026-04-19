---
description: Specifies where the resulting container image is pushed.
layout: schema
name: BuildOutput
properties_list:
- description: Secret holding credentials for pushing to the output registry.
  name: pushSecret
  type: object
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-build-output-schema.json
slug: openshift-rest-build-output
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: BuildOutput
---
