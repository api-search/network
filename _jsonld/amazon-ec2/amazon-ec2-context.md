---
class_count: 6
classes:
- Amazon EC2 Instance
- CreateImageResponse
- DescribeInstancesResponse
- Instance
- RunInstancesResponse
- Tag
context_file: json-ld/amazon-ec2-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-ec2/refs/heads/main/json-ld/amazon-ec2-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Ec2 from Amazon EC2.
layout: jsonld
name: Amazon Ec2 Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: pan
  uri: https://aws.amazon.com/schema/
properties:
- container: ''
  name: instanceId
  type: string
- container: ''
  name: imageId
  type: string
- container: ''
  name: instanceType
  type: string
- container: ''
  name: keyName
  type: string
- container: ''
  name: launchTime
  type: dateTime
- container: ''
  name: placement
  type: reference
- container: ''
  name: availabilityZone
  type: string
- container: ''
  name: monitoring
  type: reference
- container: ''
  name: state
  type: string
- container: ''
  name: instanceState
  type: reference
- container: ''
  name: code
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: subnetId
  type: string
- container: ''
  name: vpcId
  type: string
- container: ''
  name: privateIpAddress
  type: string
- container: ''
  name: publicIpAddress
  type: string
- container: ''
  name: architecture
  type: string
- container: ''
  name: rootDeviceType
  type: string
- container: set
  name: tags
  type: string
- container: set
  name: securityGroups
  type: string
- container: ''
  name: groupId
  type: string
- container: ''
  name: groupName
  type: string
- container: ''
  name: reservationId
  type: string
- container: ''
  name: ownerId
  type: string
- container: set
  name: instances
  type: string
- container: ''
  name: rootDeviceName
  type: string
- container: set
  name: blockDeviceMappings
  type: string
- container: ''
  name: platform
  type: string
- container: ''
  name: ebsOptimized
  type: boolean
- container: ''
  name: enaSupport
  type: boolean
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: set
  name: reservationSet
  type: string
- container: ''
  name: nextToken
  type: string
- container: set
  name: instancesSet
  type: string
property_count: 35
provider_name: Amazon EC2
provider_slug: amazon-ec2
slug: amazon-ec2-context
tags:
- AWS
- Cloud Computing
- Compute
- IaaS
- Infrastructure
- Virtual Machines
- JSON-LD
- Linked Data
- Semantic Web
---
