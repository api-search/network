---
description: Use these settings to insert a DVB Network Information Table (NIT) in the transport stream of this output. When you work directly in your JSON job specification, include this object only when your job has a transport stream output and the container settings contain the object M2tsSettings.
layout: schema
name: DvbNitSettings
properties_list:
- description: ''
  name: NetworkId
  type: object
- description: ''
  name: NetworkName
  type: object
- description: ''
  name: NitInterval
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-dvb-nit-settings-schema.json
slug: mediaconvert-api-dvb-nit-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: DvbNitSettings
---
