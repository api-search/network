---
class_count: 61
classes:
- DeleteFlowRequest
- ListConnectorsResponse
- DescribeFlowExecutionRecordsResponse
- UnregisterConnectorRequest
- RegisterConnectorResponse
- ConnectorProfile
- UpdateFlowRequest
- ExecutionDetails
- DeleteConnectorProfileRequest
- DescribeConnectorProfilesResponse
- DescribeConnectorRequest
- CreateFlowRequest
- DescribeFlowRequest
- TagResourceRequest
- ScheduledTriggerProperties
- ResetConnectorMetadataCacheRequest
- ListFlowsRequest
- FlowExecution
- CreateConnectorProfileResponse
- DescribeFlowResponse
- ListFlowsResponse
- ConnectorDetail
- RegisterConnectorRequest
- TriggerConfig
- UpdateConnectorRegistrationResponse
- Task
- StopFlowRequest
- Amazon AppFlow Flow Definition
- ListConnectorEntitiesRequest
- UpdateConnectorRegistrationRequest
- ConnectorEntityField
- DescribeConnectorsRequest
- CreateConnectorProfileRequest
- SourceFlowConfig
- ConnectorEntity
- ListConnectorsRequest
- StartFlowResponse
- ListTagsForResourceResponse
- StartFlowRequest
- UpdateFlowResponse
- CancelFlowExecutionsResponse
- FlowDefinition
- StopFlowResponse
- CancelFlowExecutionsRequest
- DescribeConnectorEntityRequest
- DestinationFlowConfig
- DescribeConnectorResponse
- ListConnectorEntitiesResponse
- UpdateConnectorProfileResponse
- DescribeConnectorEntityResponse
- MetadataCatalogConfig
- UpdateConnectorProfileRequest
- DescribeConnectorsResponse
- ExecutionResult
- DescribeFlowExecutionRecordsRequest
- CreateFlowResponse
- DescribeConnectorProfilesRequest
- createdAt
- lastUpdatedAt
- description
- name
context_file: json-ld/amazon-appflow-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-appflow/refs/heads/main/json-ld/amazon-appflow-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Appflow from Amazon AppFlow.
layout: jsonld
name: Amazon Appflow Context
namespaces:
- prefix: amzn
  uri: https://amazonaws.com/schema/appflow/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: flowName
  type: string
- container: ''
  name: forceDelete
  type: boolean
- container: set
  name: connectors
  type: string
- container: ''
  name: nextToken
  type: string
- container: set
  name: flowExecutions
  type: string
- container: ''
  name: connectorLabel
  type: string
- container: ''
  name: connectorArn
  type: string
- container: ''
  name: connectorProfileArn
  type: string
- container: ''
  name: connectorProfileName
  type: string
- container: ''
  name: connectorType
  type: string
- container: ''
  name: connectionMode
  type: string
- container: ''
  name: credentialsArn
  type: string
- container: ''
  name: connectorProfileProperties
  type: reference
- container: ''
  name: privateConnectionProvisioningState
  type: reference
- container: ''
  name: clientToken
  type: string
- container: ''
  name: triggerConfig
  type: reference
- container: ''
  name: triggerType
  type: string
- container: ''
  name: triggerProperties
  type: reference
- container: ''
  name: Scheduled
  type: string
- container: ''
  name: sourceFlowConfig
  type: reference
- container: ''
  name: apiVersion
  type: string
- container: ''
  name: sourceConnectorProperties
  type: reference
- container: ''
  name: incrementalPullConfig
  type: reference
- container: ''
  name: datetimeTypeFieldName
  type: string
- container: set
  name: destinationFlowConfigList
  type: string
- container: set
  name: tasks
  type: string
- container: ''
  name: metadataCatalogConfig
  type: reference
- container: ''
  name: glueDataCatalog
  type: reference
- container: ''
  name: roleArn
  type: string
- container: ''
  name: databaseName
  type: string
- container: ''
  name: tablePrefix
  type: string
- container: ''
  name: mostRecentExecutionMessage
  type: string
- container: ''
  name: mostRecentExecutionTime
  type: integer
- container: ''
  name: mostRecentExecutionStatus
  type: string
- container: set
  name: connectorProfileDetails
  type: string
- container: ''
  name: kmsArn
  type: string
- container: ''
  name: tags
  type: reference
- container: ''
  name: scheduleExpression
  type: string
- container: ''
  name: dataPullMode
  type: string
- container: ''
  name: scheduleStartTime
  type: integer
- container: ''
  name: scheduleEndTime
  type: integer
- container: ''
  name: timezone
  type: string
- container: ''
  name: scheduleOffset
  type: integer
- container: ''
  name: firstExecutionFrom
  type: integer
- container: ''
  name: flowErrorDeactivationThreshold
  type: integer
- container: ''
  name: connectorEntityName
  type: string
- container: ''
  name: entitiesPath
  type: string
- container: ''
  name: maxResults
  type: integer
- container: ''
  name: executionId
  type: string
- container: ''
  name: executionStatus
  type: string
- container: ''
  name: executionResult
  type: reference
- container: ''
  name: errorInfo
  type: reference
- container: ''
  name: bytesProcessed
  type: integer
- container: ''
  name: bytesWritten
  type: integer
- container: ''
  name: recordsProcessed
  type: integer
- container: ''
  name: numParallelProcesses
  type: integer
- container: ''
  name: startedAt
  type: integer
- container: ''
  name: dataPullStartTime
  type: integer
- container: ''
  name: dataPullEndTime
  type: integer
- container: ''
  name: flowArn
  type: string
- container: ''
  name: flowStatus
  type: string
- container: ''
  name: flowStatusMessage
  type: string
- container: ''
  name: lastRunExecutionDetails
  type: reference
- container: ''
  name: createdBy
  type: string
- container: ''
  name: lastUpdatedBy
  type: string
- container: set
  name: lastRunMetadataCatalogDetails
  type: reference
- container: set
  name: flows
  type: string
- container: ''
  name: connectorDescription
  type: string
- container: ''
  name: connectorName
  type: string
- container: ''
  name: connectorOwner
  type: string
- container: ''
  name: connectorVersion
  type: string
- container: ''
  name: applicationType
  type: string
- container: ''
  name: registeredAt
  type: integer
- container: ''
  name: registeredBy
  type: string
- container: ''
  name: connectorProvisioningType
  type: string
- container: set
  name: connectorModes
  type: string
- container: set
  name: supportedDataTransferTypes
  type: string
- container: ''
  name: connectorProvisioningConfig
  type: reference
- container: ''
  name: lambda
  type: reference
- container: ''
  name: lambdaArn
  type: string
- container: set
  name: sourceFields
  type: string
- container: ''
  name: connectorOperator
  type: reference
- container: ''
  name: destinationField
  type: string
- container: ''
  name: taskType
  type: string
- container: ''
  name: taskProperties
  type: reference
- container: ''
  name: identifier
  type: string
- container: ''
  name: parentIdentifier
  type: string
- container: ''
  name: label
  type: string
- container: ''
  name: isPrimaryKey
  type: boolean
- container: ''
  name: defaultValue
  type: string
- container: ''
  name: isDeprecated
  type: boolean
- container: ''
  name: supportedFieldTypeDetails
  type: reference
- container: ''
  name: sourceProperties
  type: reference
- container: ''
  name: isQueryable
  type: boolean
- container: ''
  name: isRetrievable
  type: boolean
- container: ''
  name: isPartitioningSupported
  type: boolean
- container: ''
  name: destinationProperties
  type: reference
- container: ''
  name: isCreatable
  type: boolean
- container: ''
  name: isNullable
  type: boolean
- container: ''
  name: isUpsertable
  type: boolean
- container: ''
  name: isUpdatable
  type: boolean
- container: ''
  name: isDefaultedOnCreate
  type: boolean
- container: set
  name: supportedWriteOperations
  type: string
- container: set
  name: connectorTypes
  type: string
- container: ''
  name: connectorProfileConfig
  type: reference
- container: ''
  name: hasNestedEntities
  type: boolean
- container: set
  name: invalidExecutions
  type: string
- container: ''
  name: sourceConnectorType
  type: string
- container: ''
  name: sourceConnectorLabel
  type: string
- container: ''
  name: destinationConnectorType
  type: string
- container: ''
  name: destinationConnectorLabel
  type: string
- container: set
  name: executionIds
  type: string
- container: ''
  name: destinationConnectorProperties
  type: reference
- container: ''
  name: connectorConfiguration
  type: reference
- container: ''
  name: canUseAsSource
  type: boolean
- container: ''
  name: canUseAsDestination
  type: boolean
- container: ''
  name: connectorEntityMap
  type: reference
- container: set
  name: connectorEntityFields
  type: string
- container: ''
  name: connectorConfigurations
  type: reference
- container: set
  name: connectorProfileNames
  type: string
property_count: 120
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
slug: amazon-appflow-context
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
- JSON-LD
- Linked Data
- Semantic Web
---
