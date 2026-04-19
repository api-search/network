---
description: InvalidationList schema
layout: schema
name: InvalidationList
properties_list:
- description: ''
  name: Marker
  type: string
- description: ''
  name: NextMarker
  type: string
- description: ''
  name: MaxItems
  type: integer
- description: ''
  name: IsTruncated
  type: boolean
- description: ''
  name: Quantity
  type: integer
- description: ''
  name: Items
  type: array
provider_name: Amazon CloudFront
provider_slug: amazon-cloudfront
schema_file: json-schema/cloudfront-invalidation-list-schema.json
slug: cloudfront-invalidation-list
tags:
- AWS
- CloudFront
- CDN
- Content Delivery
- Edge
title: InvalidationList
---
