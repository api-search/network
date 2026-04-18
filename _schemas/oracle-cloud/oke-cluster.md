---
description: A Kubernetes cluster managed by OKE.
layout: schema
name: Cluster
properties_list:
- description: The OCID of the cluster.
  name: id
  type: string
- description: ''
  name: compartmentId
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: kubernetesVersion
  type: string
- description: ''
  name: vcnId
  type: string
- description: ''
  name: lifecycleState
  type: string
- description: ''
  name: endpoints
  type: object
- description: ''
  name: timeCreated
  type: string
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/oke-cluster-schema.json
slug: oke-cluster
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: Cluster
---
