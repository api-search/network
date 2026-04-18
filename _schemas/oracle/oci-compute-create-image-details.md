---
description: Details for creating an image
layout: schema
name: CreateImageDetails
properties_list:
- description: The OCID of the compartment to create the image in
  name: compartmentId
  type: string
- description: A user-friendly name for the image. Avoid entering confidential information.
  name: displayName
  type: string
- description: The OCID of the instance to use as the basis for the image. Required if imageSourceDetails is not specified.
  name: instanceId
  type: string
- description: The launch mode for instances created from this image
  name: launchMode
  type: string
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-create-image-details-schema.json
slug: oci-compute-create-image-details
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: CreateImageDetails
---
