---
description: A paginated list of clusters.
layout: schema
name: ClusterList
properties_list:
- description: The resource kind.
  name: kind
  type: string
- description: The current page number.
  name: page
  type: integer
- description: The number of items in this page.
  name: size
  type: integer
- description: The total number of items across all pages.
  name: total
  type: integer
- description: The list of clusters.
  name: items
  type: array
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-openshift-cluster-manager-cluster-list-schema.json
slug: red-hat-openshift-cluster-manager-cluster-list
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: ClusterList
---
