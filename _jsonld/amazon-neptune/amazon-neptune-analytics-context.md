---
class_count: 13
classes:
- CreateGraphInput
- CreateGraphSnapshotInput
- CreateGraphUsingImportTaskInput
- CreatePrivateGraphEndpointInput
- GraphOutput
- GraphSnapshotOutput
- ImportTaskOutput
- ListGraphSnapshotsOutput
- ListGraphsOutput
- ListImportTasksOutput
- PrivateGraphEndpointOutput
- RestoreGraphFromSnapshotInput
- UpdateGraphInput
context_file: json-ld/amazon-neptune-analytics-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/json-ld/amazon-neptune-analytics-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Neptune Analytics from Amazon Neptune.
layout: jsonld
name: Amazon Neptune Analytics Context
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
  name: arn
  type: string
- container: ''
  name: buildNumber
  type: string
- container: ''
  name: createTime
  type: dateTime
- container: ''
  name: deletionProtection
  type: boolean
- container: ''
  name: dictionaryEntryCount
  type: integer
- container: ''
  name: dimension
  type: integer
- container: ''
  name: endpoint
  type: string
- container: ''
  name: errorCount
  type: integer
- container: ''
  name: errorDetails
  type: string
- container: ''
  name: format
  type: string
- container: ''
  name: graphId
  type: string
- container: ''
  name: graphIdentifier
  type: string
- container: ''
  name: graphName
  type: string
- container: set
  name: graphSnapshots
  type: reference
- container: set
  name: graphs
  type: reference
- container: ''
  name: id
  type: string
- container: ''
  name: importOptions
  type: reference
- container: ''
  name: importTaskDetails
  type: reference
- container: ''
  name: kmsKeyIdentifier
  type: string
- container: ''
  name: name
  type: ''
- container: ''
  name: nextToken
  type: string
- container: ''
  name: progressPercentage
  type: integer
- container: ''
  name: provisionedMemory
  type: integer
- container: ''
  name: publicConnectivity
  type: boolean
- container: ''
  name: replicaCount
  type: integer
- container: ''
  name: roleArn
  type: string
- container: ''
  name: snapshotCreateTime
  type: dateTime
- container: ''
  name: snapshotName
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: sourceGraphId
  type: string
- container: ''
  name: sourceSnapshotId
  type: string
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: statementCount
  type: integer
- container: ''
  name: status
  type: string
- container: ''
  name: statusReason
  type: string
- container: set
  name: subnetIds
  type: string
- container: ''
  name: tags
  type: reference
- container: ''
  name: taskId
  type: string
- container: set
  name: tasks
  type: reference
- container: ''
  name: timeElapsedSeconds
  type: integer
- container: ''
  name: vectorSearchConfiguration
  type: reference
- container: ''
  name: vpcEndpointId
  type: string
- container: ''
  name: vpcId
  type: string
- container: set
  name: vpcSecurityGroupIds
  type: string
property_count: 44
provider_name: Amazon Neptune
provider_slug: amazon-neptune
slug: amazon-neptune-analytics-context
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
