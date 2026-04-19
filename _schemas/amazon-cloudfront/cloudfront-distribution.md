---
description: Distribution schema
layout: schema
name: Distribution
properties_list:
- description: The distribution's unique identifier.
  name: Id
  type: string
- description: The ARN of the distribution.
  name: ARN
  type: string
- description: The current status of the distribution (e.g., Deployed, InProgress).
  name: Status
  type: string
- description: The date and time the distribution was last modified.
  name: LastModifiedTime
  type: string
- description: The domain name corresponding to the distribution (e.g., d111111abcdef8.cloudfront.net).
  name: DomainName
  type: string
- description: ''
  name: DistributionConfig
  type: object
provider_name: Amazon CloudFront
provider_slug: amazon-cloudfront
schema_file: json-schema/cloudfront-distribution-schema.json
slug: cloudfront-distribution
tags:
- AWS
- CloudFront
- CDN
- Content Delivery
- Edge
title: Distribution
---
