---
description: Compute resource requirements for a container.
layout: schema
name: ResourceRequirements
properties_list:
- description: Maximum compute resources allowed (e.g., cpu, memory).
  name: limits
  type: object
- description: Minimum compute resources required (e.g., cpu, memory).
  name: requests
  type: object
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-resource-requirements-schema.json
slug: openshift-rest-resource-requirements
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: ResourceRequirements
---
