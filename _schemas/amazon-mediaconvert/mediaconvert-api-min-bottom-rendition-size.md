---
description: 'Use Min bottom rendition size to specify a minimum size for the lowest resolution in your ABR stack. * The lowest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 640x360 the lowest resolution in your ABR stack will be equal to or greater than to 640x360. * If you specify a Min top rendition size rule, the value that you specify for Min bottom rendition size must be less than, or equal to, Min top rendition size.'
layout: schema
name: MinBottomRenditionSize
properties_list:
- description: ''
  name: Height
  type: object
- description: ''
  name: Width
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-min-bottom-rendition-size-schema.json
slug: mediaconvert-api-min-bottom-rendition-size
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: MinBottomRenditionSize
---
