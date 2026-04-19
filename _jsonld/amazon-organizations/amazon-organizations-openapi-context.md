---
class_count: 4
classes:
- Account
- Organization
- OrganizationalUnit
- Policy
context_file: json-ld/amazon-organizations-openapi-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-organizations/refs/heads/main/json-ld/amazon-organizations-openapi-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Organizations Openapi from Amazon Organizations.
layout: jsonld
name: Amazon Organizations Openapi Context
namespaces:
- prefix: organizations
  uri: https://organizations.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Arn
  type: string
- container: ''
  name: Content
  type: string
- container: ''
  name: Email
  type: string
- container: ''
  name: FeatureSet
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: JoinedMethod
  type: string
- container: ''
  name: JoinedTimestamp
  type: dateTime
- container: ''
  name: MasterAccountArn
  type: string
- container: ''
  name: MasterAccountEmail
  type: string
- container: ''
  name: MasterAccountId
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: PolicySummary
  type: reference
- container: ''
  name: Status
  type: string
- container: ''
  name: Type
  type: string
property_count: 14
provider_name: Amazon Organizations
provider_slug: amazon-organizations
slug: amazon-organizations-openapi-context
tags:
- Account Management
- AWS
- Consolidated Billing
- Governance
- Multi-Account
- Organizations
- Policies
- JSON-LD
- Linked Data
- Semantic Web
---
