---
description: Settings related to your HLS output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html. When you work directly in your JSON job specification, include this object and any required children when you set Type, under OutputGroupSettings, to HLS_GROUP_SETTINGS.
layout: schema
name: HlsGroupSettings
properties_list:
- description: ''
  name: AdMarkers
  type: object
- description: ''
  name: AdditionalManifests
  type: object
- description: ''
  name: AudioOnlyHeader
  type: object
- description: ''
  name: BaseUrl
  type: object
- description: ''
  name: CaptionLanguageMappings
  type: object
- description: ''
  name: CaptionLanguageSetting
  type: object
- description: ''
  name: CaptionSegmentLengthControl
  type: object
- description: ''
  name: ClientCache
  type: object
- description: ''
  name: CodecSpecification
  type: object
- description: ''
  name: Destination
  type: object
- description: ''
  name: DestinationSettings
  type: object
- description: ''
  name: DirectoryStructure
  type: object
- description: ''
  name: Encryption
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
  name: MinFinalSegmentLength
  type: object
- description: ''
  name: MinSegmentLength
  type: object
- description: ''
  name: OutputSelection
  type: object
- description: ''
  name: ProgramDateTime
  type: object
- description: ''
  name: ProgramDateTimePeriod
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
  name: SegmentsPerSubdirectory
  type: object
- description: ''
  name: StreamInfResolution
  type: object
- description: ''
  name: TargetDurationCompatibilityMode
  type: object
- description: ''
  name: TimedMetadataId3Frame
  type: object
- description: ''
  name: TimedMetadataId3Period
  type: object
- description: ''
  name: TimestampDeltaMilliseconds
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-hls-group-settings-schema.json
slug: mediaconvert-api-hls-group-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: HlsGroupSettings
---
