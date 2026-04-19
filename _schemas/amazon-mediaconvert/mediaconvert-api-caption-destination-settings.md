---
description: Settings related to one captions tab on the MediaConvert console. In your job JSON, an instance of captions DestinationSettings is equivalent to one captions tab in the console. Usually, one captions tab corresponds to one output captions track. Depending on your output captions format, one tab might correspond to a set of output captions tracks. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/including-captions.html.
layout: schema
name: CaptionDestinationSettings
properties_list:
- description: ''
  name: BurninDestinationSettings
  type: object
- description: ''
  name: DestinationType
  type: object
- description: ''
  name: DvbSubDestinationSettings
  type: object
- description: ''
  name: EmbeddedDestinationSettings
  type: object
- description: ''
  name: ImscDestinationSettings
  type: object
- description: ''
  name: SccDestinationSettings
  type: object
- description: ''
  name: SrtDestinationSettings
  type: object
- description: ''
  name: TeletextDestinationSettings
  type: object
- description: ''
  name: TtmlDestinationSettings
  type: object
- description: ''
  name: WebvttDestinationSettings
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-caption-destination-settings-schema.json
slug: mediaconvert-api-caption-destination-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: CaptionDestinationSettings
---
