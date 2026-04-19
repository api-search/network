---
description: Settings for your Nielsen configuration. If you don't do Nielsen measurement and analytics, ignore these settings. When you enable Nielsen configuration (nielsenConfiguration), MediaConvert enables PCM to ID3 tagging for all outputs in the job. To enable Nielsen configuration programmatically, include an instance of nielsenConfiguration in your JSON job specification. Even if you don't include any children of nielsenConfiguration, you still enable the setting.
layout: schema
name: NielsenConfiguration
properties_list:
- description: ''
  name: BreakoutCode
  type: object
- description: ''
  name: DistributorId
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-nielsen-configuration-schema.json
slug: mediaconvert-api-nielsen-configuration
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: NielsenConfiguration
---
