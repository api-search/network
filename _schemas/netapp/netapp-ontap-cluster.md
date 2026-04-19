---
description: ONTAP cluster configuration and status
layout: schema
name: Cluster
properties_list:
- description: Cluster UUID
  name: uuid
  type: string
- description: Cluster name
  name: name
  type: string
- description: Contact information for the cluster administrator
  name: contact
  type: string
- description: Physical location of the cluster
  name: location
  type: string
- description: ONTAP software version
  name: version
  type: object
- description: DNS domain names for the cluster
  name: dns_domains
  type: array
- description: NTP server addresses
  name: ntp_servers
  type: array
- description: Cluster timezone setting
  name: timezone
  type: object
- description: Cluster management network interfaces
  name: management_interfaces
  type: array
- description: Nodes in the cluster
  name: nodes
  type: array
provider_name: NetApp
provider_slug: netapp
schema_file: json-schema/netapp-ontap-cluster-schema.json
slug: netapp-ontap-cluster
tags:
- Cloud
- Data Management
- Hybrid Cloud
- Infrastructure
- Storage
title: Cluster
---
