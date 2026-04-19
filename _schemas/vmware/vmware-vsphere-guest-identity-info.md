---
description: Guest operating system identity information from VMware Tools
layout: schema
name: GuestIdentityInfo
properties_list:
- description: Guest OS full name
  name: name
  type: string
- description: Guest OS family
  name: family
  type: string
- description: ''
  name: full_name
  type: object
- description: Guest hostname
  name: host_name
  type: string
- description: Primary IP address of the guest
  name: ip_address
  type: string
provider_name: VMware
provider_slug: vmware
schema_file: json-schema/vmware-vsphere-guest-identity-info-schema.json
slug: vmware-vsphere-guest-identity-info
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
title: GuestIdentityInfo
---
