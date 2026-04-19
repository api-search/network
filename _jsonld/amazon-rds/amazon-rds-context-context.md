---
class_count: 12
classes:
- Amazon RDS DB Instance
- CreateDBClusterResponse
- CreateDBInstanceResponse
- CreateDBSnapshotResponse
- DBCluster
- DBInstance
- DBSnapshot
- DescribeDBClustersResponse
- DescribeDBInstancesResponse
- DescribeDBSnapshotsResponse
- ModifyDBInstanceResponse
- Tag
context_file: json-ld/amazon-rds-context-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-rds/refs/heads/main/json-ld/amazon-rds-context-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Rds from Amazon RDS.
layout: jsonld
name: Amazon Rds Context
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
  name: dBInstanceIdentifier
  type: string
- container: ''
  name: dBInstanceClass
  type: string
- container: ''
  name: engine
  type: string
- container: ''
  name: engineVersion
  type: string
- container: ''
  name: dBInstanceStatus
  type: string
- container: ''
  name: masterUsername
  type: string
- container: ''
  name: dBName
  type: string
- container: ''
  name: endpoint
  type: string
- container: ''
  name: allocatedStorage
  type: integer
- container: ''
  name: instanceCreateTime
  type: dateTime
- container: ''
  name: preferredBackupWindow
  type: string
- container: ''
  name: backupRetentionPeriod
  type: integer
- container: set
  name: vpcSecurityGroups
  type: string
- container: ''
  name: availabilityZone
  type: string
- container: ''
  name: dBSubnetGroup
  type: string
- container: ''
  name: multiAZ
  type: boolean
- container: ''
  name: autoMinorVersionUpgrade
  type: boolean
- container: ''
  name: storageType
  type: string
- container: ''
  name: storageEncrypted
  type: boolean
- container: ''
  name: publiclyAccessible
  type: boolean
- container: ''
  name: cACertificateIdentifier
  type: string
- container: ''
  name: dBInstanceArn
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: port
  type: integer
- container: ''
  name: dBClusterIdentifier
  type: string
- container: ''
  name: licenseModel
  type: string
- container: ''
  name: dBCluster
  type: string
- container: ''
  name: dBInstance
  type: string
- container: ''
  name: dBSnapshot
  type: string
- container: ''
  name: dBClusterArn
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: databaseName
  type: string
- container: ''
  name: readerEndpoint
  type: string
- container: set
  name: dBClusterMembers
  type: string
- container: set
  name: availabilityZones
  type: string
- container: ''
  name: clusterCreateTime
  type: dateTime
- container: ''
  name: dBSnapshotIdentifier
  type: string
- container: ''
  name: snapshotCreateTime
  type: dateTime
- container: ''
  name: vpcId
  type: string
- container: ''
  name: snapshotType
  type: string
- container: ''
  name: encrypted
  type: boolean
- container: ''
  name: dBSnapshotArn
  type: string
- container: set
  name: dBClusters
  type: string
- container: ''
  name: marker
  type: string
- container: set
  name: dBInstances
  type: string
- container: set
  name: dBSnapshots
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
property_count: 48
provider_name: Amazon RDS
provider_slug: amazon-rds
slug: amazon-rds-context-context
tags:
- AWS
- Cloud Databases
- Database Service
- DBaaS
- Managed Databases
- Relational Databases
- JSON-LD
- Linked Data
- Semantic Web
---
