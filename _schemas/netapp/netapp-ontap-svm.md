---
description: A storage virtual machine (SVM), also known as a vserver, is a secure virtual storage server that provides isolated data access to clients. Each SVM has its own set of volumes, network interfaces, and protocol configurations.
layout: schema
name: Svm
properties_list:
- description: SVM UUID
  name: uuid
  type: string
- description: SVM name (unique within the cluster)
  name: name
  type: string
- description: SVM operational state
  name: state
  type: string
- description: SVM subtype
  name: subtype
  type: string
- description: Default language encoding for volumes in the SVM
  name: language
  type: string
- description: Optional comment or description for the SVM
  name: comment
  type: string
- description: IPspace associated with the SVM
  name: ipspace
  type: object
- description: Aggregates assigned to the SVM for volume provisioning
  name: aggregates
  type: array
- description: Network interfaces configured for the SVM
  name: ip_interfaces
  type: array
- description: NFS protocol configuration
  name: nfs
  type: object
- description: CIFS/SMB protocol configuration
  name: cifs
  type: object
- description: iSCSI protocol configuration
  name: iscsi
  type: object
- description: Fibre Channel Protocol configuration
  name: fcp
  type: object
- description: NVMe over Fabrics protocol configuration
  name: nvme
  type: object
- description: Default snapshot policy for the SVM
  name: snapshot_policy
  type: object
- description: DNS configuration for the SVM
  name: dns
  type: object
- description: SSL/TLS certificate for the SVM
  name: certificate
  type: object
- description: Maximum number of volumes allowed on the SVM
  name: max_volumes
  type: string
provider_name: NetApp
provider_slug: netapp
schema_file: json-schema/netapp-ontap-svm-schema.json
slug: netapp-ontap-svm
tags:
- Cloud
- Data Management
- Hybrid Cloud
- Infrastructure
- Storage
title: Svm
---
