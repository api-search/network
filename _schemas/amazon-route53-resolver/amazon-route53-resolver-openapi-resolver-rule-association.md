---
description: In the response to an <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverRule.html">AssociateResolverRule</a>, <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverRule.html">DisassociateResolverRule</a>, or <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html">ListResolverRuleAssociations</a> request, provides information about an association between a Resolver rule and a VPC. The association determines which DNS queries that originate in the VPC are forwarded to your network.
layout: schema
name: ResolverRuleAssociation
properties_list:
- description: ''
  name: Id
  type: object
- description: ''
  name: ResolverRuleId
  type: object
- description: ''
  name: Name
  type: object
- description: ''
  name: VPCId
  type: object
- description: ''
  name: Status
  type: object
- description: ''
  name: StatusMessage
  type: object
provider_name: Amazon Route 53 Resolver
provider_slug: amazon-route53-resolver
schema_file: json-schema/amazon-route53-resolver-openapi-resolver-rule-association-schema.json
slug: amazon-route53-resolver-openapi-resolver-rule-association
tags:
- AWS
- DNS
- Hybrid Cloud
- Networking
title: ResolverRuleAssociation
---
