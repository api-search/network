---
description: <p>Settings for the size, location, and opacity of graphics that you want Elastic Transcoder to overlay over videos that are transcoded using this preset. You can specify settings for up to four watermarks. Watermarks appear in the specified size and location, and with the specified opacity for the duration of the transcoded video.</p> <p>Watermarks can be in .png or .jpg format. If you want to display a watermark that is not rectangular, use the .png format, which supports transparency.</p> <p>When you create a job that uses this preset, you specify the .png or .jpg graphics that you want Elastic Transcoder to include in the transcoded videos. You can specify fewer graphics in the job than you specify watermark settings in the preset, which allows you to use the same preset for up to four watermarks that have different dimensions.</p>
layout: schema
name: PresetWatermark
properties_list:
- description: ''
  name: Id
  type: object
- description: ''
  name: MaxWidth
  type: object
- description: ''
  name: MaxHeight
  type: object
- description: ''
  name: SizingPolicy
  type: object
- description: ''
  name: HorizontalAlign
  type: object
- description: ''
  name: HorizontalOffset
  type: object
- description: ''
  name: VerticalAlign
  type: object
- description: ''
  name: VerticalOffset
  type: object
- description: ''
  name: Opacity
  type: object
- description: ''
  name: Target
  type: object
provider_name: Amazon Elastic Transcoder
provider_slug: amazon-elastic-transcoder
schema_file: json-schema/amazon-elastic-transcoder-preset-watermark-schema.json
slug: amazon-elastic-transcoder-preset-watermark
tags:
- Amazon Web Services
- AWS
- Media
- Transcoding
- Video
title: PresetWatermark
---
