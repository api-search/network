---
class_count: 14
classes:
- CreateDBClusterRequest
- CreateDBInstanceRequest
- DBCluster
- DBClusterMember
- DBClusterRole
- DBClusterSnapshot
- DBInstance
- DescribeDBClusterSnapshotsResponse
- DescribeDBClustersResponse
- DescribeDBInstancesResponse
- DescribeDBSubnetGroupsResponse
- ModifyDBClusterRequest
- ModifyDBInstanceRequest
- RestoreDBClusterFromSnapshotRequest
context_file: json-ld/amazon-neptune-management-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/json-ld/amazon-neptune-management-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Neptune Management from Amazon Neptune.
layout: jsonld
name: Amazon Neptune Management Context
namespaces:
- prefix: neptune
  uri: https://neptune.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: DBSubnetGroup
  type: string
- container: ''
  name: Address
  type: string
- container: ''
  name: AllocatedStorage
  type: integer
- container: ''
  name: ApplyImmediately
  type: boolean
- container: set
  name: AssociatedRoles
  type: string
- container: ''
  name: AutoMinorVersionUpgrade
  type: boolean
- container: ''
  name: AvailabilityZone
  type: string
- container: ''
  name: BackupRetentionPeriod
  type: integer
- container: ''
  name: ClusterCreateTime
  type: dateTime
- container: ''
  name: DBClusterArn
  type: string
- container: ''
  name: DBClusterIdentifier
  type: string
- container: set
  name: DBClusterMembers
  type: string
- container: ''
  name: DBClusterParameterGroup
  type: string
- container: ''
  name: DBClusterParameterGroupName
  type: string
- container: ''
  name: DBClusterParameterGroupStatus
  type: string
- container: ''
  name: DBClusterSnapshotArn
  type: string
- container: ''
  name: DBClusterSnapshotIdentifier
  type: string
- container: set
  name: DBClusterSnapshots
  type: string
- container: set
  name: DBClusters
  type: string
- container: ''
  name: DBInstanceArn
  type: string
- container: ''
  name: DBInstanceClass
  type: string
- container: ''
  name: DBInstanceIdentifier
  type: string
- container: ''
  name: DBInstanceStatus
  type: string
- container: set
  name: DBInstances
  type: string
- container: ''
  name: DBSubnetGroupArn
  type: string
- container: ''
  name: DBSubnetGroupDescription
  type: string
- container: ''
  name: DBSubnetGroupName
  type: string
- container: set
  name: DBSubnetGroups
  type: string
- container: ''
  name: DeletionProtection
  type: boolean
- container: ''
  name: Endpoint
  type: reference
- container: ''
  name: Engine
  type: string
- container: ''
  name: EngineVersion
  type: string
- container: ''
  name: IAMDatabaseAuthenticationEnabled
  type: boolean
- container: ''
  name: IsClusterWriter
  type: boolean
- container: ''
  name: KmsKeyId
  type: string
- container: ''
  name: Marker
  type: string
- container: ''
  name: MasterUsername
  type: string
- container: ''
  name: MultiAZ
  type: boolean
- container: ''
  name: NewDBClusterIdentifier
  type: string
- container: ''
  name: NewDBInstanceIdentifier
  type: string
- container: ''
  name: Port
  type: integer
- container: ''
  name: PreferredBackupWindow
  type: string
- container: ''
  name: PreferredMaintenanceWindow
  type: string
- container: ''
  name: PromotionTier
  type: integer
- container: ''
  name: PubliclyAccessible
  type: boolean
- container: ''
  name: ReaderEndpoint
  type: string
- container: ''
  name: RoleArn
  type: string
- container: ''
  name: SnapshotCreateTime
  type: dateTime
- container: ''
  name: SnapshotIdentifier
  type: string
- container: ''
  name: SnapshotType
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: StorageEncrypted
  type: boolean
- container: ''
  name: SubnetGroupStatus
  type: string
- container: set
  name: Subnets
  type: reference
- container: ''
  name: VpcId
  type: string
- container: set
  name: VpcSecurityGroupIds
  type: string
property_count: 56
provider_name: Amazon Neptune
provider_slug: amazon-neptune
slug: amazon-neptune-management-context
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
- JSON-LD
- Linked Data
- Semantic Web
---
