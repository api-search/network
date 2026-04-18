---
description: Details for importing an image from Object Storage
layout: schema
name: ImageSourceDetails
properties_list:
- description: The source type for the image
  name: sourceType
  type: string
- description: The Object Storage bucket name (for objectStorageTuple)
  name: bucketName
  type: string
- description: The Object Storage namespace (for objectStorageTuple)
  name: namespaceName
  type: string
- description: The Object Storage object name (for objectStorageTuple)
  name: objectName
  type: string
- description: The Object Storage URL for the image (for objectStorageUri source type)
  name: sourceUri
  type: string
- description: The format of the image to import
  name: sourceImageType
  type: string
- description: The operating system of the image
  name: operatingSystem
  type: string
- description: The operating system version of the image
  name: operatingSystemVersion
  type: string
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-image-source-details-schema.json
slug: oci-compute-image-source-details
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: ImageSourceDetails
---
