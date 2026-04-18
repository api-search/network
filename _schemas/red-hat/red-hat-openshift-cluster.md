---
description: Schema for an OpenShift cluster managed through the Red Hat OpenShift Cluster Manager, representing a Kubernetes cluster deployed on a cloud provider.
layout: schema
name: Red Hat OpenShift Cluster
properties_list:
- description: The unique identifier of the cluster assigned by the Cluster Manager.
  name: id
  type: string
- description: The name of the cluster, used as a human-readable identifier.
  name: name
  type: string
- description: The display name of the cluster shown in the Hybrid Cloud Console.
  name: display_name
  type: string
- description: The current lifecycle state of the cluster.
  name: state
  type: string
- description: The cloud provider where the cluster is deployed.
  name: cloud_provider
  type: object
- description: The cloud provider region where the cluster is deployed.
  name: region
  type: object
- description: Whether the cluster spans multiple availability zones for high availability.
  name: multi_az
  type: boolean
- description: The OpenShift version running on the cluster.
  name: openshift_version
  type: string
- description: The node configuration of the cluster.
  name: nodes
  type: object
- description: The cluster API server configuration.
  name: api
  type: object
- description: The OpenShift web console configuration.
  name: console
  type: object
- description: The network configuration of the cluster.
  name: network
  type: object
- description: The subscription associated with this cluster.
  name: subscription
  type: object
- description: The date and time when the cluster was created in ISO 8601 format.
  name: creation_timestamp
  type: string
- description: The date and time when the cluster is set to expire, if applicable.
  name: expiration_timestamp
  type:
  - string
  - 'null'
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-openshift-cluster-schema.json
slug: red-hat-openshift-cluster
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Red Hat OpenShift Cluster
---
