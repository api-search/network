---
description: If your input captions are SCC, TTML, STL, SMI, SRT, or IMSC in an xml file, specify the URI of the input captions source file. If your input captions are IMSC in an IMF package, use TrackSourceSettings instead of FileSoureSettings.
layout: schema
name: CaptionSourceSettings
properties_list:
- description: ''
  name: AncillarySourceSettings
  type: object
- description: ''
  name: DvbSubSourceSettings
  type: object
- description: ''
  name: EmbeddedSourceSettings
  type: object
- description: ''
  name: FileSourceSettings
  type: object
- description: ''
  name: SourceType
  type: object
- description: ''
  name: TeletextSourceSettings
  type: object
- description: ''
  name: TrackSourceSettings
  type: object
- description: ''
  name: WebvttHlsSourceSettings
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-caption-source-settings-schema.json
slug: mediaconvert-api-caption-source-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: CaptionSourceSettings
---
