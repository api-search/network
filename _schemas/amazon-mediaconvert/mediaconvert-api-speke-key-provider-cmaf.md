---
description: If your output group type is CMAF, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is HLS, DASH, or Microsoft Smooth, use the SpekeKeyProvider settings instead.
layout: schema
name: SpekeKeyProviderCmaf
properties_list:
- description: ''
  name: CertificateArn
  type: object
- description: ''
  name: DashSignaledSystemIds
  type: object
- description: ''
  name: HlsSignaledSystemIds
  type: object
- description: ''
  name: ResourceId
  type: object
- description: ''
  name: Url
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-speke-key-provider-cmaf-schema.json
slug: mediaconvert-api-speke-key-provider-cmaf
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: SpekeKeyProviderCmaf
---
