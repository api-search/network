---
description: Origin schema
layout: schema
name: Origin
properties_list:
- description: A unique identifier for the origin.
  name: Id
  type: string
- description: The domain name for the origin (e.g., my-bucket.s3.amazonaws.com).
  name: DomainName
  type: string
- description: An optional path to append to the origin domain name.
  name: OriginPath
  type: string
- description: ''
  name: S3OriginConfig
  type: object
- description: ''
  name: CustomOriginConfig
  type: object
provider_name: Amazon CloudFront
provider_slug: amazon-cloudfront
schema_file: json-schema/cloudfront-origin-schema.json
slug: cloudfront-origin
tags:
- AWS
- CloudFront
- CDN
- Content Delivery
- Edge
title: Origin
---
