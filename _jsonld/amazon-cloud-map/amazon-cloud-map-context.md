---
class_count: 15
classes:
- Namespace
- name
- description
- Service
- Instance
- HttpInstanceSummary
- ListNamespacesResponse
- ListServicesResponse
- CreateServiceRequest
- CreateServiceResponse
- ListInstancesResponse
- RegisterInstanceRequest
- RegisterInstanceResponse
- DiscoverInstancesRequest
- DiscoverInstancesResponse
context_file: json-ld/amazon-cloud-map-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloud-map/refs/heads/main/json-ld/amazon-cloud-map-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Cloud Map from Amazon Cloud Map.
layout: jsonld
name: Amazon Cloud Map Context
namespaces:
- prefix: cloudmap
  uri: https://aws.amazon.com/cloud-map/schema/
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
  name: arn
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: createDate
  type: dateTime
- container: ''
  name: namespaceId
  type: string
- container: ''
  name: instanceCount
  type: integer
- container: ''
  name: attributes
  type: string
- container: ''
  name: instanceId
  type: string
- container: ''
  name: namespaceName
  type: string
- container: ''
  name: serviceName
  type: string
- container: ''
  name: healthStatus
  type: string
- container: set
  name: namespaces
  type: string
- container: ''
  name: nextToken
  type: string
- container: set
  name: services
  type: string
- container: ''
  name: dnsConfig
  type: string
- container: ''
  name: creatorRequestId
  type: string
- container: ''
  name: service
  type: string
- container: set
  name: instances
  type: string
- container: ''
  name: operationId
  type: string
- container: ''
  name: maxResults
  type: integer
property_count: 20
provider_name: Amazon Cloud Map
provider_slug: amazon-cloud-map
slug: amazon-cloud-map-context
tags:
- AWS
- Cloud Map
- Service Discovery
- Microservices
- DNS
- JSON-LD
- Linked Data
- Semantic Web
---
