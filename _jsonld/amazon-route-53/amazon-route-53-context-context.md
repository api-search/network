---
class_count: 14
classes:
- Amazon Route 53 Hosted Zone
- ChangeResourceRecordSetsRequest
- ChangeResourceRecordSetsResponse
- CreateHealthCheckRequest
- CreateHealthCheckResponse
- CreateHostedZoneRequest
- CreateHostedZoneResponse
- DeleteHostedZoneResponse
- GetHealthCheckResponse
- GetHostedZoneResponse
- ListHealthChecksResponse
- ListHostedZonesResponse
- ListResourceRecordSetsResponse
- ResourceRecordSet
context_file: json-ld/amazon-route-53-context-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-route-53/refs/heads/main/json-ld/amazon-route-53-context-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Route 53 from Amazon Route 53.
layout: jsonld
name: Amazon Route 53 Context
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
  name: ChangeInfo
  type: string
- container: ''
  name: DelegationSet
  type: string
- container: ''
  name: HealthCheck
  type: string
- container: ''
  name: HostedZone
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: CallerReference
  type: string
- container: ''
  name: Config
  type: string
- container: ''
  name: Comment
  type: string
- container: ''
  name: PrivateZone
  type: boolean
- container: ''
  name: ResourceRecordSetCount
  type: integer
- container: ''
  name: LinkedService
  type: string
- container: ''
  name: ServicePrincipal
  type: string
- container: ''
  name: Description
  type: string
- container: set
  name: NameServers
  type: string
- container: set
  name: VPCs
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: SubmittedAt
  type: dateTime
- container: ''
  name: ChangeBatch
  type: string
- container: set
  name: Changes
  type: string
- container: ''
  name: HealthCheckConfig
  type: string
- container: ''
  name: IPAddress
  type: string
- container: ''
  name: Port
  type: integer
- container: ''
  name: Type
  type: string
- container: ''
  name: ResourcePath
  type: string
- container: ''
  name: FullyQualifiedDomainName
  type: string
- container: ''
  name: RequestInterval
  type: integer
- container: ''
  name: FailureThreshold
  type: integer
- container: ''
  name: HostedZoneConfig
  type: string
- container: ''
  name: VPC
  type: string
- container: ''
  name: VPCRegion
  type: string
- container: ''
  name: VPCId
  type: string
- container: ''
  name: DelegationSetId
  type: string
- container: ''
  name: HealthCheckVersion
  type: integer
- container: set
  name: HealthChecks
  type: string
- container: ''
  name: Marker
  type: string
- container: ''
  name: IsTruncated
  type: boolean
- container: ''
  name: NextMarker
  type: string
- container: ''
  name: MaxItems
  type: integer
- container: set
  name: HostedZones
  type: string
- container: set
  name: ResourceRecordSets
  type: string
- container: ''
  name: NextRecordName
  type: string
- container: ''
  name: NextRecordType
  type: string
- container: ''
  name: NextRecordIdentifier
  type: string
- container: ''
  name: SetIdentifier
  type: string
- container: ''
  name: Weight
  type: integer
- container: ''
  name: Region
  type: string
- container: ''
  name: Failover
  type: string
- container: ''
  name: TTL
  type: integer
- container: set
  name: ResourceRecords
  type: string
- container: ''
  name: AliasTarget
  type: string
- container: ''
  name: HostedZoneId
  type: string
- container: ''
  name: DNSName
  type: string
- container: ''
  name: EvaluateTargetHealth
  type: boolean
- container: ''
  name: HealthCheckId
  type: string
property_count: 55
provider_name: Amazon Route 53
provider_slug: amazon-route-53
slug: amazon-route-53-context-context
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
