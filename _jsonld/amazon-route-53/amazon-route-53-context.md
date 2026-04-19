---
class_count: 0
classes: []
context_file: json-ld/amazon-route-53-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-route-53/refs/heads/main/json-ld/amazon-route-53-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Route 53 from Amazon Route 53.
layout: jsonld
name: Amazon Route 53 Context
namespaces:
- prefix: route53
  uri: https://docs.aws.amazon.com/Route53/latest/APIReference/
- prefix: aws
  uri: https://aws.amazon.com/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: schema
  uri: https://schema.org/
properties:
- container: ''
  name: HostedZone
  type: reference
- container: ''
  name: ResourceRecordSet
  type: reference
- container: ''
  name: HealthCheck
  type: reference
- container: ''
  name: DelegationSet
  type: reference
property_count: 4
provider_name: Amazon Route 53
provider_slug: amazon-route-53
slug: amazon-route-53-context
tags:
- AWS
- DNS
- Domain Registration
- Health Checks
- Routing
- JSON-LD
- Linked Data
- Semantic Web
---
