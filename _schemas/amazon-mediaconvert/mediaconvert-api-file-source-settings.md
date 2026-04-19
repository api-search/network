---
description: If your input captions are SCC, SMI, SRT, STL, TTML, WebVTT, or IMSC 1.1 in an xml file, specify the URI of the input caption source file. If your caption source is IMSC in an IMF package, use TrackSourceSettings instead of FileSoureSettings.
layout: schema
name: FileSourceSettings
properties_list:
- description: ''
  name: Convert608To708
  type: object
- description: ''
  name: Framerate
  type: object
- description: ''
  name: SourceFile
  type: object
- description: ''
  name: TimeDelta
  type: object
- description: ''
  name: TimeDeltaUnits
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-file-source-settings-schema.json
slug: mediaconvert-api-file-source-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: FileSourceSettings
---
