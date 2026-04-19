---
description: Use inputs to define the source files used in your transcoding job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/specify-input-settings.html. You can use multiple video inputs to do input stitching. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/assembling-multiple-inputs-and-input-clips.html
layout: schema
name: Input
properties_list:
- description: ''
  name: AudioSelectorGroups
  type: object
- description: ''
  name: AudioSelectors
  type: object
- description: ''
  name: CaptionSelectors
  type: object
- description: ''
  name: Crop
  type: object
- description: ''
  name: DeblockFilter
  type: object
- description: ''
  name: DecryptionSettings
  type: object
- description: ''
  name: DenoiseFilter
  type: object
- description: ''
  name: DolbyVisionMetadataXml
  type: object
- description: ''
  name: FileInput
  type: object
- description: ''
  name: FilterEnable
  type: object
- description: ''
  name: FilterStrength
  type: object
- description: ''
  name: ImageInserter
  type: object
- description: ''
  name: InputClippings
  type: object
- description: ''
  name: InputScanType
  type: object
- description: ''
  name: Position
  type: object
- description: ''
  name: ProgramNumber
  type: object
- description: ''
  name: PsiControl
  type: object
- description: ''
  name: SupplementalImps
  type: object
- description: ''
  name: TimecodeSource
  type: object
- description: ''
  name: TimecodeStart
  type: object
- description: ''
  name: VideoGenerator
  type: object
- description: ''
  name: VideoSelector
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-input-schema.json
slug: mediaconvert-api-input
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: Input
---
