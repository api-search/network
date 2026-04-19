---
description: Settings related to SRT captions. SRT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. When you work directly in your JSON job specification, include this object and any required children when you set destinationType to SRT.
layout: schema
name: SrtDestinationSettings
properties_list:
- description: ''
  name: StylePassthrough
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-srt-destination-settings-schema.json
slug: mediaconvert-api-srt-destination-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: SrtDestinationSettings
---
