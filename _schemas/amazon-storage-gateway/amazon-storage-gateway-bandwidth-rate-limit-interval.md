---
description: Describes a bandwidth rate limit interval for a gateway. A bandwidth rate limit schedule consists of one or more bandwidth rate limit intervals. A bandwidth rate limit interval defines a period of time on one or more days of the week, during which bandwidth rate limits are specified for uploading, downloading, or both.
layout: schema
name: BandwidthRateLimitInterval
properties_list:
- description: ''
  name: StartHourOfDay
  type: object
- description: ''
  name: StartMinuteOfHour
  type: object
- description: ''
  name: EndHourOfDay
  type: object
- description: ''
  name: EndMinuteOfHour
  type: object
- description: ''
  name: DaysOfWeek
  type: object
- description: ''
  name: AverageUploadRateLimitInBitsPerSec
  type: object
- description: ''
  name: AverageDownloadRateLimitInBitsPerSec
  type: object
provider_name: Amazon Storage Gateway
provider_slug: amazon-storage-gateway
schema_file: json-schema/amazon-storage-gateway-bandwidth-rate-limit-interval-schema.json
slug: amazon-storage-gateway-bandwidth-rate-limit-interval
tags:
- AWS
- Backup
- File Storage
- Gateway
- Hybrid Cloud
- Storage
title: BandwidthRateLimitInterval
---
