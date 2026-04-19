---
description: Summary of a cluster in the vCenter inventory
layout: schema
name: ClusterSummary
properties_list:
- description: Unique identifier of the cluster (e.g., domain-c7)
  name: cluster
  type: string
- description: Display name of the cluster
  name: name
  type: string
- description: Whether vSphere HA is enabled
  name: ha_enabled
  type: boolean
- description: Whether vSphere DRS is enabled
  name: drs_enabled
  type: boolean
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-cluster-summary-schema.json
slug: vmware-vsphere-cluster-summary
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: ClusterSummary
---
