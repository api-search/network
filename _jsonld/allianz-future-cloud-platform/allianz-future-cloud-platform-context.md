---
class_count: 12
classes:
- Deployment
- MetricsResponse
- InfrastructureResource
- NamespaceList
- DeployServiceRequest
- DeploymentList
- ResourceRequirements
- Service
- RegisterServiceRequest
- ServiceList
- ProvisionResourceRequest
- Namespace
context_file: json-ld/allianz-future-cloud-platform-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/allianz-future-cloud-platform/refs/heads/main/json-ld/allianz-future-cloud-platform-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Allianz Future Cloud Platform from Allianz Future Cloud Platform.
layout: jsonld
name: Allianz Future Cloud Platform Context
namespaces:
- prefix: allianz
  uri: https://platform.allianz.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: deploymentId
  type: string
- container: ''
  name: serviceId
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: image
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: strategy
  type: string
- container: ''
  name: deployedAt
  type: dateTime
- container: ''
  name: deployedBy
  type: string
- container: ''
  name: initiatedAt
  type: dateTime
- container: ''
  name: timeRangeMinutes
  type: integer
- container: ''
  name: cpuUtilization
  type: double
- container: ''
  name: memoryUtilization
  type: double
- container: ''
  name: requestRate
  type: double
- container: ''
  name: errorRate
  type: double
- container: ''
  name: p99LatencyMs
  type: integer
- container: ''
  name: resourceId
  type: string
- container: ''
  name: resourceType
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: namespace
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: total
  type: integer
- container: set
  name: items
  type: string
- container: ''
  name: cpu
  type: string
- container: ''
  name: memory
  type: string
- container: ''
  name: cpuLimit
  type: string
- container: ''
  name: memoryLimit
  type: string
- container: ''
  name: replicas
  type: integer
- container: ''
  name: language
  type: string
- container: ''
  name: repositoryUrl
  type: reference
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: resourceRequirements
  type: string
- container: ''
  name: configuration
  type: string
- container: ''
  name: namespaceId
  type: string
- container: ''
  name: team
  type: string
- container: ''
  name: serviceCount
  type: integer
property_count: 35
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
slug: allianz-future-cloud-platform-context
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
- JSON-LD
- Linked Data
- Semantic Web
---
