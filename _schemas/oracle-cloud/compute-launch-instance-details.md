---
description: Details for launching a new compute instance.
layout: schema
name: LaunchInstanceDetails
properties_list:
- description: The OCID of the compartment.
  name: compartmentId
  type: string
- description: The availability domain.
  name: availabilityDomain
  type: string
- description: The shape of the instance.
  name: shape
  type: string
- description: A user-friendly name.
  name: displayName
  type: string
- description: The OCID of the image to use.
  name: imageId
  type: string
- description: The OCID of the subnet.
  name: subnetId
  type: string
- description: Configuration for flexible shapes.
  name: shapeConfig
  type: object
- description: ''
  name: freeformTags
  type: object
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/compute-launch-instance-details-schema.json
slug: compute-launch-instance-details
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: LaunchInstanceDetails
---
