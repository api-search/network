---
description: MPEG-2 TS container settings. These apply to outputs in a File output group when the output's container (ContainerType) is MPEG-2 Transport Stream (M2TS). In these assets, data is organized by the program map table (PMT). Each transport stream program contains subsets of data, including audio, video, and metadata. Each of these subsets of data has a numerical label called a packet identifier (PID). Each transport stream program corresponds to one MediaConvert output. The PMT lists the types of data in a program along with their PID. Downstream systems and players use the program map table to look up the PID for each type of data it accesses and then uses the PIDs to locate specific data within the asset.
layout: schema
name: M2tsSettings
properties_list:
- description: ''
  name: AudioBufferModel
  type: object
- description: ''
  name: AudioDuration
  type: object
- description: ''
  name: AudioFramesPerPes
  type: object
- description: ''
  name: AudioPids
  type: object
- description: ''
  name: Bitrate
  type: object
- description: ''
  name: BufferModel
  type: object
- description: ''
  name: DataPTSControl
  type: object
- description: ''
  name: DvbNitSettings
  type: object
- description: ''
  name: DvbSdtSettings
  type: object
- description: ''
  name: DvbSubPids
  type: object
- description: ''
  name: DvbTdtSettings
  type: object
- description: ''
  name: DvbTeletextPid
  type: object
- description: ''
  name: EbpAudioInterval
  type: object
- description: ''
  name: EbpPlacement
  type: object
- description: ''
  name: EsRateInPes
  type: object
- description: ''
  name: ForceTsVideoEbpOrder
  type: object
- description: ''
  name: FragmentTime
  type: object
- description: ''
  name: KlvMetadata
  type: object
- description: ''
  name: MaxPcrInterval
  type: object
- description: ''
  name: MinEbpInterval
  type: object
- description: ''
  name: NielsenId3
  type: object
- description: ''
  name: NullPacketBitrate
  type: object
- description: ''
  name: PatInterval
  type: object
- description: ''
  name: PcrControl
  type: object
- description: ''
  name: PcrPid
  type: object
- description: ''
  name: PmtInterval
  type: object
- description: ''
  name: PmtPid
  type: object
- description: ''
  name: PrivateMetadataPid
  type: object
- description: ''
  name: ProgramNumber
  type: object
- description: ''
  name: RateMode
  type: object
- description: ''
  name: Scte35Esam
  type: object
- description: ''
  name: Scte35Pid
  type: object
- description: ''
  name: Scte35Source
  type: object
- description: ''
  name: SegmentationMarkers
  type: object
- description: ''
  name: SegmentationStyle
  type: object
- description: ''
  name: SegmentationTime
  type: object
- description: ''
  name: TimedMetadataPid
  type: object
- description: ''
  name: TransportStreamId
  type: object
- description: ''
  name: VideoPid
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-m2ts-settings-schema.json
slug: mediaconvert-api-m2ts-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: M2tsSettings
---
