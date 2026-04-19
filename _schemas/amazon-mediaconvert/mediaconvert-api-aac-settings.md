---
description: Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode (rateControlMode) to "VBR" or "CBR". In VBR mode, you control the audio quality with the setting VBR quality (vbrQuality). In CBR mode, you use the setting Bitrate (bitrate). Defaults and valid values depend on the rate control mode.
layout: schema
name: AacSettings
properties_list:
- description: ''
  name: AudioDescriptionBroadcasterMix
  type: object
- description: ''
  name: Bitrate
  type: object
- description: ''
  name: CodecProfile
  type: object
- description: ''
  name: CodingMode
  type: object
- description: ''
  name: RateControlMode
  type: object
- description: ''
  name: RawFormat
  type: object
- description: ''
  name: SampleRate
  type: object
- description: ''
  name: Specification
  type: object
- description: ''
  name: VbrQuality
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-aac-settings-schema.json
slug: mediaconvert-api-aac-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: AacSettings
---
