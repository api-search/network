---
class_count: 102
classes:
- AssociateClientDeviceWithCoreDeviceEntry
- AssociateClientDeviceWithCoreDeviceErrorEntry
- AssociateServiceRoleToAccountRequest
- AssociateServiceRoleToAccountResponse
- AssociatedClientDevice
- BatchAssociateClientDeviceWithCoreDeviceRequest
- BatchAssociateClientDeviceWithCoreDeviceResponse
- BatchDisassociateClientDeviceFromCoreDeviceRequest
- BatchDisassociateClientDeviceFromCoreDeviceResponse
- CancelDeploymentRequest
- CancelDeploymentResponse
- CloudComponentStatus
- Component
- ComponentCandidate
- ComponentConfigurationUpdate
- ComponentDependencyMap
- ComponentDependencyRequirement
- ComponentDeploymentSpecification
- ComponentDeploymentSpecifications
- ComponentLatestVersion
- ComponentPlatform
- ComponentRunWith
- ComponentVersionListItem
- ComponentVersionRequirementMap
- ConnectivityInfo
- CoreDevice
- CreateComponentVersionRequest
- CreateComponentVersionResponse
- CreateDeploymentRequest
- CreateDeploymentResponse
- DeleteComponentRequest
- DeleteCoreDeviceRequest
- DeleteDeploymentRequest
- Deployment
- DeploymentComponentUpdatePolicy
- DeploymentConfigurationValidationPolicy
- DeploymentIoTJobConfiguration
- DeploymentPolicies
- DescribeComponentRequest
- DescribeComponentResponse
- DisassociateClientDeviceFromCoreDeviceEntry
- DisassociateClientDeviceFromCoreDeviceErrorEntry
- DisassociateServiceRoleFromAccountRequest
- DisassociateServiceRoleFromAccountResponse
- EffectiveDeployment
- EffectiveDeploymentStatusDetails
- GetComponentRequest
- GetComponentResponse
- GetComponentVersionArtifactRequest
- GetComponentVersionArtifactResponse
- GetConnectivityInfoRequest
- GetConnectivityInfoResponse
- GetCoreDeviceRequest
- GetCoreDeviceResponse
- GetDeploymentRequest
- GetDeploymentResponse
- GetServiceRoleForAccountRequest
- GetServiceRoleForAccountResponse
- InstalledComponent
- IoTJobAbortConfig
- IoTJobAbortCriteria
- IoTJobExecutionsRolloutConfig
- IoTJobExponentialRolloutRate
- IoTJobRateIncreaseCriteria
- IoTJobTimeoutConfig
- LambdaContainerParams
- LambdaDeviceMount
- LambdaEnvironmentVariables
- LambdaEventSource
- LambdaExecutionParameters
- LambdaFunctionRecipeSource
- LambdaLinuxProcessParams
- LambdaVolumeMount
- ListClientDevicesAssociatedWithCoreDeviceRequest
- ListClientDevicesAssociatedWithCoreDeviceResponse
- ListComponentVersionsRequest
- ListComponentVersionsResponse
- ListComponentsRequest
- ListComponentsResponse
- ListCoreDevicesRequest
- ListCoreDevicesResponse
- ListDeploymentsRequest
- ListDeploymentsResponse
- ListEffectiveDeploymentsRequest
- ListEffectiveDeploymentsResponse
- ListInstalledComponentsRequest
- ListInstalledComponentsResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- PlatformAttributesMap
- ResolveComponentCandidatesRequest
- ResolveComponentCandidatesResponse
- ResolvedComponentVersion
- StringMap
- SystemResourceLimits
- TagMap
- TagResourceRequest
- TagResourceResponse
- UntagResourceRequest
- UntagResourceResponse
- description
- name
context_file: json-ld/amazon-iot-greengrass-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-greengrass/refs/heads/main/json-ld/amazon-iot-greengrass-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Iot Greengrass from Amazon IoT Greengrass.
layout: jsonld
name: Amazon Iot Greengrass Context
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
  name: abortConfig
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: addGroupOwner
  type: string
- container: ''
  name: architecture
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: associatedAt
  type: string
- container: ''
  name: associatedClientDevices
  type: string
- container: ''
  name: associationTimestamp
  type: string
- container: ''
  name: attributes
  type: string
- container: ''
  name: baseRatePerMinute
  type: string
- container: ''
  name: clientToken
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: componentCandidates
  type: string
- container: ''
  name: componentDependencies
  type: string
- container: ''
  name: componentLambdaParameters
  type: string
- container: ''
  name: componentName
  type: string
- container: ''
  name: componentPlatforms
  type: string
- container: ''
  name: componentState
  type: string
- container: ''
  name: componentUpdatePolicy
  type: string
- container: ''
  name: componentVersion
  type: string
- container: ''
  name: componentVersions
  type: string
- container: ''
  name: components
  type: string
- container: ''
  name: configurationUpdate
  type: string
- container: ''
  name: configurationValidationPolicy
  type: string
- container: ''
  name: connectivityInfo
  type: string
- container: ''
  name: containerParams
  type: string
- container: ''
  name: coreDeviceExecutionStatus
  type: string
- container: ''
  name: coreDeviceThingName
  type: string
- container: ''
  name: coreDevices
  type: string
- container: ''
  name: coreVersion
  type: string
- container: ''
  name: cpus
  type: string
- container: ''
  name: creationTimestamp
  type: string
- container: ''
  name: criteriaList
  type: string
- container: ''
  name: dependencyType
  type: string
- container: ''
  name: deploymentId
  type: string
- container: ''
  name: deploymentName
  type: string
- container: ''
  name: deploymentPolicies
  type: string
- container: ''
  name: deploymentStatus
  type: string
- container: ''
  name: deployments
  type: string
- container: ''
  name: destinationPath
  type: string
- container: ''
  name: devices
  type: string
- container: ''
  name: disassociatedAt
  type: string
- container: ''
  name: effectiveDeployments
  type: string
- container: ''
  name: entries
  type: string
- container: ''
  name: environmentVariables
  type: string
- container: ''
  name: errorEntries
  type: string
- container: ''
  name: errorStack
  type: string
- container: ''
  name: errorTypes
  type: string
- container: ''
  name: errors
  type: string
- container: ''
  name: eventSources
  type: string
- container: ''
  name: execArgs
  type: string
- container: ''
  name: exponentialRate
  type: string
- container: ''
  name: failureHandlingPolicy
  type: string
- container: ''
  name: failureType
  type: string
- container: ''
  name: hostAddress
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: inProgressTimeoutInMinutes
  type: string
- container: ''
  name: incrementFactor
  type: string
- container: ''
  name: inlineRecipe
  type: string
- container: ''
  name: inputPayloadEncodingType
  type: string
- container: ''
  name: installedComponents
  type: string
- container: ''
  name: iotJobArn
  type: string
- container: ''
  name: iotJobConfiguration
  type: string
- container: ''
  name: iotJobId
  type: string
- container: ''
  name: isLatestForTarget
  type: string
- container: ''
  name: isRoot
  type: string
- container: ''
  name: isolationMode
  type: string
- container: ''
  name: jobExecutionsRolloutConfig
  type: string
- container: ''
  name: lambdaArn
  type: string
- container: ''
  name: lambdaFunction
  type: string
- container: ''
  name: lastInstallationSource
  type: string
- container: ''
  name: lastReportedTimestamp
  type: string
- container: ''
  name: lastStatusChangeTimestamp
  type: string
- container: ''
  name: lastStatusUpdateTimestamp
  type: string
- container: ''
  name: latestVersion
  type: string
- container: ''
  name: lifecycleState
  type: string
- container: ''
  name: lifecycleStateDetails
  type: string
- container: ''
  name: lifecycleStatusCodes
  type: string
- container: ''
  name: linuxProcessParams
  type: string
- container: ''
  name: maxIdleTimeInSeconds
  type: string
- container: ''
  name: maxInstancesCount
  type: string
- container: ''
  name: maxQueueSize
  type: string
- container: ''
  name: maximumPerMinute
  type: string
- container: ''
  name: memory
  type: string
- container: ''
  name: memorySizeInKB
  type: string
- container: ''
  name: merge
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: metadata
  type: string
- container: ''
  name: minNumberOfExecutedThings
  type: string
- container: ''
  name: modifiedTimestamp
  type: string
- container: ''
  name: mountROSysfs
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: numberOfNotifiedThings
  type: string
- container: ''
  name: numberOfSucceededThings
  type: string
- container: ''
  name: parentTargetArn
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: permission
  type: string
- container: ''
  name: pinned
  type: string
- container: ''
  name: platform
  type: string
- container: ''
  name: platforms
  type: string
- container: ''
  name: portNumber
  type: string
- container: ''
  name: posixUser
  type: string
- container: ''
  name: preSignedUrl
  type: string
- container: ''
  name: publisher
  type: string
- container: ''
  name: rateIncreaseCriteria
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: recipe
  type: string
- container: ''
  name: recipeOutputFormat
  type: string
- container: ''
  name: reset
  type: string
- container: ''
  name: resolvedComponentVersions
  type: string
- container: ''
  name: revisionId
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: runWith
  type: string
- container: ''
  name: sourcePath
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusDetails
  type: string
- container: ''
  name: statusTimeoutInSeconds
  type: string
- container: ''
  name: systemResourceLimits
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: targetArn
  type: string
- container: ''
  name: thingName
  type: string
- container: ''
  name: thresholdPercentage
  type: string
- container: ''
  name: timeoutConfig
  type: string
- container: ''
  name: timeoutInSeconds
  type: string
- container: ''
  name: topic
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: vendorGuidance
  type: string
- container: ''
  name: vendorGuidanceMessage
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: versionRequirement
  type: string
- container: ''
  name: versionRequirements
  type: string
- container: ''
  name: volumes
  type: string
- container: ''
  name: windowsUser
  type: string
property_count: 133
provider_name: Amazon IoT Greengrass
provider_slug: amazon-iot-greengrass
slug: amazon-iot-greengrass-context
tags:
- AWS
- Edge Computing
- IoT
- Lambda
- Machine Learning
- Real-Time Processing
- JSON-LD
- Linked Data
- Semantic Web
---
