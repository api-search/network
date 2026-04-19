---
class_count: 95
classes:
- InstanceRecommendation
- ECSServiceProjectedUtilizationMetric
- InferredWorkloadSaving
- GetEBSVolumeRecommendationsRequest
- JobFilter
- S3Destination
- LambdaFunctionMemoryRecommendationOption
- RecommendationSource
- ExportEC2InstanceRecommendationsResponse
- RecommendationSummary
- GetLambdaFunctionRecommendationsResponse
- AutoScalingGroupRecommendationOption
- EnrollmentFilter
- EBSFilter
- RecommendedOptionProjectedMetric
- ExportLambdaFunctionRecommendationsRequest
- GetECSServiceRecommendationProjectedMetricsResponse
- PutRecommendationPreferencesResponse
- AccountEnrollmentStatus
- VolumeRecommendationOption
- GetEnrollmentStatusesForOrganizationRequest
- ExportECSServiceRecommendationsRequest
- ContainerRecommendation
- GetEBSVolumeRecommendationsResponse
- SavingsOpportunity
- DescribeRecommendationExportJobsRequest
- UpdateEnrollmentStatusRequest
- ContainerConfiguration
- GetEnrollmentStatusRequest
- DescribeRecommendationExportJobsResponse
- ExportEBSVolumeRecommendationsRequest
- DeleteRecommendationPreferencesResponse
- LambdaFunctionUtilizationMetric
- GetAutoScalingGroupRecommendationsResponse
- ExportLambdaFunctionRecommendationsResponse
- MemorySizeConfiguration
- ExportAutoScalingGroupRecommendationsRequest
- GetEnrollmentStatusResponse
- Scope
- GetRecommendationSummariesRequest
- InstanceRecommendationOption
- AutoScalingGroupConfiguration
- ProjectedMetric
- GetRecommendationPreferencesRequest
- ECSServiceRecommendationFilter
- ECSServiceRecommendation
- GetEffectiveRecommendationPreferencesRequest
- ExportEC2InstanceRecommendationsRequest
- ExportDestination
- EstimatedMonthlySavings
- GetEC2InstanceRecommendationsResponse
- GetLambdaFunctionRecommendationsRequest
- RecommendationPreferencesDetail
- ECSServiceUtilizationMetric
- S3DestinationConfig
- GetEffectiveRecommendationPreferencesResponse
- AutoScalingGroupRecommendation
- EffectiveRecommendationPreferences
- RecommendationExportJob
- GetECSServiceRecommendationProjectedMetricsRequest
- GetAutoScalingGroupRecommendationsRequest
- ECSServiceRecommendationOption
- ReasonCodeSummary
- ServiceConfiguration
- UtilizationMetric
- RecommendationPreferences
- CurrentPerformanceRiskRatings
- VolumeRecommendation
- GetRecommendationSummariesResponse
- ExternalMetricStatus
- GetEC2InstanceRecommendationsRequest
- DeleteRecommendationPreferencesRequest
- LambdaFunctionRecommendation
- GetRecommendationPreferencesResponse
- GetECSServiceRecommendationsRequest
- Tag
- Filter
- GetECSServiceRecommendationsResponse
- ECSServiceRecommendedOptionProjectedMetric
- LambdaFunctionMemoryProjectedMetric
- EBSUtilizationMetric
- ExportEBSVolumeRecommendationsResponse
- ExternalMetricsPreference
- ECSServiceProjectedMetric
- LambdaFunctionRecommendationFilter
- PutRecommendationPreferencesRequest
- GetEC2RecommendationProjectedMetricsRequest
- GetEnrollmentStatusesForOrganizationResponse
- Summary
- UpdateEnrollmentStatusResponse
- GetEC2RecommendationProjectedMetricsResponse
- ExportAutoScalingGroupRecommendationsResponse
- VolumeConfiguration
- ExportECSServiceRecommendationsResponse
- name
context_file: json-ld/amazon-compute-optimizer-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-compute-optimizer/refs/heads/main/json-ld/amazon-compute-optimizer-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Compute Optimizer from Amazon Compute Optimizer.
layout: jsonld
name: Amazon Compute Optimizer Context
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
  name: instanceArn
  type: string
- container: ''
  name: accountId
  type: string
- container: ''
  name: instanceName
  type: string
- container: ''
  name: currentInstanceType
  type: string
- container: ''
  name: finding
  type: string
- container: ''
  name: findingReasonCodes
  type: string
- container: ''
  name: utilizationMetrics
  type: string
- container: ''
  name: lookBackPeriodInDays
  type: string
- container: ''
  name: recommendationOptions
  type: string
- container: ''
  name: recommendationSources
  type: string
- container: ''
  name: lastRefreshTimestamp
  type: string
- container: ''
  name: currentPerformanceRisk
  type: string
- container: ''
  name: effectiveRecommendationPreferences
  type: string
- container: ''
  name: inferredWorkloadTypes
  type: string
- container: ''
  name: instanceState
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: externalMetricStatus
  type: string
- container: ''
  name: statistic
  type: string
- container: ''
  name: lowerBoundValue
  type: string
- container: ''
  name: upperBoundValue
  type: string
- container: ''
  name: estimatedMonthlySavings
  type: string
- container: ''
  name: volumeArns
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: filters
  type: string
- container: ''
  name: accountIds
  type: string
- container: ''
  name: values
  type: string
- container: ''
  name: bucket
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: metadataKey
  type: string
- container: ''
  name: rank
  type: string
- container: ''
  name: memorySize
  type: string
- container: ''
  name: projectedUtilizationMetrics
  type: string
- container: ''
  name: savingsOpportunity
  type: string
- container: ''
  name: recommendationSourceArn
  type: string
- container: ''
  name: recommendationSourceType
  type: string
- container: ''
  name: jobId
  type: string
- container: ''
  name: s3Destination
  type: string
- container: ''
  name: summaries
  type: string
- container: ''
  name: recommendationResourceType
  type: string
- container: ''
  name: currentPerformanceRiskRatings
  type: string
- container: ''
  name: inferredWorkloadSavings
  type: string
- container: ''
  name: lambdaFunctionRecommendations
  type: string
- container: ''
  name: configuration
  type: string
- container: ''
  name: performanceRisk
  type: string
- container: ''
  name: migrationEffort
  type: string
- container: ''
  name: recommendedInstanceType
  type: string
- container: ''
  name: projectedMetrics
  type: string
- container: ''
  name: fieldsToExport
  type: string
- container: ''
  name: s3DestinationConfig
  type: string
- container: ''
  name: fileFormat
  type: string
- container: ''
  name: includeMemberAccounts
  type: string
- container: ''
  name: recommendedOptionProjectedMetrics
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusReason
  type: string
- container: ''
  name: lastUpdatedTimestamp
  type: string
- container: ''
  name: containerName
  type: string
- container: ''
  name: memorySizeConfiguration
  type: string
- container: ''
  name: cpu
  type: string
- container: ''
  name: volumeRecommendations
  type: string
- container: ''
  name: errors
  type: string
- container: ''
  name: savingsOpportunityPercentage
  type: string
- container: ''
  name: jobIds
  type: string
- container: ''
  name: recommendationExportJobs
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: autoScalingGroupRecommendations
  type: string
- container: ''
  name: memory
  type: string
- container: ''
  name: memoryReservation
  type: string
- container: ''
  name: recommendationPreferences
  type: string
- container: ''
  name: memberAccountsEnrolled
  type: string
- container: ''
  name: numberOfMemberAccountsOptedIn
  type: string
- container: ''
  name: instanceType
  type: string
- container: ''
  name: platformDifferences
  type: string
- container: ''
  name: desiredCapacity
  type: string
- container: ''
  name: minSize
  type: string
- container: ''
  name: maxSize
  type: string
- container: ''
  name: timestamps
  type: string
- container: ''
  name: resourceType
  type: string
- container: ''
  name: scope
  type: string
- container: ''
  name: serviceArn
  type: string
- container: ''
  name: currentServiceConfiguration
  type: string
- container: ''
  name: lookbackPeriodInDays
  type: string
- container: ''
  name: launchType
  type: string
- container: ''
  name: serviceRecommendationOptions
  type: string
- container: ''
  name: resourceArn
  type: string
- container: ''
  name: s3
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: instanceRecommendations
  type: string
- container: ''
  name: functionArns
  type: string
- container: ''
  name: enhancedInfrastructureMetrics
  type: string
- container: ''
  name: externalMetricsPreference
  type: string
- container: ''
  name: keyPrefix
  type: string
- container: ''
  name: autoScalingGroupArn
  type: string
- container: ''
  name: autoScalingGroupName
  type: string
- container: ''
  name: currentConfiguration
  type: string
- container: ''
  name: cpuVendorArchitectures
  type: string
- container: ''
  name: destination
  type: string
- container: ''
  name: creationTimestamp
  type: string
- container: ''
  name: failureReason
  type: string
- container: ''
  name: stat
  type: string
- container: ''
  name: period
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: autoScalingGroupArns
  type: string
- container: ''
  name: containerRecommendations
  type: string
- container: ''
  name: containerConfigurations
  type: string
- container: ''
  name: autoScalingConfiguration
  type: string
- container: ''
  name: taskDefinitionArn
  type: string
- container: ''
  name: high
  type: string
- container: ''
  name: medium
  type: string
- container: ''
  name: low
  type: string
- container: ''
  name: veryLow
  type: string
- container: ''
  name: volumeArn
  type: string
- container: ''
  name: volumeRecommendationOptions
  type: string
- container: ''
  name: recommendationSummaries
  type: string
- container: ''
  name: statusCode
  type: string
- container: ''
  name: instanceArns
  type: string
- container: ''
  name: recommendationPreferenceNames
  type: string
- container: ''
  name: functionArn
  type: string
- container: ''
  name: functionVersion
  type: string
- container: ''
  name: currentMemorySize
  type: string
- container: ''
  name: numberOfInvocations
  type: string
- container: ''
  name: memorySizeRecommendationOptions
  type: string
- container: ''
  name: recommendationPreferencesDetails
  type: string
- container: ''
  name: serviceArns
  type: string
- container: ''
  name: ecsServiceRecommendations
  type: string
- container: ''
  name: recommendedCpuUnits
  type: string
- container: ''
  name: recommendedMemorySize
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: upperBoundValues
  type: string
- container: ''
  name: lowerBoundValues
  type: string
- container: ''
  name: accountEnrollmentStatuses
  type: string
- container: ''
  name: reasonCodeSummaries
  type: string
- container: ''
  name: volumeType
  type: string
- container: ''
  name: volumeSize
  type: string
- container: ''
  name: volumeBaselineIOPS
  type: string
- container: ''
  name: volumeBurstIOPS
  type: string
- container: ''
  name: volumeBaselineThroughput
  type: string
- container: ''
  name: volumeBurstThroughput
  type: string
- container: ''
  name: rootVolume
  type: string
property_count: 140
provider_name: Amazon Compute Optimizer
provider_slug: amazon-compute-optimizer
slug: amazon-compute-optimizer-context
tags:
- AWS
- Cost Optimization
- FinOps
- Machine Learning
- Resource Recommendations
- JSON-LD
- Linked Data
- Semantic Web
---
