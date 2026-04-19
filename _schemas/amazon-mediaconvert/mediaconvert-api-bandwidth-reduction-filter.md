---
description: The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor.
layout: schema
name: BandwidthReductionFilter
properties_list:
- description: ''
  name: Sharpening
  type: object
- description: ''
  name: Strength
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-bandwidth-reduction-filter-schema.json
slug: mediaconvert-api-bandwidth-reduction-filter
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: BandwidthReductionFilter
---
