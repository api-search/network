---
description: A network interface (LIF) providing data or management access
layout: schema
name: NetworkInterface
properties_list:
- description: Network interface UUID
  name: uuid
  type: string
- description: Interface name
  name: name
  type: string
- description: IP address configuration
  name: ip
  type: object
- description: Operational state of the interface
  name: state
  type: string
- description: Whether the interface is administratively enabled
  name: enabled
  type: boolean
- description: Interface scope
  name: scope
  type: string
- description: Service policy governing the interface
  name: service_policy
  type: object
- description: Current location of the interface
  name: location
  type: object
provider_name: NetApp
provider_slug: netapp
schema_file: json-schema/netapp-ontap-network-interface-schema.json
slug: netapp-ontap-network-interface
tags:
- Cloud
- Data Management
- Hybrid Cloud
- Infrastructure
- Storage
title: NetworkInterface
---
