---
description: A resource message representing a data stream.
layout: schema
name: DataStream
properties_list:
- description: Data specific to Android app streams.
  name: androidAppStreamData
  type: object
- description: Output only. Time when this stream was originally created.
  name: createTime
  type: string
- description: Human-readable display name for the Data Stream. Required for web data streams. The max allowed display name length is 255 UTF-16 code units.
  name: displayName
  type: string
- description: Data specific to iOS app streams.
  name: iosAppStreamData
  type: object
- description: 'Output only. Resource name of this Data Stream. Format: properties/{property_id}/dataStreams/{stream_id} Example: "properties/1000/dataStreams/2000"'
  name: name
  type: string
- description: Required. Immutable. The type of this DataStream resource.
  name: type
  type: string
- description: Output only. Time when stream payload fields were last updated.
  name: updateTime
  type: string
- description: Data specific to web streams.
  name: webStreamData
  type: object
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/admin-api-data-stream-schema.json
slug: admin-api-data-stream
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: DataStream
---
