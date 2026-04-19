---
class_count: 102
classes:
- AccessPolicySummary
- AggregatedValue
- Aggregates
- Alarms
- AssetCompositeModel
- AssetErrorDetails
- AssetHierarchy
- AssetHierarchyInfo
- AssetModelCompositeModel
- AssetModelCompositeModelDefinition
- AssetModelHierarchy
- AssetModelHierarchyDefinition
- AssetModelProperty
- AssetModelPropertyDefinition
- AssetModelPropertySummary
- AssetModelStatus
- AssetModelSummary
- AssetProperty
- AssetPropertySummary
- AssetPropertyValue
- AssetRelationshipSummary
- AssetStatus
- AssetSummary
- AssociateAssetsRequest
- AssociateTimeSeriesToAssetPropertyRequest
- AssociatedAssetsSummary
- Attribute
- BatchAssociateProjectAssetsRequest
- BatchAssociateProjectAssetsResponse
- BatchDisassociateProjectAssetsRequest
- BatchDisassociateProjectAssetsResponse
- BatchGetAssetPropertyAggregatesEntry
- BatchGetAssetPropertyAggregatesErrorEntry
- BatchGetAssetPropertyAggregatesErrorInfo
- BatchGetAssetPropertyAggregatesRequest
- BatchGetAssetPropertyAggregatesResponse
- BatchGetAssetPropertyAggregatesSkippedEntry
- BatchGetAssetPropertyAggregatesSuccessEntry
- BatchGetAssetPropertyValueEntry
- BatchGetAssetPropertyValueErrorEntry
- BatchGetAssetPropertyValueErrorInfo
- BatchGetAssetPropertyValueHistoryEntry
- BatchGetAssetPropertyValueHistoryErrorEntry
- BatchGetAssetPropertyValueHistoryErrorInfo
- BatchGetAssetPropertyValueHistoryRequest
- BatchGetAssetPropertyValueHistoryResponse
- BatchGetAssetPropertyValueHistorySkippedEntry
- BatchGetAssetPropertyValueHistorySuccessEntry
- BatchGetAssetPropertyValueRequest
- BatchGetAssetPropertyValueResponse
- BatchGetAssetPropertyValueSkippedEntry
- BatchGetAssetPropertyValueSuccessEntry
- BatchPutAssetPropertyError
- BatchPutAssetPropertyErrorEntry
- BatchPutAssetPropertyValueRequest
- BatchPutAssetPropertyValueResponse
- CompositeModelProperty
- CreateAccessPolicyResponse
- CreateAssetModelResponse
- CreateAssetResponse
- CreateBulkImportJobResponse
- CreateDashboardResponse
- CreateGatewayResponse
- CreatePortalResponse
- CreateProjectResponse
- CustomerManagedS3Storage
- DeleteAccessPolicyResponse
- DeleteAssetModelResponse
- DeleteAssetResponse
- DeleteDashboardResponse
- DeletePortalResponse
- DeleteProjectResponse
- DescribeAccessPolicyResponse
- DescribeAssetModelResponse
- DescribeAssetPropertyResponse
- DescribeAssetResponse
- DescribeBulkImportJobResponse
- DescribeDashboardResponse
- DescribeDefaultEncryptionConfigurationResponse
- DescribeGatewayCapabilityConfigurationResponse
- DescribeGatewayResponse
- DescribeLoggingOptionsResponse
- DescribePortalResponse
- DescribeProjectResponse
- DescribeStorageConfigurationResponse
- DescribeTimeSeriesResponse
- ErrorDetails
- File
- FileFormat
- GetAssetPropertyAggregatesResponse
- GetAssetPropertyValueHistoryResponse
- GetAssetPropertyValueResponse
- GetInterpolatedAssetPropertyValuesResponse
- Greengrass
- GreengrassV2
- GroupIdentity
- IAMRoleIdentity
- IAMUserIdentity
- Identity
- ImageFile
- description
- name
context_file: json-ld/amazon-iot-sitewise-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-sitewise/refs/heads/main/json-ld/amazon-iot-sitewise-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Iot Sitewise from Amazon IoT SiteWise.
layout: jsonld
name: Amazon Iot Sitewise Context
namespaces:
- prefix: amzn
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: TimeSeriesSummaries
  type: string
- container: ''
  name: accessPolicyArn
  type: string
- container: ''
  name: accessPolicyCreationDate
  type: string
- container: ''
  name: accessPolicyId
  type: string
- container: ''
  name: accessPolicyIdentity
  type: string
- container: ''
  name: accessPolicyLastUpdateDate
  type: string
- container: ''
  name: accessPolicyPermission
  type: string
- container: ''
  name: accessPolicyResource
  type: string
- container: ''
  name: accessPolicySummaries
  type: string
- container: ''
  name: aggregateTypes
  type: string
- container: ''
  name: aggregatedValues
  type: string
- container: ''
  name: alarmRoleArn
  type: string
- container: ''
  name: alarms
  type: string
- container: ''
  name: alias
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: assetArn
  type: string
- container: ''
  name: assetCompositeModelId
  type: string
- container: ''
  name: assetCompositeModels
  type: string
- container: ''
  name: assetCreationDate
  type: string
- container: ''
  name: assetDescription
  type: string
- container: ''
  name: assetHierarchies
  type: string
- container: ''
  name: assetId
  type: string
- container: ''
  name: assetIds
  type: string
- container: ''
  name: assetLastUpdateDate
  type: string
- container: ''
  name: assetModelArn
  type: string
- container: ''
  name: assetModelCompositeModelId
  type: string
- container: ''
  name: assetModelCompositeModels
  type: string
- container: ''
  name: assetModelCreationDate
  type: string
- container: ''
  name: assetModelDescription
  type: string
- container: ''
  name: assetModelHierarchies
  type: string
- container: ''
  name: assetModelId
  type: string
- container: ''
  name: assetModelLastUpdateDate
  type: string
- container: ''
  name: assetModelName
  type: string
- container: ''
  name: assetModelProperties
  type: string
- container: ''
  name: assetModelPropertySummaries
  type: string
- container: ''
  name: assetModelStatus
  type: string
- container: ''
  name: assetModelSummaries
  type: string
- container: ''
  name: assetName
  type: string
- container: ''
  name: assetProperties
  type: string
- container: ''
  name: assetProperty
  type: string
- container: ''
  name: assetPropertySummaries
  type: string
- container: ''
  name: assetPropertyValue
  type: string
- container: ''
  name: assetPropertyValueHistory
  type: string
- container: ''
  name: assetRelationshipSummaries
  type: string
- container: ''
  name: assetStatus
  type: string
- container: ''
  name: assetSummaries
  type: string
- container: ''
  name: attribute
  type: string
- container: ''
  name: average
  type: string
- container: ''
  name: booleanValue
  type: string
- container: ''
  name: bucket
  type: string
- container: ''
  name: capabilityConfiguration
  type: string
- container: ''
  name: capabilityNamespace
  type: string
- container: ''
  name: capabilitySyncStatus
  type: string
- container: ''
  name: childAssetId
  type: string
- container: ''
  name: childAssetModelId
  type: string
- container: ''
  name: clientToken
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: completionStatus
  type: string
- container: ''
  name: compositeModel
  type: string
- container: ''
  name: configurationStatus
  type: string
- container: ''
  name: coreDeviceThingName
  type: string
- container: ''
  name: count
  type: string
- container: ''
  name: creationDate
  type: string
- container: ''
  name: csv
  type: string
- container: ''
  name: dashboardArn
  type: string
- container: ''
  name: dashboardCreationDate
  type: string
- container: ''
  name: dashboardDefinition
  type: string
- container: ''
  name: dashboardDescription
  type: string
- container: ''
  name: dashboardId
  type: string
- container: ''
  name: dashboardLastUpdateDate
  type: string
- container: ''
  name: dashboardName
  type: string
- container: ''
  name: dashboardSummaries
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: dataType
  type: string
- container: ''
  name: dataTypeSpec
  type: string
- container: ''
  name: defaultValue
  type: string
- container: ''
  name: details
  type: string
- container: ''
  name: disassociatedDataStorage
  type: string
- container: ''
  name: doubleValue
  type: string
- container: ''
  name: encryptionType
  type: string
- container: ''
  name: endDate
  type: string
- container: ''
  name: entries
  type: string
- container: ''
  name: entryId
  type: string
- container: ''
  name: error
  type: string
- container: ''
  name: errorCode
  type: string
- container: ''
  name: errorEntries
  type: string
- container: ''
  name: errorInfo
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: errorReportLocation
  type: string
- container: ''
  name: errorTimestamp
  type: string
- container: ''
  name: errors
  type: string
- container: ''
  name: files
  type: string
- container: ''
  name: gatewayArn
  type: string
- container: ''
  name: gatewayCapabilitySummaries
  type: string
- container: ''
  name: gatewayId
  type: string
- container: ''
  name: gatewayName
  type: string
- container: ''
  name: gatewayPlatform
  type: string
- container: ''
  name: gatewaySummaries
  type: string
- container: ''
  name: group
  type: string
- container: ''
  name: groupArn
  type: string
- container: ''
  name: hierarchies
  type: string
- container: ''
  name: hierarchyId
  type: string
- container: ''
  name: hierarchyInfo
  type: string
- container: ''
  name: iamRole
  type: string
- container: ''
  name: iamUser
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: identity
  type: string
- container: ''
  name: integerValue
  type: string
- container: ''
  name: interpolatedAssetPropertyValues
  type: string
- container: ''
  name: jobConfiguration
  type: string
- container: ''
  name: jobCreationDate
  type: string
- container: ''
  name: jobId
  type: string
- container: ''
  name: jobLastUpdateDate
  type: string
- container: ''
  name: jobName
  type: string
- container: ''
  name: jobRoleArn
  type: string
- container: ''
  name: jobStatus
  type: string
- container: ''
  name: jobSummaries
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: kmsKeyArn
  type: string
- container: ''
  name: lastUpdateDate
  type: string
- container: ''
  name: loggingOptions
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: maximum
  type: string
- container: ''
  name: measurement
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: metric
  type: string
- container: ''
  name: minimum
  type: string
- container: ''
  name: multiLayerStorage
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: notification
  type: string
- container: ''
  name: notificationLambdaArn
  type: string
- container: ''
  name: notificationSenderEmail
  type: string
- container: ''
  name: offsetInNanos
  type: string
- container: ''
  name: parentAssetId
  type: string
- container: ''
  name: permission
  type: string
- container: ''
  name: portal
  type: string
- container: ''
  name: portalArn
  type: string
- container: ''
  name: portalAuthMode
  type: string
- container: ''
  name: portalClientId
  type: string
- container: ''
  name: portalContactEmail
  type: string
- container: ''
  name: portalCreationDate
  type: string
- container: ''
  name: portalDescription
  type: string
- container: ''
  name: portalId
  type: string
- container: ''
  name: portalLastUpdateDate
  type: string
- container: ''
  name: portalLogoImageLocation
  type: string
- container: ''
  name: portalName
  type: string
- container: ''
  name: portalStartUrl
  type: string
- container: ''
  name: portalStatus
  type: string
- container: ''
  name: portalSummaries
  type: string
- container: ''
  name: project
  type: string
- container: ''
  name: projectArn
  type: string
- container: ''
  name: projectCreationDate
  type: string
- container: ''
  name: projectDescription
  type: string
- container: ''
  name: projectId
  type: string
- container: ''
  name: projectLastUpdateDate
  type: string
- container: ''
  name: projectName
  type: string
- container: ''
  name: projectSummaries
  type: string
- container: ''
  name: properties
  type: string
- container: ''
  name: propertyAlias
  type: string
- container: ''
  name: propertyId
  type: string
- container: ''
  name: propertyValue
  type: string
- container: ''
  name: propertyValues
  type: string
- container: ''
  name: qualities
  type: string
- container: ''
  name: quality
  type: string
- container: ''
  name: relationshipType
  type: string
- container: ''
  name: resolution
  type: string
- container: ''
  name: resource
  type: string
- container: ''
  name: retentionPeriod
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: s3ResourceArn
  type: string
- container: ''
  name: skippedEntries
  type: string
- container: ''
  name: ssoApplicationId
  type: string
- container: ''
  name: standardDeviation
  type: string
- container: ''
  name: startDate
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: storageType
  type: string
- container: ''
  name: stringValue
  type: string
- container: ''
  name: successEntries
  type: string
- container: ''
  name: sum
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: timeInSeconds
  type: string
- container: ''
  name: timeOrdering
  type: string
- container: ''
  name: timeSeriesArn
  type: string
- container: ''
  name: timeSeriesCreationDate
  type: string
- container: ''
  name: timeSeriesId
  type: string
- container: ''
  name: timeSeriesLastUpdateDate
  type: string
- container: ''
  name: timestamp
  type: string
- container: ''
  name: timestamps
  type: string
- container: ''
  name: topic
  type: string
- container: ''
  name: transform
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: user
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: versionId
  type: string
property_count: 196
provider_name: Amazon IoT SiteWise
provider_slug: amazon-iot-sitewise
slug: amazon-iot-sitewise-context
tags:
- AWS
- Asset Management
- Industrial IoT
- IoT
- Time Series Data
- JSON-LD
- Linked Data
- Semantic Web
---
