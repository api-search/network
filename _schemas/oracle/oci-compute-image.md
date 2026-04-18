---
description: A boot disk image for launching compute instances. Images can be platform images provided by Oracle, custom images, or Marketplace partner images.
layout: schema
name: Image
properties_list:
- description: The OCID of the image
  name: id
  type: string
- description: The OCID of the compartment containing the image
  name: compartmentId
  type: string
- description: A user-friendly name for the image. It does not have to be unique, and it is changeable.
  name: displayName
  type: string
- description: The image operating system (e.g., Oracle Linux)
  name: operatingSystem
  type: string
- description: The image operating system version (e.g., 8, 9)
  name: operatingSystemVersion
  type: string
- description: The date and time the image was created
  name: timeCreated
  type: string
- description: The OCID of the image originally used to create this custom image
  name: baseImageId
  type: string
- description: The boot volume size for an instance launched from this image, in MBs
  name: sizeInMBs
  type: integer
- description: The billable size of the image in GBs
  name: billableSizeInGBs
  type: integer
- description: Whether instances launched from this image can be used to create new images
  name: createImageAllowed
  type: boolean
- description: Oracle Cloud Agent features supported on the image
  name: agentFeatures
  type: object
- description: The launch mode of instances created from this image
  name: launchMode
  type: string
- description: The listing type of the image
  name: listingType
  type: string
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-image-schema.json
slug: oci-compute-image
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: Image
---
