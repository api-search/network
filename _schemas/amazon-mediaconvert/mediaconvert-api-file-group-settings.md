---
description: Settings related to your File output group. MediaConvert uses this group of settings to generate a single standalone file, rather than a streaming package. When you work directly in your JSON job specification, include this object and any required children when you set Type, under OutputGroupSettings, to FILE_GROUP_SETTINGS.
layout: schema
name: FileGroupSettings
properties_list:
- description: ''
  name: Destination
  type: object
- description: ''
  name: DestinationSettings
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-file-group-settings-schema.json
slug: mediaconvert-api-file-group-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: FileGroupSettings
---
