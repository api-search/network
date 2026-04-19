---
description: Use these settings only when you use Kantar watermarking. Specify the values that MediaConvert uses to generate and place Kantar watermarks in your output audio. These settings apply to every output in your job. In addition to specifying these values, you also need to store your Kantar credentials in AWS Secrets Manager. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/kantar-watermarking.html.
layout: schema
name: KantarWatermarkSettings
properties_list:
- description: ''
  name: ChannelName
  type: object
- description: ''
  name: ContentReference
  type: object
- description: ''
  name: CredentialsSecretName
  type: object
- description: ''
  name: FileOffset
  type: object
- description: ''
  name: KantarLicenseId
  type: object
- description: ''
  name: KantarServerUrl
  type: object
- description: ''
  name: LogDestination
  type: object
- description: ''
  name: Metadata3
  type: object
- description: ''
  name: Metadata4
  type: object
- description: ''
  name: Metadata5
  type: object
- description: ''
  name: Metadata6
  type: object
- description: ''
  name: Metadata7
  type: object
- description: ''
  name: Metadata8
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-kantar-watermark-settings-schema.json
slug: mediaconvert-api-kantar-watermark-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: KantarWatermarkSettings
---
