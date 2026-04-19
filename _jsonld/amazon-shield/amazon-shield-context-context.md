---
class_count: 14
classes:
- AttackDetail
- CreateProtectionGroupRequest
- CreateProtectionRequest
- CreateProtectionResponse
- DescribeAttackRequest
- DescribeAttackResponse
- DescribeProtectionRequest
- DescribeProtectionResponse
- ListProtectionsRequest
- ListProtectionsResponse
- Mitigation
- SummarizedCounter
- Tag
- Amazon Shield Protection
context_file: json-ld/amazon-shield-context-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-shield/refs/heads/main/json-ld/amazon-shield-context-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Shield from Amazon Shield.
layout: jsonld
name: Amazon Shield Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Protection
  type: string
- container: ''
  name: AttackId
  type: string
- container: ''
  name: ResourceArn
  type: string
- container: ''
  name: StartTime
  type: dateTime
- container: ''
  name: EndTime
  type: dateTime
- container: set
  name: AttackCounters
  type: string
- container: set
  name: Mitigations
  type: string
- container: ''
  name: ProtectionGroupId
  type: string
- container: ''
  name: Aggregation
  type: string
- container: ''
  name: Pattern
  type: string
- container: ''
  name: ResourceType
  type: string
- container: set
  name: Members
  type: string
- container: ''
  name: Name
  type: string
- container: set
  name: Tags
  type: string
- container: ''
  name: ProtectionId
  type: string
- container: ''
  name: Attack
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: MaxResults
  type: integer
- container: set
  name: Protections
  type: string
- container: ''
  name: MitigationName
  type: string
- container: ''
  name: Id
  type: string
- container: set
  name: HealthCheckIds
  type: string
- container: ''
  name: ProtectionArn
  type: string
- container: ''
  name: Max
  type: decimal
- container: ''
  name: Average
  type: decimal
- container: ''
  name: Sum
  type: decimal
- container: ''
  name: N
  type: integer
- container: ''
  name: Unit
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: ApplicationLayerAutomaticResponseConfiguration
  type: string
property_count: 31
provider_name: Amazon Shield
provider_slug: amazon-shield
slug: amazon-shield-context-context
tags:
- AWS
- DDoS Protection
- Networking
- Security
- JSON-LD
- Linked Data
- Semantic Web
---
