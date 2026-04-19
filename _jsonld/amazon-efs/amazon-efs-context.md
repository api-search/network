---
class_count: 4
classes:
- Amazon EFS FileSystem
- DescribeFileSystemsResponse
- FileSystem
- MountTarget
context_file: json-ld/amazon-efs-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-efs/refs/heads/main/json-ld/amazon-efs-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Efs from Amazon EFS.
layout: jsonld
name: Amazon Efs Context
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
- container: set
  name: FileSystems
  type: string
- container: ''
  name: Marker
  type: string
- container: ''
  name: NextMarker
  type: string
- container: ''
  name: FileSystemId
  type: string
- container: ''
  name: FileSystemArn
  type: string
- container: ''
  name: CreationToken
  type: string
- container: ''
  name: OwnerId
  type: string
- container: ''
  name: CreationTime
  type: dateTime
- container: ''
  name: LifeCycleState
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: NumberOfMountTargets
  type: integer
- container: ''
  name: SizeInBytes
  type: reference
- container: ''
  name: Value
  type: integer
- container: ''
  name: Timestamp
  type: dateTime
- container: ''
  name: ValueInIA
  type: integer
- container: ''
  name: ValueInStandard
  type: integer
- container: ''
  name: PerformanceMode
  type: string
- container: ''
  name: Encrypted
  type: boolean
- container: ''
  name: KmsKeyId
  type: string
- container: ''
  name: ThroughputMode
  type: string
- container: ''
  name: ProvisionedThroughputInMibps
  type: decimal
- container: set
  name: Tags
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: AvailabilityZoneId
  type: string
- container: ''
  name: AvailabilityZoneName
  type: string
- container: ''
  name: MountTargetId
  type: string
- container: ''
  name: SubnetId
  type: string
- container: ''
  name: IpAddress
  type: string
- container: ''
  name: NetworkInterfaceId
  type: string
- container: ''
  name: VpcId
  type: string
property_count: 30
provider_name: Amazon EFS
provider_slug: amazon-efs
slug: amazon-efs-context
tags:
- Amazon Web Services
- AWS
- EFS
- Elastic File System
- File Storage
- NFS
- Serverless
- Storage
- JSON-LD
- Linked Data
- Semantic Web
---
