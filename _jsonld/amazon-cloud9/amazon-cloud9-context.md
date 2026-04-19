---
class_count: 7
classes:
- Environment
- name
- description
- ListEnvironmentsResponse
- CreateEnvironmentEC2Request
- CreateEnvironmentEC2Response
- DescribeEnvironmentsResponse
context_file: json-ld/amazon-cloud9-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloud9/refs/heads/main/json-ld/amazon-cloud9-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Cloud9 from Amazon Cloud9.
layout: jsonld
name: Amazon Cloud9 Context
namespaces:
- prefix: cloud
  uri: https://aws.amazon.com/cloud9/schema/
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
  name: type
  type: string
- container: ''
  name: connectionType
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: ownerArn
  type: string
- container: ''
  name: nextToken
  type: string
- container: set
  name: environmentIds
  type: ''
- container: ''
  name: instanceType
  type: string
- container: ''
  name: automaticStopTimeMinutes
  type: integer
- container: ''
  name: environmentId
  type: string
- container: set
  name: environments
  type: ''
property_count: 11
provider_name: Amazon Cloud9
provider_slug: amazon-cloud9
slug: amazon-cloud9-context
tags:
- AWS
- Cloud9
- IDE
- Development
- Browser-Based
- JSON-LD
- Linked Data
- Semantic Web
---
