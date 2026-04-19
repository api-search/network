---
description: Use these settings to specify static color calibration metadata, as defined by SMPTE ST 2086. These values don't affect the pixel values that are encoded in the video stream. They are intended to help the downstream video player display content in a way that reflects the intentions of the the content creator.
layout: schema
name: Hdr10Metadata
properties_list:
- description: ''
  name: BluePrimaryX
  type: object
- description: ''
  name: BluePrimaryY
  type: object
- description: ''
  name: GreenPrimaryX
  type: object
- description: ''
  name: GreenPrimaryY
  type: object
- description: ''
  name: MaxContentLightLevel
  type: object
- description: ''
  name: MaxFrameAverageLightLevel
  type: object
- description: ''
  name: MaxLuminance
  type: object
- description: ''
  name: MinLuminance
  type: object
- description: ''
  name: RedPrimaryX
  type: object
- description: ''
  name: RedPrimaryY
  type: object
- description: ''
  name: WhitePointX
  type: object
- description: ''
  name: WhitePointY
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-hdr10-metadata-schema.json
slug: mediaconvert-api-hdr10-metadata
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: Hdr10Metadata
---
