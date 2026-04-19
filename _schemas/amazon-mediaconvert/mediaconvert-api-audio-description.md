---
description: Settings related to one audio tab on the MediaConvert console. In your job JSON, an instance of AudioDescription is equivalent to one audio tab in the console. Usually, one audio tab corresponds to one output audio track. Depending on how you set up your input audio selectors and whether you use audio selector groups, one audio tab can correspond to a group of output audio tracks.
layout: schema
name: AudioDescription
properties_list:
- description: ''
  name: AudioChannelTaggingSettings
  type: object
- description: ''
  name: AudioNormalizationSettings
  type: object
- description: ''
  name: AudioSourceName
  type: object
- description: ''
  name: AudioType
  type: object
- description: ''
  name: AudioTypeControl
  type: object
- description: ''
  name: CodecSettings
  type: object
- description: ''
  name: CustomLanguageCode
  type: object
- description: ''
  name: LanguageCode
  type: object
- description: ''
  name: LanguageCodeControl
  type: object
- description: ''
  name: RemixSettings
  type: object
- description: ''
  name: StreamName
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-audio-description-schema.json
slug: mediaconvert-api-audio-description
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: AudioDescription
---
