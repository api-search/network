---
class_count: 3
classes:
- Amazon DocumentDB DBCluster
- CreateDBClusterResult
- DescribeDBClustersResult
context_file: json-ld/amazon-documentdb-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-documentdb/refs/heads/main/json-ld/amazon-documentdb-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Documentdb from Amazon DocumentDB.
layout: jsonld
name: Amazon Documentdb Context
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
  name: DBCluster
  type: string
- container: ''
  name: DBClusterIdentifier
  type: string
- container: ''
  name: DBClusterArn
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: Engine
  type: string
- container: ''
  name: EngineVersion
  type: string
- container: ''
  name: Endpoint
  type: string
- container: ''
  name: ReaderEndpoint
  type: string
- container: ''
  name: Port
  type: integer
- container: ''
  name: MasterUsername
  type: string
- container: ''
  name: DBSubnetGroup
  type: string
- container: ''
  name: StorageEncrypted
  type: boolean
- container: ''
  name: KmsKeyId
  type: string
- container: ''
  name: BackupRetentionPeriod
  type: integer
- container: ''
  name: PreferredBackupWindow
  type: string
- container: ''
  name: PreferredMaintenanceWindow
  type: string
- container: ''
  name: ClusterCreateTime
  type: dateTime
- container: set
  name: DBClusterMembers
  type: string
- container: set
  name: VpcSecurityGroups
  type: string
- container: ''
  name: DeletionProtection
  type: boolean
- container: set
  name: EnabledCloudwatchLogsExports
  type: string
- container: ''
  name: DBInstanceIdentifier
  type: string
- container: ''
  name: IsClusterWriter
  type: boolean
- container: ''
  name: DBClusterParameterGroupStatus
  type: string
- container: ''
  name: PromotionTier
  type: integer
- container: ''
  name: VpcSecurityGroupId
  type: string
- container: set
  name: DBClusters
  type: string
- container: ''
  name: Marker
  type: string
property_count: 28
provider_name: Amazon DocumentDB
provider_slug: amazon-documentdb
slug: amazon-documentdb-context
tags:
- Amazon Web Services
- AWS
- Database
- Document Database
- DocumentDB
- Managed Database
- MongoDB
- NoSQL
- JSON-LD
- Linked Data
- Semantic Web
---
