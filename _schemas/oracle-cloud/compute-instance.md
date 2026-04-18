---
description: A compute instance running in Oracle Cloud Infrastructure.
layout: schema
name: Instance
properties_list:
- description: The OCID of the instance.
  name: id
  type: string
- description: The OCID of the compartment.
  name: compartmentId
  type: string
- description: The availability domain the instance is running in.
  name: availabilityDomain
  type: string
- description: A user-friendly name.
  name: displayName
  type: string
- description: The shape of the instance.
  name: shape
  type: string
- description: The current state of the instance.
  name: lifecycleState
  type: string
- description: The region that contains the availability domain.
  name: region
  type: string
- description: The OCID of the image used to boot the instance.
  name: imageId
  type: string
- description: The date and time the instance was created.
  name: timeCreated
  type: string
- description: Free-form tags for the instance.
  name: freeformTags
  type: object
- description: Defined tags for the instance.
  name: definedTags
  type: object
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/compute-instance-schema.json
slug: compute-instance
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: Instance
---
