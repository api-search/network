---
class_count: 167
classes:
- BatchDeleteWorldsRequest
- BatchDeleteWorldsResponse
- BatchDescribeSimulationJobRequest
- BatchDescribeSimulationJobResponse
- BatchPolicy
- CancelDeploymentJobRequest
- CancelDeploymentJobResponse
- CancelSimulationJobBatchRequest
- CancelSimulationJobBatchResponse
- CancelSimulationJobRequest
- CancelSimulationJobResponse
- CancelWorldExportJobRequest
- CancelWorldExportJobResponse
- CancelWorldGenerationJobRequest
- CancelWorldGenerationJobResponse
- ComputeResponse
- Compute
- CreateDeploymentJobRequest
- CreateDeploymentJobResponse
- CreateFleetRequest
- CreateFleetResponse
- CreateRobotApplicationRequest
- CreateRobotApplicationResponse
- CreateRobotApplicationVersionRequest
- CreateRobotApplicationVersionResponse
- CreateRobotRequest
- CreateRobotResponse
- CreateSimulationApplicationRequest
- CreateSimulationApplicationResponse
- CreateSimulationApplicationVersionRequest
- CreateSimulationApplicationVersionResponse
- CreateSimulationJobRequest
- CreateSimulationJobResponse
- CreateWorldExportJobRequest
- CreateWorldExportJobResponse
- CreateWorldGenerationJobRequest
- CreateWorldGenerationJobResponse
- CreateWorldTemplateRequest
- CreateWorldTemplateResponse
- DataSourceConfig
- DataSource
- DeleteFleetRequest
- DeleteFleetResponse
- DeleteRobotApplicationRequest
- DeleteRobotApplicationResponse
- DeleteRobotRequest
- DeleteRobotResponse
- DeleteSimulationApplicationRequest
- DeleteSimulationApplicationResponse
- DeleteWorldTemplateRequest
- DeleteWorldTemplateResponse
- DeploymentApplicationConfig
- DeploymentConfig
- DeploymentJob
- DeploymentLaunchConfig
- DeregisterRobotRequest
- DeregisterRobotResponse
- DescribeDeploymentJobRequest
- DescribeDeploymentJobResponse
- DescribeFleetRequest
- DescribeFleetResponse
- DescribeRobotApplicationRequest
- DescribeRobotApplicationResponse
- DescribeRobotRequest
- DescribeRobotResponse
- DescribeSimulationApplicationRequest
- DescribeSimulationApplicationResponse
- DescribeSimulationJobBatchRequest
- DescribeSimulationJobBatchResponse
- DescribeSimulationJobRequest
- DescribeSimulationJobResponse
- DescribeWorldExportJobRequest
- DescribeWorldExportJobResponse
- DescribeWorldGenerationJobRequest
- DescribeWorldGenerationJobResponse
- DescribeWorldRequest
- DescribeWorldResponse
- DescribeWorldTemplateRequest
- DescribeWorldTemplateResponse
- Environment
- EnvironmentVariableMap
- FailedCreateSimulationJobRequest
- FailureSummary
- Filter
- FinishedWorldsSummary
- Fleet
- GetWorldTemplateBodyRequest
- GetWorldTemplateBodyResponse
- LaunchConfig
- ListDeploymentJobsRequest
- ListDeploymentJobsResponse
- ListFleetsRequest
- ListFleetsResponse
- ListRobotApplicationsRequest
- ListRobotApplicationsResponse
- ListRobotsRequest
- ListRobotsResponse
- ListSimulationApplicationsRequest
- ListSimulationApplicationsResponse
- ListSimulationJobBatchesRequest
- ListSimulationJobBatchesResponse
- ListSimulationJobsRequest
- ListSimulationJobsResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- ListWorldExportJobsRequest
- ListWorldExportJobsResponse
- ListWorldGenerationJobsRequest
- ListWorldGenerationJobsResponse
- ListWorldTemplatesRequest
- ListWorldTemplatesResponse
- ListWorldsRequest
- ListWorldsResponse
- LoggingConfig
- NetworkInterface
- OutputLocation
- PortForwardingConfig
- PortMapping
- ProgressDetail
- RegisterRobotRequest
- RegisterRobotResponse
- RenderingEngine
- RestartSimulationJobRequest
- RestartSimulationJobResponse
- RobotApplicationConfig
- RobotApplicationSummary
- RobotDeployment
- Robot
- RobotSoftwareSuite
- S3KeyOutput
- S3Object
- SimulationApplicationConfig
- SimulationApplicationSummary
- SimulationJobBatchSummary
- SimulationJobRequest
- SimulationJob
- SimulationJobSummary
- SimulationSoftwareSuite
- SourceConfig
- Source
- StartSimulationJobBatchRequest
- StartSimulationJobBatchResponse
- SyncDeploymentJobRequest
- SyncDeploymentJobResponse
- TagMap
- TagResourceRequest
- TagResourceResponse
- TemplateLocation
- TemplateSummary
- Tool
- UntagResourceRequest
- UntagResourceResponse
- UpdateRobotApplicationRequest
- UpdateRobotApplicationResponse
- UpdateSimulationApplicationRequest
- UpdateSimulationApplicationResponse
- UpdateWorldTemplateRequest
- UpdateWorldTemplateResponse
- UploadConfiguration
- VPCConfigResponse
- VPCConfig
- WorldConfig
- WorldCount
- WorldExportJobSummary
- WorldFailure
- WorldGenerationJobSummary
- WorldSummary
context_file: json-ld/amazon-robomaker-context-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-robomaker/refs/heads/main/json-ld/amazon-robomaker-context-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Robomaker from Amazon RoboMaker.
layout: jsonld
name: Amazon Robomaker Context
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
  name: worlds
  type: string
- container: ''
  name: unprocessedWorlds
  type: string
- container: ''
  name: jobs
  type: string
- container: ''
  name: unprocessedJobs
  type: string
- container: ''
  name: timeoutInSeconds
  type: string
- container: ''
  name: maxConcurrency
  type: string
- container: ''
  name: job
  type: string
- container: ''
  name: batch
  type: string
- container: ''
  name: simulationUnitLimit
  type: string
- container: ''
  name: computeType
  type: string
- container: ''
  name: gpuUnitLimit
  type: string
- container: ''
  name: deploymentConfig
  type: string
- container: ''
  name: clientRequestToken
  type: string
- container: ''
  name: fleet
  type: string
- container: ''
  name: deploymentApplicationConfigs
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: failureReason
  type: string
- container: ''
  name: failureCode
  type: string
- container: ''
  name: createdAt
  type: string
- container: ''
  name: name
  type: ''
- container: ''
  name: sources
  type: string
- container: ''
  name: robotSoftwareSuite
  type: string
- container: ''
  name: environment
  type: string
- container: ''
  name: version
  type: ''
- container: ''
  name: lastUpdatedAt
  type: string
- container: ''
  name: revisionId
  type: string
- container: ''
  name: application
  type: string
- container: ''
  name: currentRevisionId
  type: string
- container: ''
  name: s3Etags
  type: string
- container: ''
  name: imageDigest
  type: string
- container: ''
  name: architecture
  type: string
- container: ''
  name: greengrassGroupId
  type: string
- container: ''
  name: simulationSoftwareSuite
  type: string
- container: ''
  name: renderingEngine
  type: string
- container: ''
  name: outputLocation
  type: string
- container: ''
  name: loggingConfig
  type: string
- container: ''
  name: maxJobDurationInSeconds
  type: string
- container: ''
  name: iamRole
  type: string
- container: ''
  name: failureBehavior
  type: string
- container: ''
  name: robotApplications
  type: string
- container: ''
  name: simulationApplications
  type: string
- container: ''
  name: dataSources
  type: string
- container: ''
  name: vpcConfig
  type: string
- container: ''
  name: compute
  type: string
- container: ''
  name: lastStartedAt
  type: string
- container: ''
  name: simulationTimeMillis
  type: string
- container: ''
  name: template
  type: string
- container: ''
  name: worldCount
  type: string
- container: ''
  name: worldTags
  type: string
- container: ''
  name: templateBody
  type: string
- container: ''
  name: templateLocation
  type: string
- container: ''
  name: s3Bucket
  type: string
- container: ''
  name: s3Keys
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: destination
  type: string
- container: ''
  name: applicationVersion
  type: string
- container: ''
  name: robot
  type: string
- container: ''
  name: launchConfig
  type: string
- container: ''
  name: concurrentDeploymentPercentage
  type: string
- container: ''
  name: failureThresholdPercentage
  type: string
- container: ''
  name: robotDeploymentTimeoutInSeconds
  type: string
- container: ''
  name: downloadConditionFile
  type: string
- container: ''
  name: packageName
  type: string
- container: ''
  name: preLaunchFile
  type: string
- container: ''
  name: launchFile
  type: string
- container: ''
  name: postLaunchFile
  type: string
- container: ''
  name: environmentVariables
  type: string
- container: ''
  name: robotDeploymentSummary
  type: string
- container: ''
  name: robots
  type: string
- container: ''
  name: lastDeploymentStatus
  type: string
- container: ''
  name: lastDeploymentJob
  type: string
- container: ''
  name: lastDeploymentTime
  type: string
- container: ''
  name: fleetArn
  type: string
- container: ''
  name: batchPolicy
  type: string
- container: ''
  name: failedRequests
  type: string
- container: ''
  name: pendingRequests
  type: string
- container: ''
  name: createdRequests
  type: string
- container: ''
  name: networkInterface
  type: string
- container: ''
  name: finishedWorldsSummary
  type: string
- container: ''
  name: world
  type: string
- container: ''
  name: generationJob
  type: string
- container: ''
  name: worldDescriptionBody
  type: string
- container: ''
  name: uri
  type: string
- container: ''
  name: request
  type: string
- container: ''
  name: failedAt
  type: string
- container: ''
  name: totalFailureCount
  type: string
- container: ''
  name: failures
  type: string
- container: ''
  name: values
  type: string
- container: ''
  name: finishedCount
  type: string
- container: ''
  name: succeededWorlds
  type: string
- container: ''
  name: failureSummary
  type: string
- container: ''
  name: portForwardingConfig
  type: string
- container: ''
  name: streamUI
  type: string
- container: ''
  name: command
  type: string
- container: ''
  name: filters
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: deploymentJobs
  type: string
- container: ''
  name: fleetDetails
  type: string
- container: ''
  name: versionQualifier
  type: string
- container: ''
  name: robotApplicationSummaries
  type: string
- container: ''
  name: simulationApplicationSummaries
  type: string
- container: ''
  name: simulationJobBatchSummaries
  type: string
- container: ''
  name: simulationJobSummaries
  type: string
- container: ''
  name: worldExportJobSummaries
  type: string
- container: ''
  name: worldGenerationJobSummaries
  type: string
- container: ''
  name: templateSummaries
  type: string
- container: ''
  name: worldSummaries
  type: string
- container: ''
  name: recordAllRosTopics
  type: string
- container: ''
  name: networkInterfaceId
  type: string
- container: ''
  name: privateIpAddress
  type: string
- container: ''
  name: publicIpAddress
  type: string
- container: ''
  name: s3Prefix
  type: string
- container: ''
  name: portMappings
  type: string
- container: ''
  name: jobPort
  type: string
- container: ''
  name: applicationPort
  type: string
- container: ''
  name: enableOnPublicIp
  type: string
- container: ''
  name: currentProgress
  type: string
- container: ''
  name: percentDone
  type: string
- container: ''
  name: estimatedTimeRemainingSeconds
  type: string
- container: ''
  name: targetResource
  type: string
- container: ''
  name: uploadConfigurations
  type: string
- container: ''
  name: useDefaultUploadConfigurations
  type: string
- container: ''
  name: tools
  type: string
- container: ''
  name: useDefaultTools
  type: string
- container: ''
  name: deploymentStartTime
  type: string
- container: ''
  name: deploymentFinishTime
  type: string
- container: ''
  name: progressDetail
  type: string
- container: ''
  name: greenGrassGroupId
  type: string
- container: ''
  name: s3Key
  type: string
- container: ''
  name: etag
  type: string
- container: ''
  name: bucket
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: worldConfigs
  type: string
- container: ''
  name: failedRequestCount
  type: string
- container: ''
  name: pendingRequestCount
  type: string
- container: ''
  name: createdRequestCount
  type: string
- container: ''
  name: useDefaultApplications
  type: string
- container: ''
  name: simulationApplicationNames
  type: string
- container: ''
  name: robotApplicationNames
  type: string
- container: ''
  name: dataSourceNames
  type: string
- container: ''
  name: createSimulationJobRequests
  type: string
- container: ''
  name: streamOutputToCloudWatch
  type: string
- container: ''
  name: exitBehavior
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: uploadBehavior
  type: string
- container: ''
  name: subnets
  type: string
- container: ''
  name: securityGroups
  type: string
- container: ''
  name: vpcId
  type: string
- container: ''
  name: assignPublicIp
  type: string
- container: ''
  name: floorplanCount
  type: string
- container: ''
  name: interiorCountPerFloorplan
  type: string
- container: ''
  name: sampleFailureReason
  type: string
- container: ''
  name: failureCount
  type: string
- container: ''
  name: succeededWorldCount
  type: string
- container: ''
  name: failedWorldCount
  type: string
property_count: 158
provider_name: Amazon RoboMaker
provider_slug: amazon-robomaker
slug: amazon-robomaker-context-context
tags:
- AWS
- Robotics
- Simulation
- JSON-LD
- Linked Data
- Semantic Web
---
