---
class_count: 139
classes:
- StorageInfo
- ListClustersRequest
- NodeInfo
- ClusterOperationStep
- UpdateBrokerCountResponse
- UpdateConfigurationRequest
- EncryptionAtRest
- ListClustersResponse
- Scram
- ConfigurationInfo
- DeleteClusterRequest
- DescribeClusterResponse
- RebootBrokerRequest
- KafkaVersionStatus
- UpdateBrokerStorageResponse
- BatchAssociateScramSecretRequest
- BrokerLogs
- UpdateClusterKafkaVersionRequest
- UpdateMonitoringResponse
- BrokerAZDistribution
- KafkaVersion
- ServerlessSasl
- Tls
- DescribeConfigurationRevisionRequest
- ConnectivityInfo
- GetCompatibleKafkaVersionsResponse
- StorageMode
- CreateClusterV2Request
- CompatibleKafkaVersion
- ClusterInfo
- ClientBroker
- Iam
- Unauthenticated
- ClusterState
- DescribeConfigurationRequest
- BatchDisassociateScramSecretRequest
- ListNodesRequest
- TagResourceRequest
- UpdateClusterConfigurationRequest
- LoggingInfo
- PublicAccess
- CloudWatchLogs
- Firehose
- NodeExporter
- CreateClusterResponse
- VpcConfig
- ServerlessRequest
- ListScramSecretsRequest
- UnauthorizedException
- BrokerNodeGroupInfo
- BrokerEBSVolumeInfo
- StateInfo
- ListScramSecretsResponse
- ListConfigurationRevisionsResponse
- ZookeeperNodeInfo
- DeleteConfigurationResponse
- ListConfigurationsRequest
- EBSStorageInfo
- BatchDisassociateScramSecretResponse
- UpdateStorageResponse
- ListClusterOperationsRequest
- MaxResults
- UpdateBrokerTypeRequest
- ServerlessClientAuthentication
- BatchAssociateScramSecretResponse
- PrometheusInfo
- ClusterOperationStepInfo
- UpdateClusterConfigurationResponse
- UpdateBrokerTypeResponse
- UpdateSecurityResponse
- ConfigurationState
- ListConfigurationRevisionsRequest
- UntagResourceRequest
- CreateConfigurationResponse
- DescribeClusterOperationRequest
- OpenMonitoringInfo
- CreateClusterRequest
- OpenMonitoring
- UpdateBrokerCountRequest
- ProvisionedThroughput
- Sasl
- Serverless
- UpdateMonitoringRequest
- DeleteClusterResponse
- ErrorInfo
- BrokerNodeInfo
- UpdateSecurityRequest
- UpdateConnectivityRequest
- GetCompatibleKafkaVersionsRequest
- JmxExporter
- DescribeClusterV2Response
- ListKafkaVersionsRequest
- ListClusterOperationsResponse
- DescribeConfigurationResponse
- ClusterOperationInfo
- UpdateClusterKafkaVersionResponse
- EncryptionInfo
- ListTagsForResourceRequest
- DescribeConfigurationRevisionResponse
- ListKafkaVersionsResponse
- UnprocessedScramSecret
- CreateClusterV2Response
- Cluster
- NodeExporterInfo
- GetBootstrapBrokersResponse
- EnhancedMonitoring
- ConfigurationRevision
- DescribeClusterOperationResponse
- S3
- JmxExporterInfo
- GetBootstrapBrokersRequest
- RebootBrokerResponse
- ClientAuthentication
- MutableClusterInfo
- ListConfigurationsResponse
- NodeType
- UpdateConnectivityResponse
- CreateConfigurationRequest
- UpdateBrokerStorageRequest
- DeleteConfigurationRequest
- ProvisionedRequest
- UpdateStorageRequest
- Configuration
- DescribeClusterRequest
- ListClustersV2Response
- Provisioned
- ListClustersV2Request
- ListNodesResponse
- UpdateConfigurationResponse
- Prometheus
- ClusterType
- DescribeClusterV2Request
- EncryptionInTransit
- ListTagsForResourceResponse
- BrokerSoftwareInfo
- description
- version
- creationTime
- name
context_file: json-ld/amazon-msk-msk-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-msk/refs/heads/main/json-ld/amazon-msk-msk-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Msk Msk Api from Amazon MSK.
layout: jsonld
name: Amazon Msk Msk Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: ebsStorageInfo
  type: string
- container: ''
  name: addedToClusterTime
  type: string
- container: ''
  name: brokerNodeInfo
  type: string
- container: ''
  name: instanceType
  type: string
- container: ''
  name: nodeArn
  type: string
- container: ''
  name: nodeType
  type: string
- container: ''
  name: zookeeperNodeInfo
  type: string
- container: ''
  name: stepInfo
  type: string
- container: ''
  name: stepName
  type: string
- container: ''
  name: clusterArn
  type: string
- container: ''
  name: clusterOperationArn
  type: string
- container: ''
  name: serverProperties
  type: string
- container: ''
  name: dataVolumeKmsKeyId
  type: string
- container: ''
  name: clusterInfoList
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: enabled
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: revision
  type: string
- container: ''
  name: clusterInfo
  type: string
- container: ''
  name: brokerIds
  type: string
- container: ''
  name: secretArnList
  type: string
- container: ''
  name: cloudWatchLogs
  type: string
- container: ''
  name: firehose
  type: string
- container: ''
  name: s3
  type: string
- container: ''
  name: configurationInfo
  type: string
- container: ''
  name: currentVersion
  type: string
- container: ''
  name: targetKafkaVersion
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: iam
  type: string
- container: ''
  name: certificateAuthorityArnList
  type: string
- container: ''
  name: publicAccess
  type: string
- container: ''
  name: compatibleKafkaVersions
  type: string
- container: ''
  name: clusterName
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: provisioned
  type: string
- container: ''
  name: serverless
  type: string
- container: ''
  name: sourceVersion
  type: string
- container: ''
  name: targetVersions
  type: string
- container: ''
  name: activeOperationArn
  type: string
- container: ''
  name: brokerNodeGroupInfo
  type: string
- container: ''
  name: clientAuthentication
  type: string
- container: ''
  name: currentBrokerSoftwareInfo
  type: string
- container: ''
  name: encryptionInfo
  type: string
- container: ''
  name: enhancedMonitoring
  type: string
- container: ''
  name: openMonitoring
  type: string
- container: ''
  name: loggingInfo
  type: string
- container: ''
  name: numberOfBrokerNodes
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: stateInfo
  type: string
- container: ''
  name: zookeeperConnectString
  type: string
- container: ''
  name: zookeeperConnectStringTls
  type: string
- container: ''
  name: storageMode
  type: string
- container: ''
  name: brokerLogs
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: logGroup
  type: string
- container: ''
  name: deliveryStream
  type: string
- container: ''
  name: enabledInBroker
  type: string
- container: ''
  name: subnetIds
  type: string
- container: ''
  name: securityGroupIds
  type: string
- container: ''
  name: vpcConfigs
  type: string
- container: ''
  name: brokerAzDistribution
  type: string
- container: ''
  name: clientSubnets
  type: string
- container: ''
  name: securityGroups
  type: string
- container: ''
  name: storageInfo
  type: string
- container: ''
  name: connectivityInfo
  type: string
- container: ''
  name: kafkaBrokerNodeId
  type: string
- container: ''
  name: provisionedThroughput
  type: string
- container: ''
  name: volumeSizeGb
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: revisions
  type: string
- container: ''
  name: attachedEniId
  type: string
- container: ''
  name: clientVpcIpAddress
  type: string
- container: ''
  name: endpoints
  type: string
- container: ''
  name: zookeeperId
  type: string
- container: ''
  name: zookeeperVersion
  type: string
- container: ''
  name: volumeSize
  type: string
- container: ''
  name: unprocessedScramSecrets
  type: string
- container: ''
  name: targetInstanceType
  type: string
- container: ''
  name: sasl
  type: string
- container: ''
  name: jmxExporter
  type: string
- container: ''
  name: nodeExporter
  type: string
- container: ''
  name: stepStatus
  type: string
- container: ''
  name: latestRevision
  type: string
- container: ''
  name: prometheus
  type: string
- container: ''
  name: kafkaVersion
  type: string
- container: ''
  name: targetNumberOfBrokerNodes
  type: string
- container: ''
  name: volumeThroughput
  type: string
- container: ''
  name: scram
  type: string
- container: ''
  name: errorCode
  type: string
- container: ''
  name: errorString
  type: string
- container: ''
  name: brokerId
  type: string
- container: ''
  name: clientSubnet
  type: string
- container: ''
  name: clusterOperationInfoList
  type: string
- container: ''
  name: kafkaVersions
  type: string
- container: ''
  name: clientRequestId
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: errorInfo
  type: string
- container: ''
  name: operationArn
  type: string
- container: ''
  name: operationState
  type: string
- container: ''
  name: operationSteps
  type: string
- container: ''
  name: operationType
  type: string
- container: ''
  name: sourceClusterInfo
  type: string
- container: ''
  name: targetClusterInfo
  type: string
- container: ''
  name: encryptionAtRest
  type: string
- container: ''
  name: encryptionInTransit
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: secretArn
  type: string
- container: ''
  name: clusterType
  type: string
- container: ''
  name: bootstrapBrokerString
  type: string
- container: ''
  name: bootstrapBrokerStringTls
  type: string
- container: ''
  name: bootstrapBrokerStringSaslScram
  type: string
- container: ''
  name: bootstrapBrokerStringSaslIam
  type: string
- container: ''
  name: bootstrapBrokerStringPublicTls
  type: string
- container: ''
  name: bootstrapBrokerStringPublicSaslScram
  type: string
- container: ''
  name: bootstrapBrokerStringPublicSaslIam
  type: string
- container: ''
  name: clusterOperationInfo
  type: string
- container: ''
  name: bucket
  type: string
- container: ''
  name: prefix
  type: string
- container: ''
  name: tls
  type: string
- container: ''
  name: unauthenticated
  type: string
- container: ''
  name: brokerEbsVolumeInfo
  type: string
- container: ''
  name: configurations
  type: string
- container: ''
  name: targetBrokerEbsVolumeInfo
  type: string
- container: ''
  name: nodeInfoList
  type: string
- container: ''
  name: clientBroker
  type: string
- container: ''
  name: inCluster
  type: string
- container: ''
  name: configurationArn
  type: string
- container: ''
  name: configurationRevision
  type: string
property_count: 129
provider_name: Amazon MSK
provider_slug: amazon-msk
slug: amazon-msk-msk-api-context
tags:
- AWS
- Broadcasting
- Media Processing
- Media
- JSON-LD
- Linked Data
- Semantic Web
---
