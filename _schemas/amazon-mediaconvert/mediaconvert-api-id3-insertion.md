---
description: To insert ID3 tags in your output, specify two values. Use ID3 tag (Id3) to specify the base 64 encoded string and use Timecode (TimeCode) to specify the time when the tag should be inserted. To insert multiple ID3 tags in your output, create multiple instances of ID3 insertion (Id3Insertion).
layout: schema
name: Id3Insertion
properties_list:
- description: ''
  name: Id3
  type: object
- description: ''
  name: Timecode
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-id3-insertion-schema.json
slug: mediaconvert-api-id3-insertion
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: Id3Insertion
---
