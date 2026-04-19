---
class_count: 8
classes:
- Distribution
- DistributionConfig
- Origin
- CacheBehavior
- Invalidation
- InvalidationBatch
- DistributionList
- InvalidationList
context_file: json-ld/amazon-cloudfront-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudfront/refs/heads/main/json-ld/amazon-cloudfront-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Cloudfront from Amazon CloudFront.
layout: jsonld
name: Amazon Cloudfront Context
namespaces:
- prefix: cloudfront
  uri: https://aws.amazon.com/cloudfront/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: aRN
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: lastModifiedTime
  type: dateTime
- container: ''
  name: domainName
  type: string
- container: ''
  name: distributionConfig
  type: string
- container: ''
  name: callerReference
  type: string
- container: ''
  name: aliases
  type: string
- container: ''
  name: defaultRootObject
  type: string
- container: ''
  name: origins
  type: string
- container: ''
  name: defaultCacheBehavior
  type: string
- container: ''
  name: cacheBehaviors
  type: string
- container: ''
  name: comment
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: priceClass
  type: string
- container: ''
  name: viewerCertificate
  type: string
- container: ''
  name: webACLId
  type: string
- container: ''
  name: httpVersion
  type: string
- container: ''
  name: isIPV6Enabled
  type: boolean
- container: ''
  name: originPath
  type: string
- container: ''
  name: s3OriginConfig
  type: string
- container: ''
  name: customOriginConfig
  type: string
- container: ''
  name: pathPattern
  type: string
- container: ''
  name: targetOriginId
  type: string
- container: ''
  name: viewerProtocolPolicy
  type: string
- container: ''
  name: allowedMethods
  type: string
- container: ''
  name: cachePolicyId
  type: string
- container: ''
  name: originRequestPolicyId
  type: string
- container: ''
  name: compress
  type: boolean
- container: ''
  name: functionAssociations
  type: string
- container: ''
  name: lambdaFunctionAssociations
  type: string
- container: ''
  name: createTime
  type: dateTime
- container: ''
  name: invalidationBatch
  type: string
- container: ''
  name: paths
  type: string
- container: ''
  name: marker
  type: string
- container: ''
  name: nextMarker
  type: string
- container: ''
  name: maxItems
  type: integer
- container: ''
  name: isTruncated
  type: boolean
- container: ''
  name: quantity
  type: integer
- container: set
  name: items
  type: string
property_count: 40
provider_name: Amazon CloudFront
provider_slug: amazon-cloudfront
slug: amazon-cloudfront-context
tags:
- AWS
- CloudFront
- CDN
- Content Delivery
- Edge
- JSON-LD
- Linked Data
- Semantic Web
---
