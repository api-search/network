---
description: Use these settings to insert a DVB Service Description Table (SDT) in the transport stream of this output. When you work directly in your JSON job specification, include this object only when your job has a transport stream output and the container settings contain the object M2tsSettings.
layout: schema
name: DvbSdtSettings
properties_list:
- description: ''
  name: OutputSdt
  type: object
- description: ''
  name: SdtInterval
  type: object
- description: ''
  name: ServiceName
  type: object
- description: ''
  name: ServiceProviderName
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-dvb-sdt-settings-schema.json
slug: mediaconvert-api-dvb-sdt-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: DvbSdtSettings
---
