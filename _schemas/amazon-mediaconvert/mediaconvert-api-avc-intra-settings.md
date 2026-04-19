---
description: Required when you choose AVC-Intra for your output video codec. For more information about the AVC-Intra settings, see the relevant specification. For detailed information about SD and HD in AVC-Intra, see https://ieeexplore.ieee.org/document/7290936. For information about 4K/2K in AVC-Intra, see https://pro-av.panasonic.net/en/avc-ultra/AVC-ULTRAoverview.pdf.
layout: schema
name: AvcIntraSettings
properties_list:
- description: ''
  name: AvcIntraClass
  type: object
- description: ''
  name: AvcIntraUhdSettings
  type: object
- description: ''
  name: FramerateControl
  type: object
- description: ''
  name: FramerateConversionAlgorithm
  type: object
- description: ''
  name: FramerateDenominator
  type: object
- description: ''
  name: FramerateNumerator
  type: object
- description: ''
  name: InterlaceMode
  type: object
- description: ''
  name: ScanTypeConversionMode
  type: object
- description: ''
  name: SlowPal
  type: object
- description: ''
  name: Telecine
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-avc-intra-settings-schema.json
slug: mediaconvert-api-avc-intra-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: AvcIntraSettings
---
