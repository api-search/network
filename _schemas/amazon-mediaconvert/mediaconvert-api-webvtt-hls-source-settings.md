---
description: Settings specific to WebVTT sources in HLS alternative rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique subtitle track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the specified properties, the job fails. If there is only one subtitle track in the rendition group, the settings can be left empty and the default subtitle track will be chosen. If your caption source is a sidecar file, use FileSourceSettings instead of WebvttHlsSourceSettings.
layout: schema
name: WebvttHlsSourceSettings
properties_list:
- description: ''
  name: RenditionGroupId
  type: object
- description: ''
  name: RenditionLanguageCode
  type: object
- description: ''
  name: RenditionName
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-webvtt-hls-source-settings-schema.json
slug: mediaconvert-api-webvtt-hls-source-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: WebvttHlsSourceSettings
---
