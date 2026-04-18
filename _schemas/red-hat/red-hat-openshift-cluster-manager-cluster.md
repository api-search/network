---
description: Represents an OpenShift cluster managed through the Cluster Manager.
layout: schema
name: Cluster
properties_list:
- description: The unique identifier of the cluster.
  name: id
  type: string
- description: The name of the cluster.
  name: name
  type: string
- description: The display name of the cluster.
  name: display_name
  type: string
- description: The current state of the cluster.
  name: state
  type: string
- description: The cloud provider where the cluster is deployed.
  name: cloud_provider
  type: object
- description: The cloud region where the cluster is deployed.
  name: region
  type: object
- description: Whether the cluster spans multiple availability zones for high availability.
  name: multi_az
  type: boolean
- description: Node configuration for the cluster.
  name: nodes
  type: object
- description: API server endpoint configuration.
  name: api
  type: object
- description: Web console configuration.
  name: console
  type: object
- description: The OpenShift version of the cluster.
  name: version
  type: object
- description: The date and time when the cluster was created.
  name: creation_timestamp
  type: string
- description: The date and time when the cluster is set to expire, if applicable.
  name: expiration_timestamp
  type: string
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-openshift-cluster-manager-cluster-schema.json
slug: red-hat-openshift-cluster-manager-cluster
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Cluster
---
