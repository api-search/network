---
description: Specification for the desired project state.
layout: schema
name: ProjectSpec
properties_list:
- description: Finalizers that must complete before the project is deleted.
  name: finalizers
  type: array
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-project-spec-schema.json
slug: openshift-rest-project-spec
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: ProjectSpec
---
