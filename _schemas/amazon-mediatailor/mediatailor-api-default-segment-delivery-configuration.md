---
description: The optional configuration for a server that serves segments. Use this if you want the segment delivery server to be different from the source location server. For example, you can configure your source location server to be an origination server, such as MediaPackage, and the segment delivery server to be a content delivery network (CDN), such as CloudFront. If you don't specify a segment delivery server, then the source location server is used.
layout: schema
name: DefaultSegmentDeliveryConfiguration
properties_list:
- description: ''
  name: BaseUrl
  type: object
provider_name: Amazon MediaTailor
provider_slug: amazon-mediatailor
schema_file: json-schema/mediatailor-api-default-segment-delivery-configuration-schema.json
slug: mediatailor-api-default-segment-delivery-configuration
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: DefaultSegmentDeliveryConfiguration
---
