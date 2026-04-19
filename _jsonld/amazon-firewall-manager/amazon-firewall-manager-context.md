---
class_count: 5
classes:
- Policy
- ComplianceViolator
- ResourceSet
- SecurityServicePolicyData
- Tag
context_file: json-ld/amazon-firewall-manager-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-firewall-manager/refs/heads/main/json-ld/amazon-firewall-manager-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Firewall Manager from Amazon Firewall Manager.
layout: jsonld
name: Amazon Firewall Manager Context
namespaces:
- prefix: fms
  uri: https://aws.amazon.com/firewall-manager/vocabulary/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: PolicyId
  type: string
- container: ''
  name: PolicyName
  type: string
- container: ''
  name: PolicyArn
  type: string
- container: ''
  name: RemediationEnabled
  type: boolean
- container: ''
  name: ExcludeResourceTags
  type: boolean
- container: ''
  name: ResourceType
  type: string
- container: ''
  name: ResourceId
  type: string
- container: ''
  name: ViolationReason
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: LastUpdateTime
  type: dateTime
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
property_count: 14
provider_name: Amazon Firewall Manager
provider_slug: amazon-firewall-manager
slug: amazon-firewall-manager-context
tags:
- AWS
- Compliance
- Firewall
- Network Security
- Security
- JSON-LD
- Linked Data
- Semantic Web
---
