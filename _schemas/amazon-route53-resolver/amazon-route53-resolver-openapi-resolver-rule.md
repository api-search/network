---
description: For queries that originate in your VPC, detailed information about a Resolver rule, which specifies how to route DNS queries out of the VPC. The <code>ResolverRule</code> parameter appears in the response to a <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html">CreateResolverRule</a>, <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverRule.html">DeleteResolverRule</a>, <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRule.html">GetResolverRule</a>, <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html">ListResolverRules</a>, or <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverRule.html">UpdateResolverRule</a> request.
layout: schema
name: ResolverRule
properties_list:
- description: ''
  name: Id
  type: object
- description: ''
  name: CreatorRequestId
  type: object
- description: ''
  name: Arn
  type: object
- description: ''
  name: DomainName
  type: object
- description: ''
  name: Status
  type: object
- description: ''
  name: StatusMessage
  type: object
- description: ''
  name: RuleType
  type: object
- description: ''
  name: Name
  type: object
- description: ''
  name: TargetIps
  type: object
- description: ''
  name: ResolverEndpointId
  type: object
- description: ''
  name: OwnerId
  type: object
- description: ''
  name: ShareStatus
  type: object
- description: ''
  name: CreationTime
  type: object
- description: ''
  name: ModificationTime
  type: object
provider_name: Amazon Route 53 Resolver
provider_slug: amazon-route53-resolver
schema_file: json-schema/amazon-route53-resolver-openapi-resolver-rule-schema.json
slug: amazon-route53-resolver-openapi-resolver-rule
tags:
- AWS
- DNS
- Hybrid Cloud
- Networking
title: ResolverRule
---
