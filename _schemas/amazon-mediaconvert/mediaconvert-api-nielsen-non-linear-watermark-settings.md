---
description: 'Ignore these settings unless you are using Nielsen non-linear watermarking. Specify the values that MediaConvert uses to generate and place Nielsen watermarks in your output audio. In addition to specifying these values, you also need to set up your cloud TIC server. These settings apply to every output in your job. The MediaConvert implementation is currently with the following Nielsen versions: Nielsen Watermark SDK Version 5.2.1 Nielsen NLM Watermark Engine Version 1.2.7 Nielsen Watermark Authenticator [SID_TIC] Version [5.0.0]'
layout: schema
name: NielsenNonLinearWatermarkSettings
properties_list:
- description: ''
  name: ActiveWatermarkProcess
  type: object
- description: ''
  name: AdiFilename
  type: object
- description: ''
  name: AssetId
  type: object
- description: ''
  name: AssetName
  type: object
- description: ''
  name: CbetSourceId
  type: object
- description: ''
  name: EpisodeId
  type: object
- description: ''
  name: MetadataDestination
  type: object
- description: ''
  name: SourceId
  type: object
- description: ''
  name: SourceWatermarkStatus
  type: object
- description: ''
  name: TicServerUrl
  type: object
- description: ''
  name: UniqueTicPerAudioTrack
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-nielsen-non-linear-watermark-settings-schema.json
slug: mediaconvert-api-nielsen-non-linear-watermark-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: NielsenNonLinearWatermarkSettings
---
