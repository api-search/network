---
description: A request to create a new project. ProjectRequests are processed according to the cluster project request template and may include default resource quotas, limit ranges, and role bindings.
layout: schema
name: ProjectRequest
properties_list:
- description: ''
  name: apiVersion
  type: string
- description: ''
  name: kind
  type: string
- description: A human-readable name for the project, used in the web console.
  name: displayName
  type: string
- description: A longer description of the project purpose.
  name: description
  type: string
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-project-request-schema.json
slug: openshift-rest-project-request
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: ProjectRequest
---
