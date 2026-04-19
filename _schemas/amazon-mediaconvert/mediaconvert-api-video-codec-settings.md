---
description: Video codec settings, (CodecSettings) under (VideoDescription), contains the group of settings related to video encoding. The settings in this group vary depending on the value that you choose for Video codec (Codec). For each codec enum that you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. * AV1, Av1Settings * AVC_INTRA, AvcIntraSettings * FRAME_CAPTURE, FrameCaptureSettings * H_264, H264Settings * H_265, H265Settings * MPEG2, Mpeg2Settings * PRORES, ProresSettings * VC3, Vc3Settings * VP8, Vp8Settings * VP9, Vp9Settings * XAVC, XavcSettings
layout: schema
name: VideoCodecSettings
properties_list:
- description: ''
  name: Av1Settings
  type: object
- description: ''
  name: AvcIntraSettings
  type: object
- description: ''
  name: Codec
  type: object
- description: ''
  name: FrameCaptureSettings
  type: object
- description: ''
  name: H264Settings
  type: object
- description: ''
  name: H265Settings
  type: object
- description: ''
  name: Mpeg2Settings
  type: object
- description: ''
  name: ProresSettings
  type: object
- description: ''
  name: Vc3Settings
  type: object
- description: ''
  name: Vp8Settings
  type: object
- description: ''
  name: Vp9Settings
  type: object
- description: ''
  name: XavcSettings
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-video-codec-settings-schema.json
slug: mediaconvert-api-video-codec-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: VideoCodecSettings
---
