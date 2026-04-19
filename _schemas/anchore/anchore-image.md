---
description: Schema for a container image analyzed by Anchore Enterprise
layout: schema
name: Anchore Image
properties_list:
- description: SHA256 digest of the image
  name: imageDigest
  type: string
- description: ''
  name: analysisStatus
  type: string
- description: ''
  name: imageStatus
  type: string
- description: ''
  name: createdAt
  type: string
- description: ''
  name: updatedAt
  type: string
- description: ''
  name: imageContent
  type: object
provider_name: Anchore
provider_slug: anchore
schema_file: json-schema/anchore-image-schema.json
slug: anchore-image
tags:
- Container Security
- Containers
- SBOM
- Software Supply Chain
- Vulnerability Scanning
title: Anchore Image
---
