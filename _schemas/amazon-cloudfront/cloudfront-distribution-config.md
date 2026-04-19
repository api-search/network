---
description: DistributionConfig schema
layout: schema
name: DistributionConfig
properties_list:
- description: A unique value that ensures the request can't be replayed.
  name: CallerReference
  type: string
- description: CNAMEs (alternate domain names) for the distribution.
  name: Aliases
  type: object
- description: The object that you want CloudFront to return when an end user requests the root URL.
  name: DefaultRootObject
  type: string
- description: ''
  name: Origins
  type: object
- description: ''
  name: DefaultCacheBehavior
  type: object
- description: ''
  name: CacheBehaviors
  type: object
- description: A comment to describe the distribution.
  name: Comment
  type: string
- description: Whether the distribution is enabled to accept user requests.
  name: Enabled
  type: boolean
- description: The price class for the distribution.
  name: PriceClass
  type: string
- description: ''
  name: ViewerCertificate
  type: object
- description: The AWS WAF web ACL to associate with this distribution.
  name: WebACLId
  type: string
- description: ''
  name: HttpVersion
  type: string
- description: ''
  name: IsIPV6Enabled
  type: boolean
provider_name: Amazon CloudFront
provider_slug: amazon-cloudfront
schema_file: json-schema/cloudfront-distribution-config-schema.json
slug: cloudfront-distribution-config
tags:
- AWS
- CloudFront
- CDN
- Content Delivery
- Edge
title: DistributionConfig
---
