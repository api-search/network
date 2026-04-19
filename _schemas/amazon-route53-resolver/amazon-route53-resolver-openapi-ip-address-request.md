---
description: In a <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html">CreateResolverEndpoint</a> request, the IP address that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). <code>IpAddressRequest</code> also includes the ID of the subnet that contains the IP address.
layout: schema
name: IpAddressRequest
properties_list:
- description: ''
  name: SubnetId
  type: object
- description: ''
  name: Ip
  type: object
- description: ''
  name: Ipv6
  type: object
provider_name: Amazon Route 53 Resolver
provider_slug: amazon-route53-resolver
schema_file: json-schema/amazon-route53-resolver-openapi-ip-address-request-schema.json
slug: amazon-route53-resolver-openapi-ip-address-request
tags:
- AWS
- DNS
- Hybrid Cloud
- Networking
title: IpAddressRequest
---
