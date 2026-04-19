---
class_count: 18
classes:
- RejectVpcEndpointConnectionsRequest
- DescribeVpcEndpointsResult
- VpcEndpoint
- CreateVpcEndpointServiceConfigurationResult
- ServiceConfiguration
- ModifyVpcEndpointServicePermissionsRequest
- CreateVpcEndpointServiceConfigurationRequest
- ModifyVpcEndpointRequest
- VpcEndpointConnection
- CreateVpcEndpointResult
- DeleteVpcEndpointServiceConfigurationsRequest
- DescribeVpcEndpointServicesResult
- AcceptVpcEndpointConnectionsRequest
- CreateVpcEndpointRequest
- DeleteVpcEndpointsRequest
- DescribeVpcEndpointConnectionsResult
- ModifyVpcEndpointServiceConfigurationRequest
- ServiceDetail
context_file: json-ld/amazon-privatelink-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-privatelink/refs/heads/main/json-ld/amazon-privatelink-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Privatelink from Amazon PrivateLink.
layout: jsonld
name: Amazon Privatelink Context
namespaces:
- prefix: pl
  uri: https://ec2.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: ServiceId
  type: string
- container: set
  name: VpcEndpointId
  type: string
- container: set
  name: VpcEndpoints
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: VpcEndpointType
  type: string
- container: ''
  name: VpcId
  type: string
- container: ''
  name: ServiceName
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: PolicyDocument
  type: string
- container: set
  name: SubnetIds
  type: string
- container: set
  name: NetworkInterfaceIds
  type: string
- container: set
  name: DnsEntries
  type: string
- container: set
  name: AddAllowedPrincipals
  type: string
- container: set
  name: RemoveAllowedPrincipals
  type: string
- container: set
  name: NetworkLoadBalancerArn
  type: string
- container: set
  name: GatewayLoadBalancerArn
  type: string
- container: ''
  name: AcceptanceRequired
  type: boolean
- container: ''
  name: PrivateDnsName
  type: string
- container: ''
  name: ResetPolicy
  type: boolean
- container: ''
  name: VpcEndpointOwner
  type: string
- container: ''
  name: VpcEndpointState
  type: string
- container: ''
  name: CreationTimestamp
  type: dateTime
- container: set
  name: ServiceNames
  type: string
- container: set
  name: ServiceDetails
  type: string
- container: set
  name: SubnetId
  type: string
- container: set
  name: SecurityGroupId
  type: string
- container: ''
  name: PrivateDnsEnabled
  type: boolean
- container: set
  name: ServiceType
  type: string
- container: ''
  name: ServiceState
  type: string
- container: set
  name: AvailabilityZones
  type: string
- container: set
  name: NetworkLoadBalancerArns
  type: string
- container: set
  name: VpcEndpointConnections
  type: string
- container: ''
  name: Owner
  type: string
- container: set
  name: BaseEndpointDnsNames
  type: string
property_count: 34
provider_name: Amazon PrivateLink
provider_slug: amazon-privatelink
slug: amazon-privatelink-context
tags:
- AWS
- Networking
- Private Connectivity
- Security
- VPC
- Zero Trust
- Endpoint Services
- JSON-LD
- Linked Data
- Semantic Web
---
