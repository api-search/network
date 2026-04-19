---
description: Settings related to CEA/EIA-608 and CEA/EIA-708 (also called embedded or ancillary) captions. Set up embedded captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/embedded-output-captions.html. When you work directly in your JSON job specification, include this object and any required children when you set destinationType to EMBEDDED, EMBEDDED_PLUS_SCTE20, or SCTE20_PLUS_EMBEDDED.
layout: schema
name: EmbeddedDestinationSettings
properties_list:
- description: ''
  name: Destination608ChannelNumber
  type: object
- description: ''
  name: Destination708ServiceNumber
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-embedded-destination-settings-schema.json
slug: mediaconvert-api-embedded-destination-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: EmbeddedDestinationSettings
---
