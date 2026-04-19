---
class_count: 69
classes:
- CustomerAgentInfo
- DescribeTagsResponse
- DescribeBatchDeleteConfigurationTaskRequest
- DescribeImportTasksRequest
- CreateApplicationResponse
- StartBatchDeleteConfigurationTaskRequest
- DeleteAgent
- AgentNetworkInfo
- GetDiscoverySummaryResponse
- StartExportTaskRequest
- DescribeAgentsRequest
- BatchDeleteImportDataRequest
- DisassociateConfigurationItemsRequest
- BatchDeleteAgentsRequest
- UpdateApplicationRequest
- BatchDeleteAgentsResponse
- ImportTask
- OrderByElement
- StartDataCollectionByAgentIdsResponse
- DescribeExportTasksRequest
- ListConfigurationsResponse
- FailedConfiguration
- AgentConfigurationStatus
- StartImportTaskRequest
- DescribeContinuousExportsRequest
- DeletionWarning
- DescribeAgentsResponse
- Tag
- DescribeBatchDeleteConfigurationTaskResponse
- ExportFilter
- DescribeConfigurationsRequest
- CustomerConnectorInfo
- DescribeConfigurationsResponse
- BatchDeleteImportDataError
- Filter
- DescribeImportTasksResponse
- DeleteApplicationsRequest
- ConfigurationTag
- BatchDeleteImportDataResponse
- TagFilter
- StartExportTaskResponse
- StartDataCollectionByAgentIdsRequest
- CreateTagsRequest
- DescribeTagsRequest
- DescribeExportTasksResponse
- AssociateConfigurationItemsRequest
- NeighborConnectionDetail
- DeleteTagsRequest
- ImportTaskFilter
- DescribeContinuousExportsResponse
- StopDataCollectionByAgentIdsResponse
- ListConfigurationsRequest
- ExportInfo
- BatchDeleteConfigurationTask
- StartBatchDeleteConfigurationTaskResponse
- StopContinuousExportResponse
- StartImportTaskResponse
- ContinuousExportDescription
- CreateApplicationRequest
- ListServerNeighborsResponse
- StopDataCollectionByAgentIdsRequest
- StopContinuousExportRequest
- BatchDeleteAgentError
- ListServerNeighborsRequest
- StartContinuousExportResponse
- AgentInfo
- name
- description
- version
context_file: json-ld/amazon-application-discovery-service-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-application-discovery-service/refs/heads/main/json-ld/amazon-application-discovery-service-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Application Discovery Service from Amazon Application Discovery Service.
layout: jsonld
name: Amazon Application Discovery Service Context
namespaces:
- prefix: amzn
  uri: https://amazonaws.com/schema/application-discovery/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: activeAgents
  type: integer
- container: ''
  name: healthyAgents
  type: integer
- container: ''
  name: blackListedAgents
  type: integer
- container: ''
  name: shutdownAgents
  type: integer
- container: ''
  name: unhealthyAgents
  type: integer
- container: ''
  name: totalAgents
  type: integer
- container: ''
  name: unknownAgents
  type: integer
- container: set
  name: tags
  type: reference
- container: ''
  name: nextToken
  type: string
- container: ''
  name: taskId
  type: string
- container: set
  name: filters
  type: reference
- container: ''
  name: maxResults
  type: integer
- container: ''
  name: configurationId
  type: string
- container: ''
  name: configurationType
  type: string
- container: set
  name: configurationIds
  type: string
- container: ''
  name: agentId
  type: string
- container: ''
  name: force
  type: boolean
- container: ''
  name: ipAddress
  type: string
- container: ''
  name: macAddress
  type: string
- container: ''
  name: servers
  type: integer
- container: ''
  name: applications
  type: integer
- container: ''
  name: serversMappedToApplications
  type: integer
- container: ''
  name: serversMappedtoTags
  type: integer
- container: ''
  name: mappedServerCount
  type: integer
- container: ''
  name: unmappedServerCount
  type: integer
- container: ''
  name: agentSummary
  type: reference
- container: ''
  name: connectorSummary
  type: reference
- container: ''
  name: activeConnectors
  type: integer
- container: ''
  name: healthyConnectors
  type: integer
- container: ''
  name: blackListedConnectors
  type: integer
- container: ''
  name: shutdownConnectors
  type: integer
- container: ''
  name: unhealthyConnectors
  type: integer
- container: ''
  name: totalConnectors
  type: integer
- container: ''
  name: unknownConnectors
  type: integer
- container: set
  name: exportDataFormat
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: preferences
  type: reference
- container: set
  name: agentIds
  type: string
- container: set
  name: importTaskIds
  type: string
- container: ''
  name: deleteHistory
  type: boolean
- container: ''
  name: applicationConfigurationId
  type: string
- container: set
  name: deleteAgents
  type: reference
- container: set
  name: errors
  type: reference
- container: ''
  name: importTaskId
  type: string
- container: ''
  name: clientRequestToken
  type: string
- container: ''
  name: importUrl
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: importRequestTime
  type: string
- container: ''
  name: importCompletionTime
  type: string
- container: ''
  name: importDeletedTime
  type: string
- container: ''
  name: serverImportSuccess
  type: integer
- container: ''
  name: serverImportFailure
  type: integer
- container: ''
  name: applicationImportSuccess
  type: integer
- container: ''
  name: applicationImportFailure
  type: integer
- container: ''
  name: errorsAndFailedEntriesZip
  type: string
- container: ''
  name: fieldName
  type: string
- container: ''
  name: sortOrder
  type: string
- container: set
  name: agentsConfigurationStatus
  type: reference
- container: set
  name: exportIds
  type: string
- container: set
  name: configurations
  type: reference
- container: ''
  name: errorStatusCode
  type: integer
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: operationSucceeded
  type: boolean
- container: ''
  name: warningCode
  type: integer
- container: ''
  name: warningText
  type: string
- container: set
  name: agentsInfo
  type: reference
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: task
  type: reference
- container: set
  name: requestedConfigurations
  type: string
- container: set
  name: deletedConfigurations
  type: string
- container: set
  name: failedConfigurations
  type: reference
- container: set
  name: deletionWarnings
  type: reference
- container: set
  name: values
  type: string
- container: ''
  name: condition
  type: string
- container: ''
  name: errorCode
  type: string
- container: ''
  name: errorDescription
  type: string
- container: set
  name: tasks
  type: reference
- container: ''
  name: timeOfCreation
  type: string
- container: ''
  name: exportId
  type: string
- container: set
  name: exportsInfo
  type: reference
- container: ''
  name: sourceServerId
  type: string
- container: ''
  name: destinationServerId
  type: string
- container: ''
  name: destinationPort
  type: integer
- container: ''
  name: transportProtocol
  type: string
- container: ''
  name: connectionsCount
  type: integer
- container: set
  name: descriptions
  type: reference
- container: set
  name: orderBy
  type: reference
- container: ''
  name: exportStatus
  type: string
- container: ''
  name: statusMessage
  type: string
- container: ''
  name: configurationsDownloadUrl
  type: string
- container: ''
  name: exportRequestTime
  type: string
- container: ''
  name: isTruncated
  type: boolean
- container: ''
  name: requestedStartTime
  type: string
- container: ''
  name: requestedEndTime
  type: string
- container: ''
  name: stopTime
  type: string
- container: ''
  name: statusDetail
  type: string
- container: ''
  name: s3Bucket
  type: string
- container: ''
  name: dataSource
  type: string
- container: ''
  name: schemaStorageConfig
  type: reference
- container: set
  name: neighbors
  type: reference
- container: ''
  name: knownDependencyCount
  type: integer
- container: ''
  name: portInformationNeeded
  type: boolean
- container: set
  name: neighborConfigurationIds
  type: string
- container: ''
  name: hostName
  type: string
- container: set
  name: agentNetworkInfoList
  type: reference
- container: ''
  name: connectorId
  type: string
- container: ''
  name: health
  type: string
- container: ''
  name: lastHealthPingTime
  type: string
- container: ''
  name: collectionStatus
  type: string
- container: ''
  name: agentType
  type: string
- container: ''
  name: registeredTime
  type: string
property_count: 113
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
slug: amazon-application-discovery-service-context
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
- JSON-LD
- Linked Data
- Semantic Web
---
