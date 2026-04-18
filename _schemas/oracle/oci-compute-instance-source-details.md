---
description: Details for creating an instance source
layout: schema
name: InstanceSourceDetails
properties_list:
- description: The source type for the instance
  name: sourceType
  type: string
- description: The OCID of the image used to boot the instance
  name: imageId
  type: string
- description: The OCID of the boot volume used to boot the instance
  name: bootVolumeId
  type: string
- description: The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 32,768 GB (32 TB).
  name: bootVolumeSizeInGBs
  type: integer
- description: The number of volume performance units (VPUs) per GB for the boot volume. Values range from 10 to 120. The default is 10 (Balanced).
  name: bootVolumeVpusPerGB
  type: integer
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-instance-source-details-schema.json
slug: oci-compute-instance-source-details
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: InstanceSourceDetails
---
