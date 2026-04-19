---
description: Schema for an Amazon CloudFront distribution resource, representing a CDN distribution that delivers content from origins to edge locations worldwide.
layout: schema
name: Amazon CloudFront Distribution
properties_list:
- description: The unique identifier for the distribution.
  name: Id
  type: string
- description: The ARN (Amazon Resource Name) for the distribution.
  name: ARN
  type: string
- description: The current status of the distribution.
  name: Status
  type: string
- description: The date and time the distribution was last modified.
  name: LastModifiedTime
  type: string
- description: The CloudFront domain name assigned to the distribution (e.g., d111111abcdef8.cloudfront.net).
  name: DomainName
  type: string
- description: The distribution's configuration.
  name: DistributionConfig
  type: object
provider_name: Amazon CloudFront
provider_slug: amazon-cloudfront
schema_file: json-schema/amazon-cloudfront-distribution-schema.json
slug: amazon-cloudfront-distribution
tags:
- AWS
- CloudFront
- CDN
- Content Delivery
- Edge
title: Amazon CloudFront Distribution
---
