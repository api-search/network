---
description: CacheBehavior schema
layout: schema
name: CacheBehavior
properties_list:
- description: The pattern that specifies which requests to apply the behavior to. Not required for the default cache behavior.
  name: PathPattern
  type: string
- description: The ID of the origin that you want CloudFront to route requests to.
  name: TargetOriginId
  type: string
- description: The protocol that viewers can use to access the files in the origin.
  name: ViewerProtocolPolicy
  type: string
- description: ''
  name: AllowedMethods
  type: object
- description: The unique identifier of the cache policy.
  name: CachePolicyId
  type: string
- description: The unique identifier of the origin request policy.
  name: OriginRequestPolicyId
  type: string
- description: Whether you want CloudFront to automatically compress certain files for this cache behavior.
  name: Compress
  type: boolean
- description: ''
  name: FunctionAssociations
  type: object
- description: ''
  name: LambdaFunctionAssociations
  type: object
provider_name: Amazon CloudFront
provider_slug: amazon-cloudfront
schema_file: json-schema/cloudfront-cache-behavior-schema.json
slug: cloudfront-cache-behavior
tags:
- AWS
- CloudFront
- CDN
- Content Delivery
- Edge
title: CacheBehavior
---
