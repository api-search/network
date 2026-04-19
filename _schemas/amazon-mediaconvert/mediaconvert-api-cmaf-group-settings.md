---
description: Settings related to your CMAF output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html. When you work directly in your JSON job specification, include this object and any required children when you set Type, under OutputGroupSettings, to CMAF_GROUP_SETTINGS.
layout: schema
name: CmafGroupSettings
properties_list:
- description: ''
  name: AdditionalManifests
  type: object
- description: ''
  name: BaseUrl
  type: object
- description: ''
  name: ClientCache
  type: object
- description: ''
  name: CodecSpecification
  type: object
- description: ''
  name: DashManifestStyle
  type: object
- description: ''
  name: Destination
  type: object
- description: ''
  name: DestinationSettings
  type: object
- description: ''
  name: Encryption
  type: object
- description: ''
  name: FragmentLength
  type: object
- description: ''
  name: ImageBasedTrickPlay
  type: object
- description: ''
  name: ImageBasedTrickPlaySettings
  type: object
- description: ''
  name: ManifestCompression
  type: object
- description: ''
  name: ManifestDurationFormat
  type: object
- description: ''
  name: MinBufferTime
  type: object
- description: ''
  name: MinFinalSegmentLength
  type: object
- description: ''
  name: MpdManifestBandwidthType
  type: object
- description: ''
  name: MpdProfile
  type: object
- description: ''
  name: PtsOffsetHandlingForBFrames
  type: object
- description: ''
  name: SegmentControl
  type: object
- description: ''
  name: SegmentLength
  type: object
- description: ''
  name: SegmentLengthControl
  type: object
- description: ''
  name: StreamInfResolution
  type: object
- description: ''
  name: TargetDurationCompatibilityMode
  type: object
- description: ''
  name: VideoCompositionOffsets
  type: object
- description: ''
  name: WriteDashManifest
  type: object
- description: ''
  name: WriteHlsManifest
  type: object
- description: ''
  name: WriteSegmentTimelineInRepresentation
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-cmaf-group-settings-schema.json
slug: mediaconvert-api-cmaf-group-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: CmafGroupSettings
---
