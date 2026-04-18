---
description: A boot disk image for launching compute instances.
layout: schema
name: Image
properties_list:
- description: The OCID of the image.
  name: id
  type: string
- description: The OCID of the compartment.
  name: compartmentId
  type: string
- description: A user-friendly name.
  name: displayName
  type: string
- description: The image operating system.
  name: operatingSystem
  type: string
- description: The image operating system version.
  name: operatingSystemVersion
  type: string
- description: ''
  name: lifecycleState
  type: string
- description: Size of the image in megabytes.
  name: sizeInMBs
  type: integer
- description: ''
  name: timeCreated
  type: string
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/compute-image-schema.json
slug: compute-image
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: Image
---
