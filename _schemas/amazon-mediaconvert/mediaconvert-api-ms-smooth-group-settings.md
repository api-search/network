---
description: Settings related to your Microsoft Smooth Streaming output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html. When you work directly in your JSON job specification, include this object and any required children when you set Type, under OutputGroupSettings, to MS_SMOOTH_GROUP_SETTINGS.
layout: schema
name: MsSmoothGroupSettings
properties_list:
- description: ''
  name: AdditionalManifests
  type: object
- description: ''
  name: AudioDeduplication
  type: object
- description: ''
  name: Destination
  type: object
- description: ''
  name: DestinationSettings
  type: object
- description: ''
  name: Encryption
  type: object
- description: ''
  name: FragmentLength
  type: object
- description: ''
  name: FragmentLengthControl
  type: object
- description: ''
  name: ManifestEncoding
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-ms-smooth-group-settings-schema.json
slug: mediaconvert-api-ms-smooth-group-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: MsSmoothGroupSettings
---
