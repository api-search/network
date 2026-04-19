---
description: Invalidation schema
layout: schema
name: Invalidation
properties_list:
- description: The identifier for the invalidation request.
  name: Id
  type: string
- description: The status of the invalidation request.
  name: Status
  type: string
- description: The date and time the invalidation request was created.
  name: CreateTime
  type: string
- description: ''
  name: InvalidationBatch
  type: object
provider_name: Amazon CloudFront
provider_slug: amazon-cloudfront
schema_file: json-schema/cloudfront-invalidation-schema.json
slug: cloudfront-invalidation
tags:
- AWS
- CloudFront
- CDN
- Content Delivery
- Edge
title: Invalidation
---
