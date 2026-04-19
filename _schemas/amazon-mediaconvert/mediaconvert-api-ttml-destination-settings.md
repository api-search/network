---
description: Settings related to TTML captions. TTML is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html. When you work directly in your JSON job specification, include this object and any required children when you set destinationType to TTML.
layout: schema
name: TtmlDestinationSettings
properties_list:
- description: ''
  name: StylePassthrough
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-ttml-destination-settings-schema.json
slug: mediaconvert-api-ttml-destination-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: TtmlDestinationSettings
---
