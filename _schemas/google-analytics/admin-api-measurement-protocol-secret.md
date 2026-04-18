---
description: A secret value used for sending hits to Measurement Protocol.
layout: schema
name: MeasurementProtocolSecret
properties_list:
- description: Required. Human-readable display name for this secret.
  name: displayName
  type: string
- description: 'Output only. Resource name of this secret. This secret may be a child of any type of stream. Format: properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{measurementProtocolSecre'
  name: name
  type: string
- description: Output only. The measurement protocol secret value. Pass this value to the api_secret field of the Measurement Protocol API when sending hits to this secret's parent property.
  name: secretValue
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/admin-api-measurement-protocol-secret-schema.json
slug: admin-api-measurement-protocol-secret
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: MeasurementProtocolSecret
---
